Run Your First Playbook
==============================

This document explains how to run your first FortiFlexVM Ansible playbook.

--------------

.. warning::
  Due to the design of the FortiFlex API, all modules ending with ``_create`` are not idempotent.
  You will create a correspond resource every time you call the modules end with ``_create``.

  It is highly recommended you use a separate playbook to run ``_create`` modules, and only run it when you need new resources.

Write a playbook
~~~~~~~~~~~~~~~~~~

For each module, we provide an example playbook. You can view it on the module details page.

In this example, we try to get the details of our FortiFlex program.

.. code-block:: yaml

  - name: Get list of Programs for the account
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
  

There are several options which might need you special care:

-  **collections** : The namespace must be ``fortinet.fortiflexvm``.
-  **username**, **password**: To get a username and password, please refer to :doc:`token`. You need to specify it in the playbook or the environment variable: ``FORTIFLEX_ACCESS_USERNAME`` and ``FORTIFLEX_ACCESS_PASSWORD``.