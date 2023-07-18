fortiflexvm_configs_update - Update a FortiFlex Configuration.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
This module update a FortiFlex Configuration under a program.

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

.. option:: id

  The ID of the configuration you want to update.

  :type: int
  :required: True

.. option:: name

  The name of your Flex VM Configuration.

  :type: str
  :required: False

.. option:: status

  Active of disable the configuration.

  :type: str
  :required: False
  :choices: ['ACTIVE', 'DISABLED']

.. option:: bypass_validation

  Only set to True when module schema diffs with FortiFlex API structure, module continues to execute without validating parameters.

  :type: bool
  :required: False
  :default: False

.. option:: check_parameters

  Check whether the parameters are set correctly before sending the data. If set to true, FortiFlexVM Ansible will check the parameter correctness based on the rules. It is only for debugging purposes, not recommended to set it as true since the rules in FortiFlexVM Ansible may be outdated.

  :type: bool
  :required: False
  :default: False

.. option:: fortiGateBundle

  FortiGate Virtual Machine - Service Bundle.

  :type: dict
  :required: False

  .. option:: cpu

    The number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16",  "32" or "2147483647" (unlimited).

  :type: str
  :required: True

  .. option:: service

    The value of this attribute is one of "FC" (FortiCare), "UTM", "ENT" (Enterprise) or "ATP".

  :type: str
  :required: True

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

  .. option:: service

    Service Package. Valid values are "FWBSTD" (Standard) or "FWBADV" (Advanced).

  :type: str
  :required: True

.. option:: fortiGateLCS

  FortiGate Virtual Machine - A La Carte Services.

  :type: dict
  :required: False

  .. option:: cpu

    The number of CPUs. A number between 1 and 96 (inclusive).

  :type: int
  :required: True

  .. option:: fortiGuardServices

    The fortiguard services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["IPS", "AVDB", "FGSA", "DLDB", "FAIS", "FURLDNS"].

  :type: list
  :required: False
  :default: []

  .. option:: supportService

    Valid values are "FC247" (FortiCare 24x7) or "ASET" (FortiCare Elite).

  :type: str
  :required: True

  .. option:: vdom

    Number of VDOMs. A number between 1 and 500 (inclusive).

  :type: int
  :required: True

  .. option:: cloudServices

    The cloud services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["FAMS", "SWNM", "AFAC", "FAZC"].

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

.. option:: fortiPortal

  FortiPortal Virtual Machine.

  :type: dict
  :required: False

  .. option:: device

    Number of managed devices. A number between 0 and 100000 (inclusive).

  :type: int
  :required: True

.. option:: fortiADC

  FortiADC Virtual Machine.

  :type: dict
  :required: False

  .. option:: cpu

    Number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16" or "32".

  :type: str
  :required: True

  .. option:: service

    Support Service. "FDVSTD" (Standard), "FDVADV" (Advanced) or "FDVFC247" (FortiCare Premium).

  :type: str
  :required: True

.. option:: fortiGateHardware

  FortiGate Hardware.

  :type: dict
  :required: False

  .. option:: model

    The device model. Possible values are FGT40F (FortiGate-40F), FGT60F (FortiGate-60F), FGT70F (FortiGate-70F), FGT80F (FortiGate-80F), FG100F (FortiGate-100F), FGT60E (FortiGate-60E), FGT61F (FortiGate-61F), FG100E (FortiGate-100E), FG101F (FortiGate-101F), FG200E (FortiGate-200E), FG200F (FortiGate-200F), FG201F (FortiGate-201F), FG4H0F (FortiGate-400F), FG6H0F (FortiGate-600F).

  :type: str
  :required: True

  .. option:: service

    Support Service. Possible values are FGHWFC247 (FortiCare Premium), FGHWFCEL (FortiCare Elite), FDVFC247 (ATP), FGHWUTP (UTP) or FGHWENT (Enterprise).

  :type: str
  :required: True

  .. option:: addons

    Addons. Only support "NONE" now, will support "FGHWFCELU" (FortiCare Elite Upgrade) in the future.

  :type: str
  :required: False
  :default: NONE


Examples
-------------

.. code-block:: yaml

  - name: Update a FortiFlex configuration
    hosts: localhost
    collections:
      - fortinet.fortiflexvm
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Update a FortiFlex configuration
        fortinet.fortiflexvm.fortiflexvm_configs_update:
          username: "{{ username }}"
          password: "{{ password }}"
          id: 3643
          name: "ansible_modify"
          status: "DISABLED" # ACTIVE or DISABLED
  
          # If FortiFlex API supports new params while FortiFlex Ansible does not support them yet,
          # you can set bypass_validation: true. The FortiFlex Ansible will allow you to use new param
          # without perforam any sanity check. The default value is false.
          bypass_validation: false
  
          # Check whether the parameters are set correctly before sending the data. The default value is false.
          # If set to true, FortiFlexVM Ansible will check the parameter correctness based on the rules.
          # It is only for debugging purposes, not recommended to set it as true since the rules in FortiFlexVM Ansible may be outdated.
          check_parameters: false
  
          # Please only use zero or one of the following.
          # If you want to update the configuration, please use the type you declared in fortiflexvm_configs_create.
  
          fortiGateBundle:
            cpu: "2"      # "1", "2", "4", "8", "16", "32", "2147483647"
            service: "FC" # "FC", "UTM", "ENT", "ATP"
            vdom: 10      # 0 ~ 500
  
          # fortiManager:
          #   device: 1                         # 1 ~ 100000
          #   adom: 1                           # 1 ~ 100000
  
          # fortiWeb:
          #   cpu: "4"                          # "1", "2", "4", "8", "16"
          #   service: "FWBSTD"                 # "FWBSTD" or "FWBADV"
  
          # fortiGateLCS:
          #   cpu: 4                            # 1 ~ 96
          #   fortiGuardServices: []            # "IPS", "AVDB", "FGSA", "DLDB", "FAIS", "FURLDNS"
          #   supportService: "FC247"           # "FC247", "ASET"
          #   vdom: 1                           # 1 ~ 500
          #   cloudServices: ["FAMS", "SWNM"]   # "FAMS", "SWNM", "AFAC", "FAZC"
  
          # fortiAnalyzer:
          #   storage: 5                        # 5 ~ 8300
          #   adom: 1                           # 0 ~ 1200
          #   service: "FAZFC247"               # "FAZFC247"
  
          # fortiPortal:
          #   device: 1                         # 0 ~ 100000
  
          # fortiADC:
          #   cpu: "1"                          # "1", "2", "4", "8", "16", "32"
          #   service: "FDVSTD"                 # "FDVSTD", "FDVADV" or "FDVFC247"
  
          # fortiGateHardware:
          #   model: "FGT40F"                   # "FGT40F", "FGT60F", "FGT70F", "FGT80F", "FG100F", "FGT60E", "FGT61F",
          #                                     # "FG100E", "FG101F", "FG200E", "FG200F", "FG201F", "FG4H0F", "FG6H0F"
          #   service: "FGHWFC247"              # "FGHWFC247", "FGHWFCEL", "FDVFC247", "FGHWUTP" or "FGHWENT"
          #   addons: "NONE"
  
        register: result
  
      - name: Display response
        debug:
          var: result.configs
  


Return Values
-------------

.. option:: configs

  The configuration you update.

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
    
      The fortiguard services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["IPS", "AVDB", "FGSA", "DLDB", "FAIS", "FURLDNS"].
    
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
    
      The cloud services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["FAMS", "SWNM", "AFAC", "FAZC"].
    
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
  
  .. option:: fortiADC
  
    FortiADC Virtual Machine.
  
    :type: dict
    :returned: changed
    
    .. option:: cpu
    
      Number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16" or "32".
    
      :type: str
      :returned: always
    
    .. option:: service
    
      Support Service. "FDVSTD" (Standard), "FDVADV" (Advanced) or "FDVFC247" (FortiCare Premium).
    
      :type: str
      :returned: always
  
  .. option:: fortiGateHardware
  
    FortiGate Hardware.
  
    :type: dict
    :returned: changed
    
    .. option:: model
    
      The device model. Possible values are FGT40F (FortiGate-40F), FGT60F (FortiGate-60F), FGT70F (FortiGate-70F), FGT80F (FortiGate-80F), FG100F (FortiGate-100F), FGT60E (FortiGate-60E), FGT61F (FortiGate-61F), FG100E (FortiGate-100E), FG101F (FortiGate-101F), FG200E (FortiGate-200E), FG200F (FortiGate-200F), FG201F (FortiGate-201F), FG4H0F (FortiGate-400F), FG6H0F (FortiGate-600F).
    
      :type: str
      :returned: always
    
    .. option:: service
    
      Support Service. Possible values are FGHWFC247 (FortiCare Premium), FGHWFCEL (FortiCare Elite), FDVFC247 (ATP), FGHWUTP (UTP) or FGHWENT (Enterprise).
    
      :type: str
      :returned: always
    
    .. option:: addons
    
      Addons. Only support "NONE" now, will support "FGHWFCELU" (FortiCare Elite Upgrade) in the future.
    
      :type: str
      :returned: always

Authors
-------

- Xinwei Du (@DrMofu)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.