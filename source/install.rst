Install FortiFlexVM Ansible Galaxy
======================================

This document explains how to install the FortiFlexVM Ansible Galaxy
Collection.

--------------

Install Python3
~~~~~~~~~~~~~~~

-  Follow steps in https://www.python.org/ to install Python3 on your
   host.

Install Ansible Core
~~~~~~~~~~~~~~~~~~~~

-  Follow instructions in
   https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
   to install Ansible
-  The Ansible core version requirement: >= 2.9.0

Install FortiOS Galaxy Collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The FortiFlexVM Ansible Galaxy supports multilple FortiFlexVM major releases,
you can install the latest collection by default via command
``ansible-galaxy collection install fortinet.fortiflexvm``. you can also
choose another galaxy version to match your FortiFlexVM device.

Please see the `versionig notes` for more recently released collections
and install the ones which are marked ``latest`` for your devices.

.. _versioning notes: version.html

