fortiflexvm_programs_list_info - Get list of FortiFlex Programs for the account.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
This module retrieves a list of FortiFlex Programs using the provided credentials.

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


Examples
-------------

.. code-block:: yaml

  - name: Get list of programs for the account
    hosts: localhost
    collections:
      - fortinet.fortiflexvm
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Get programs list
        fortinet.fortiflexvm.fortiflexvm_programs_list_info:
          username: "{{ username }}"
          password: "{{ password }}"
        register: result
  
      - name: Display response
        debug:
          var: result.programs
  


Return Values
-------------

.. option:: programs

  List of programs associated with the specified user.

  :type: list
  :returned: always
  
  .. option:: accountId
  
    The ID of the account associated with the program.
  
    :type: int
    :returned: always
  
  .. option:: endDate
  
    The end date of the program.
  
    :type: str
    :returned: always
  
  .. option:: hasSupportCoverage
  
    A flag indicating whether the program has support coverage.
  
    :type: bool
    :returned: always
  
  .. option:: serialNumber
  
    The serial number of the program.
  
    :type: str
    :returned: always
  
  .. option:: startDate
  
    The start date of the program.
  
    :type: str
    :returned: always

Authors
-------

- Xinwei Du (@DrMofu)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.