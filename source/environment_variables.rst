Index of all Collection Environment Variables
=============================================

The following index documents all environment variables declared by plugins in collections.
You can use ``export ENV_VAR_NAME="your_value"`` to set the environment variable.

- `FORTIFLEX_ACCESS_USERNAME`: Your username. If you don't specify the username in the playbook, the program will try to read the username from here.
- `FORTIFLEX_ACCESS_PASSWORD`: Your password. If you don't specify the password in the playbook, the program will try to read the password from here.
- `FORTIFLEX_API_URL`: The API URL. The default value is "https://support.fortinet.com/ES/api/". You can overwrite it by setting this environment variable.

Environment variables used by the Ansible core configuration are documented in `Ansible Configuration Settings`_.

.. _Ansible Configuration Settings: https://docs.ansible.com/ansible/devel/reference_appendices/config.html#ansible-configuration-settings
