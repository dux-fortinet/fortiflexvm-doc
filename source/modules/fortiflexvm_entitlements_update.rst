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

.. option:: serialNumber

  The serial number of the entitlement to update.

  :type: str
  :required: True

.. option:: configId

  The ID of the configuration.

  :type: int
  :required: False

.. option:: description

  The description of the entitlement.

  :type: str
  :required: False

.. option:: endDate

  The end date of the entitlement's validity. Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted. Recommended format is "YYYY-MM-DDThh:mm:ss".

  :type: str
  :required: False

.. option:: status

  The status of the entitlement.

  :type: str
  :required: False
  :choices: ['ACTIVE', 'STOPPED']


Examples
-------------

.. code-block:: yaml

  - name: Update entitlement
    hosts: localhost
    collections:
      - fortinet.fortiflexvm
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Update an entitlement.
        fortinet.fortiflexvm.fortiflexvm_entitlements_update:
          username: "{{ username }}"
          password: "{{ password }}"
          serialNumber: "FGVMMLTM23001324"
          # Please specify configId if you want to update configId, description or endDate
          configId: 3196
          description: "Modify through Ansible"
          endDate: "2023-12-12T00:00:00"
          status: "ACTIVE" # ACTIVE or STOPPED
        register: result
  
      - name: Display response
        debug:
          var: result.entitlements
  


Return Values
-------------

.. option:: entitlements

  The entitlement you update. This list only contains one entitlement.

  :type: list
  :returned: always
  
  .. option:: serialNumber
  
    The serial number of the entitlement.
  
    :type: str
    :returned: always
  
  .. option:: description
  
    The description of the entitlement.
  
    :type: str
    :returned: always
  
  .. option:: configId
  
    The config ID of the entitlement.
  
    :type: int
    :returned: always
  
  .. option:: startDate
  
    The start date of the entitlement.
  
    :type: str
    :returned: always
  
  .. option:: endDate
  
    The end date of the entitlement.
  
    :type: str
    :returned: always
  
  .. option:: status
  
    The status of the VM. Possible values are "PENDING", "ACTIVE", "STOPPED" or "EXPIRED".
  
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