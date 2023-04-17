fortiflexvm_configs_create - Create a new FlexVM Configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
This module creates a new FlexVM Configuration under a program.

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

.. option:: programSerialNumber

  The serial number of your Flex VM Program.

  :type: str
  :required: True

.. option:: name

  The name of your Flex VM Configuration.

  :type: str
  :required: True

.. option:: fortiGateBundle

  FortiGate Virtual Machine - Service Bundle.

  :type: dict
  :required: False

  .. option:: cpu

    The number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16",  "32" or "2147483647" (unlimited).

  :type: str
  :required: True
  :choices: ['1', '2', '4', '8', '16', '32', '2147483647']

  .. option:: service

    The value of this attribute is one of "FC" (FortiCare), "UTM", "ENT" (Enterprise) or "ATP".

  :type: str
  :required: True
  :choices: ['FC', 'UTM', 'ENT', 'ATP']

  .. option:: vdom

    Number of VDOMs. A number between 0 and 500 (inclusive). The default number is 0.

  :type: int
  :required: False
  :default: 0

.. option:: fortiManager

  FortiManager Virtual Machine.

  :type: dict
  :required: False

  .. option:: device

    Number of managed devices. A number between 1 and 100000 (inclusive).

  :type: int
  :required: True

  .. option:: adom

    Number of ADOMs. A number between 1 and 100000 (inclusive).

  :type: int
  :required: True

.. option:: fortiWeb

  FortiWeb Virtual Machine - Service Bundle.

  :type: dict
  :required: False

  .. option:: cpu

    Number of CPUs. The value of this attribute is one of "1", "2" "4", "8" or "16".

  :type: str
  :required: True
  :choices: ['1', '2', '4', '8', '16']

  .. option:: service

    Service Package. Valid values are "FWBSTD" (Standard) or "FWBADV" (Advanced).

  :type: str
  :required: True
  :choices: ['FWBSTD', 'FWBADV']

.. option:: fortiGateLCS

  FortiGate Virtual Machine - A La Carte Services.

  :type: dict
  :required: False

  .. option:: cpu

    The number of CPUs. A number between 1 and 96 (inclusive).

  :type: int
  :required: True

  .. option:: fortiGuardServices

    The fortiguard services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["IPS", "AVDB", "FURL", "IOTH", "FGSA", "ISSS"].

  :type: list
  :required: False
  :default: []

  .. option:: supportService

    Valid values are "FC247" (FortiCare 24x7) or "ASET" (FortiCare Elite).

  :type: str
  :required: True
  :choices: ['FC247', 'ASET']

  .. option:: vdom

    Number of VDOMs. A number between 1 and 500 (inclusive).

  :type: int
  :required: True

  .. option:: cloudServices

    The cloud services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["FAMS", "SWNM", "FMGC", "AFAC"].

  :type: list
  :required: False
  :default: []

.. option:: fortiAnalyzer

  FortiAnalyzer Virtual Machine.

  :type: dict
  :required: False

  .. option:: storage

    Daily Storage (GB). A number between 5 and 8300 (inclusive).

  :type: int
  :required: True

  .. option:: adom

    Number of ADOMs. A number between 0 and 1200 (inclusive).

  :type: int
  :required: True

  .. option:: service

    Support Service. Currently, the only available option is "FAZFC247" (FortiCare Premium). The default value is "FAZFC247".

  :type: str
  :required: True
  :choices: ['FAZFC247']

.. option:: fortiPortal

  FortiPortal Virtual Machine.

  :type: dict
  :required: False

  .. option:: device

    Number of managed devices. A number between 0 and 100000 (inclusive).

  :type: int
  :required: True


Examples
-------------

.. code-block:: yaml

  - name: Create VM configuration
    hosts: localhost
    collections:
      - fortinet.fortiflexvm
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Create a Virtual Machine configuration
        fortinet.fortiflexvm.fortiflexvm_configs_create:
          username: "{{ username }}"
          password: "{{ password }}"
          programSerialNumber: "ELAVMS000000XXXX"
          name: "ansible"
  
          # Please only use one of the following.
  
          fortiGateBundle:
            cpu: "2" # "1", "2", "4", "8", "16", "32", "2147483647"
            service: "FC" # "FC", "UTM", "ENT", "ATP"
            vdom: 10 # 0 ~ 500
  
          # fortiManager:
          #   device: 1 # 1 ~ 100000
          #   adom: 1 # 1 ~ 100000
  
          # fortiWeb:
          #   cpu: "4" # "1", "2", "4", "8", "16"
          #   service: "FWBSTD" # "FWBSTD" or "FWBADV"
  
          # fortiGateLCS:
          #   cpu: 4 # 1 ~ 96
          #   fortiGuardServices: [] # "IPS", "AVDB", "FURL", "IOTH", "FGSA", "ISSS"
          #   supportService: "FC247" # "FC247", "ASET"
          #   vdom: 1 # 1 ~ 500
          #   cloudServices: ["FAMS", "SWNM"] # "FAMS", "SWNM", "FMGC", "AFAC"
  
          # fortiAnalyzer:
          #   storage: 5 # 5 ~ 8300
          #   adom: 1 # 0 ~ 1200
          #   service: "FAZFC247" # "FAZFC247"
  
          # fortiPortal:
          #   device: 1 # 0 ~ 100000
  
        register: result
  
      - name: Display response
        debug:
          var: result.configs
  


Return Values
-------------

.. option:: configs

  The configuration you create.

  :type: dict
  :returned: always
  
  .. option:: id
  
    The ID of the configuration.
  
    :type: int
    :returned: always
  
  .. option:: name
  
    The name of the configuration.
  
    :type: str
    :returned: always
  
  .. option:: programSerialNumber
  
    The program serial number the configuration belongs to.
  
    :type: str
    :returned: always
  
  .. option:: status
  
    The status of the configuration.
  
    :type: str
    :returned: always
  
  .. option:: fortiGateBundle
  
    FortiGate Virtual Machine - Service Bundle.
  
    :type: dict
    :returned: changed
    
    .. option:: cpu
    
      The number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16",  "32" or "2147483647" (unlimited).
    
      :type: str
      :returned: always
    
    .. option:: service
    
      he value of this attribute is one of "FC" (FortiCare), "UTM", "ENT" (Enterprise) or "ATP".
    
      :type: str
      :returned: always
    
    .. option:: vdom
    
      Number of VDOMs. A number between 0 and 500 (inclusive). The default number is 0.
    
      :type: int
      :returned: always
  
  .. option:: fortiManager
  
    FortiManager Virtual Machine.
  
    :type: dict
    :returned: changed
    
    .. option:: device
    
      Number of managed devices. A number between 1 and 100000 (inclusive).
    
      :type: int
      :returned: always
    
    .. option:: adom
    
      Number of ADOMs. A number between 1 and 100000 (inclusive).
    
      :type: int
      :returned: always
  
  .. option:: fortiWeb
  
    FortiWeb Virtual Machine - Service Bundle.
  
    :type: dict
    :returned: changed
    
    .. option:: cpu
    
      Number of CPUs. The value of this attribute is one of "1", "2", "4", "8" or "16".
    
      :type: str
      :returned: always
    
    .. option:: service
    
      Service Package. Valid values are "FWBSTD" (Standard) or "FWBADV" (Advanced).
    
      :type: str
      :returned: always
  
  .. option:: fortiGateLCS
  
    FortiGate Virtual Machine - A La Carte Services.
  
    :type: dict
    :returned: changed
    
    .. option:: cpu
    
      The number of CPUs. A number between 1 and 96 (inclusive).
    
      :type: int
      :returned: always
    
    .. option:: fortiGuardServices
    
      The fortiguard services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["IPS", "AVDB", "FURL", "IOTH", "FGSA", "ISSS"].
    
      :type: list
      :returned: always
    
    .. option:: supportService
    
      Valid values are "FC247" (FortiCare 24x7) or "ASET" (FortiCare Elite).
    
      :type: str
      :returned: always
    
    .. option:: vdom
    
      Number of VDOMs. A number between 1 and 500 (inclusive).
    
      :type: int
      :returned: always
    
    .. option:: cloudServices
    
      The cloud services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["FAMS", "SWNM", "FMGC", "AFAC"].
    
      :type: list
      :returned: always
  
  .. option:: fortiAnalyzer
  
    FortiAnalyzer Virtual Machine.
  
    :type: dict
    :returned: changed
    
    .. option:: storage
    
      Daily Storage (GB). A number between 5 and 8300 (inclusive).
    
      :type: int
      :returned: always
    
    .. option:: adom
    
      Number of ADOMs. A number between 0 and 1200 (inclusive).
    
      :type: int
      :returned: always
    
    .. option:: service
    
      Support Service. Currently, the only available option is "FAZFC247" (FortiCare Premium). The default value is "FAZFC247".
    
      :type: str
      :returned: always
  
  .. option:: fortiPortal
  
    FortiPortal Virtual Machine.
  
    :type: dict
    :returned: changed
    
    .. option:: device
    
      Number of managed devices. A number between 0 and 100000 (inclusive).
    
      :type: str
      :returned: always

Authors
-------

- Xinwei Du (@DrMofu)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.