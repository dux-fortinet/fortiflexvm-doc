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

- ansible>=2.15


Parameters
----------
.. raw:: html

 <ul>
 <li><span class="li-head">username</span> The username to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_USERNAME.<span class="li-normal">type: str</span></li>
 <li><span class="li-head">password</span> The password to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_PASSWORD.<span class="li-normal">type: str</span></li>
 <li><span class="li-head">accountId</span> Account ID.<span class="li-normal">type: str</span></li>
 </ul>



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
          # accountId: 12345 # Optional
        register: result
  
      - name: Display response
        ansible.builtin.debug:
          var: result.groups
  


Return Values
-------------
.. raw:: html

 <ul>
 <li><span class="li-head">groups</span> List of groups associated with the specified user.<span class="li-normal">type: list</span><span class="li-normal">returned: always</span></li>
 <ul class="ul-self">
 <li><span class="li-head">accountId</span> Account ID.<span class="li-normal">type: int</span><span class="li-normal">returned: if specified account ID in the argument</span></li>
 <li><span class="li-head">availableTokens</span> The number of available tokens for the FortiFlex group.<span class="li-normal">type: int</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">folderPath</span> The folder path of the FortiFlex group.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">usedTokens</span> The number of used tokens for the FortiFlex group.<span class="li-normal">type: int</span><span class="li-normal">returned: always</span></li>
 </ul>
 </ul>


Authors
-------

- Xinwei Du (@dux-fortinet)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.