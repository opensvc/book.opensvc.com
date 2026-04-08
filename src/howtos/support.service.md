# Support Service Procedures

## Introduction

OpenSVC provides commercial support for its product catalog. Active support contract owners are able to open service requests. Contact [sales@opensvc.com](mailto:sales@opensvc.com) for a quotation.

This section **describes** the guidelines for being assisted by our support team.

---

## Support Ticket Opening

To open a service request, you can use one of the four following methods:

### Mattermost
OpenSVC Mattermost channels are available at [https://meet.opensvc.com](https://meet.opensvc.com).

Please request your access via [support@opensvc.com](mailto:support@opensvc.com) if no invitation has been received in your mailbox.

### Web Portal
The support website is available at [https://www.opensvc.com](https://www.opensvc.com).

First, you must register for an account on the web portal:
1. Open a browser to [https://www.opensvc.com](https://www.opensvc.com).
2. Click on the **Sign In** link.
3. Click on the **Register** link.
4. Fill in the requested **information** and submit.
5. Contact [support@opensvc.com](mailto:support@opensvc.com) to link your new account to your company support contract.

Once your account is active and linked to a support contract, you can open a service request:
1. Open a browser to [https://www.opensvc.com](https://www.opensvc.com).
2. Login with your email address and password.
3. Click on the **Support** icon, then **Create Ticket**.
4. Fill in the requested information and click **Submit**.
5. You can then modify or view the ticket to complete it with a problem description, error messages, context, and any other information you want to provide.

### Email
Send your request to [support@opensvc.com](mailto:support@opensvc.com).

### Phone
Premium support enabled accounts are presented with a **Call Me Back** button in the web portal support section.
1. Open a browser to [https://www.opensvc.com](https://www.opensvc.com).
2. Login with your email address and password.
3. Click on the **Support** icon, and then the red **Call Me Back** button.
4. Fill in the form with your international phone number and submit.
5. Wait for a support representative to call you back.

> ⚠️ **Warning**:
> Please consider using the callback service only for urgent purposes requiring immediate answers.

---

## Support Data Collection

To ease resolution, you will be asked to provide **information**, configuration, and log files related to the encountered issue.

### Issue Description
* What is the ticket purpose? (Unexpected behavior, error message, technical question, etc.)
* What is the context? (Any known cause or event related)
* When did the problem start?
* What is the impact on service?

### Node & Cluster Configuration
* `/etc/opensvc/node.conf`
* `/etc/opensvc/cluster.conf`

### Logs
* Node agent log: `/var/log/opensvc/node.log`
* Scheduler agent log: `/var/log/opensvc/scheduler.log`
* **Object logs:**
    * `/var/log/opensvc/<service>.log`
    * **OR**
    * `/var/log/opensvc/namespaces/<namespace>/<kind>/<service>.log`

All **information** can be sent through email at [support@opensvc.com](mailto:support@opensvc.com) or uploaded using our [Support File Exchange](#support-file-exchange).

> **Note:** To save time in data collection, consider using the [SOS Report Data Collection Tool](#sos-report-data-collection-tool).

---

## SOS Report Data Collection Tool

Sos (formerly known as `sosreport`) is an extensible, portable support data collection tool primarily aimed at Linux distributions and other UNIX-like operating systems.

It is available on major distributions (RHEL, Ubuntu, Debian, Fedora, etc.) and supports OpenSVC environments (**sos version >= 4.2**).

```bash
# Check for opensvc plugin existence
user@node:~$ sudo sos report --list-plugins | grep opensvc

opensvc              OpenSVC cluster and services (config and state collection)

# Launch data collection on BOTH OpenSVC cluster nodes
user@node:~$ sudo sos report --enable-plugins opensvc --all-logs
```

*See the [Sos website](https://sos.readthedocs.io/) for more details.*

---

## Support Open Hours

Depending on your support subscription, you can call **us** according to the table below:

| Support Service Level | Open Hours                                |
|:----------------------|:------------------------------------------|
| **Standard**          | Monday to Friday, 9am to 6pm (Paris time) |
| **Premium**           | 24x7                                      |

---

## Support File Exchange

In case you need to share files with the support team, you can use either an email attachment or the secure file exchange web portal.

1. Open a browser to [https://sfx.opensvc.com](https://sfx.opensvc.com).
2. At the top right, there is a **Login** field and button; enter `support` and click the **Login** button.
3. Attach as many files as needed and submit for upload.
4. Once done, inform the support team that your upload is finished.

> **Note:** If allowed by your network security policy, you can use the `om <svcname> support` command to automatically:
> * Build a `tar.gz` with all required `<svcname>` logs.
> * Upload it to [https://sfx.opensvc.com](https://sfx.opensvc.com).

> **Note:** You can also directly upload any file using the `curl` command. In the example below, we use an internal web proxy named `my.preferred.proxy`, and the file to be sent is named `FILE_TO_UPLOAD.TAR.GZ`.

```bash
# export https_proxy=http://my.preferred.proxy:8080/
# curl -k -F 'file=@FILE_TO_UPLOAD.TAR.GZ;type=application/octet-stream' https://user:support@sfx.opensvc.com/+upload -X POST
```

---

## Premium Support Instructions

Nodes under a Premium support contract must be tagged in the associated collector to ensure proper node identification and accurate billing.

| Tag Action | Command                                               |
|:-----------|:------------------------------------------------------|
| **Set**    | `om node collector tag attach --name PREMIUM_SUPPORT` |
| **Unset**  | `om node collector tag detach --name PREMIUM_SUPPORT` |
| **Check**  | `om node collector tag show`                          |

> **Note:** Services running on a Premium supported node are implicitly included in the Premium support scope and billing.

Please get in touch with us for any questions you may have.