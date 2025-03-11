# CIS Oracle MySQL Enterprise Edition 8.4 Benchmark
**Version 1.0.0 - 01-29-2025**

## Table of Contents
- [Overview](#overview)
  - [Important Usage Information](#important-usage-information)
  - [Target Technology Details](#target-technology-details)
  - [Intended Audience](#intended-audience)
  - [Consensus Guidance](#consensus-guidance)
  - [Typographical Conventions](#typographical-conventions)
- [Recommendation Definitions](#recommendation-definitions)
- [Recommendations](#recommendations)
  - [1 Operating System Level Configuration](#1-operating-system-level-configuration)
  - [2 Installation and Planning](#2-installation-and-planning)
  - [3 File Permissions](#3-file-permissions)
  - [4 General](#4-general)
  - [5 MySQL Permissions](#5-mysql-permissions)
  - [6 Auditing and Logging](#6-auditing-and-logging)
  - [7 Authentication](#7-authentication)
  - [8 Network](#8-network)
  - [9 Replication](#9-replication)
  - [10 MySQL InnoDB Cluster / Group Replication](#10-mysql-innodb-cluster--group-replication)

## Overview

All CIS Benchmarks™ (Benchmarks) focus on technical configuration settings used to maintain and/or increase the security of the addressed technology, and they should be used in conjunction with other essential cyber hygiene tasks like:
- Monitoring the base operating system and applications for vulnerabilities and quickly updating with the latest security patches.
- End-point protection (Antivirus software, Endpoint Detection and Response (EDR), etc.).
- Logging and monitoring user and system activity.

In the end, the Benchmarks are designed to be a key component of a comprehensive cybersecurity program.

### Important Usage Information

All Benchmarks are available free for non-commercial use from the CIS Website. They can be used to manually assess and remediate systems and applications. In lieu of manual assessment and remediation, there are several tools available to assist with assessment:
- CIS Configuration Assessment Tool (CIS-CAT® Pro Assessor)
- CIS Benchmarks™ Certified 3rd Party Tooling

These tools make the hardening process much more scalable for large numbers of systems and applications.

> **NOTE**: Some tooling focuses only on the Benchmark Recommendations that can be fully automated (skipping ones marked Manual). It is important that ALL Recommendations (Automated and Manual) be addressed since all are important for properly securing systems and are typically in scope for audits.

#### Key Stakeholders

Cybersecurity is a collaborative effort, and cross functional cooperation is imperative within an organization to discuss, test, and deploy Benchmarks in an effective and efficient way. The Benchmarks are developed to be best practice configuration guidelines applicable to a wide range of use cases. In some organizations, exceptions to specific Recommendations will be needed, and this team should work to prioritize the problematic Recommendations based on several factors like risk, time, cost, and labor. These exceptions should be properly categorized and documented for auditing purposes.

#### Apply the Correct Version of a Benchmark

Benchmarks are developed and tested for a specific set of products and versions and applying an incorrect Benchmark to a system can cause the resulting pass/fail score to be incorrect. This is due to the assessment of settings that do not apply to the target systems. To assure the correct Benchmark is being assessed:

- Deploy the Benchmark applicable to the way settings are managed in the environment: An example of this is the Microsoft Windows family of Benchmarks, which have separate Benchmarks for Group Policy, Intune, and Stand-alone systems based upon how system management is deployed. Applying the wrong Benchmark in this case will give invalid results.
- Use the most recent version of a Benchmark: This is true for all Benchmarks, but especially true for cloud technologies. Cloud technologies change frequently and using an older version of a Benchmark may have invalid methods for auditing and remediation.

#### Exceptions

The guidance items in the Benchmarks are called recommendations and not requirements, and exceptions to some of them are expected and acceptable. The Benchmarks strive to be a secure baseline, or starting point, for a specific technology, with known issues identified during Benchmark development are documented in the Impact section of each Recommendation. In addition, organizational, system specific requirements, or local site policy may require changes as well, or an exception to a Recommendation or group of Recommendations (e.g. A Benchmark could Recommend that a Web server not be installed on the system, but if a system's primary purpose is to function as a Webserver, there should be a documented exception to this Recommendation for that specific server).

In the end, exceptions to some Benchmark Recommendations are common and acceptable, and should be handled as follows:
- The reasons for the exception should be reviewed cross-functionally and be well documented for audit purposes.
- A plan should be developed for mitigating, or eliminating, the exception in the future, if applicable.
- If the organization decides to accept the risk of this exception (not work toward mitigation or elimination), this should be documented for audit purposes.

It is the responsibility of the organization to determine their overall security policy, and which settings are applicable to their unique needs based on the overall risk profile for the organization.

#### Remediation

CIS has developed Build Kits for many technologies to assist in the automation of hardening systems. Build Kits are designed to correspond to Benchmark's "Remediation" section, which provides the manual remediation steps necessary to make that Recommendation compliant to the Benchmark.

> When remediating systems (changing configuration settings on deployed systems as per the Benchmark's Recommendations), please approach this with caution and test thoroughly.

The following is a reasonable remediation approach to follow:
- CIS Build Kits, or internally developed remediation methods should never be applied to production systems without proper testing.
- Proper testing consists of the following:
  - Understand the configuration (including installed applications) of the targeted systems. Various parts of the organization may need different configurations (e.g., software developers vs standard office workers).
  - Read the Impact section of the given Recommendation to help determine if there might be an issue with the targeted systems.
  - Test the configuration changes with representative lab system(s). If issues arise during testing, they can be resolved prior to deploying to any production systems.
  - When testing is complete, initially deploy to a small sub-set of production systems and monitor closely for issues. If there are issues, they can be resolved prior to deploying more broadly.
  - When the initial deployment above is completes successfully, iteratively deploy to additional systems and monitor closely for issues. Repeat this process until the full deployment is complete.

#### Summary

Using the Benchmarks Certified tools, working as a team with key stakeholders, being selective with exceptions, and being careful with remediation deployment, it is possible to harden large numbers of deployed systems in a cost effective, efficient, and safe manner.

> **NOTE**: As previously stated, the PDF versions of the CIS Benchmarks™ are available for free, non-commercial use on the CIS Website. All other formats of the CIS Benchmarks™ (MS Word, Excel, and Build Kits) are available for CIS SecureSuite® members. CIS-CAT® Pro is also available to CIS SecureSuite® members.

### Target Technology Details

This document, CIS Oracle MySQL Enterprise Edition 8.4 Benchmark, provides prescriptive guidance for establishing a secure configuration posture for MySQL Enterprise Edition 8.4. This guide was tested against MySQL Enterprise Edition 8.4 running on Oracle Linux, but applies to other Linux distributions as well. To obtain the latest version of this guide, please visit http://benchmarks.cisecurity.org. If you have questions, comments, or have identified ways to improve this guide, please write us at feedback@cisecurity.org.

### Intended Audience

This document is intended for system and application administrators, security specialists, auditors, help desk, and platform deployment personnel who plan to develop, deploy, assess, or secure solutions that incorporate Oracle MySQL Enterprise Edition 8.4.

### Consensus Guidance

This CIS Benchmark™ was created using a consensus review process comprised of a global community of subject matter experts. The process combines real world experience with data-based information to create technology specific guidance to assist users to secure their environments. Consensus participants provide perspective from a diverse set of backgrounds including consulting, software development, audit and compliance, security research, operations, government, and legal.

Each CIS Benchmark undergoes two phases of consensus review. The first phase occurs during initial Benchmark development. During this phase, subject matter experts convene to discuss, create, and test working drafts of the Benchmark. This discussion occurs until consensus has been reached on Benchmark recommendations. The second phase begins after the Benchmark has been published. During this phase, all feedback provided by the Internet community is reviewed by the consensus team for incorporation in the Benchmark. If you are interested in participating in the consensus process, please visit https://workbench.cisecurity.org/.

### Typographical Conventions

The following typographical conventions are used throughout this guide:

| Convention | Meaning |
|------------|---------|
| Stylized Monospace font | Used for blocks of code, command, and script examples. Text should be interpreted exactly as presented. |
| Monospace font | Used for inline code, commands, UI/Menu selections or examples. Text should be interpreted exactly as presented. |
| <Monospace font in brackets> | Text set in angle brackets denote a variable requiring substitution for a real value. |
| Italic font | Used to reference other relevant settings, CIS Benchmarks and/or Benchmark Communities. Also, used to denote the title of a book, article, or other publication. |
| Bold font | Additional information or caveats things like Notes, Warnings, or Cautions (usually just the word itself and the rest of the text normal). |

## Recommendation Definitions

The following defines the various components included in a CIS recommendation as applicable. If any of the components are not applicable it will be noted, or the component will not be included in the recommendation.

### Title

Concise description for the recommendation's intended configuration.

### Assessment Status

An assessment status is included for every recommendation. The assessment status indicates whether the given recommendation can be automated or requires manual steps to implement. Both statuses are equally important and are determined and supported as defined below:

#### Automated

Represents recommendations for which assessment of a technical control can be fully automated and validated to a pass/fail state. Recommendations will include the necessary information to implement automation.

#### Manual

Represents recommendations for which assessment of a technical control cannot be fully automated and requires all or some manual steps to validate that the configured state is set as expected. The expected state can vary depending on the environment.

### Profile

A collection of recommendations for securing a technology or a supporting platform. Most benchmarks include at least a Level 1 and Level 2 Profile. Level 2 extends Level 1 recommendations and is not a standalone profile. The Profile Definitions section in the benchmark provides the definitions as they pertain to the recommendations included for the technology.

### Description

Detailed information pertaining to the setting with which the recommendation is concerned. In some cases, the description will include the recommended value.

### Rationale Statement

Detailed reasoning for the recommendation to provide the user a clear and concise understanding on the importance of the recommendation.

### Impact Statement

Any security, functionality, or operational consequences that can result from following the recommendation.

### Audit Procedure

Systematic instructions for determining if the target system complies with the recommendation.

### Remediation Procedure

Systematic instructions for applying recommendations to the target system to bring it into compliance according to the recommendation.

### Default Value

Default value for the given setting in this recommendation, if known. If not known, either not configured or not defined will be applied.

### References

Additional documentation relative to the recommendation.

### CIS Critical Security Controls® (CIS Controls®)

The mapping between a recommendation and the CIS Controls is organized by CIS Controls version, Safeguard, and Implementation Group (IG). The Benchmark in its entirety addresses the CIS Controls safeguards of (v7) "5.1 - Establish Secure Configurations" and (v8) '4.1 - Establish and Maintain a Secure Configuration Process" so individual recommendations will not be mapped to these safeguards.

### Additional Information

Supplementary information that does not correspond to any other field but may be useful to the user.

## Profile Definitions

The following configuration profiles are defined by this Benchmark:

- **Level 1 - MySQL RDBMS on Linux**  
  Items in this profile apply to MySQL Enterprise Edition 8.4 running on Linux and intend to:
  - be practical and prudent;
  - provide a clear security benefit; and
  - not inhibit the utility of the technology beyond acceptable means.

- **Level 2 - MySQL RDBMS on Linux**  
  This profile extends the "Level 1 - MySQL RDBMS on Linux" profile. Items in this profile apply to MySQL Enterprise Edition 8.4 running on Linux and exhibit one or more of the following characteristics:
  - are intended for environments or use cases where security is paramount
  - acts as defense in depth measure
  - may negatively inhibit the utility or performance of the technology.

- **Level 1 - MySQL RDBMS**  
  Items in this profile apply to MySQL Enterprise Edition 8.4 and intend to:
  - be practical and prudent;
  - provide a clear security benefit; and
  - not inhibit the utility of the technology beyond acceptable means.  
  Note: The intent of this profile is to include checks that can be assessed by remotely connecting to a MySQL RDBMS. Therefore, file system-related checks are not contained in this profile.

- **Level 2 - MySQL RDBMS**  
  This profile extends the "Level 1 - MySQL RDBMS" profile. Items in this profile apply to MySQL Enterprise Edition 8.4 and exhibit one or more of the following characteristics:
  - are intended for environments or use cases where security is paramount
  - acts as defense in depth measure
  - may negatively inhibit the utility or performance of the technology.  
  Note: The intent of this profile is to include checks that can be assessed by remotely connecting to a MySQL RDBMS. Therefore, file system-related checks are not contained in this profile.

## Recommendations

### 1 Operating System Level Configuration

This section contains recommendations related to the Operating System on which the MySQL database server is running.

#### 1.1 Place Databases on Non-System Partitions (Manual)

**Profile Applicability:** Level 1 - MySQL RDBMS on Linux

**Description:**  
It is generally accepted that host operating systems should include different filesystem partitions for different purposes. One set of filesystems is typically called system partitions, and these are generally reserved for host system/application operation. The other set of filesystems is typically called "non-system partitions", and such locations are generally reserved for storing data.

**Rationale:**  
Moving the database off the system partition will reduce the probability of denial of service caused by exhaustion of available disk space to the operating system.

**Impact:**  
Moving database files and directories to a non-system partition may be difficult depending on whether there was only a single partition when the operating system was set up and whether there are additional non-system partitions available.

**Audit:**  
Execute the following steps to assess this recommendation:

1. Obtain the location of the datadir and other MySQL database files by executing the following SQL statement:
   ```sql
   SELECT VARIABLE_NAME, VARIABLE_VALUE
   FROM performance_schema.global_variables
   WHERE (VARIABLE_NAME LIKE '%dir' or VARIABLE_NAME LIKE '%file') and
   (VARIABLE_NAME NOT LIKE '%core%'
   AND VARIABLE_NAME <> 'local_infile' AND VARIABLE_NAME <>
   'relay_log_info_file') order by
   VARIABLE_NAME;
   ```

2. Using the value returned for the datadir, and other results from the above query, execute the following in a system terminal:
   ```bash
   df -h <directory>
   ```
   The output returned from the df command above should not include root (/), /var, or /usr.

**Remediation:**  
Perform the following steps to remediate this setting for the datadir:

1. Backup the database.
2. Choose a non-system partition new location for MySQL data.
3. Stop mysqld using a command like: `service mysql stop`.
4. Copy the data using a command like: `cp -rp<datadir Value> <new location>`.
5. Set the datadir location to the new location in the MySQL configuration file.
6. Start mysqld using a command like: `service mysql start`

Note: On some Linux distributions you may need to additionally modify apparmor settings. For example, on a Ubuntu 14.04.1 system edit the file `/etc/apparmor.d/usr.sbin.mysqld` so that the datadir access is appropriate. The original might look like this:
```
# Allow data dir access
/var/lib/mysql/ r,
/var/lib/mysql/** rwk,
```

Alter those two paths to be the new location you chose above. For example, if that new location were /media/mysql, then the `/etc/apparmor.d/usr.sbin.mysqld` file should include something like this:
```
# Allow data dir access
/media/mysql/ r,
/media/mysql/** rwk,
```

**Default Value:** Not Applicable.

**References:**  
1. https://dev.mysql.com/doc/mysql-secure-deployment-guide/8.4/en/secure-deployment-permissions.html

#### 1.2 Use Dedicated Least Privileged Account for MySQL Daemon/Service (Automated)

**Profile Applicability:** Level 1 - MySQL RDBMS on Linux

**Description:**  
As with any service installed on a host, it can be provided with its own user context. Providing a dedicated user to the service provides the ability to precisely constrain the service within the larger host context.

**Rationale:**  
Utilizing a least privilege account for MySQL to execute as needed may reduce the impact of a MySQL-born vulnerability. A restricted account will be unable to access resources unrelated to MySQL, such as operating system configurations.

**Audit:**  
Execute the following command at a terminal prompt to assess this recommendation:
```bash
ps -ef | egrep "^mysql.*$"
```
If no lines are returned, then this is a fail.

Note: It is assumed that the MySQL user is mysql. Additionally, you may consider running `sudo -l` as the MySQL user or to check the sudoers file.

**Remediation:**  
Create a user which is only used for running MySQL and directly related processes. This user must not have administrative rights to the system. Additionally, it's best to avoid providing shell access to such an account.

Shell access can be removed using the following command at a terminal prompt:
```bash
/usr/sbin/groupadd -g 27 -o -r mysql >/dev/null 2>&1 || :
/usr/sbin/useradd -M -N -g mysql -o -r -d /var/lib/mysql -s /bin/false \
-c "MySQL Server" -u 27 mysql >/dev/null 2>&1 || :
```

**References:**  
1. https://dev.mysql.com/doc/refman/8.4/en/changing-mysql-user.html
2. https://dev.mysql.com/doc/refman/8.4/en/server-options.html#option_mysqld_user

**Additional Information:**  
The root user may be used to start the MySQL service on Linux/UNIX, but then it must be configured to drop privileges by specifying a service specific user in the my.cnf or my.ini file.

#### 1.3 Disable MySQL Command History (Automated)

**Profile Applicability:** Level 2 - MySQL RDBMS on Linux

**Description:**  
On Linux/UNIX, the MySQL client and MySQL Shell log statements executed interactively to a history file. The default MySQL Client file is named .mysql_history in the user's home directory. The files are split by language and named history.sql, history.js and history.py. Most interactive commands run in the MySQL client application are saved to a history file. The MySQL command history should be disabled. By default, the MySQL Shell does not save history between sessions.

**Rationale:**  
Disabling the MySQL Client and MySQL Shell command history reduces the probability of exposing sensitive information, such as passwords, encryption keys, or other sensitive data or information.

**Audit:**  
Execute the following commands to assess this recommendation:
```bash
find /home -name ".mysql_history"
find /root -name ".mysql_history"
```

For MySQL Shell:
```bash
ls -d .??*/* | egrep history | grep mysql
```

For each file returned determine whether that file is symbolically linked to /dev/null.

**Remediation:**  
For MySQL Client perform the following steps to remediate this setting:

1. Remove .mysql_history if it exists.
2. Use either of the techniques below to prevent it from being created again:
   - Set the MYSQL_HISTFILE environment variable to /dev/null. This will need to be placed in the shell's startup script.
   - Create $HOME/.mysql_history as a symbolic to /dev/null.
     ```bash
     ln -s /dev/null $HOME/.mysql_history
     ```

Another way to prevent history from being recorded is to use --batch option.

For MySQL Shell perform the following steps to remediate this setting:
1. Remove $HOME/.mysqlsh/history.* if files exists.
2. Use either of the techniques below to prevent it from being created again:
   - Start shell and list show options using `\option -l`
   - Set to no history using the command `\option --persist history.autoSave=1`

**Default Value:**  
By default, the MySQL command history file is located in $HOME/.mysql_history.

**References:**  
1. https://dev.mysql.com/doc/refman/8.4/en/mysql-logging.html
2. https://bugs.mysql.com/bug.php?id=72158
3. https://dev.mysql.com/doc/mysql-shell/8.4/en/mysql-shell-working-with-history.html

#### 1.4 Verify That the MYSQL_PWD Environment Variable is Not in Use (Automated)

**Profile Applicability:** Level 1 - MySQL RDBMS on Linux

**Description:**  
MySQL can read a default database password from an environment variable called MYSQL_PWD. Avoiding use of this environment variable can better safeguard the confidentiality of MySQL credentials.

**Rationale:**  
Using the MYSQL_PWD environment variable implies MySQL credentials are stored as clear text.

**Audit:**  
To assess this recommendation, use the /proc filesystem to determine if MYSQL_PWD is currently set for any process:
```bash
grep MYSQL_PWD /proc/*/environ
```
This may return one entry for the process which is executing the grep command.

**Remediation:**  
Check which users and/or scripts are setting MYSQL_PWD and change them to use a more secure method.

For unattended logins you should consider:
1. MySQL Configuration Editor
2. Different authentication methods (e.g., X509 certificate verification)
3. Use MySQL Enterprise LDAP plugin with Kerberos or SASL tokens.

**Default Value:** Not set.

**References:**  
1. https://dev.mysql.com/doc/refman/8.4/en/environment-variables.html
2. https://dev.mysql.com/doc/refman/8.4/en/mysql-config-editor.html
3. https://dev.mysql.com/doc/refman/8.4/en/pluggable-authentication.html

#### 1.5 Ensure Interactive Login is Disabled (Automated)

**Profile Applicability:** Level 2 - MySQL RDBMS on Linux

**Description:**  
When created, the MySQL user may have interactive access to the operating system, which means that the MySQL user could login to the host as any other user would.

**Rationale:**  
Preventing the MySQL user from logging in interactively may reduce the impact of a compromised MySQL account. There is also more accountability, as accessing the operating system where the MySQL server lies will require the user's own account. Interactive access by the MySQL user is unnecessary and should be disabled.

**Impact:**  
This setting will prevent the MySQL administrator from interactively logging into the operating system using the MySQL user. Instead, the administrator will need to log in using one's own account.

**Audit:**  
Execute the following command to assess this recommendation:
```bash
getent passwd mysql | egrep "^.*[\/bin\/false|\/sbin\/nologin]$"
```
Lack of output implies a fail.

**Remediation:**  
Execute one of the following commands in a terminal:
```bash
usermod -s /bin/false mysql
```
Or
```bash
usermod -s /sbin/nologin mysql
```

#### 1.6 Verify That 'MYSQL_PWD' is Not Set in Users' Profiles (Automated)

**Profile Applicability:** Level 1 - MySQL RDBMS on Linux

**Description:**  
MySQL can read a default database password from an environment variable called MYSQL_PWD.

**Rationale:**  
Use of the MYSQL_PWD environment variable implies MySQL credentials are stored as clear text. Avoiding use of this environment variable may increase assurance that the confidentiality of MySQL credentials is preserved.

**Audit:**  
To assess this recommendation, check if MYSQL_PWD is set in login scripts using the following command:
```bash
grep MYSQL_PWD /home/*/.{bashrc,profile,bash_profile}
```

**Remediation:**  
Check which users and/or scripts are setting MYSQL_PWD and change them to use a more secure method.

**Default Value:** Not set.

**References:**  
1. https://dev.mysql.com/doc/refman/8.4/en/environment-variables.html

#### 1.7 Ensure MySQL is Run Under a Sandbox Environment (Manual)

**Profile Applicability:** 
- Level 2 - MySQL RDBMS on Linux
- Level 2 - MySQL RDBMS

**Description:**  
Use of the chroot() system call at startup, Systemd with settings to achieve isolation, or docker will put MySQL in a Sandbox environment.

**Rationale:**  
Running MySQL in a Sandbox environment may reduce the impact of a MySQL-born vulnerability by making portions of the file system inaccessible to the MySQL instance.

**Impact:**  
Use of the chroot option somewhat limits LOAD DATA INFILE and SELECT ... INTO OUTFILE.

**Audit:**  
Perform the following steps for each mySQL instance to assess this recommendation:

1. Execute the following SQL statement to determine the value of chroot:
   ```bash
   cat /etc/mysql | egrep '(?<=^chroot=).+$'
   ```
   The returned value should specify a valid path which differs from the datadir. No results implies 'chroot' is not in use.

2. Perform the following to check systemd:
   ```bash
   systemctl status <mysqld>.service
   ```
   If something other than (root) is listed beside the PID, e.g. Main PID: <PID> (root), this is a pass. No results implies mysql is not managed by systemd.

3. Perform the following to determine if Docker is installed and a MySQL container is in use:
   1. To check for docker installation, execute this command:
      ```bash
      $ docker -v
      ```
      If a message stating the version of docker which is installed proceed to the next steps, otherwise no further action is needed as docker must be installed for mysql to be run in docker.
   
   2. To check if a mysql image exists in docker run this command:
      ```bash
      $ sudo docker images
      REPOSITORY TAG IMAGE ID CREATED SIZE
      mysql latest 2fe463762680 1 week ago 514MB
      mysql/mysql-server latest 1504607f1ce7 2 weeks ago 401MB
      ```
      If a mysql image is listed proceed to the next steps, otherwise no further action is needed as a mysql image is required for mysql to be run in docker.
   
   3. Check if a mysql container is running:
      ```bash
      $ sudo docker ps
      CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
      0fc229e3df77 mysql "docker…" 1 hour ago Up 1 hour 0.0.0.0:3306->3306/tcp, mysql-server
      :::3306->3306/tcp, 33060/tcp
      ```
      If a mysql container is listed then mysql is running in docker and this is a pass.

If MySQL does not use chroot, systemd, or docker, this is a fail.

**Remediation:**  
Perform one of the following steps to remediate this setting:

- Configure MySQL to use chroot:
  1. Choose a non-system partition <chroot location> for MySQL
  2. Add `chroot=<chroot_location>` to the my.cnf option file

- Configure MySQL to run under systemd:
  1. If mysql is managed by systemd and running, stop the service:
     ```bash
     $ sudo systemctl stop <mysqld>.service
     ```
  2. If a mysql user and group do not already exist, create them:
     ```bash
     $ sudo groupadd mysql
     $ sudo useradd -r -g mysql -s /bin/false mysql
     ```
  3. Set the ownership of the base director:
     ```bash
     $ sudo chown -R mysql:mysql /usr/local/mysql/
     ```
  4. Create or modify the <mysqld>.service file in /lib/systemd/system to include the following entries, if not already present:
     ```
     [Unit]
     Description=MySQL Server
     [Install]
     WantedBy=multi-user.target
     [Service]
     User=mysql
     Group=mysql
     ```
  5. If mysql was not already already managed by systemd execute this command:
     ```bash
     $ sudo systemctl daemon-reload
     ```
  6. Start the MySQL server:
     ```bash
     $ sudo systemctl start <mysqld>.service
     ```
  7. If you would like mysql to automatically run at startup execute this command:
     ```bash
     $ sudo systemctl enable <mysqld>.service
     ```

- Follow documentation in the references for standing up MySQL in a Docker container.

**References:**  
1. https://dev.mysql.com/doc/refman/8.4/en/server-options.html#option_mysqld_chroot
2. https://dev.mysql.com/doc/refman/8.4/en/docker-mysql-getting-started.html
3. https://hub.docker.com/r/mysql/mysql-server