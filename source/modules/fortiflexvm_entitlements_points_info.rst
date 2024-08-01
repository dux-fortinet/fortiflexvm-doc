fortiflexvm_entitlements_points_info - Get point usage for entitlements.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
Returns total points consumed by one or more entitlements in a date range. Either configId or (accountId and programSerialNumber) should be provided.

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
 <li><span class="li-head">accountId</span> Account ID.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">configId</span> The ID of the configuration.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">endDate</span> The end date of the date range to query. Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted. Recommended format is YYYY-MM-DD.<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">programSerialNumber</span> The serial number of your FortiFlex Program.<span class="li-normal">type: str</span></li>
 <li><span class="li-head">serialNumber</span> The entitlement serial number. Instead of configId you can pass serialNumber to get results for one VM only.<span class="li-normal">type: str</span></li>
 <li><span class="li-head">startDate</span> The start date of the date range to query. Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted. Recommended format is YYYY-MM-DD.<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 </ul>



Examples
-------------

.. code-block:: yaml

  - name: Get point usage for entitlementss
    hosts: localhost
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Get entitlements points
        fortinet.fortiflexvm.fortiflexvm_entitlements_points_info:
          username: "{{ username }}"
          password: "{{ password }}"
          # Either configId or (accountId and programSerialNumber) should be provided.
          # configId: 3196
          accountId: 12345
          programSerialNumber: "ELAVMS0XXXXXX"
          # Instead of configId you can pass serialNumber to get results for one VM only.
          serialNumber: "FZVMMLTMXXXXXX"
          startDate: "2020-10-01"
          endDate: "2020-10-25"
        register: result
  
      - name: Display response
        ansible.builtin.debug:
          var: result.entitlements
  


Return Values
-------------
.. raw:: html

 <ul>
 <li><span class="li-head">entitlements</span> List of entitlements and their consumed points in the specified date range.<span class="li-normal">type: list</span><span class="li-normal">returned: always</span></li>
 <ul class="ul-self">
 <li><span class="li-head">accountId</span> The ID of the account associated with the program.<span class="li-normal">type: int</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">points</span> The total points consumed by the entitlement in the specified date range.<span class="li-normal">type: int</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">serialNumber</span> The serial number of the entitlement.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 </ul>
 </ul>


Authors
-------

- Xinwei Du (@dux-fortinet)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.