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

.. option:: password

  The password to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_PASSWORD.

  :type: str

.. option:: accountId

  Account ID.

  :type: int

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
  :default: False

.. option:: check_parameters

  Check whether the parameters are set correctly before sending the data. If set to true, FortiFlexVM Ansible will check the parameter correctness based on the rules. It is only for debugging purposes, not recommended to set it as true since the rules in FortiFlexVM Ansible may be outdated.

  :type: bool
  :default: False

.. option:: fortiGateBundle

  FortiGate Virtual Machine - Service Bundle.

  :type: dict

  .. option:: cpu

    The number of CPUs. Number between 1 and 96 (inclusive).

    :type: int
    :required: True

  .. option:: service

    The value of this attribute is one of "FC" (FortiCare), "UTP", "ENT" (Enterprise) or "ATP".

    :type: str
    :required: True

  .. option:: vdom

    Number of VDOMs. A number between 0 and 500 (inclusive). The default number is 0.

    :type: int
    :default: 0

  .. option:: fortiGuardServices

    Fortiguard Services. The default value is an empty list. It should contain zero, one or more elements of ["FGTAVDB", "FGTFAIS", "FGTISSS", "FGTDLDB", "FGTFGSA", "FGTFCSS"].

    :type: list
    :default: []

  .. option:: cloudServices

    Cloud Services. The default value is an empty list. It should contain zero, one or more elements of ["FGTFAMS", "FGTSWNM", "FGTSOCA", "FGTFAZC", "FGTSWOS", "FGTFSPA"].

    :type: list
    :default: []

  .. option:: supportService

    Suport service. "FGTFCELU" or "NONE". Default is "NONE".

    :type: str
    :default: NONE

.. option:: fortiManager

  FortiManager Virtual Machine.

  :type: dict

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

  .. option:: cpu

    The number of CPUs. A number between 1 and 96 (inclusive).

    :type: int
    :required: True

  .. option:: fortiGuardServices

    The fortiguard services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["IPS", "AVDB", "FGSA", "DLDB", "FAIS", "FURLDNS"].

    :type: list
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
    :default: []

.. option:: fortiClientEMSOP

  FortiClient EMS On-Prem.

  :type: dict

  .. option:: ZTNA

    ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.

    :type: int
    :required: True

  .. option:: EPP

    EPP/ATP + ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.

    :type: int
    :required: True

  .. option:: chromebook

    Chromebook (number of endpoints). Value should be 0 or between 25 and 25000.

    :type: int
    :required: True

  .. option:: service

    Support Services. Possible value is "FCTFC247" (FortiCare Premium)

    :type: str
    :required: True

  .. option:: addons

    Addons. A list. Possible value is "BPS" ( FortiCare Best Practice).

    :type: list
    :default: []

.. option:: fortiAnalyzer

  FortiAnalyzer Virtual Machine.

  :type: dict

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

  .. option:: device

    Number of managed devices. A number between 0 and 100000 (inclusive).

    :type: int
    :required: True

.. option:: fortiADC

  FortiADC Virtual Machine.

  :type: dict

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

  .. option:: model

    The device model. For all supported models, please check FNDN. Possible values are FGT40F (FortiGate-40F), FGT60F (FortiGate-60F), FGT70F (FortiGate-70F), FGT80F (FortiGate-80F), FG100F (FortiGate-100F), FGT60E (FortiGate-60E), FGT61F (FortiGate-61F), FG100E (FortiGate-100E), FG101F (FortiGate-101F), FG200E (FortiGate-200E), FG200F (FortiGate-200F), FG201F (FortiGate-201F), FG4H0F (FortiGate-400F), FG6H0F (FortiGate-600F), FWF40F (FortiWifi-40F), FWF60F (FortiWifi-60F), FGR60F (FortiGateRugged-60F), FR70FB (FortiGateRugged-70F), FGT81F (FortiGate-81F), FG101E (FortiGate-101E), FG4H1F (FortiGate-401F), FG1K0F (FortiGate-1000F), FG180F (FortiGate-1800F), F2K60F (FortiGate-2600F), FG3K0F (FortiGate-3000F), FG3K1F (FortiGate-3001F), FG3K2F (FortiGate-3200F).

    :type: str
    :required: True

  .. option:: service

    Support Service. Possible values are FGHWFC247 (FortiCare Premium), FGHWFCEL (FortiCare Elite), FDVFC247 (ATP), FGHWUTP (UTP) or FGHWENT (Enterprise).

    :type: str
    :required: True

  .. option:: addons

    Addons. A list, can be empty, possible values are FGHWFCELU (FortiCare Elite Upgrade), FGHWFAMS (FortiGate Cloud Management), FGHWFAIS (AI-Based In-line Sandbox), FGHWSWNM (SD-WAN Underlay), FGHWDLDB (FortiGuard DLP), FGHWFAZC (FortiAnalyzer Cloud), FGHWSOCA (SOCaaS), FGHWMGAS (Managed FortiGate), FGHWSPAL (SD-WAN Connector for FortiSASE), FGHWFCSS (FortiConverter Service).

    :type: list
    :default: []

.. option:: fortiCloudPrivate

  FortiWeb Cloud, Private.

  :type: dict

  .. option:: throughput

    Average Throughput (Mbps). Possible values are 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000.

    :type: int
    :required: True

  .. option:: applications

    Number of web applications. Number between 0 and 2000 (inclusive).

    :type: int
    :required: True

.. option:: fortiCloudPublic

  FortiWeb Cloud, Public.

  :type: dict

  .. option:: throughput

    Average Throughput (Mbps). Possible values are 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000.

    :type: int
    :required: True

  .. option:: applications

    Number of web applications. Number between 0 and 2000 (inclusive).

    :type: int
    :required: True

.. option:: fortiClientEMSCloud

  FortiClient EMS Cloud.

  :type: dict

  .. option:: ZTNA

    ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.

    :type: int
    :required: True

  .. option:: ZTNA_FGF

    ZTNA/VPN + FortiGuard Forensics (number of endpoints). Value should be 0 or between 25 and 25000.

    :type: int
    :required: True

  .. option:: EPP_ZTNA

    EPP/ATP + ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.

    :type: int
    :required: True

  .. option:: EPP_ZTNA_FGF

    EPP/ATP + ZTNA/VPN + FortiGuard Forensics (number of endpoints). Value should be 0 or between 25 and 25000.

    :type: int
    :required: True

  .. option:: chromebook

    Chromebook (number of endpoints). Value should be 0 or between 25 and 25000.

    :type: int
    :required: True

  .. option:: addons

    Addons. A list. Possible value is "BPS" (FortiCare Best Practice).

    :type: list
    :default: []

.. option:: fortiSASE

  fortiSASE Cloud Configuration.

  :type: dict

  .. option:: users

    Number of users. Number between 50 and 50,000 (inclusive). Value should be divisible by 25.

    :type: int
    :required: True

  .. option:: service

    Service package. "FSASESTD" (Standard) or "FSASEADV" (Advanced).

    :type: str
    :required: True

  .. option:: bandwidth

    Number between 25 and 10,000 (inclusive). Value should be divisible by 25.

    :type: int
    :required: True

  .. option:: dedicatedIPs

    Number between 4 and 65,534 (inclusive).

    :type: int
    :required: True

.. option:: fortiEDR

  fortiEDR Cloud Configuration.

  :type: dict

  .. option:: service

    Service package. "FEDRPDR" (Discover/Protect/Respond).

    :type: str
    :required: True

  .. option:: addons

    Addons. A list. Possible value is "FEDRXDR" (XDR).

    :type: list
    :default: []


Examples
-------------

.. code-block:: yaml

  - name: Create entitlement configuration
    hosts: localhost
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
            cpu: 2                              # 1 ~ 96
            service: "UTP"                      # "FC", "UTP", "ENT", "ATP"
            vdom: 10                            # 0 ~ 500
            fortiGuardServices: ["FGTFAIS"]     # ["FGTAVDB", "FGTFAIS", "FGTISSS", "FGTDLDB", "FGTFGSA", "FGTFCSS"]
            cloudServices: ["FGTFAMS"]          # ["FGTFAMS", "FGTSWNM", "FGTSOCA", "FGTFAZC", "FGTSWOS", "FGTFSPA"]
            supportService: "NONE"              # "FGTFCELU", "NONE"
  
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
          #   ZTNA: 1000                        # Value should be 0 or between 25 and 25000.
          #   EPP: 1000                         # Value should be 0 or between 25 and 25000.
          #   chromebook: 1000                  # Value should be 0 or between 25 and 25000.
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
          #   model: "FGT60F"                   # For all supported modules, please check FNDN.
          #                                     # "FGT40F", "FGT60F", "FGT70F", "FGT80F", "FG100F", "FGT60E", "FGT61F",
          #                                     # "FG100E", "FG101F", "FG200E", "FG200F", "FG201F", "FG4H0F", "FG6H0F",
          #                                     # "FWF40F", "FWF60F", "FGR60F", "FR70FB", "FGT81F", "FG101E", "FG4H1F",
          #                                     # "FG1K0F", "FG180F", "F2K60F", "FG3K0F", "FG3K1F", "FG3K2F"...
          #   service: "FGHWFCEL"               # "FGHWFC247", "FGHWFCEL", "FDVFC247", "FGHWUTP" or "FGHWENT"
          #   addons: []                        # "FGHWFCELU", "FGHWFAMS", "FGHWFAIS", "FGHWSWNM", "FGHWDLDB",
          #                                     # "FGHWFAZC", "FGHWSOCA", "FGHWMGAS", "FGHWSPAL", "FGHWFCSS"
  
          # fortiCloudPrivate:
          #   throughput: 100                   # 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800,
          #                                     # 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
          #                                     # 7000, 7500, 8000, 8500, 9000, 9500, 10000.
          #   applications: 10                  # 0 ~ 2000
  
          # fortiCloudPublic:
          #   throughput: 100                   # 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800,
          #                                     # 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
          #                                     # 7000, 7500, 8000, 8500, 9000, 9500, 10000.
          #   applications: 10                  # 0 ~ 2000
  
          # fortiClientEMSCloud:
          #   ZTNA: 100                         # Value should be 0 or between 25 and 25000.
          #   ZTNA_FGF: 100                     # Value should be 0 or between 25 and 25000.
          #   EPP_ZTNA: 100                     # Value should be 0 or between 25 and 25000.
          #   EPP_ZTNA_FGF: 100                 # Value should be 0 or between 25 and 25000.
          #   chromebook: 100                   # Value should be 0 or between 25 and 25000.
          #   addons: ["BPS"]                   # [] or "BPS"
  
          # fortiSASE:
          #   users: 50                         # 50 ~ 50000. Value should be divisible by 25.
          #   service: "FSASESTD"               # "FSASESTD" (Standard) or "FSASEADV" (Advanced).
          #   bandwidth: 100                    # 25 ~ 10000. Value should be divisible by 25.
          #   dedicatedIPs: 10                  # 4 ~ 65534
  
          # fortiEDR:
          #   service: "FEDRPDR"                # "FEDRPDR" (Discover/Protect/Respond)
          #   addons: ["FEDRXDR"]               # Empty list or "FEDRXDR"
  
        register: result
  
      - name: Display response
        ansible.builtin.debug:
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
    
      :type: int
    
    .. option:: service
    
      The value of this attribute is one of "FC" (FortiCare), "UTP", "ENT" (Enterprise) or "ATP".
    
      :type: str
    
    .. option:: vdom
    
      Number of VDOMs. A number between 0 and 500 (inclusive). The default number is 0.
    
      :type: int
    
    .. option:: fortiGuardServices
    
      Fortiguard Services. The default value is an empty list. It should contain zero, one or more elements of ["FGTAVDB", "FGTFAIS", "FGTISSS", "FGTDLDB", "FGTFGSA", "FGTFCSS"].
    
      :type: list
    
    .. option:: cloudServices
    
      Cloud Services. The default value is an empty list. It should contain zero, one or more elements of ["FGTFAMS", "FGTSWNM", "FGTSOCA", "FGTFAZC", "FGTSWOS", "FGTFSPA"].
    
      :type: list
    
    .. option:: supportService
    
      Suport service. "FGTFCELU" or "NONE". Default is "NONE".
    
      :type: str
  
  .. option:: fortiManager
  
    FortiManager Virtual Machine.
  
    :type: dict
    
    .. option:: device
    
      Number of managed devices. A number between 1 and 100000 (inclusive).
    
      :type: int
    
    .. option:: adom
    
      Number of ADOMs. A number between 1 and 100000 (inclusive).
    
      :type: int
  
  .. option:: fortiWeb
  
    FortiWeb Virtual Machine - Service Bundle.
  
    :type: dict
    
    .. option:: cpu
    
      Number of CPUs. The value of this attribute is one of "1", "2", "4", "8" or "16".
    
      :type: str
    
    .. option:: service
    
      Service Package. Valid values are "FWBSTD" (Standard) or "FWBADV" (Advanced).
    
      :type: str
  
  .. option:: fortiGateLCS
  
    FortiGate Virtual Machine - A La Carte Services.
  
    :type: dict
    
    .. option:: cpu
    
      The number of CPUs. A number between 1 and 96 (inclusive).
    
      :type: int
    
    .. option:: fortiGuardServices
    
      The fortiguard services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["IPS", "AVDB", "FGSA", "DLDB", "FAIS", "FURLDNS"].
    
      :type: list
    
    .. option:: supportService
    
      Valid values are "FC247" (FortiCare 24x7) or "ASET" (FortiCare Elite).
    
      :type: str
    
    .. option:: vdom
    
      Number of VDOMs. A number between 1 and 500 (inclusive).
    
      :type: int
    
    .. option:: cloudServices
    
      The cloud services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["FAMS", "SWNM", "AFAC", "FAZC"].
    
      :type: list
  
  .. option:: fortiClientEMSOP
  
    FortiClient EMS On-Prem.
  
    :type: dict
    
    .. option:: ZTNA
    
      ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.
    
      :type: int
    
    .. option:: EPP
    
      EPP/ATP + ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.
    
      :type: int
    
    .. option:: chromebook
    
      Chromebook (number of endpoints). Value should be 0 or between 25 and 25000.
    
      :type: int
    
    .. option:: service
    
      Support Services. Possible value is "FCTFC247" (FortiCare Premium)
    
      :type: str
    
    .. option:: addons
    
      Addons. A list. Possible value is "BPS" ( FortiCare Best Practice).
    
      :type: list
  
  .. option:: fortiAnalyzer
  
    FortiAnalyzer Virtual Machine.
  
    :type: dict
    
    .. option:: storage
    
      Daily Storage (GB). A number between 5 and 8300 (inclusive).
    
      :type: int
    
    .. option:: adom
    
      Number of ADOMs. A number between 0 and 1200 (inclusive).
    
      :type: int
    
    .. option:: service
    
      Support Service. Currently, the only available option is "FAZFC247" (FortiCare Premium). The default value is "FAZFC247".
    
      :type: str
  
  .. option:: fortiPortal
  
    FortiPortal Virtual Machine.
  
    :type: dict
    
    .. option:: device
    
      Number of managed devices. A number between 0 and 100000 (inclusive).
    
      :type: str
  
  .. option:: fortiADC
  
    FortiADC Virtual Machine.
  
    :type: dict
    
    .. option:: cpu
    
      Number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16" or "32".
    
      :type: str
    
    .. option:: service
    
      Support Service. "FDVSTD" (Standard), "FDVADV" (Advanced) or "FDVFC247" (FortiCare Premium).
    
      :type: str
  
  .. option:: fortiGateHardware
  
    FortiGate Hardware.
  
    :type: dict
    
    .. option:: model
    
      The device model. Possible values are FGT40F (FortiGate-40F), FGT60F (FortiGate-60F), FGT70F (FortiGate-70F), FGT80F (FortiGate-80F), FG100F (FortiGate-100F), FGT60E (FortiGate-60E), FGT61F (FortiGate-61F), FG100E (FortiGate-100E), FG101F (FortiGate-101F), FG200E (FortiGate-200E), FG200F (FortiGate-200F), FG201F (FortiGate-201F), FG4H0F (FortiGate-400F), FG6H0F (FortiGate-600F), FWF40F (FortiWifi-40F), FWF60F (FortiWifi-60F), FGR60F (FortiGateRugged-60F), FR70FB (FortiGateRugged-70F), FGT81F (FortiGate-81F), FG101E (FortiGate-101E), FG4H1F (FortiGate-401F), FG1K0F (FortiGate-1000F), FG180F (FortiGate-1800F), F2K60F (FortiGate-2600F), FG3K0F (FortiGate-3000F), FG3K1F (FortiGate-3001F), FG3K2F (FortiGate-3200F)...
    
      :type: str
    
    .. option:: service
    
      Support Service. Possible values are FGHWFC247 (FortiCare Premium), FGHWFCEL (FortiCare Elite), FDVFC247 (ATP), FGHWUTP (UTP) or FGHWENT (Enterprise).
    
      :type: str
    
    .. option:: addons
    
      Addons. Possible values are NONE, FGHWFCELU (FortiCare Elite Upgrade), FGHWFAMS (FortiGate Cloud Management), FGHWFAIS (AI-Based In-line Sandbox), FGHWSWNM (SD-WAN Underlay), FGHWDLDB (FortiGuard DLP), FGHWFAZC (FortiAnalyzer Cloud), FGHWSOCA (SOCaaS), FGHWMGAS (Managed FortiGate), FGHWSPAL (SD-WAN Connector for FortiSASE), FGHWFCSS (FortiConverter Service).
    
      :type: list
  
  .. option:: fortiCloudPrivate
  
    FortiWeb Cloud, Private.
  
    :type: dict
    
    .. option:: throughput
    
      Average Throughput (Mbps). Possible values are 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000.
    
      :type: int
    
    .. option:: applications
    
      Number of web applications. Number between 0 and 2000 (inclusive).
    
      :type: int
  
  .. option:: fortiCloudPublic
  
    FortiWeb Cloud, Public.
  
    :type: dict
    
    .. option:: throughput
    
      Average Throughput (Mbps). Possible values are 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000.
    
      :type: int
    
    .. option:: applications
    
      Number of web applications. Number between 0 and 2000 (inclusive).
    
      :type: int
  
  .. option:: fortiClientEMSCloud
  
    FortiClient EMS Cloud.
  
    :type: dict
    
    .. option:: ZTNA
    
      ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.
    
      :type: int
    
    .. option:: ZTNA_FGF
    
      ZTNA/VPN + FortiGuard Forensics (number of endpoints). Value should be 0 or between 25 and 25000.
    
      :type: int
    
    .. option:: EPP_ZTNA
    
      EPP/ATP + ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.
    
      :type: int
    
    .. option:: EPP_ZTNA_FGF
    
      EPP/ATP + ZTNA/VPN + FortiGuard Forensics (number of endpoints). Value should be 0 or between 25 and 25000.
    
      :type: int
    
    .. option:: chromebook
    
      Chromebook (number of endpoints). Value should be 0 or between 25 and 25000.
    
      :type: int
    
    .. option:: addons
    
      Addons. A list. Possible value is "BPS" ( FortiCare Best Practice).
    
      :type: list
  
  .. option:: fortiSASE
  
    fortiSASE Cloud Configuration.
  
    :type: dict
    
    .. option:: users
    
      Number of users. Number between 50 and 50,000 (inclusive). Number between 50 and 50,000 (inclusive). Value should be divisible by 25.
    
      :type: int
    
    .. option:: service
    
      Service package. "FSASESTD" (Standard) or "FSASEADV" (Advanced).
    
      :type: str
    
    .. option:: bandwidth
    
      Number between 25 and 10,000 (inclusive). Value should be divisible by 25.
    
      :type: int
    
    .. option:: dedicatedIPs
    
      Number between 4 and 65,534 (inclusive).
    
      :type: int
  
  .. option:: fortiEDR
  
    fortiEDR Cloud Configuration.
  
    :type: dict
    
    .. option:: service
    
      Service package. "FEDRPDR" (Discover/Protect/Respond).
    
      :type: str
    
    .. option:: endpoints
    
      Number of Endpoints. Read only.
    
      :type: int
    
    .. option:: addons
    
      Addons. A list. Possible value is "FEDRXDR" (XDR).
    
      :type: list

Authors
-------

- Xinwei Du (@dux-fortinet)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.