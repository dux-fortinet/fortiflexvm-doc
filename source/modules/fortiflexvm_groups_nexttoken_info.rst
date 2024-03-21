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

.. option:: username

  The username to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_USERNAME.

  :type: str

.. option:: password

  The password to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_PASSWORD.

  :type: str

.. option:: accountId

  Account ID.

  :type: str

.. option:: configId

  The ID of a Flex VM Configuration. Please declare at least one of the two arguments folderPath and configId.

  :type: int
  :default: 0

.. option:: folderPath

  Folder path. Please declare at least one of the two arguments folderPath and configId.

  :type: str
  :default: ""

.. option:: status

  Filter option. A list. Possible values are "ACTIVE", "PENDDING", "STOPPED" and "EXPIRED".

  :type: list


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
          # Please declare at least one of the following two arguments: folderPath and configId.
          # You can comment at most one argument that you don"t want to specify.
          folderPath: "My Assets"
          configId: 22
  
          # Optional parameters
          # accountId: 12345
          status: ["ACTIVE", "PENDING"] # "ACTIVE", "PENDING", "STOPPED", "EXPIRED"
        register: result
  
      - name: Display response
        ansible.builtin.debug:
          var: result.entitlements
  


Return Values
-------------

.. option:: entitlements

  Next available (unused) token. This list only has one element.

  :type: list
  :returned: always
  
  .. option:: accountId
  
    Account ID.
  
    :type: int
    :returned: if specified account ID in the argument
  
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
  
    The token status of the entitlement.
  
    :type: str
    :returned: always

Authors
-------

- Xinwei Du (@dux-fortinet)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.