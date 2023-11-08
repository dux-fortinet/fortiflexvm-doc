fortiflexvm_entitlements_list_info - Get list of existing entitlements for a FlexVM Configuration.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
This module retrieves a list of entitlements for a configuration. Either configId or (accountId and programSerialNumber) should be provided.

Requirements
------------

The below requirements are needed on the host that executes this module.

- ansible>=2.9


Parameters
----------

.. option:: username

  The username to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_USERNAME.

  :type: str
  :required: False

.. option:: password

  The password to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_PASSWORD.

  :type: str
  :required: False

.. option:: accountId

  Account ID.

  :type: int
  :required: False

.. option:: configId

  The ID of the configuration for which to retrieve the list of VMs.

  :type: int
  :required: False

.. option:: programSerialNumber

  The serial number of your FortiFlex Program.

  :type: str
  :required: False


Examples
-------------

.. code-block:: yaml

  - name: Get list of entitlements for a specific config ID
    hosts: localhost
    collections:
      - fortinet.fortiflexvm
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
        register: result
  
      - name: Display response
        debug:
          var: result.entitlements
  


Return Values
-------------

.. option:: entitlements

  List of entitlements associated with the specified config ID.

  :type: list
  :returned: always
  
  .. option:: accountId
  
    Account ID.
  
    :type: int
    :returned: always
  
  .. option:: configId
  
    The config ID of the entitlement.
  
    :type: int
    :returned: always
  
  .. option:: description
  
    The description of the entitlement.
  
    :type: str
    :returned: always
  
  .. option:: endDate
  
    The end date of the entitlement.
  
    :type: str
    :returned: always
  
  .. option:: serialNumber
  
    The serial number of the entitlement.
  
    :type: str
    :returned: always
  
  .. option:: startDate
  
    The start date of the entitlement.
  
    :type: str
    :returned: always
  
  .. option:: status
  
    The status of the entitlement. Possible values are "PENDING", "ACTIVE", "STOPPED" or "EXPIRED".
  
    :type: str
    :returned: always
  
  .. option:: token
  
    The token of the entitlement.
  
    :type: str
    :returned: always
  
  .. option:: tokenStatus
  
    The token status of the entitlement. Possible values are "NOTUSED" or "USED".
  
    :type: str
    :returned: always

Authors
-------

- Xinwei Du (@DrMofu)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.