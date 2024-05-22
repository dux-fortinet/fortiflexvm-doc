fortiflexvm_groups_nexttoken_info - Get net available (unused) token.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
Returns first available token by asset folder or Configuration id (folder path, or config id or both can be specified in request).

Requirements
------------

The below requirements are needed on the host that executes this module.

- ansible>=2.9


Parameters
----------
.. raw:: html

 <ul>
 <li><span class="li-head">username</span> The username to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_USERNAME.<span class="li-normal">type: str</span></li>
 <li><span class="li-head">password</span> The password to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_PASSWORD.<span class="li-normal">type: str</span></li>
 <li><span class="li-head">accountId</span> Account ID. Please declare at least one of the two arguments, accountId or configId.<span class="li-normal">type: str</span></li>
 <li><span class="li-head">configId</span> The ID of a Flex VM Configuration. Please declare at least one of the two arguments, accountId or configId.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">folderPath</span> Folder path.<span class="li-normal">type: str</span></li>
 <li><span class="li-head">status</span> Filter option. A list. Possible values are "ACTIVE", "PENDDING", "STOPPED" and "EXPIRED".<span class="li-normal">type: list</span></li>
 </ul>



Examples
-------------

.. code-block:: yaml

  - name: Get next available (unused) token
    hosts: localhost
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Get groups nexttoken
        fortinet.fortiflexvm.fortiflexvm_groups_nexttoken_info:
          username: "{{ username }}"
          password: "{{ password }}"
          # Please declare at least one of the following two arguments: accountId or configId.
          # You can comment at most one argument that you don't want to specify.
          configId: 22
          # accountId: 12345
  
          # Optional parameters
          folderPath: "My Assets"
          status: ["ACTIVE", "PENDING"] # "ACTIVE", "PENDING", "STOPPED", "EXPIRED"
        register: result
  
      - name: Display response
        ansible.builtin.debug:
          var: result.entitlements
  


Return Values
-------------
.. raw:: html

 <ul>
 <li><span class="li-head">entitlements</span> Next available (unused) token. This list only has one element.<span class="li-normal">type: list</span><span class="li-normal">returned: always</span></li>
 <ul class="ul-self">
 <li><span class="li-head">accountId</span> Account ID.<span class="li-normal">type: int</span><span class="li-normal">returned: if specified account ID in the argument</span></li>
 <li><span class="li-head">configId</span> The config ID of the entitlement.<span class="li-normal">type: int</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">description</span> The description of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">endDate</span> The end date of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">serialNumber</span> The serial number of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">startDate</span> The start date of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">status</span> The status of the entitlement. Possible values are "PENDING", "ACTIVE", "STOPPED" or "EXPIRED".<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">token</span> The token of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">tokenStatus</span> The token status of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 </ul>
 </ul>


Authors
-------

- Xinwei Du (@dux-fortinet)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.