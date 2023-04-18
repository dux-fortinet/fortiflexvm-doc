FortiFlexVM Galaxy Versions and Release Notes
====================================================

+---------------------+----------------+------------------------------------------------------------------+
| Galaxy Version      | Release date   | Path to Install                                                  |
+=====================+================+==================================================================+
| 1.0.0 ``latest``    | 2023/04/18     | ``ansible-galaxy collection install fortinet.fortiflexvm:1.0.0`` |
+---------------------+----------------+------------------------------------------------------------------+

**Note**: Use ``-f`` option (i.e.
``ansible-galaxy collection install -f fortinet.fortiflexvm:x.x.x``) to
renew your existing local installation.


Release Galaxy 1.0.0
--------------------

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