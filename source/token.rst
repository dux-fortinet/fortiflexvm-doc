Generate an API token (username and password) for FortiFlexVM
=====================================================================

FortiFlexVM Provider requires an API token to be authenticated.

.. note::

  Before generating an API token for FortiFlexVM, please ensure you have a FortiCloud account and have FortiFlex activated.

Step 1 (Optional): Create a new permission profile in IAM
------------------------------------------------------------

Go to the `IAM Website <https://support.fortinet.com/iam/>`_. Click **Permission Profiles** in the left navigation bar. On the new page, click **Add New** to create a new permission profile.

On the **New Portal Permission Profile** page, fill in the **Permission Profile Name**, and keep **Status** as Active.

Click the **Add Portal** button. Select **FortiFlex**. Then click the **Add** button.

You will see **FortiFlex** is listed under **PERMISSION PROFILE**. Click **Access** in **FortiFlex** and set its **Access Type** as you want. Actions that involve changing or creating data (such as creating a new Configuration or updating a VM) will require ReadWrite permission or above.

Click the **Submit** button in the upper right corner to submit.

Step 2: Create an API User in IAM with permission to access FortiFlex
---------------------------------------------------------------------

In the `IAM Website <https://support.fortinet.com/iam/>`_, click **Users** in the left navigation bar. On the new page, click **Add New > API User** to create an API User.

In the **Select a Permission Profile**, select the user you created in Step 1. (If you skipped Step 1, you could select **SysAdmin**, in this case, you will create an admin user who has full access to Asset Management, IAM and FortiCare, which is not recommended).

Click **Next > Confirm** to create an API user. The system will randomly assign a user name (API User ID).

Step 3: Download your username and password
--------------------------------------------------------------------

In the `IAM Website <https://support.fortinet.com/iam/>`_, click **Users** in the left navigation bar. Click the user you created in Step 2.

In the **API User Information** page, click the **Download Credentials** button in the bottom right to download your user name and password.

For security purposes, please set a password when downloading your credential file. You will need this password to extract the file.

.. warning::

  Downloading the API User Credentials will reset the Users security credentials each time.

  If you download the credentials again, the password for the previous credential file will no longer be valid.

Refer to the `FortiFlex Administration Guide <https://docs.fortinet.com/product/flex-vm/>`_ for more information about FortiFlex.
