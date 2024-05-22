FortiFlexVM Galaxy Versions and Release Notes
====================================================

+---------------------+----------------+------------------------------------------------------------------+
| Galaxy Version      | Release date   | Path to Install                                                  |
+=====================+================+==================================================================+
| 2.2.1 ``latest``    | 2024/05/24     | ``ansible-galaxy collection install fortinet.fortiflexvm:2.2.1`` |
+---------------------+----------------+------------------------------------------------------------------+
| 2.2.0               | 2024/03/29     | ``ansible-galaxy collection install fortinet.fortiflexvm:2.2.0`` |
+---------------------+----------------+------------------------------------------------------------------+
| 2.1.0               | 2024/01/25     | ``ansible-galaxy collection install fortinet.fortiflexvm:2.1.0`` |
+---------------------+----------------+------------------------------------------------------------------+
| 2.0.2               | 2023/11/15     | ``ansible-galaxy collection install fortinet.fortiflexvm:2.0.2`` |
+---------------------+----------------+------------------------------------------------------------------+
| 2.0.1               | 2023/09/06     | ``ansible-galaxy collection install fortinet.fortiflexvm:2.0.1`` |
+---------------------+----------------+------------------------------------------------------------------+
| 2.0.0               | 2023/07/20     | ``ansible-galaxy collection install fortinet.fortiflexvm:2.0.0`` |
+---------------------+----------------+------------------------------------------------------------------+
| 1.0.0               | 2023/04/18     | ``ansible-galaxy collection install fortinet.fortiflexvm:1.0.0`` |
+---------------------+----------------+------------------------------------------------------------------+

**Note**: Use ``-f`` option (i.e.
``ansible-galaxy collection install -f fortinet.fortiflexvm:x.x.x``) to
renew your existing local installation.



Release Galaxy 2.2.1
--------------------

Release Summary
^^^^^^^^^^^^^^^

Release FortiFlex 2.2.1, 2 new configurations.

Bugfixes
^^^^^^^^

- Configuration fortiAnalyzer support parameter addons.
- Suppoered 2 new configuration fortiAPHardware, fortiSwitchHardware.
- fortiflexvm_entitlements_vm_create supported parameter skipPending.


Release Galaxy 2.2.0
--------------------

Release Summary
^^^^^^^^^^^^^^^

Added 1 new resource, 2 new configurations.

Minor Changes
^^^^^^^^^^^^^

- Added 1 new resource, fortiflexvm_tool_calc_info.
- Added 2 new configurations, fortiSASE and fortiEDR.
- fortiflexvm_entitlements_list_info supported options "description", "serialnumber", "status", "tokenstatus".
- fortiflexvm_groups_nexttoken_info supported option "status". According to API, either "configId" or "accountId" is required now.

Bugfixes
^^^^^^^^

- Imporved the format of example Ansible playbooks.
- Improved logic of fortiflexvm_entitlements_update.

New Modules
^^^^^^^^^^^

- fortinet.fortiflexvm.fortiflexvm_tools_calc_info - Estimate points that will be consumed for configuration with certain parameters.



Release Galaxy 2.1.0
--------------------

Support one new module and one configuration.

Minor Changes
^^^^^^^^^^^^^

- One new module entitlements_cloud_create.
- Support new configurations, fortiClientEMSCloud.

Bugfixes
^^^^^^^^

- Change the tpye of parameter cpu in fortiGateBundle from str to int.
- Configuration fortiGateBundle supports new parameters, fortiGuardServices, cloudServices and supportService.

New Modules
^^^^^^^^^^^

- fortinet.fortiflexvm.fortiflexvm_entitlements_cloud_create - Create one cloud entitlement based on a FortiFlex Configuration.



Release Galaxy 2.0.2
--------------------

Support 3 new configurations.

Bugfixes
^^^^^^^^

- Support 3 new configurations, fortiClientEMSOP, fortiCloudPrivate and fortiCloudPublic.
- Support optional argument accountId in some modules.
- Update parameters for existing products.
- entitlements_points_info supports getting results for specified entitlement.



Release Galaxy 2.0.1
--------------------

Improve document. Release to Ansible Automation Hub.

Bugfixes
^^^^^^^^

- Improve document quality.



Release Galaxy 2.0.0
--------------------

Update FortiFlexVM Ansible to support FortiFlex v2.

Major Changes
^^^^^^^^^^^^^

- Support creating hardware entitlements by using fortiflexvm_entitlements_hardware_create.

Minor Changes
^^^^^^^^^^^^^

- Support bypass_validation and check_parameters in fortiflexvm_configs_create and fortiflexvm_configs_update.
- Support two new configurations, fortiADC and fortiGateHardware.

Breaking Changes / Porting Guide
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- All vms modules are renamed to entitlements modules. The return value vms are renamed to entitlements.

Removed Features (previously deprecated)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- fortiflexvm_vms_create (renamed to fortiflexvm_entitlements_vm_create)
- fortiflexvm_vms_list_info (renamed to fortiflexvm_entitlements_list_info)
- fortiflexvm_vms_points_info (renamed to fortiflexvm_entitlements_points_info)
- fortiflexvm_vms_update (renamed to fortiflexvm_entitlements_update)

New Modules
^^^^^^^^^^^

- fortinet.fortiflexvm.fortiflexvm_entitlements_hardware_create - Create hardware entitlements based on a FortiFlex Configuration.
- fortinet.fortiflexvm.fortiflexvm_entitlements_list_info - Get list of existing entitlements for a FlexVM Configuration.
- fortinet.fortiflexvm.fortiflexvm_entitlements_points_info - Get point usage for entitlements.
- fortinet.fortiflexvm.fortiflexvm_entitlements_vm_create - Create one or more VMs based on a FortiFlex Configuration.
- fortinet.fortiflexvm.fortiflexvm_entitlements_vm_regenerate_token - Regenerate token for a VM.



Release Galaxy 1.0.0
--------------------

First release of the fortiflex.

New Modules
^^^^^^^^^^^

- ``fortiflexvm_configs_create``: Create a new FlexVM Configuration.
- ``fortiflexvm_configs_list_info``: Get list of FlexVM Configurations.
- ``fortiflexvm_configs_update``: Update a FlexVM Configuration.
- ``fortiflexvm_groups_list_info``: Get list of FlexVM groups (asset folders).
- ``fortiflexvm_groups_nexttoken_info``: Get net available (unused) token.
- ``fortiflexvm_programs_list_info``: Get list of Flex VM Programs for the account.
- ``fortiflexvm_vms_create``: Create one or more VMs based on a FlexVM Configuration.
- ``fortiflexvm_vms_list_info``: Get list of existing VMs for FlexVM Configuration.
- ``fortiflexvm_vms_points_info``: Get point usage for VMs.
- ``fortiflexvm_vms_update``: Update an existing VM.