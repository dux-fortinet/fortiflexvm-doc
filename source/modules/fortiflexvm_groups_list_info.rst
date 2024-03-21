fortiflexvm_groups_list_info - Get list of FortiFlex groups (asset folders).
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
This module returns list of FortiFlex groups (asset folders that have FortiFlex products in them).

Requirements
------------

The below requirements are needed on the host that executes this module.

- ansible>=2.9


Parameters
----------

.. option:: username

  The username to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_USERNAME.

  :type: str

.. option:: password

  The password to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_PASSWORD.

  :type: str

.. option:: accountId

  Account ID.

  :type: str


Examples
-------------

.. code-block:: yaml

  - name: Get list of FortiFlex groups
    hosts: localhost
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Get groups list
        fortinet.fortiflexvm.fortiflexvm_groups_list_info:
          username: "{{ username }}"
          password: "{{ password }}"
          # accountId: 12345 # optional
        register: result
  
      - name: Display response
        ansible.builtin.debug:
          var: result.groups
  


Return Values
-------------

.. option:: groups

  List of groups associated with the specified user.

  :type: list
  :returned: always
  
  .. option:: accountId
  
    Account ID.
  
    :type: int
    :returned: if specified account ID in the argument
  
  .. option:: availableTokens
  
    The number of available tokens for the FortiFlex group.
  
    :type: int
    :returned: always
  
  .. option:: folderPath
  
    The folder path of the FortiFlex group.
  
    :type: str
    :returned: always
  
  .. option:: usedTokens
  
    The number of used tokens for the FortiFlex group.
  
    :type: int
    :returned: always

Authors
-------

- Xinwei Du (@dux-fortinet)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.