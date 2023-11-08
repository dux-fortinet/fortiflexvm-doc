fortiflexvm_entitlements_vm_create - Create one or more VMs based on a FortiFlex Configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
Create one or more VMs based on a FortiFlex Configuration. This API is only used to create one or more VMs. To modify a VM, please refer to fortiflexvm_entitlements_update.

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

  The ID of a FortiFlex Configuration.

  :type: int
  :required: True

.. option:: count

  The number of VM(s) to be created. The default value is 1.

  :type: int
  :required: False
  :default: 1

.. option:: description

  The description of VM(s).

  :type: str
  :required: False
  :default: ""

.. option:: endDate

  VM(s) end date. It can not be before today's date or after the program's end date. Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted. Recommended format is "YYYY-MM-DDThh:mm:ss". If not specify, it will use the program's end date automatically.

  :type: str
  :required: False

.. option:: folderPath

  The folder path of the VM(s).

  :type: str
  :required: False


Examples
-------------

.. code-block:: yaml

  - name: Create VMs
    hosts: localhost
    collections:
      - fortinet.fortiflexvm
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Create Virtual Machines.
        fortinet.fortiflexvm.fortiflexvm_entitlements_vm_create:
          username: "{{ username }}"
          password: "{{ password }}"
          configId: 42
          count: 1 # If you set it as 0, FortiFlexvm ansible collection will not create any vm.
          description: "Create through Ansible" # Optional.
          endDate: "2023-11-11T00:00:00" # Optional. If not set, it will use the program end date automatically.
          folderPath: "My Assets" # Optional. If not set, new VM will be in "My Assets"
        register: result
  
      - name: Display response
        debug:
          var: result.entitlements
  


Return Values
-------------

.. option:: entitlements

  A list of virtual machine entitlements and their details.

  :type: list
  :returned: always
  
  .. option:: accountId
  
    The ID of the account associated with the program.
  
    :type: int
    :returned: always
  
  .. option:: configId
  
    The ID of the virtual machine configuration.
  
    :type: int
    :returned: always
  
  .. option:: description
  
    The description of the virtual machine.
  
    :type: str
    :returned: always
  
  .. option:: endDate
  
    The end date of the virtual machine's validity.
  
    :type: str
    :returned: always
  
  .. option:: serialNumber
  
    The serial number of the virtual machine.
  
    :type: str
    :returned: always
  
  .. option:: startDate
  
    The start date of the virtual machine's validity.
  
    :type: str
    :returned: always
  
  .. option:: status
  
    The status of the virtual machine.
  
    :type: str
    :returned: always
  
  .. option:: token
  
    The token assigned to the virtual machine.
  
    :type: str
    :returned: always
  
  .. option:: tokenStatus
  
    The status of the token assigned to the virtual machine.
  
    :type: str
    :returned: always

Authors
-------

- Xinwei Du (@DrMofu)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.