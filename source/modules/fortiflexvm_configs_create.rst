fortiflexvm_configs_create - Create a new FortiFlex Configuration.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 1

Synopsis
--------
This module creates a new FortiFlex Configuration under a program.

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

.. option:: accountId

  Account ID.

  :type: int
  :required: False

.. option:: programSerialNumber

  The serial number of your Flex VM Program.

  :type: str
  :required: True

.. option:: name

  The name of your Flex VM Configuration.

  :type: str
  :required: True

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

    The value of this attribute is one of "FC" (FortiCare), "UTP", "ENT" (Enterprise) or "ATP".

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

.. option:: fortiClientEMSOP

  FortiClient EMS On-Prem.

  :type: dict
  :required: False

  .. option:: ZTNA

    ZTNA/VPN (number of endpoints). Number between 0 and 25000 (inclusive). Value should be divisible by 25.

  :type: int
  :required: True

  .. option:: EPP

    EPP/ATP + ZTNA/VPN (number of endpoints). Number between 0 and 25000 (inclusive). Value should be divisible by 25.

  :type: int
  :required: True

  .. option:: chromebook

    Chromebook (number of endpoints). Number between 0 and 25000 (inclusive). Value should be divisible by 25.

  :type: int
  :required: True

  .. option:: service

    Support Services. Possible value is "FCTFC247" (FortiCare Premium)

  :type: str
  :required: True

  .. option:: addons

    A d d o n s .   A   l i s t .   P o s s i b l e   v a l u e   i s   " B P S "   (   F o r t i C a r e   B e s t   P r a c t i c e ) .

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

    The device model. Possible values are FGT40F (FortiGate-40F), FGT60F (FortiGate-60F), FGT70F (FortiGate-70F), FGT80F (FortiGate-80F), FG100F (FortiGate-100F), FGT60E (FortiGate-60E), FGT61F (FortiGate-61F), FG100E (FortiGate-100E), FG101F (FortiGate-101F), FG200E (FortiGate-200E), FG200F (FortiGate-200F), FG201F (FortiGate-201F), FG4H0F (FortiGate-400F), FG6H0F (FortiGate-600F), FWF40F (FortiWifi-40F), FWF60F (FortiWifi-60F), FGR60F (FortiGateRugged-60F), FR70FB (FortiGateRugged-70F), FGT81F (FortiGate-81F), FG101E (FortiGate-101E), FG4H1F (FortiGate-401F), FG1K0F (FortiGate-1000F), FG180F (FortiGate-1800F), F2K60F (FortiGate-2600F), FG3K0F (FortiGate-3000F), FG3K1F (FortiGate-3001F), FG3K2F (FortiGate-3200F).

  :type: str
  :required: True

  .. option:: service

    Support Service. Possible values are FGHWFC247 (FortiCare Premium), FGHWFCEL (FortiCare Elite), FDVFC247 (ATP), FGHWUTP (UTP) or FGHWENT (Enterprise).

  :type: str
  :required: True

  .. option:: addons

    Addons. A list, can be empty, possible values are FGHWFCELU (FortiCare Elite Upgrade), FGHWFAMS (FortiGate Cloud Management), FGHWFAIS (AI-Based In-line Sandbox), FGHWSWNM (SD-WAN Underlay), FGHWDLDB (FortiGuard DLP), FGHWFAZC (FortiAnalyzer Cloud), FGHWSOCA (SOCaaS), FGHWMGAS (Managed FortiGate), FGHWSPAL (SD-WAN Connector for FortiSASE), FGHWFCSS (FortiConverter Service).

  :type: list
  :required: False
  :default: []

.. option:: fortiCloudPrivate

  FortiWeb Cloud, Private.

  :type: dict
  :required: False

  .. option:: throughput

    Average Throughput (Mbps). Possible values are 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000.

  :type: int
  :required: True

  .. option:: applications

    N u m b e r   o f   w e b   a p p l i c a t i o n s .   N u m b e r   b e t w e e n   0   a n d   2 0 0 0   ( i n c l u s i v e ) .

  :type: int
  :required: True

.. option:: fortiCloudPublic

  FortiWeb Cloud, Public.

  :type: dict
  :required: False

  .. option:: throughput

    Average Throughput (Mbps). Possible values are 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000.

  :type: int
  :required: True

  .. option:: applications

    N u m b e r   o f   w e b   a p p l i c a t i o n s .   N u m b e r   b e t w e e n   0   a n d   2 0 0 0   ( i n c l u s i v e ) .

  :type: int
  :required: True


Examples
-------------

.. code-block:: yaml

  - name: Create entitlement configuration
    hosts: localhost
    collections:
      - fortinet.fortiflexvm
    vars:
      username: "<your_own_value>"
      password: "<your_own_value>"
    tasks:
      - name: Create a configuration
        fortinet.fortiflexvm.fortiflexvm_configs_create:
          username: "{{ username }}"
          password: "{{ password }}"
          programSerialNumber: "ELAVMS000000XXXX"
          name: "ansible"
  
          # If FortiFlex API supports new params while FortiFlex Ansible does not support them yet,
          # you can set bypass_validation: true. The FortiFlex Ansible will allow you to use new param
          # without perforam any sanity check. The default value is false.
          bypass_validation: false
  
          # Check whether the parameters are set correctly before sending the data. The default value is false.
          # If set to true, FortiFlexVM Ansible will check the parameter correctness based on the rules.
          # It is only for debugging purposes, not recommended to set it as true since the rules in FortiFlexVM Ansible may be outdated.
          check_parameters: false
  
          # Please only use one of the following.
          fortiGateBundle:
            cpu: "2"                            # "1", "2", "4", "8", "16", "32", "2147483647"
            service: "UTP"                      # "FC", "UTP", "ENT", "ATP"
            vdom: 10                            # 0 ~ 500
  
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
  
          # fortiClientEMSOP:
          #   ZTNA: 1000                        # 0 ~ 25000. Value should be divisible by 25.
          #   EPP: 1000                         # 0 ~ 25000. Value should be divisible by 25.
          #   chromebook: 1000                  # 0 ~ 25000. Value should be divisible by 25.
          #   service: "FCTFC247"               # "FCTFC247"
          #   addons: ["BPS"]                   # Empty or "BPS"
  
          # fortiAnalyzer:
          #   storage: 5                        # 5 ~ 8300
          #   adom: 1                           # 0 ~ 1200
          #   service: "FAZFC247"               # "FAZFC247"
  
          # fortiPortal:
          #   device: 1                         # 0 ~ 100000
  
          # fortiADC:
          #   cpu: "32"                         # "1", "2", "4", "8", "16", "32"
          #   service: "FDVSTD"                 # "FDVSTD", "FDVADV" or "FDVFC247"
  
          # fortiGateHardware:
          #   model: "FGT60F"                   # "FGT40F", "FGT60F", "FGT70F", "FGT80F", "FG100F", "FGT60E", "FGT61F",
          #                                     # "FG100E", "FG101F", "FG200E", "FG200F", "FG201F", "FG4H0F", "FG6H0F",
          #                                     # "FWF40F", "FWF60F", "FGR60F", "FR70FB", "FGT81F", "FG101E", "FG4H1F",
          #                                     # "FG1K0F", "FG180F", "F2K60F", "FG3K0F", "FG3K1F", "FG3K2F"
          #   service: "FGHWFCEL"               # "FGHWFC247", "FGHWFCEL", "FDVFC247", "FGHWUTP" or "FGHWENT"
          #   addons: []                        # "FGHWFCELU", "FGHWFAMS", "FGHWFAIS", "FGHWSWNM", "FGHWDLDB",
          #                                     # "FGHWFAZC", "FGHWSOCA", "FGHWMGAS", "FGHWSPAL", "FGHWFCSS"
  
          # fortiCloudPrivate:
          #   throughput: 100                   # 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800,
          #                                     # 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
          #                                     # 7000, 7500, 8000, 8500, 9000, 9500, 10000.
          #   applications: 10                  # 0 ~ 2000
  
          # fortiCloudPublic:
          #   throughput: 100                   # 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800,
          #                                     # 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
          #                                     # 7000, 7500, 8000, 8500, 9000, 9500, 10000.
          #   applications: 10                  # 0 ~ 2000
  
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
  
  .. option:: accountId
  
    The ID of the account associated with the program.
  
    :type: int
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
    
    .. option:: cpu
    
      The number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16",  "32" or "2147483647" (unlimited).
    
      :type: str
      :returned: always
    
    .. option:: service
    
      The value of this attribute is one of "FC" (FortiCare), "UTP", "ENT" (Enterprise) or "ATP".
    
      :type: str
      :returned: always
    
    .. option:: vdom
    
      Number of VDOMs. A number between 0 and 500 (inclusive). The default number is 0.
    
      :type: int
      :returned: always
  
  .. option:: fortiManager
  
    FortiManager Virtual Machine.
  
    :type: dict
    
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
  
  .. option:: fortiClientEMSOP
  
    FortiClient EMS On-Prem.
  
    :type: dict
    
    .. option:: ZTNA
    
      ZTNA/VPN (number of endpoints). Number between 0 and 25000 (inclusive). Value should be divisible by 25.
    
      :type: int
      :returned: always
    
    .. option:: EPP
    
      EPP/ATP + ZTNA/VPN (number of endpoints). Number between 0 and 25000 (inclusive). Value should be divisible by 25.
    
      :type: int
      :returned: always
    
    .. option:: chromebook
    
      Chromebook (number of endpoints). Number between 0 and 25000 (inclusive). Value should be divisible by 25.
    
      :type: int
      :returned: always
    
    .. option:: service
    
      Support Services. Possible value is "FCTFC247" (FortiCare Premium)
    
      :type: str
      :returned: always
    
    .. option:: addons
    
      Addons. A list. Possible value is "BPS" ( FortiCare Best Practice).
    
      :type: list
  
  .. option:: fortiAnalyzer
  
    FortiAnalyzer Virtual Machine.
  
    :type: dict
    
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
    
    .. option:: device
    
      Number of managed devices. A number between 0 and 100000 (inclusive).
    
      :type: str
      :returned: always
  
  .. option:: fortiADC
  
    FortiADC Virtual Machine.
  
    :type: dict
    
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
    
    .. option:: model
    
      The device model. Possible values are FGT40F (FortiGate-40F), FGT60F (FortiGate-60F), FGT70F (FortiGate-70F), FGT80F (FortiGate-80F), FG100F (FortiGate-100F), FGT60E (FortiGate-60E), FGT61F (FortiGate-61F), FG100E (FortiGate-100E), FG101F (FortiGate-101F), FG200E (FortiGate-200E), FG200F (FortiGate-200F), FG201F (FortiGate-201F), FG4H0F (FortiGate-400F), FG6H0F (FortiGate-600F), FWF40F (FortiWifi-40F), FWF60F (FortiWifi-60F), FGR60F (FortiGateRugged-60F), FR70FB (FortiGateRugged-70F), FGT81F (FortiGate-81F), FG101E (FortiGate-101E), FG4H1F (FortiGate-401F), FG1K0F (FortiGate-1000F), FG180F (FortiGate-1800F), F2K60F (FortiGate-2600F), FG3K0F (FortiGate-3000F), FG3K1F (FortiGate-3001F), FG3K2F (FortiGate-3200F).
    
      :type: str
      :returned: always
    
    .. option:: service
    
      Support Service. Possible values are FGHWFC247 (FortiCare Premium), FGHWFCEL (FortiCare Elite), FDVFC247 (ATP), FGHWUTP (UTP) or FGHWENT (Enterprise).
    
      :type: str
      :returned: always
    
    .. option:: addons
    
      Addons. Possible values are NONE, FGHWFCELU (FortiCare Elite Upgrade), FGHWFAMS (FortiGate Cloud Management), FGHWFAIS (AI-Based In-line Sandbox), FGHWSWNM (SD-WAN Underlay), FGHWDLDB (FortiGuard DLP), FGHWFAZC (FortiAnalyzer Cloud), FGHWSOCA (SOCaaS), FGHWMGAS (Managed FortiGate), FGHWSPAL (SD-WAN Connector for FortiSASE), FGHWFCSS (FortiConverter Service).
    
      :type: list
      :returned: always
  
  .. option:: fortiCloudPrivate
  
    FortiWeb Cloud, Private.
  
    :type: dict
    
    .. option:: throughput
    
      Average Throughput (Mbps). Possible values are 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000.
    
      :type: int
      :returned: always
    
    .. option:: applications
    
      Number of web applications. Number between 0 and 2000 (inclusive).
    
      :type: int
      :returned: always
  
  .. option:: fortiCloudPublic
  
    FortiWeb Cloud, Public.
  
    :type: dict
    
    .. option:: throughput
    
      Average Throughput (Mbps). Possible values are 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000.
    
      :type: int
      :returned: always
    
    .. option:: applications
    
      Number of web applications. Number between 0 and 2000 (inclusive).
    
      :type: int
      :returned: always

Authors
-------

- Xinwei Du (@DrMofu)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.