import os
import yaml

MODULES_PATH = "../collection/plugins/modules"
TEMPLATE_PATH = "./template/module.rst"
OUTPUT_DIR = "./source/modules"

template_data = ""
with open(TEMPLATE_PATH, "r") as f:
    template_data = f.read()


def get_meta(source_code, META):
    match_pattern = "'''"
    metadata_start = source_code.find(META + " = "+match_pattern)
    metadata_end = source_code.find(match_pattern, metadata_start + len(META + " = "+match_pattern))
    if metadata_start==-1 or metadata_end==-1:
        match_pattern = '"""'        
        metadata_start = source_code.find(META + " = "+match_pattern)
        metadata_end = source_code.find(match_pattern, metadata_start + len(META + " = "+match_pattern))
    if metadata_start==-1 or metadata_end==-1:
        return ""
    metadata = source_code[metadata_start + len(META + " = "+match_pattern):metadata_end]
    return metadata

def transfer_return(input_dict):
    return_list = []
    for key, params in input_dict.items():
        return_list.append("")
        return_list.append(".. option:: {}".format(key))
        return_list.append("")
        if isinstance(params["description"], list):
            return_list.append("  "+" ".join(params["description"]))
        else:
            return_list.append("  "+params["description"])
        return_list.append("")    
        for possible_param in ["type","returned"]:
            if possible_param in params:
                return_list.append("  :{}: {}".format(possible_param, params[possible_param]))
        if "contains" in params:
            sub_return_list = transfer_return(params["contains"])
            for line in sub_return_list:
                return_list.append("  "+line)
    return return_list

def transfer_option(input_dict):
    option_list = []
    for option_name,params in input_dict["options"].items():
        option_list.append("")
        option_list.append(".. option:: {}".format(option_name))
        option_list.append("")
        if isinstance(params["description"], list):
            option_list.append("  "+" ".join(params["description"]))
        else:
            option_list.append("  "+params["description"])
        option_list.append("")
        for possible_param in ["type","required","choices","default"]:
            if possible_param in params:
                value = params[possible_param]
                if value == "":
                    value = '""'
                option_list.append("  :{}: {}".format(possible_param, value))
        if "suboptions" in params:
            for sub_option_name, sub_params in params["suboptions"].items():
                option_list.append("")
                option_list.append("  .. option:: {}".format(sub_option_name))
                option_list.append("")
                option_list.append("    "+" ".join(sub_params["description"]))
                option_list.append("")
                for possible_param in ["type","required","choices","default"]:
                    if possible_param in sub_params:
                        value = sub_params[possible_param]
                        if value == "":
                            value = '""'
                        option_list.append("  :{}: {}".format(possible_param, value))
    return option_list


module_names = [file.split(".")[0] for file in os.listdir(MODULES_PATH)]

for module_name in module_names:
    # Get document in the code
    source_code = ""
    with open(os.path.join(MODULES_PATH, module_name+".py"), "r") as f:
        source_code = f.read()

    documentation_data = get_meta(source_code, "DOCUMENTATION")
    example_data = get_meta(source_code, "EXAMPLES")
    return_data = get_meta(source_code, "RETURN")
    documentation_dict = yaml.safe_load(documentation_data)
    return_dict = yaml.safe_load(return_data)

    # Get parameters
    option_list = transfer_option(documentation_dict)
                    
    # Get return values
    return_list = transfer_return(return_dict)

    # Write new document
    output_path = os.path.join(OUTPUT_DIR, module_name+".rst")
    title = "{} - {}\n{}".format(documentation_dict["module"], documentation_dict["short_description"],
                                  "+"*(3+len(documentation_dict["module"])+len(documentation_dict["short_description"])))
    output_data = template_data.format(title = title,
                                    description = " ".join(documentation_dict["description"]),
                                    version_added = documentation_dict["version_added"],
                                    example = "\n  ".join(example_data.split("\n")),
                                    authors = "\n- " + "\n- ".join(documentation_dict["author"]),
                                    options = "\n".join(option_list),
                                    returns = "\n".join(return_list))

    with open(output_path, "w") as f:
        f.write(output_data)
