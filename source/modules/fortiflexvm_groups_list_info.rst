fortiflexvm_groups_list_info - Get list of FlexVM groups (asset folders).
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
This module returns list of FlexVM groups (asset folders that have FlexVM products in them).

Requirements
------------

The below requirements are needed on the host that executes this module.

- ansible>=2.9


Parameters
----------

.. option:: username

  The username to authenticate. If not declared, the code will read the environment variable FLEXVM_ACCESS_USERNAME.

  :type: str
  :required: False

.. option:: password

  The password to authenticate. If not declared, the code will read the environment variable FLEXVM_ACCESS_PASSWORD.

  :type: str
  :required: False


Examples
-------------

.. code-block:: yaml

  - name: Get list of FlexVM groups
    hosts: localhost
    collections:
      - fortinet.fortiflexvm
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Get groups list
        fortinet.fortiflexvm.fortiflexvm_groups_list_info:
          username: "{{ username }}"
          password: "{{ password }}"
        register: result
  
      - name: Display response
        debug:
          var: result.groups
  


Return Values
-------------

.. option:: groups

  List of groups associated with the specified user.

  :type: list
  :returned: always
  
  .. option:: folderPath
  
    The folder path of the FlexVM group.
  
    :type: str
    :returned: always
  
  .. option:: availableTokens
  
    The number of available tokens for the FlexVM group.
  
    :type: int
    :returned: always
  
  .. option:: usedTokens
  
    The number of used tokens for the FlexVM group.
  
    :type: int
    :returned: always

Authors
-------

- Xinwei Du (@DrMofu)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.