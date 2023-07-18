fortiflexvm_entitlements_points_info - Get point usage for entitlements.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
Returns total points consumed by one or more entitlements in a date range.

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

.. option:: configId

  The ID of the configuration.

  :type: int
  :required: True

.. option:: startDate

  The start date of the date range to query. Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted. Recommended format is YYYY-MM-DD.

  :type: str
  :required: True

.. option:: endDate

  The end date of the date range to query. Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted. Recommended format is YYYY-MM-DD.

  :type: str
  :required: True


Examples
-------------

.. code-block:: yaml

  - name: Get point usage for entitlementss
    hosts: localhost
    collections:
      - fortinet.fortiflexvm
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Get entitlements points
        fortinet.fortiflexvm.fortiflexvm_entitlements_points_info:
          username: "{{ username }}"
          password: "{{ password }}"
          configId: 25
          startDate: "2020-10-01"
          endDate: "2020-10-25"
        register: result
  
      - name: Display response
        debug:
          var: result.entitlements
  


Return Values
-------------

.. option:: entitlements

  List of entitlements and their consumed points in the specified date range.

  :type: list
  :returned: always
  
  .. option:: serialNumber
  
    The serial number of the entitlement.
  
    :type: str
    :returned: always
  
  .. option:: points
  
    The total points consumed by the entitlement in the specified date range.
  
    :type: int
    :returned: always

Authors
-------

- Xinwei Du (@DrMofu)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.