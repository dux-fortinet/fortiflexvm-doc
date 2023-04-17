fortiflexvm_vms_list_info - Get list of existing VMs for FlexVM Configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
This module retrieves a list of VMs associated with a specific config ID from FortiFlexVM API using the provided credentials.

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

  The ID of the configuration for which to retrieve the list of VMs.

  :type: int
  :required: True


Examples
-------------

.. code-block:: yaml

  - name: Get list of VMs for a specific config ID
    hosts: localhost
    collections:
      - fortinet.fortiflexvm
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Get VMs list
        fortinet.fortiflexvm.fortiflexvm_vms_list_info:
          username: "{{ username }}"
          password: "{{ password }}"
          configId: 22
        register: result
  
      - name: Display response
        debug:
          var: result.vms
  


Return Values
-------------

.. option:: vms

  List of VMs associated with the specified config ID.

  :type: list
  :returned: always
  
  .. option:: serialNumber
  
    The serial number of the VM.
  
    :type: str
    :returned: always
  
  .. option:: description
  
    The description of the VM.
  
    :type: str
    :returned: always
  
  .. option:: configId
  
    The config ID of the VM.
  
    :type: int
    :returned: always
  
  .. option:: startDate
  
    The start date of the VM.
  
    :type: str
    :returned: always
  
  .. option:: endDate
  
    The end date of the VM.
  
    :type: str
    :returned: always
  
  .. option:: status
  
    The status of the VM. Possible values are "PENDING", "ACTIVE", "STOPPED" or "EXPIRED".
  
    :type: str
    :returned: always
  
  .. option:: token
  
    The token of the VM.
  
    :type: str
    :returned: always
  
  .. option:: tokenStatus
  
    The token status of the VM. Possible values are "NOTUSED" or "USED".
  
    :type: str
    :returned: always

Authors
-------

- Xinwei Du (@DrMofu)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.