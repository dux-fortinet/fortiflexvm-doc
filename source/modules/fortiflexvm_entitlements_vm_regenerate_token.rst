fortiflexvm_entitlements_vm_regenerate_token - Regenerate token for a VM.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
Regenerate token for a VM.

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
 <li><span class="li-head">regenerate</span> Whether regenerate a new token.<span class="li-normal">type: bool</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">serialNumber</span> The serial number of the entitlement to update.<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 </ul>



Examples
-------------

.. code-block:: yaml

  - name: Regenerate token
    hosts: localhost
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Regenerate token
        fortinet.fortiflexvm.fortiflexvm_entitlements_vm_regenerate_token:
          username: "{{ username }}"
          password: "{{ password }}"
          serialNumber: "FGVMMLTM23001324"
          regenerate: true # If you set it as false, FortiFlexvm ansible collection will return an empty list.
        register: result
  
      - name: Display response
        ansible.builtin.debug:
          var: result.entitlements
  


Return Values
-------------
.. raw:: html

 <ul>
 <li><span class="li-head">entitlements</span> The entitlement you update. This list only contains one entitlement. It will be empty if you set regenerate as false.<span class="li-normal">type: list</span><span class="li-normal">returned: always</span></li>
 <ul class="ul-self">
 <li><span class="li-head">accountId</span> Account ID.<span class="li-normal">type: int</span><span class="li-normal">returned: always</span></li>
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