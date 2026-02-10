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

- ansible>=2.15


Parameters
----------
.. raw:: html

 <ul>
 <li><span class="li-head">username</span> The username to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_USERNAME.<span class="li-normal">type: str</span></li>
 <li><span class="li-head">password</span> The password to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_PASSWORD.<span class="li-normal">type: str</span></li>
 <li><span class="li-head">accountId</span> Account ID.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">programSerialNumber</span> The serial number of your Flex VM Program.<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">name</span> The name of your Flex VM Configuration.<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">bypass_validation</span> Only set to True when module schema diffs with FortiFlex API structure, module continues to execute without validating parameters.<span class="li-normal">type: bool</span><span class="li-normal">default: False</span></li>
 <li><span class="li-head">check_parameters</span> Check whether the parameters are set correctly before sending the data. If set to true, FortiFlexVM Ansible will check the parameter correctness based on the rules. It is only for debugging purposes, not recommended to set it as true since the rules in FortiFlexVM Ansible may be outdated.<span class="li-normal">type: bool</span><span class="li-normal">default: False</span></li>
 <li><span class="li-head">fortiGateBundle</span> FortiGate Virtual Machine - Service Bundle.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">cpu</span> The number of CPUs. Number between 1 and 96 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">service</span> The value of this attribute is one of "FC" (FortiCare), "UTP", "ENT" (Enterprise) or "ATP".<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">vdom</span> Number of VDOMs. A number between 0 and 500 (inclusive). The default number is 0.<span class="li-normal">type: int</span><span class="li-normal">default: 0</span></li>
 <li><span class="li-head">fortiGuardServices</span> Fortiguard Services. The default value is an empty list. It should contain zero, one or more elements of ["FGTAVDB", "FGTFAIS", "FGTISSS", "FGTDLDB", "FGTFGSA"].<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 <li><span class="li-head">cloudServices</span> Cloud Services. The default value is an empty list. It should contain zero, one or more elements of ["FGTFAMS", "FGTSWNM", "FGTSOCA", "FGTFAZC", "FGTSWOS", "FGTFSPA"].<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 <li><span class="li-head">supportService</span> Suport service. "FGTFCELU" or "NONE". Default is "NONE".<span class="li-normal">type: str</span><span class="li-normal">default: NONE</span></li>
 </ul> <li><span class="li-head">fortiManager</span> FortiManager Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">device</span> Number of managed devices. A number between 1 and 100000 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">adom</span> Number of ADOMs. A number between 0 and 100000 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 </ul> <li><span class="li-head">fortiWeb</span> FortiWeb Virtual Machine - Service Bundle.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">cpu</span> Number of CPUs. The value of this attribute is one of "1", "2" "4", "8" or "16".<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">service</span> Service Package. Valid values are "FWBSTD" (Standard), "FWBADV" (Advanced) or "FWBENT" (Advanced).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 </ul> <li><span class="li-head">fortiGateLCS</span> FortiGate Virtual Machine - A La Carte Services.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">cpu</span> The number of CPUs. A number between 1 and 96 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">fortiGuardServices</span> The fortiguard services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["IPS", "AVDB", "FURLDNS", "FGSA", "ISSS", "DLDB", "FAIS"].<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 <li><span class="li-head">supportService</span> Valid values are "FC247" (FortiCare 24x7) or "ASET" (FortiCare Elite).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">vdom</span> Number of VDOMs. A number between 0 and 500 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">cloudServices</span> The cloud services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["FAMS", "SWNM", "AFAC", "FAZC", "FSPA", "SWOS", "FMGC"].<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 </ul> <li><span class="li-head">fortiClientEMSOP</span> FortiClient EMS On-Prem.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">ZTNA</span> ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">EPP</span> EPP/ATP + ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">chromebook</span> Chromebook (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">service</span> Support Services. Possible value is "FCTFC247" (FortiCare Premium)<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">addons</span> Addons. A list. Possible value is "BPS" (FortiCare Best Practice).<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 </ul> <li><span class="li-head">fortiAnalyzer</span> FortiAnalyzer Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">storage</span> Daily Storage (GB). A number between 5 and 8300 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">adom</span> Number of ADOMs. A number between 0 and 1200 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">service</span> Support Service. Currently, the only available option is "FAZFC247" (FortiCare Premium). The default value is "FAZFC247".<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">addons</span> Addons. A list. "FAZISSS" (OT Security Service), "FAZFGSA" (Attack Surface Security Service), "FAZAISN" (FortiAI Service).<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 </ul> <li><span class="li-head">fortiPortal</span> FortiPortal Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">device</span> Number of managed devices. A number between 0 and 100000 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 </ul> <li><span class="li-head">fortiADC</span> FortiADC Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">cpu</span> Number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16" or "32".<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">service</span> Support Service. "FDVFC247" (FortiCare Premium), "FDVNET" (Network Security), "FDVAPP" (Application Security), "FDVAI" (AI Security).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 </ul> <li><span class="li-head">fortiSOAR</span> FortiSOAR Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">service</span> Service Package. One of ["FSRE", "FSRM", "FSRD", "FSRR"].<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">licenseNum</span> Additional Users License. Number between 0 and 1000 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">default: 0</span></li>
 <li><span class="li-head">addons</span> Addons. A list. The default value is an empty list. Possible value is "FSRTIMS" (Threat Intelligence Management).<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 </ul> <li><span class="li-head">fortiMail</span> FortiMail Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">cpu</span> Number of CPUs. The value of this attribute is one of ["1", "2", "4", "8", "16", "32"].<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">service</span> Service Package. Valid values are "FMLBASE" (Base Bundle) or "FMLATP" (ATP Bundle).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">addons</span> Addons. A list. The default value is an empty list. It should contain zero, one or more elements of ["FMLFEMS", "FMLFCAS", "FMLFEOP", "FMLFEEC"]<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 </ul> <li><span class="li-head">fortiNAC</span> FortiNAC Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">service</span> Service Package. Valid values are "FNCPLUS" (Plus) or "FNCPRO" (Pro).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">endpoints</span> Number of endpoints. A number between 25 and 100000 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">supportService</span> Support Service. Currently, the only available option is "FNCFC247" (FortiCare Premium).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 </ul> <li><span class="li-head">fortiGateHardware</span> FortiGate Hardware.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">model</span> Device model. For all supported models, please check FNDN. Possible values include FGT40F (FortiGate 40F), FGT60F (FortiGate 60F), FGT70F (FortiGate 70F), FGT80F (FortiGate 80F), FG100F (FortiGate 100F), FGT60E (FortiGate 60E), FGT61F (FortiGate 61F), FG100E (FortiGate 100E), FG101F (FortiGate 101F), FG200E (FortiGate 200E), FG200F (FortiGate 200F), FG201F (FortiGate 201F), FG4H0F (FortiGate 400F), FG6H0F (FortiGate 600F), FWF40F (FortiWiFi 40F), FWF60F (FortiWiFi 60F), FGR60F (FortiGateRugged 60F), FR70FB (FortiGateRugged 70F), FGT81F (FortiGate 81F), FG101E (FortiGate 101E), FG4H1F (FortiGate 401F), FG1K0F (FortiGate 1000F), FG180F (FortiGate 1800F), F2K60F (FortiGate 2600F), FG3K0F (FortiGate 3000F), FG3K1F (FortiGate 3001F), FG3K2F (FortiGate 3200F), FG40FI (FortiGate 40F-3G4G), FW40FI (FortiWiFi 40F-3G4G), FWF61F (FortiWiFi 61F), FR60FI (FortiGateRugged 60F 3G4G), FGT71F (FortiGate 71F), FG80FP (FortiGate 80F-PoE), FG80FB (FortiGate 80F-Bypass), FG80FD (FortiGate 80F DSL), FWF80F (FortiWiFi 80F-2R), FW80FS (FortiWiFi 80F-2R-3G4G-DSL), FWF81F (FortiWiFi 81F 2R), FW81FS (FortiWiFi 81F-2R-3G4G-DSL), FW81FD (FortiWiFi 81F-2R-3G4G-PoE), FW81FP (FortiWiFi 81F 2R POE), FG81FP (FortiGate 81F-PoE), FGT90G (FortiGate 90G), FGT91G (FortiGate 91G), FG201E (FortiGate 201E), FG4H0E (FortiGate 400E), FG4HBE (FortiGate 400E BYPASS), FG4H1E (FortiGate 401E), FD4H1E (FortiGate 401E DC), FG6H0E (FortiGate 600E), FG6H1E (FortiGate 601E), FG6H1F (FortiGate 601F), FG9H0G (FortiGate 900G), FG9H1G (FortiGate 901G), FG1K1F (FortiGate 1001F), FG181F (FortiGate 1801F), FG3K7F (FortiGate 3700F), FG39E6 (FortiGate 3960E), FG441F (FortiGate 4401F), FGR35D (FortiGateRugged 35D), FR70FM (FortiGateRugged 70F 3G4G), FG60EV (FortiGate 60E DSL), FG60EP (FortiGate 60E POE), FGT61E (FortiGate 61E), FGT80E (FortiGate 80E), FG80EP (FortiGate 80E POE), FGT81E (FortiGate 81E), FG81EP (FortiGate 81E POE), FGT90E (FortiGate 90E), FGT91E (FortiGate 91E), FG3H0E (FortiGate 300E), FG3H1E (FortiGate 301E), FG10E0 (FortiGate 1100E), FD10E0 (FortiGate 1100E DC), FG10E1 (FortiGate 1101E), FD180F (FortiGate 1800F DC), FD181F (FortiGate 1801F DC), FG2K2E (FortiGate 2200E), FG22E1 (FortiGate 2201E), FD260F (FortiGate 2600F DC), F2K61F (FortiGate 2601F), FD261F (FortiGate 2601F DC), FD3K0F (FortiGate 3000F DC), FD3K1F (FortiGate 3001F DC), FG32F1 (FortiGate 3201F), FG3K3E (FortiGate 3300E), FG33E1 (FortiGate 3301E), FG3K4E (FortiGate 3400E), FD3K4E (FortiGate 3400E DC), FG34E1 (FortiGate 3401E), FD34E1 (FortiGate 3401E DC), FG3K5F (FortiGate 3500F), FG35F1 (FortiGate 3501F), FG3K6E (FortiGate 3600E), FD3K6E (FortiGate 3600E-DC), FG36E1 (FortiGate 3601E), FG37F1 (FortiGate 3701F), FG39E8 (FortiGate 3980E), FGD398 (FortiGate 3980E-DC), FG420F (FortiGate 4200F), FD420F (FortiGate 4200F DC), FG421F (FortiGate 4201F), FD421F (FortiGate 4201F DC), FG440F (FortiGate 4400F), FD440F (FortiGate 4400F DC), FD441F (FortiGate 4401F DC), FG480F (FortiGate 4800F), FD480F (FortiGate 4800F-DC), FG481F (FortiGate 4801F), FD481F (FortiGate 4801F-DC), FGT2KE (FortiGate 2000E), FG2K5E (FortiGate 2500E), FG120G (FortiGate 120G), FG121G (FortiGate 121G), FGT30E (FortiGate 30E), FG30EG (FortiGate 30E 3G4G GBL), FGT50E (FortiGate 50E), FGT51E (FortiGate 51E), FG60EJ (FortiGate 60E DSLJ), FG1HEF (FortiGate 100EF), F140EP (FortiGate 140E POE), FG5H0E (FortiGate 500E), FG5H1E (FortiGate 501E), FGD396 (FortiGate 3960E-DC), FWF30E (FortiWiFi 30E), FWF50E (FortiWiFi 50E), FW502R (FortiWiFi 50E 2R), FWF51E (FortiWiFi 51E), FWF60E (FortiWiFi 60E), FW60EV (FortiWiFi 60E DSL), FW60EJ (FortiWiFi 60E DSLJ), FWF61E (FortiWiFi 61E), FW50GD (FortiWiFi-50G-DSL), FW50GS (FortiWiFi-50G-SFP), FG50GD (FortiGate-50G-DSL), FG50GS (FortiGate-50G-SFP), FG50GP (FortiGate-50G-SFP-PoE), FG51GP (FortiGate-51G-SFP-PoE), FG2H0G (FortiGate-200G), FG2H1G (FortiGate-201G), FGT30G (FortiGate-30G), FGT50G (FortiGate-50G), FG50G5 (FortiGate-50G-5G), FGT51G (FortiGate-51G), FG51G5 (FortiGate-51G-5G), FGT70G (FortiGate-70G), FGT71G (FortiGate-71G), FD9H0G (FortiGate-900G-DC), FD9H1G (FortiGate-901G-DC), F6KF01 (FortiGate-6001F).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">service</span> Service Package. Possible values include FGHWFC247 (FortiCare Premium), FGHWFCEL (FortiCare Elite), FGHWATP (ATP), FGHWUTP (UTP), FGHWENT (Enterprise), FGHWFCESN (FortiCare Essential).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">addons</span> Add-on services. A list, can be empty. Possible values include FGHWFCELU (FortiCare Elite Upgrade), FGHWFAMS (FortiGate Cloud Management), FGHWFAIS (AI-Based In-line Sandbox), FGHWSWNM (SD-WAN Underlay), FGHWDLDB (FortiGuard DLP), FGHWFAZC (FortiAnalyzer Cloud), FGHWSOCA (SOCaaS), FGHWMGAS (Managed FortiGate), FGHWSPAL (SD-WAN Connector for FortiSASE), FGHWISSS (FortiGuard OT Security Service), FGHWSWOS (SD-WAN Overlay-as-a-Service), FGHWAVDB (Advanced Malware Protection), FGHWNIDS (Intrusion Prevention), FGHWFGSA (Attack Surface Security Service), FGHWFURL (Web, DNS & Video Filtering), FGHWFSFG (FortiSASE Subscription).<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 </ul> <li><span class="li-head">fortiAPHardware</span> FortiAP Hardware.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">model</span> Device model. For all supported models, please check FNDN. Possible values include FP23JF (FortiAP-23JF), FP221E (FortiAP-221E), FP223E (FortiAP-223E), FP231E (FortiAP-231E), FP231F (FortiAP-231F), FP231G (FortiAP-231G), FP233G (FortiAP-233G), FP234F (FortiAP-234F), FP234G (FortiAP-234G), FP431F (FortiAP-431F), FP431G (FortiAP-431G), FP432F (FortiAP-432F), F432FR (FortiAP-432FR), FP432G (FortiAP-432G), FP433F (FortiAP-433F), FP433G (FortiAP-433G), FP441K (FortiAP-441K), FP443K (FortiAP-443K), FP831F (FortiAP-831F), PU231F (FortiAP-U231F), PU234F (FortiAP-U234F), PU422E (FortiAP-U422EV), PU431F (FortiAP-U431F), PU432F (FortiAP-U432F), PU433F (FortiAP-U433F), FP222E (FortiAP-222E), FP224E (FortiAP-224E).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">service</span> Support Service Possible values include FAPHWFC247 (FortiCare Premium), FAPHWFCEL (FortiCare Elite).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">addons</span> Add-on services. A list, can be empty. Possible values include FAPHWFSFG (FortiSASE Cloud Managed AP).<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 </ul> <li><span class="li-head">fortiSwitchHardware</span> FortiSwitch Hardware.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">model</span> Device model. For all supported models, please check FNDN. Possible values include S108EN (FortiSwitch-108E), S108EF (FortiSwitch-108E-FPOE), S108EP (FortiSwitch-108E-POE), S108FN (FortiSwitch-108F), S108FF (FortiSwitch-108F-FPOE), S108FP (FortiSwitch-108F-POE), S124EN (FortiSwitch-124E), S124EF (FortiSwitch-124E-FPOE), S124EP (FortiSwitch-124E-POE), S124FN (FortiSwitch-124F), S124FF (FortiSwitch-124F-FPOE), S124FP (FortiSwitch-124F-POE), S148EN (FortiSwitch-148E), S148EP (FortiSwitch-148E-POE), S148FN (FortiSwitch-148F), S148FF (FortiSwitch-148F-FPOE), S148FP (FortiSwitch-148F-POE), S224DF (FortiSwitch-224D-FPOE), S224EN (FortiSwitch-224E), S224EP (FortiSwitch-224E-POE), S248DN (FortiSwitch-248D), S248EF (FortiSwitch-248E-FPOE), S248EP (FortiSwitch-248E-POE), S424DN (FortiSwitch-424D), S424DF (FortiSwitch-424D-FPOE), S424DP (FortiSwitch-424D-POE), S424EN (FortiSwitch-424E), S424EF (FortiSwitch-424E-FPOE), S424EI (FortiSwitch-424E-Fiber), S424EP (FortiSwitch-424E-POE), S448DN (FortiSwitch-448D), S448DP (FortiSwitch-448D-POE), S448EN (FortiSwitch-448E), S448EF (FortiSwitch-448E-FPOE), S448EP (FortiSwitch-448E-POE), S524DN (FortiSwitch-524D), S524DF (FortiSwitch-524D-FPOE), S548DN (FortiSwitch-548D), S548DF (FortiSwitch-548D-FPOE), S624FN (FortiSwitch-624F), S624FF (FortiSwitch-624F-FPOE), S648FN (FortiSwitch-648F), S648FF (FortiSwitch-648F-FPOE), FS1D24 (FortiSwitch-1024D), FS1E24 (FortiSwitch-1024E), FS1D48 (FortiSwitch-1048D), FS1E48 (FortiSwitch-1048E), FS2F48 (FortiSwitch-2048F), FS3D32 (FortiSwitch-3032D), FS3E32 (FortiSwitch-3032E), S426EF (FortiSwitch-M426E-FPOE), ST1E24 (FortiSwitch-T1024E), SR12DP (FortiSwitchRugged-112D-POE), SR24DN (FortiSwitchRugged-124D), SM10GF (FortiSwitch-110G-FPOE), SR16FP (FortiSwitchRugged-216F-POE), SR24FP (FortiSwitchRugged-424F-POE).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">service</span> Support service package. Possible values include FSWHWFC247 (FortiCare Premium), FSWHWFCEL (FortiCare Elite).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 </ul> <li><span class="li-head">fortiCloudPrivate</span> FortiWeb Cloud, Private.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">throughput</span> Average Throughput (Mbps). Possible values are 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000.<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">applications</span> Number of web applications. Number between 1 and 5000 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 </ul> <li><span class="li-head">fortiCloudPublic</span> FortiWeb Cloud, Public.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">throughput</span> Average Throughput (Mbps). Possible values are 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000.<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">applications</span> Number of web applications. Number between 0 and 2000 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 </ul> <li><span class="li-head">fortiClientEMSCloud</span> FortiClient EMS Cloud.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">ZTNA</span> ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">ZTNA_FGF</span> ZTNA/VPN + FortiGuard Forensics (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">EPP_ZTNA</span> EPP/ATP + ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">EPP_ZTNA_FGF</span> EPP/ATP + ZTNA/VPN + FortiGuard Forensics (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">chromebook</span> Chromebook (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">addons</span> Addons. A list. Possible value is "BPS" (FortiCare Best Practice).<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 </ul> <li><span class="li-head">fortiSASE</span> fortiSASE Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">users</span> Number of users. Number between 50 and 50,000 (inclusive). Value should be divisible by 25.<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">service</span> Service package. Possible values include "FSASESTD" (Standard), "FSASEADV" (Advanced), "FSASECOM" (Comprehensive).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">dedicatedIPs</span> Number between 4 and 65,534 (inclusive). Value should be divisible by 4.<span class="li-normal">type: int</span><span class="li-normal">default: 0</span></li>
 <li><span class="li-head">dataTransfer</span> Data Transfer. Number between 0 and 2,500,000 (inclusive). Value should be divisible by 250.<span class="li-normal">type: int</span><span class="li-normal">default: 0</span></li>
 <li><span class="li-head">onRampLocations_FortinetCloud</span> SD-WAN On-Ramp Locations. Number between 0 and 20 (inclusive). It can be scaled up in an increment of 1 but scaling down is NOT allowed.<span class="li-normal">type: int</span><span class="li-normal">default: 0</span></li>
 <li><span class="li-head">onRampLocations_PublicCloud</span> SD-WAN On-Ramp Locations. Number between 0 and 20 (inclusive). It can be scaled up in an increment of 1 but scaling down is NOT allowed.<span class="li-normal">type: int</span><span class="li-normal">default: 0</span></li>
 <li><span class="li-head">globalRegion</span> Global Region. "ENABLED" (Enabled), "NONE" (None).<span class="li-normal">type: str</span><span class="li-normal">default: NONE</span></li>
 <li><span class="li-head">computeRegion_FortinetCloud</span> Additional Compute Region. Number between 0 and 16 (inclusive). It can be scaled up in an increment of 1 but scaling down is NOT allowed.<span class="li-normal">type: int</span><span class="li-normal">default: 0</span></li>
 <li><span class="li-head">computeRegion_PublicCloud</span> Additional Compute Region. Number between 0 and 16 (inclusive). It can be scaled up in an increment of 1 but scaling down is NOT allowed.<span class="li-normal">type: int</span><span class="li-normal">default: 0</span></li>
 </ul> <li><span class="li-head">fortiEDR</span> fortiEDR Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">service</span> Service package. "FEDRPDR" (Discover/Protect/Respond).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">addons</span> Add-on services. A list, can be empty. Possible value is "FEDRXDR" (XDR).<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 <li><span class="li-head">repoStorage</span> Repository Storage. Number between 0 and 30720 (inclusive) It can be scaled up in an increment of 512 but scaling down is NOT allowed.<span class="li-normal">type: int</span><span class="li-normal">default: 0</span></li>
 </ul> <li><span class="li-head">fortiNDRCloud</span> fortiNDR Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <li><span class="li-head">fortiRecon</span> fortiRecon Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">service</span> Service package. FRNEASM (External Attack Surface Monitoring); FRNEASMBP (External Attack Surface Monitoring & Brand Protect); FRNEASMBPACI (External Attack Surface Monitoring & Brand Protect & Adversary Centric Intelligence).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">assets</span> Number of Monitored Assets. Number between 200 and 1,000,000 (inclusive). Value should be divisible by 50.<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">networks</span> Internal Attack Surface Monitoring (number of networks). Number between 0 and 100 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">executives</span> Executive Monitoring (number of executives). Number between 0 and 1,000 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">vendors</span> Vendor Monitoring (number of vendors). Number between 0 and 1,000 (inclusive).<span class="li-normal">type: int</span></li>
 </ul> <li><span class="li-head">fortiSIEMCloud</span> fortiSIEM Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">computeUnits</span> Number of Compute Units. Number between 10 and 600 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">onlineStorage</span> Additional Online Storage. Number between 500 and 60,000 (inclusive). Value should be divisible by 500. It can be scaled up in an increment of 500 but scaling down is NOT allowed.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">archiveStorage</span> Archive Storage. Number between 0 and 60,000 (inclusive). Value should be divisible by 500. can be scaled up in an increment of 500 but scaling down is NOT allowed.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">region</span> Region. Possible values include "RegionA", "RegionB".<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 </ul> <li><span class="li-head">fortiAppSec</span> fortiAppSec Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">services</span> Services. A list. Possible values include "UCWAF" (Cloud WAF), "UCGSLB" (Cloud GSLB).<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 <li><span class="li-head">WAF_services</span> WAF Services. Required if services includes "UCWAF". Possible values include "UCWAFSTD" (Standard), "UCWAFADV" (Advanced),  "UCWAFENT" (Enterprise), "NONE".<span class="li-normal">type: str</span><span class="li-normal">default: NONE</span></li>
 <li><span class="li-head">addons</span> Add-ons. A list. Possible value is "UCSOCA" (SOCaaS).<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 </ul> <li><span class="li-head">fortiDLP</span> fortiDLP Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">service</span> Service package. Possible values include "DLPSTD" (Standard), "DLPENT" (Enterprise), "DLPENTP" (Enterprise Premium).<span class="li-normal">type: str</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">endpoints</span> Number of endpoints. Number between 25 and 10,000 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">addons</span> Add-ons. A list. Possible value is "BPS" (Best Practice Service).<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 </ul> <li><span class="li-head">fortiManagerCloud</span> fortiManager Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li><span class="li-head">devices</span> Number of devices. Number between 3 and 100,000 (inclusive).<span class="li-normal">type: int</span><span class="li-normal">required: True</span></li>
 <li><span class="li-head">addons</span> Add-ons. A list. Possible value is "FMGCLDAISN" (FortiAI Service).<span class="li-normal">type: list</span><span class="li-normal">default: []</span></li>
 </ul> </ul>



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
          programSerialNumber: "{{ programSerialNumber }}"
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
          # [FortiGate Virtual Machine - Service Bundle]
          fortiGateBundle:
            cpu: 2                              # 1 ~ 96
            service: "UTP"                      # "FC", "UTP", "ENT", "ATP"
            vdom: 10                            # 0 ~ 500
            fortiGuardServices: ["FGTAVDB"]     # ["FGTAVDB", "FGTFAIS", "FGTISSS", "FGTDLDB", "FGTFGSA"]
            cloudServices: ["FGTFAMS"]          # ["FGTFAMS", "FGTSWNM", "FGTSOCA", "FGTFAZC", "FGTSWOS", "FGTFSPA"]
            supportService: "NONE"              # "FGTFCELU", "NONE"
  
          # [FortiManager Virtual Machine]
          # fortiManager:
          #   device: 1                         # 1 ~ 100000
          #   adom: 1                           # 1 ~ 100000
  
          # [FortiWeb Virtual Machine - Service Bundle]
          # fortiWeb:
          #   cpu: "4"                          # "1", "2", "4", "8", "16"
          #   service: "FWBSTD"                 # "FWBSTD", "FWBADV", "FWBENT"
  
          # [FortiGate Virtual Machine - A La Carte Services]
          # fortiGateLCS:
          #   cpu: 4                            # 1 ~ 96
          #   fortiGuardServices: []            # ["IPS", "AVDB", "FURLDNS", "FGSA", "ISSS", "DLDB", "FAIS"]
          #   supportService: "FC247"           # "FC247", "ASET"
          #   vdom: 1                           # 0 ~ 500
          #   cloudServices: ["FAMS", "SWNM"]   # ["FAMS", "SWNM", "AFAC", "FAZC", "FSPA", "SWOS", "FMGC"]
  
          # [FortiClient EMS On-Prem]
          # fortiClientEMSOP:
          #   ZTNA: 1000                        # Value should be 0 or between 25 and 25000.
          #   EPP: 1000                         # Value should be 0 or between 25 and 25000.
          #   chromebook: 1000                  # Value should be 0 or between 25 and 25000.
          #   service: "FCTFC247"               # "FCTFC247"
          #   addons: ["BPS"]                   # Empty or "BPS"
  
          # [FortiAnalyzer Virtual Machine]
          # fortiAnalyzer:
          #   storage: 5                        # 5 ~ 8300
          #   adom: 1                           # 0 ~ 1200
          #   service: "FAZFC247"               # "FAZFC247"
          #   addons: []                        # ["FAZISSS", "FAZFGSA", "FAZAISN"]
  
          # [FortiPortal Virtual Machine]
          # fortiPortal:
          #   device: 1                         # 0 ~ 100000
  
          # [FortiADC Virtual Machine]
          # fortiADC:
          #   cpu: "1"                          # "1", "2", "4", "8", "16", "32"
          #   service: "FDVFC247"               # "FDVFC247", "FDVNET", "FDVAPP", "FDVAI"
  
          # [FortiSOAR Virtual Machine]
          # fortiSOAR:
          #   service: "FSRE"                   # "FSRE", "FSRM", "FSRD", "FSRR"
          #   licenseNum: 1                     # 0 ~ 1000
          #   addons: []                        # ["FSRTIMS"]
  
          # [FortiMail Virtual Machine - Service Bundle]
          # fortiMail:
          #   cpu: "1"                          # "1", "2", "4", "8", "16", "32"
          #   service: "FMLBASE"                # "FMLBASE", "FMLATP"
          #   addons: []                        # ["FMLFEMS", "FMLFCAS", "FMLFEOP", "FMLFEEC"]
  
          # [FortiGate Hardware]
          # fortiGateHardware:
          #   model: "FGT40F"                   # For all supported modules, please check FNDN.
          #                                     # "FGT40F", "FGT60F", "FGT70F", "FGT80F", "FG100F", "FGT60E",
          #                                     # "FGT61F", "FG100E", "FG101F", "FG200E", "FG200F", "FG201F",
          #                                     # "FG4H0F", "FG6H0F", "FWF40F", "FWF60F", "FGR60F", "FR70FB",
          #                                     # "FGT81F", "FG101E", "FG4H1F", "FG1K0F", "FG180F", "F2K60F",
          #                                     # "FG3K0F", "FG3K1F", "FG3K2F", "FG40FI", "FW40FI", "FWF61F",
          #                                     # "FR60FI", "FGT71F", "FG80FP", "FG80FB", "FG80FD", "FWF80F",
          #                                     # "FW80FS", "FWF81F", "FW81FS", "FW81FD", "FW81FP", "FG81FP",
          #                                     # "FGT90G", "FGT91G", "FG201E", "FG4H0E", "FG4HBE", "FG4H1E",
          #                                     # "FD4H1E", "FG6H0E", "FG6H1E", "FG6H1F", "FG9H0G", "FG9H1G",
          #                                     # "FG1K1F", "FG181F", "FG3K7F", "FG39E6", "FG441F", "FGR35D",
          #                                     # "FR70FM", "FG60EV", "FG60EP", "FGT61E", "FGT80E", "FG80EP",
          #                                     # "FGT81E", "FG81EP", "FGT90E", "FGT91E", "FG3H0E", "FG3H1E",
          #                                     # "FG10E0", "FD10E0", "FG10E1", "FD180F", "FD181F", "FG2K2E",
          #                                     # "FG22E1", "FD260F", "F2K61F", "FD261F", "FD3K0F", "FD3K1F",
          #                                     # "FG32F1", "FG3K3E", "FG33E1", "FG3K4E", "FD3K4E", "FG34E1",
          #                                     # "FD34E1", "FG3K5F", "FG35F1", "FG3K6E", "FD3K6E", "FG36E1",
          #                                     # "FG37F1", "FG39E8", "FGD398", "FG420F", "FD420F", "FG421F",
          #                                     # "FD421F", "FG440F", "FD440F", "FD441F", "FG480F", "FD480F",
          #                                     # "FG481F", "FD481F", "FGT2KE", "FG2K5E", "FG120G", "FG121G",
          #                                     # "FGT30E", "FG30EG", "FGT50E", "FGT51E", "FG60EJ", "FG1HEF",
          #                                     # "F140EP", "FG5H0E", "FG5H1E", "FGD396", "FWF30E", "FWF50E",
          #                                     # "FW502R", "FWF51E", "FWF60E", "FW60EV", "FW60EJ", "FWF61E",
          #                                     # "FW50GD", "FW50GS", "FG50GD", "FG50GS", "FG50GP", "FG51GP",
          #                                     # "FG2H0G", "FG2H1G", "FGT30G", "FGT50G", "FG50G5", "FGT51G",
          #                                     # "FG51G5", "FGT70G", "FGT71G", "FD9H0G", "FD9H1G", "F6KF01"
          #   service: "FGHWFC247"              # "FGHWFC247", "FGHWFCEL", "FGHWATP", "FGHWUTP", "FGHWENT", "FGHWFCESN"
          #   addons: []                        # ["FGHWFCELU", "FGHWFAMS", "FGHWFAIS", "FGHWSWNM", "FGHWDLDB",
          #                                     # "FGHWFAZC", "FGHWSOCA", "FGHWMGAS", "FGHWSPAL", "FGHWISSS",
          #                                     # "FGHWSWOS", "FGHWAVDB", "FGHWNIDS", "FGHWFGSA", "FGHWFURL",
          #                                     # "FGHWFSFG"]
  
          # [FortiAP Hardware]
          # fortiAPHardware:
          #   model: "FP23JF"                   # For all supported modules, please check FNDN.
          #                                     # "FP23JF", "FP221E", "FP223E", "FP231F", "FP231G", "FP233G",
          #                                     # "FP234F", "FP234G", "FP431F", "FP431G", "FP432F", "F432FR",
          #                                     # "FP432G", "FP433F", "FP433G", "FP441K", "FP443K", "FP831F",
          #                                     # "PU231F", "PU234F", "PU422E", "PU431F", "PU432F", "PU433F",
          #                                     # "FP222E", "FP224E", "FP231E"
          #   service: "FAPHWFC247"             # "FAPHWFC247" or "FAPHWFCEL"
          #   addons: []                        # ["FAPHWFSFG"]
  
          # [FortiSwitch Hardware]
          # fortiSwitchHardware:
          #   model: "S108EN"                   # For all supported modules, please check FNDN.
          #                                     # "S108EN", "S108EF", "S108EP", "S108FN", "S108FF", "S108FP",
          #                                     # "S124EN", "S124EF", "S124EP", "S124FN", "S124FF", "S124FP",
          #                                     # "S148EN", "S148EP", "S148FN", "S148FF", "S148FP", "S224DF",
          #                                     # "S224EN", "S224EP", "S248DN", "S248EF", "S248EP", "S424DN",
          #                                     # "S424DF", "S424DP", "S424EN", "S424EF", "S424EI", "S424EP",
          #                                     # "S448DN", "S448DP", "S448EN", "S448EF", "S448EP", "S524DN",
          #                                     # "S524DF", "S548DN", "S548DF", "S624FN", "S624FF", "S648FN",
          #                                     # "S648FF", "FS1D24", "FS1E24", "FS1D48", "FS1E48", "FS2F48",
          #                                     # "FS3D32", "FS3E32", "S426EF", "ST1E24", "SR12DP", "SR24DN",
          #                                     # "SM10GF", "SR16FP", "SR24FP"
          #   service: "FSWHWFC247"             # "FSWHWFC247" or "FSWHWFCEL"
  
          # [FortiCloud Private]
          # fortiCloudPrivate:
          #   throughput: 100                   # 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800,
          #                                     # 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
          #                                     # 7000, 7500, 8000, 8500, 9000, 9500, 10000.
          #   applications: 10                  # 0 ~ 2000
  
          # [FortiCloud Public]
          # fortiCloudPublic:
          #   throughput: 100                   # 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800,
          #                                     # 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
          #                                     # 7000, 7500, 8000, 8500, 9000, 9500, 10000.
          #   applications: 10                  # 1 ~ 5000
  
          # [FortiClient EMS Cloud]
          # fortiClientEMSCloud:
          #   ZTNA: 100                         # Value should be 0 or between 25 and 25000.
          #   ZTNA_FGF: 100                     # Value should be 0 or between 25 and 25000.
          #   EPP_ZTNA: 100                     # Value should be 0 or between 25 and 25000.
          #   EPP_ZTNA_FGF: 100                 # Value should be 0 or between 25 and 25000.
          #   chromebook: 100                   # Value should be 0 or between 25 and 25000.
          #   addons: ["BPS"]                   # [] or ["BPS"]
  
          # [FortiSASE]
          # fortiSASE:
          #   users: 50                         # 50 ~ 50000. Value should be divisible by 25.
          #   service: "FSASESTD"               # "FSASESTD", "FSASEADV", "FSASECOM"
          #   dataTransfer: 5000                # 0 ~ 2500000. Value should be divisible by 250.
          #   dedicatedIPs: 12                  # 0 ~ 65534.  Value should be divisible by 4.
          #   onRampLocations_FortinetCloud: 0  # 0 ~ 20. It can be scaled up in an increment of 1 but scaling down is NOT allowed.
          #   onRampLocations_PublicCloud: 0    # 0 ~ 20. It can be scaled up in an increment of 1 but scaling down is NOT allowed.
          #   globalRegion: "NONE"              # "ENABLED", "NONE"
          #   computeRegion_FortinetCloud: 0    # 0 ~ 16. It can be scaled up in an increment of 1 but scaling down is NOT allowed.
          #   computeRegion_PublicCloud: 0      # 0 ~ 16. It can be scaled up in an increment of 1 but scaling down is NOT allowed.
  
          # [FortiEDR MSSP]
          # fortiEDR:
          #   service: "FEDRPDR"                # "FEDRPDR"
          #   addons: ["FEDRXDR"]               # [] or ["FEDRXDR"]
          #   repoStorage: 0                    # 0 ~ 30720. It can be scaled up in an increment of 512 but scaling down is NOT allowed.
  
          # [FortiNDR Cloud]
          # fortiNDRCloud: {}                   # Since fortiNDRCloud does not have any parameters, you need to set it as empty.
  
          # [FortiRecon]
          # fortiRecon:
          #   service: "FRNEASM"                # "FRNEASM", "FRNEASMBP", "FRNEASMBPACI"
          #   assets: 200                       # 200 ~ 1000000. Value should be divisible by 50
          #   networks: 0                       # 0 ~ 100
          #   executives: 0                     # 0 ~ 1000
          #   vendors: 0                        # 0 ~ 1000
  
          # [FortiSIEM Cloud]
          # fortiSIEMCloud:
          #   computeUnits: 10                  # 10 ~ 600
          #   onlineStorage: 500                # 500 ~ 60000. Value should be divisible by 500.
          #                                     # It can be scaled up in an increment of 500 but scaling down is NOT allowed.
          #   archiveStorage: 0                 # 0 ~ 60000. Value should be divisible by 500.
          #                                     # It can be scaled up in an increment of 500 but scaling down is NOT allowed.
          #   region: "RegionA"                 # "RegionA", "RegionB"
  
          # [FortiAppSec]
          # fortiAppSec:
          #   services: ["UCWAF"]               # ["UCWAF", "UCGSLB"]
          #   WAF_services: "UCWAFSTD"          # "UCWAFSTD", "UCWAFADV", "UCWAFENT". Required if services includes "UCWAF".
          #   addons: []                        # ["UCSOCA"]
  
          # [FortiDLP]
          # fortiDLP:
          #   service: "DLPSTD"                 # "DLPSTD", "DLPENT", "DLPENTP"
          #   endpoints: 100                    # 25 ~ 100000
          #   addons: []                        # ["BPS"]
  
          # [FortiManager Cloud]
          # fortiManagerCloud:
          #   devices: 10                       # 3 ~ 100000
          #   addons: []                        # ["FMGCLDAISN"]
  
        register: result
  
      - name: Display response
        ansible.builtin.debug:
          var: result.configs
  


Return Values
-------------
.. raw:: html

 <ul>
 <li><span class="li-head">configs</span> The configuration you create.<span class="li-normal">type: dict</span><span class="li-normal">returned: always</span></li>
 <ul class="ul-self">
 <li><span class="li-head">accountId</span> The ID of the account associated with the program.<span class="li-normal">type: int</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">id</span> The ID of the configuration.<span class="li-normal">type: int</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">name</span> The name of the configuration.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">programSerialNumber</span> The program serial number the configuration belongs to.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">status</span> The status of the configuration.<span class="li-normal">type: str</span><span class="li-normal">returned: always</span></li>
 <li><span class="li-head">fortiGateBundle</span> FortiGate Virtual Machine - Service Bundle.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">cpu</span> The number of CPUs. Number between 1 and 96 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">service</span> The value of this attribute is one of "FC" (FortiCare), "UTP", "ENT" (Enterprise) or "ATP".<span class="li-normal">type: str</span></li>
 <li><span class="li-head">vdom</span> Number of VDOMs. A number between 0 and 500 (inclusive). The default number is 0.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">fortiGuardServices</span> Fortiguard Services. The default value is an empty list. It should contain zero, one or more elements of ["FGTAVDB", "FGTFAIS", "FGTISSS", "FGTDLDB", "FGTFGSA"].<span class="li-normal">type: list</span></li>
 <li><span class="li-head">cloudServices</span> Cloud Services. The default value is an empty list. It should contain zero, one or more elements of ["FGTFAMS", "FGTSWNM", "FGTSOCA", "FGTFAZC", "FGTSWOS", "FGTFSPA"].<span class="li-normal">type: list</span></li>
 <li><span class="li-head">supportService</span> Suport service. "FGTFCELU" or "NONE". Default is "NONE".<span class="li-normal">type: str</span></li>
 </ul>
 <li><span class="li-head">fortiManager</span> FortiManager Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">device</span> Number of managed devices. A number between 1 and 100000 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">adom</span> Number of ADOMs. A number between 0 and 100000 (inclusive).<span class="li-normal">type: int</span></li>
 </ul>
 <li><span class="li-head">fortiWeb</span> FortiWeb Virtual Machine - Service Bundle.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">cpu</span> Number of CPUs. The value of this attribute is one of "1", "2", "4", "8" or "16".<span class="li-normal">type: str</span></li>
 <li><span class="li-head">service</span> Service Package. Valid values are "FWBSTD" (Standard), "FWBADV" (Advanced) or "FWBENT" (Advanced).<span class="li-normal">type: str</span></li>
 </ul>
 <li><span class="li-head">fortiGateLCS</span> FortiGate Virtual Machine - A La Carte Services.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">cpu</span> The number of CPUs. A number between 1 and 96 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">fortiGuardServices</span> The fortiguard services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["IPS", "AVDB", "FURLDNS", "FGSA", "ISSS", "DLDB", "FAIS"].<span class="li-normal">type: list</span></li>
 <li><span class="li-head">supportService</span> Valid values are "FC247" (FortiCare 24x7) or "ASET" (FortiCare Elite).<span class="li-normal">type: str</span></li>
 <li><span class="li-head">vdom</span> Number of VDOMs. A number between 0 and 500 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">cloudServices</span> The cloud services this FortiGate Virtual Machine supports. The default value is an empty list. It should contain zero, one or more elements of ["FAMS", "SWNM", "AFAC", "FAZC", "FSPA", "SWOS", "FMGC"].<span class="li-normal">type: list</span></li>
 </ul>
 <li><span class="li-head">fortiClientEMSOP</span> FortiClient EMS On-Prem.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">ZTNA</span> ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">EPP</span> EPP/ATP + ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">chromebook</span> Chromebook (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">service</span> Support Services. Possible value is "FCTFC247" (FortiCare Premium)<span class="li-normal">type: str</span></li>
 <li><span class="li-head">addons</span> Addons. A list. Possible value is "BPS" ( FortiCare Best Practice).<span class="li-normal">type: list</span></li>
 </ul>
 <li><span class="li-head">fortiAnalyzer</span> FortiAnalyzer Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">storage</span> Daily Storage (GB). A number between 5 and 8300 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">adom</span> Number of ADOMs. A number between 0 and 1200 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">service</span> Support Service. Currently, the only available option is "FAZFC247" (FortiCare Premium). The default value is "FAZFC247".<span class="li-normal">type: str</span></li>
 <li><span class="li-head">addons</span> Addons. A list. "FAZISSS" (OT Security Service), "FAZFGSA" (Attack Surface Security Service), "FAZAISN" (FortiAI Service).<span class="li-normal">type: list</span></li>
 </ul>
 <li><span class="li-head">fortiPortal</span> FortiPortal Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">device</span> Number of managed devices. A number between 0 and 100000 (inclusive).<span class="li-normal">type: str</span></li>
 </ul>
 <li><span class="li-head">fortiADC</span> FortiADC Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">cpu</span> Number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16" or "32".<span class="li-normal">type: str</span></li>
 <li><span class="li-head">service</span> Support Service. "FDVFC247" (FortiCare Premium), "FDVNET" (Network Security), "FDVAPP" (Application Security), "FDVAI" (AI Security).<span class="li-normal">type: str</span></li>
 </ul>
 <li><span class="li-head">fortiSOAR</span> FortiSOAR Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">service</span> Service Package. One of ["FSRE", "FSRM", "FSRD", "FSRR"].<span class="li-normal">type: str</span></li>
 <li><span class="li-head">licenseNum</span> Additional Users License. Number between 0 and 1000 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">addons</span> Addons. A list. The default value is an empty list. Possible value is "FSRTIMS" (Threat Intelligence Management).<span class="li-normal">type: list</span></li>
 </ul>
 <li><span class="li-head">fortiMail</span> FortiMail Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">cpu</span> Number of CPUs. The value of this attribute is one of ["1", "2", "4", "8", "16", "32"].<span class="li-normal">type: str</span></li>
 <li><span class="li-head">service</span> Service Package. Valid values are "FMLBASE" (Base Bundle) or "FMLATP" (ATP Bundle).<span class="li-normal">type: str</span></li>
 <li><span class="li-head">addons</span> Addons. A list. The default value is an empty list. It should contain zero, one or more elements of ["FMLFEMS", "FMLFCAS", "FMLFEOP", "FMLFEEC"]<span class="li-normal">type: list</span></li>
 </ul>
 <li><span class="li-head">fortiNAC</span> FortiNAC Virtual Machine.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">service</span> Service Package. Valid values are "FNCPLUS" (Plus) or "FNCPRO" (Pro).<span class="li-normal">type: str</span></li>
 <li><span class="li-head">endpoints</span> Number of endpoints. A number between 25 and 100000 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">supportService</span> Support Service. Currently, the only available option is "FNCFC247" (FortiCare Premium).<span class="li-normal">type: str</span></li>
 </ul>
 <li><span class="li-head">fortiGateHardware</span> FortiGate Hardware.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">model</span> Device model. For all supported models, please check FNDN. Possible values include FGT40F (FortiGate 40F), FGT60F (FortiGate 60F), FGT70F (FortiGate 70F), FGT80F (FortiGate 80F), FG100F (FortiGate 100F), FGT60E (FortiGate 60E), FGT61F (FortiGate 61F), FG100E (FortiGate 100E), FG101F (FortiGate 101F), FG200E (FortiGate 200E), FG200F (FortiGate 200F), FG201F (FortiGate 201F), FG4H0F (FortiGate 400F), FG6H0F (FortiGate 600F), FWF40F (FortiWiFi 40F), FWF60F (FortiWiFi 60F), FGR60F (FortiGateRugged 60F), FR70FB (FortiGateRugged 70F), FGT81F (FortiGate 81F), FG101E (FortiGate 101E), FG4H1F (FortiGate 401F), FG1K0F (FortiGate 1000F), FG180F (FortiGate 1800F), F2K60F (FortiGate 2600F), FG3K0F (FortiGate 3000F), FG3K1F (FortiGate 3001F), FG3K2F (FortiGate 3200F), FG40FI (FortiGate 40F-3G4G), FW40FI (FortiWiFi 40F-3G4G), FWF61F (FortiWiFi 61F), FR60FI (FortiGateRugged 60F 3G4G), FGT71F (FortiGate 71F), FG80FP (FortiGate 80F-PoE), FG80FB (FortiGate 80F-Bypass), FG80FD (FortiGate 80F DSL), FWF80F (FortiWiFi 80F-2R), FW80FS (FortiWiFi 80F-2R-3G4G-DSL), FWF81F (FortiWiFi 81F 2R), FW81FS (FortiWiFi 81F-2R-3G4G-DSL), FW81FD (FortiWiFi 81F-2R-3G4G-PoE), FW81FP (FortiWiFi 81F 2R POE), FG81FP (FortiGate 81F-PoE), FGT90G (FortiGate 90G), FGT91G (FortiGate 91G), FG201E (FortiGate 201E), FG4H0E (FortiGate 400E), FG4HBE (FortiGate 400E BYPASS), FG4H1E (FortiGate 401E), FD4H1E (FortiGate 401E DC), FG6H0E (FortiGate 600E), FG6H1E (FortiGate 601E), FG6H1F (FortiGate 601F), FG9H0G (FortiGate 900G), FG9H1G (FortiGate 901G), FG1K1F (FortiGate 1001F), FG181F (FortiGate 1801F), FG3K7F (FortiGate 3700F), FG39E6 (FortiGate 3960E), FG441F (FortiGate 4401F), FGR35D (FortiGateRugged 35D), FR70FM (FortiGateRugged 70F 3G4G), FG60EV (FortiGate 60E DSL), FG60EP (FortiGate 60E POE), FGT61E (FortiGate 61E), FGT80E (FortiGate 80E), FG80EP (FortiGate 80E POE), FGT81E (FortiGate 81E), FG81EP (FortiGate 81E POE), FGT90E (FortiGate 90E), FGT91E (FortiGate 91E), FG3H0E (FortiGate 300E), FG3H1E (FortiGate 301E), FG10E0 (FortiGate 1100E), FD10E0 (FortiGate 1100E DC), FG10E1 (FortiGate 1101E), FD180F (FortiGate 1800F DC), FD181F (FortiGate 1801F DC), FG2K2E (FortiGate 2200E), FG22E1 (FortiGate 2201E), FD260F (FortiGate 2600F DC), F2K61F (FortiGate 2601F), FD261F (FortiGate 2601F DC), FD3K0F (FortiGate 3000F DC), FD3K1F (FortiGate 3001F DC), FG32F1 (FortiGate 3201F), FG3K3E (FortiGate 3300E), FG33E1 (FortiGate 3301E), FG3K4E (FortiGate 3400E), FD3K4E (FortiGate 3400E DC), FG34E1 (FortiGate 3401E), FD34E1 (FortiGate 3401E DC), FG3K5F (FortiGate 3500F), FG35F1 (FortiGate 3501F), FG3K6E (FortiGate 3600E), FD3K6E (FortiGate 3600E-DC), FG36E1 (FortiGate 3601E), FG37F1 (FortiGate 3701F), FG39E8 (FortiGate 3980E), FGD398 (FortiGate 3980E-DC), FG420F (FortiGate 4200F), FD420F (FortiGate 4200F DC), FG421F (FortiGate 4201F), FD421F (FortiGate 4201F DC), FG440F (FortiGate 4400F), FD440F (FortiGate 4400F DC), FD441F (FortiGate 4401F DC), FG480F (FortiGate 4800F), FD480F (FortiGate 4800F-DC), FG481F (FortiGate 4801F), FD481F (FortiGate 4801F-DC), FGT2KE (FortiGate 2000E), FG2K5E (FortiGate 2500E), FG120G (FortiGate 120G), FG121G (FortiGate 121G), FGT30E (FortiGate 30E), FG30EG (FortiGate 30E 3G4G GBL), FGT50E (FortiGate 50E), FGT51E (FortiGate 51E), FG60EJ (FortiGate 60E DSLJ), FG1HEF (FortiGate 100EF), F140EP (FortiGate 140E POE), FG5H0E (FortiGate 500E), FG5H1E (FortiGate 501E), FGD396 (FortiGate 3960E-DC), FWF30E (FortiWiFi 30E), FWF50E (FortiWiFi 50E), FW502R (FortiWiFi 50E 2R), FWF51E (FortiWiFi 51E), FWF60E (FortiWiFi 60E), FW60EV (FortiWiFi 60E DSL), FW60EJ (FortiWiFi 60E DSLJ), FWF61E (FortiWiFi 61E), FW50GD (FortiWiFi-50G-DSL), FW50GS (FortiWiFi-50G-SFP), FG50GD (FortiGate-50G-DSL), FG50GS (FortiGate-50G-SFP), FG50GP (FortiGate-50G-SFP-PoE), FG51GP (FortiGate-51G-SFP-PoE), FG2H0G (FortiGate-200G), FG2H1G (FortiGate-201G), FGT30G (FortiGate-30G), FGT50G (FortiGate-50G), FG50G5 (FortiGate-50G-5G), FGT51G (FortiGate-51G), FG51G5 (FortiGate-51G-5G), FGT70G (FortiGate-70G), FGT71G (FortiGate-71G), FD9H0G (FortiGate-900G-DC), FD9H1G (FortiGate-901G-DC), F6KF01 (FortiGate-6001F).<span class="li-normal">type: str</span></li>
 <li><span class="li-head">service</span> Service Package. Possible values include FGHWFC247 (FortiCare Premium), FGHWFCEL (FortiCare Elite), FGHWATP (ATP), FGHWUTP (UTP), FGHWENT (Enterprise), FGHWFCESN (FortiCare Essential).<span class="li-normal">type: str</span></li>
 <li><span class="li-head">addons</span> Add-on services. A list, can be empty. Possible values include FGHWFCELU (FortiCare Elite Upgrade), FGHWFAMS (FortiGate Cloud Management), FGHWFAIS (AI-Based In-line Sandbox), FGHWSWNM (SD-WAN Underlay), FGHWDLDB (FortiGuard DLP), FGHWFAZC (FortiAnalyzer Cloud), FGHWSOCA (SOCaaS), FGHWMGAS (Managed FortiGate), FGHWSPAL (SD-WAN Connector for FortiSASE), FGHWISSS (FortiGuard OT Security Service), FGHWSWOS (SD-WAN Overlay-as-a-Service), FGHWAVDB (Advanced Malware Protection), FGHWNIDS (Intrusion Prevention), FGHWFGSA (Attack Surface Security Service), FGHWFURL (Web, DNS & Video Filtering), FGHWFSFG (FortiSASE Subscription).<span class="li-normal">type: list</span></li>
 </ul>
 <li><span class="li-head">fortiAPHardware</span> FortiAP Hardware.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">model</span> Device model. For all supported models, please check FNDN. Possible values include FP23JF (FortiAP-23JF), FP221E (FortiAP-221E), FP223E (FortiAP-223E), FP231E (FortiAP-231E), FP231F (FortiAP-231F), FP231G (FortiAP-231G), FP233G (FortiAP-233G), FP234F (FortiAP-234F), FP234G (FortiAP-234G), FP431F (FortiAP-431F), FP431G (FortiAP-431G), FP432F (FortiAP-432F), F432FR (FortiAP-432FR), FP432G (FortiAP-432G), FP433F (FortiAP-433F), FP433G (FortiAP-433G), FP441K (FortiAP-441K), FP443K (FortiAP-443K), FP831F (FortiAP-831F), PU231F (FortiAP-U231F), PU234F (FortiAP-U234F), PU422E (FortiAP-U422EV), PU431F (FortiAP-U431F), PU432F (FortiAP-U432F), PU433F (FortiAP-U433F), FP222E (FortiAP-222E), FP224E (FortiAP-224E).<span class="li-normal">type: str</span></li>
 <li><span class="li-head">service</span> Support Service Possible values include FAPHWFC247 (FortiCare Premium), FAPHWFCEL (FortiCare Elite).<span class="li-normal">type: str</span></li>
 <li><span class="li-head">addons</span> Add-on services. A list, can be empty. Possible values include FAPHWFSFG (FortiSASE Cloud Managed AP).<span class="li-normal">type: list</span></li>
 </ul>
 <li><span class="li-head">fortiSwitchHardware</span> FortiSwitch Hardware.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">model</span> Device model. For all supported models, please check FNDN. Possible values include S108EN (FortiSwitch-108E), S108EF (FortiSwitch-108E-FPOE), S108EP (FortiSwitch-108E-POE), S108FN (FortiSwitch-108F), S108FF (FortiSwitch-108F-FPOE), S108FP (FortiSwitch-108F-POE), S124EN (FortiSwitch-124E), S124EF (FortiSwitch-124E-FPOE), S124EP (FortiSwitch-124E-POE), S124FN (FortiSwitch-124F), S124FF (FortiSwitch-124F-FPOE), S124FP (FortiSwitch-124F-POE), S148EN (FortiSwitch-148E), S148EP (FortiSwitch-148E-POE), S148FN (FortiSwitch-148F), S148FF (FortiSwitch-148F-FPOE), S148FP (FortiSwitch-148F-POE), S224DF (FortiSwitch-224D-FPOE), S224EN (FortiSwitch-224E), S224EP (FortiSwitch-224E-POE), S248DN (FortiSwitch-248D), S248EF (FortiSwitch-248E-FPOE), S248EP (FortiSwitch-248E-POE), S424DN (FortiSwitch-424D), S424DF (FortiSwitch-424D-FPOE), S424DP (FortiSwitch-424D-POE), S424EN (FortiSwitch-424E), S424EF (FortiSwitch-424E-FPOE), S424EI (FortiSwitch-424E-Fiber), S424EP (FortiSwitch-424E-POE), S448DN (FortiSwitch-448D), S448DP (FortiSwitch-448D-POE), S448EN (FortiSwitch-448E), S448EF (FortiSwitch-448E-FPOE), S448EP (FortiSwitch-448E-POE), S524DN (FortiSwitch-524D), S524DF (FortiSwitch-524D-FPOE), S548DN (FortiSwitch-548D), S548DF (FortiSwitch-548D-FPOE), S624FN (FortiSwitch-624F), S624FF (FortiSwitch-624F-FPOE), S648FN (FortiSwitch-648F), S648FF (FortiSwitch-648F-FPOE), FS1D24 (FortiSwitch-1024D), FS1E24 (FortiSwitch-1024E), FS1D48 (FortiSwitch-1048D), FS1E48 (FortiSwitch-1048E), FS2F48 (FortiSwitch-2048F), FS3D32 (FortiSwitch-3032D), FS3E32 (FortiSwitch-3032E), S426EF (FortiSwitch-M426E-FPOE), ST1E24 (FortiSwitch-T1024E), SR12DP (FortiSwitchRugged-112D-POE), SR24DN (FortiSwitchRugged-124D), SM10GF (FortiSwitch-110G-FPOE), SR16FP (FortiSwitchRugged-216F-POE), SR24FP (FortiSwitchRugged-424F-POE).<span class="li-normal">type: str</span></li>
 <li><span class="li-head">service</span> Support service package. Possible values include FSWHWFC247 (FortiCare Premium), FSWHWFCEL (FortiCare Elite).<span class="li-normal">type: str</span></li>
 </ul>
 <li><span class="li-head">fortiCloudPrivate</span> FortiWeb Cloud, Private.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">throughput</span> Average Throughput (Mbps). Possible values are 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">applications</span> Number of web applications. Number between 1 and 5000 (inclusive).<span class="li-normal">type: int</span></li>
 </ul>
 <li><span class="li-head">fortiCloudPublic</span> FortiWeb Cloud, Public.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">throughput</span> Average Throughput (Mbps). Possible values are 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">applications</span> Number of web applications. Number between 1 and 5000 (inclusive).<span class="li-normal">type: int</span></li>
 </ul>
 <li><span class="li-head">fortiClientEMSCloud</span> FortiClient EMS Cloud.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">ZTNA</span> ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">ZTNA_FGF</span> ZTNA/VPN + FortiGuard Forensics (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">EPP_ZTNA</span> EPP/ATP + ZTNA/VPN (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">EPP_ZTNA_FGF</span> EPP/ATP + ZTNA/VPN + FortiGuard Forensics (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">chromebook</span> Chromebook (number of endpoints). Value should be 0 or between 25 and 25000.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">addons</span> Addons. A list. Possible value is "BPS" ( FortiCare Best Practice).<span class="li-normal">type: list</span></li>
 </ul>
 <li><span class="li-head">fortiSASE</span> fortiSASE Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">users</span> Number of users. Number between 50 and 50,000 (inclusive). Number between 50 and 50,000 (inclusive). Value should be divisible by 25.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">service</span> Service package. Possible values include "FSASESTD" (Standard), "FSASEADV" (Advanced), "FSASECOM" (Comprehensive).<span class="li-normal">type: str</span></li>
 <li><span class="li-head">dedicatedIPs</span> Number between 4 and 65,534 (inclusive). Value should be divisible by 4.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">dataTransfer</span> Data Transfer. Number between 0 and 2,500,000 (inclusive). Value should be divisible by 250.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">onRampLocations_FortinetCloud</span> SD-WAN On-Ramp Locations. Number between 0 and 20 (inclusive). It can be scaled up in an increment of 1 but scaling down is NOT allowed.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">onRampLocations_PublicCloud</span> SD-WAN On-Ramp Locations. Number between 0 and 20 (inclusive). It can be scaled up in an increment of 1 but scaling down is NOT allowed.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">globalRegion</span> Global Region. "ENABLED" (Enabled), "NONE" (None).<span class="li-normal">type: str</span></li>
 <li><span class="li-head">computeRegion_FortinetCloud</span> Additional Compute Region. Number between 0 and 16 (inclusive). It can be scaled up in an increment of 1 but scaling down is NOT allowed.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">computeRegion_PublicCloud</span> Additional Compute Region. Number between 0 and 16 (inclusive). It can be scaled up in an increment of 1 but scaling down is NOT allowed.<span class="li-normal">type: int</span></li>
 </ul>
 <li><span class="li-head">fortiEDR</span> fortiEDR Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">service</span> Service package. "FEDRPDR" (Discover/Protect/Respond).<span class="li-normal">type: str</span></li>
 <li><span class="li-head">endpoints</span> Number of Endpoints. Read only.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">addons</span> Add-on services. A list, can be empty. Possible value is "FEDRXDR" (XDR).<span class="li-normal">type: list</span></li>
 <li><span class="li-head">repoStorage</span> Repository Storage. Number between 0 and 30720 (inclusive) It can be scaled up in an increment of 512 but scaling down is NOT allowed.<span class="li-normal">type: int</span></li>
 </ul>
 <li><span class="li-head">fortiNDRCloud</span> fortiNDR Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">meteredUsage</span> Metered Usage. Read only.<span class="li-normal">type: int</span></li>
 </ul>
 <li><span class="li-head">fortiRecon</span> fortiRecon Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">service</span> Service package. FRNEASM (External Attack Surface Monitoring). FRNEASMBP (External Attack Surface Monitoring & Brand Protect) FRNEASMBPACI (External Attack Surface Monitoring & Brand Protect & Adversary Centric Intelligence)<span class="li-normal">type: str</span></li>
 <li><span class="li-head">assets</span> Number of Monitored Assets. Number between 200 and 1,000,000 (inclusive). Value should be divisible by 50.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">networks</span> Internal Attack Surface Monitoring (number of networks). Number between 0 and 100 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">executives</span> Executive Monitoring (number of executives). Number between 0 and 1,000 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">vendors</span> Vendor Monitoring (number of vendors). Number between 0 and 1,000 (inclusive).<span class="li-normal">type: int</span></li>
 </ul>
 <li><span class="li-head">fortiSIEMCloud</span> fortiSIEM Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">computeUnits</span> Number of Compute Units. Number between 10 and 600 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">onlineStorage</span> Additional Online Storage. Number between 500 and 60,000 (inclusive). Value should be divisible by 500. It can be scaled up in an increment of 500 but scaling down is NOT allowed.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">archiveStorage</span> Archive Storage. Number between 0 and 60,000 (inclusive). Value should be divisible by 500. can be scaled up in an increment of 500 but scaling down is NOT allowed.<span class="li-normal">type: int</span></li>
 <li><span class="li-head">region</span> Region. Possible values include "RegionA", "RegionB".<span class="li-normal">type: str</span></li>
 </ul>
 <li><span class="li-head">fortiAppSec</span> fortiAppSec Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">services</span> Services. A list. Possible values include "UCWAF" (Cloud WAF), "UCGSLB" (Cloud GSLB).<span class="li-normal">type: list</span></li>
 <li><span class="li-head">WAF_services</span> WAF Services. Required if services includes "UCWAF". Possible values include "UCWAFSTD" (Standard), "UCWAFADV" (Advanced), "UCWAFENT" (Enterprise), "NONE".<span class="li-normal">type: str</span></li>
 <li><span class="li-head">addons</span> Add-ons. A list. Possible value is "UCSOCA" (SOCaaS).<span class="li-normal">type: list</span></li>
 </ul>
 <li><span class="li-head">fortiDLP</span> fortiDLP Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">service</span> Service package. Possible values include "DLPSTD" (Standard), "DLPENT" (Enterprise), "DLPENTP" (Enterprise Premium).<span class="li-normal">type: str</span></li>
 <li><span class="li-head">endpoints</span> Number of endpoints. Number between 25 and 10,000 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">addons</span> Add-ons. A list. Possible value is "BPS" (Best Practice Service).<span class="li-normal">type: list</span></li>
 </ul>
 <li><span class="li-head">fortiManagerCloud</span> fortiManager Cloud Configuration.<span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">devices</span> Number of devices. Number between 3 and 100,000 (inclusive).<span class="li-normal">type: int</span></li>
 <li><span class="li-head">addons</span> Add-ons. A list. Possible value is "FMGCLDAISN" (FortiAI Service).<span class="li-normal">type: list</span></li>
 </ul>
 </ul>
 </ul>


Authors
-------

- Xinwei Du (@dux-fortinet)

.. hint::
    If you notice any issues in this documentation, you can create a pull request to improve it.