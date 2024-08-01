fortiflexvm_entitlements_list_info - Get entitlements information.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
This module retrieves information of target entitlements. Either configId or (accountId and programSerialNumber) should be provided.

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
 <li><span class="li-head">accountId</span> Filter option. Account ID.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">configId</span> The ID of the configuration for which to retrieve the list of VMs.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">description</span> Filter option. Description.<span class="li-normal">type: str</span></li>
 <li><span class="li-head">serialNumber</span> Filter option. Serial number.<span class="li-normal">type: str</span></li>
 <li><span class="li-head">status</span> Filter option. "ACTIVE", "STOPPED", "PENDDING" or "EXPIRED".<span class="li-normal">type: str</span></li>
 <li><span class="li-head">tokenStatus</span> Filter option. Token status. "NOTUSED" or "USED".<span class="li-normal">type: str</span></li>
 <li><span class="li-head">programSerialNumber</span> Filter option. The serial number of your FortiFlex Program.<span class="li-normal">type: str</span></li>
 </ul>



Examples
-------------

.. code-block:: yaml

  - name: Get information of target entitlements.
    hosts: localhost
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Get entitlements list
        fortinet.fortiflexvm.fortiflexvm_entitlements_list_info:
          username: "{{ username }}"
          password: "{{ password }}"
          # Either configId or (accountId and programSerialNumber) should be provided.
          configId: 22
          # accountId: 12345
          # programSerialNumber: "ELAVMS00XXXXX"
  
          # Optional filter options
          # description: "you can use description to distinguish entitlements"
          # serialNumber: "XXXXXX0000000000"
          # status: "PENDING"
          # tokenStatus: "NOTUSED"
        register: result
  
      - name: Display response
        ansible.builtin.debug:
          var: result.entitlements
  


Return Values
-------------
.. raw:: html

 <ul>
 <li><span class="li-head">entitlements</span> List of entitlements associated with the specified config ID.<span class="li-normal">type: list</span><span class="li-normal">returned: always</span></li>
 <ul class="ul-self">
 <li><span class="li-head">accountId</span> Account ID.<span class="li-normal">type: int</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">configId</span> The config ID of the entitlement.<span class="li-normal">type: int</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">description</span> The description of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">endDate</span> The end date of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">serialNumber</span> The serial number of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">startDate</span> The start date of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">status</span> The status of the entitlement. Possible values are "PENDING", "ACTIVE", "STOPPED" or "EXPIRED".<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">token</span> The token of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">tokenStatus</span> The token status of the entitlement. Possible values are "NOTUSED" or "USED".<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 </ul>
 </ul>


Authors
-------

- Xinwei Du (@dux-fortinet)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.