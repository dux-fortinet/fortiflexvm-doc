fortiflexvm_entitlements_hardware_create - Create hardware entitlements based on a FortiFlex Configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
Create hardware entitlements based on a FortiFlex Configuration. This API is only used to create one or more hardware entitlements. To modify an entitlement, please refer to fortiflexvm_entitlements_update.

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

.. option:: configId

  The ID of a FortiFlex Configuration.

  :type: int
  :required: True

.. option:: serialNumbers

  List of hardware serial numbers.

  :type: list
  :required: True

.. option:: endDate

  VM(s) end date. It can not be before today's date or after the program's end date. Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted. Recommended format is "YYYY-MM-DDThh:mm:ss". If not specify, it will use the program's end date automatically.

  :type: str


Examples
-------------

.. code-block:: yaml

  - name: Create hardware entitlements
    hosts: localhost
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Create hardware entitlements
        fortinet.fortiflexvm.fortiflexvm_entitlements_hardware_create:
          username: "{{ username }}"
          password: "{{ password }}"
          configId: 42
          serialNumbers:
            - "FGT60FTK19000010"
            - "FGT60FTK19000013"
          endDate: "2023-11-11T00:00:00"
        register: result
  
      - name: Display response
        ansible.builtin.debug:
          var: result.entitlements
  


Return Values
-------------

.. option:: entitlements

  A list of hardware entitlements and their details.

  :type: list
  :returned: always
  
  .. option:: accountId
  
    The ID of the account associated with the program.
  
    :type: int
    :returned: always
  
  .. option:: configId
  
    The ID of the entitlement configuration.
  
    :type: int
    :returned: always
  
  .. option:: description
  
    The description of the hardware entitlement.
  
    :type: str
    :returned: always
  
  .. option:: endDate
  
    The end date of the hardware entitlement.
  
    :type: str
    :returned: always
  
  .. option:: serialNumber
  
    The serial number of the hardware.
  
    :type: str
    :returned: always
  
  .. option:: startDate
  
    The start date of the hardware entitlement.
  
    :type: str
    :returned: always
  
  .. option:: status
  
    The status of the hardware entitlement.
  
    :type: str
    :returned: always
  
  .. option:: token
  
    The token assigned to the hardware entitlement.
  
    :type: str
    :returned: always
  
  .. option:: tokenStatus
  
    The status of the token assigned to the hardware entitlement.
  
    :type: str
    :returned: always

Authors
-------

- Xinwei Du (@dux-fortinet)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.