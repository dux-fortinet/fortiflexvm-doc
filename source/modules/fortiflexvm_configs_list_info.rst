fortiflexvm_configs_list_info - Get list of FortiFlex Configurations.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
This module retrieves a list of configs from FortiFlexVM API using the provided credentials and program serial number.

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

.. option:: programSerialNumber

  The serial number of the program to get configs for.

  :type: str
  :required: True


Examples
-------------

.. code-block:: yaml

  - name: Get list of FortiFlex Configurations for a Program
    hosts: localhost
    collections:
      - fortinet.fortiflexvm
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Get configs list
        fortinet.fortiflexvm.fortiflexvm_configs_list_info:
          username: "{{ username }}"
          password: "{{ password }}"
          programSerialNumber: "ELAVMS000000XXXX"
        register: result
  
      - name: Display response
        debug:
          var: result.configs
  


Return Values
-------------

.. option:: configs

  List of configurations for the specified program serial number.

  :type: list
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