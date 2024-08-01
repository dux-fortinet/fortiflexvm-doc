fortiflexvm_entitlements_update - Update an existing entitlement.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
This module updates an existing entitlement.

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
 <li><span class="li-head">serialNumber</span> The serial number of the entitlement to update.<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">configId</span> The ID of the configuration.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">description</span> The description of the entitlement.<span class="li-normal">type: str</span></li>
 <li><span class="li-head">endDate</span> The end date of the entitlement's validity. Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted. Recommended format is "YYYY-MM-DDThh:mm:ss".<span class="li-normal">type: str</span></li>
 <li><span class="li-head">status</span> The status of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">choices: ['ACTIVE', 'STOPPED']</span></li>
 </ul>



Examples
-------------

.. code-block:: yaml

  - name: Update entitlement
    hosts: localhost
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Update an entitlement.
        fortinet.fortiflexvm.fortiflexvm_entitlements_update:
          username: "{{ username }}"
          password: "{{ password }}"
          serialNumber: "FGVMXXXX00000000"
          # Please specify configId if you want to update configId, description or endDate
          configId: 3196
          description: "Modify through Ansible" # Optional.
          endDate: "2024-12-12T00:00:00"        # Optional. If not set, it will use the program end date automatically.
          status: "ACTIVE"                      # Optional. ACTIVE or STOPPED
        register: result
  
      - name: Display response
        ansible.builtin.debug:
          var: result.entitlements
  


Return Values
-------------
.. raw:: html

 <ul>
 <li><span class="li-head">entitlements</span> The entitlement you update. This list only contains one entitlement.<span class="li-normal">type: list</span><span class="li-normal">returned: always</span></li>
 <ul class="ul-self">
 <li><span class="li-head">accountId</span> The ID of the account associated with the program.<span class="li-normal">type: int</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">configId</span> The config ID of the entitlement.<span class="li-normal">type: int</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">description</span> The description of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">endDate</span> The end date of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">serialNumber</span> The serial number of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">startDate</span> The start date of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">status</span> The status of the VM. Possible values are "PENDING", "ACTIVE", "STOPPED" or "EXPIRED".<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">token</span> The token of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">tokenStatus</span> The token status of the entitlement. Possible values are "NOTUSED" or "USED".<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 </ul>
 </ul>


Authors
-------

- Xinwei Du (@dux-fortinet)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.