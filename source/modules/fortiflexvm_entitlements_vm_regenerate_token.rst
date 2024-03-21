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

- ansible>=2.9


Parameters
----------

.. option:: username

  The username to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_USERNAME.

  :type: str

.. option:: password

  The password to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_PASSWORD.

  :type: str

.. option:: regenerate

  Whether regenerate a new token.

  :type: bool
  :required: True

.. option:: serialNumber

  The serial number of the entitlement to update.

  :type: str
  :required: True


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

.. option:: entitlements

  The entitlement you update. This list only contains one entitlement. It will be empty if you set regenerate as false.

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

- Xinwei Du (@dux-fortinet)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.