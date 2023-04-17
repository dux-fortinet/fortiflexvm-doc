fortiflexvm_vms_points_info - Get point usage for VMs.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
Returns total points consumed by one or more virtual machines in a date range.

Requirements
------------

The below requirements are needed on the host that executes this module.

- ansible>=2.9


Parameters
----------

.. option:: username

  The username to authenticate. If not declared, the code will read the environment variable FLEXVM_ACCESS_USERNAME.

  :type: str
  :required: False

.. option:: password

  The password to authenticate. If not declared, the code will read the environment variable FLEXVM_ACCESS_PASSWORD.

  :type: str
  :required: False

.. option:: configId

  The ID of the virtual machine configuration.

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

  - name: Get point usage for VMs
    hosts: localhost
    collections:
      - fortinet.fortiflexvm
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Get VMs points
        fortinet.fortiflexvm.fortiflexvm_vms_points_info:
          username: "{{ username }}"
          password: "{{ password }}"
          configId: 25
          startDate: "2020-10-01"
          endDate: "2020-10-25"
        register: result
  
      - name: Display response
        debug:
          var: result.vms
  


Return Values
-------------

.. option:: vms

  List of virtual machines and their consumed points in the specified date range.

  :type: list
  :returned: always
  
  .. option:: serialNumber
  
    The serial number of the virtual machine.
  
    :type: str
    :returned: always
  
  .. option:: points
  
    The total points consumed by the virtual machine in the specified date range.
  
    :type: int
    :returned: always

Authors
-------

- Xinwei Du (@DrMofu)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.