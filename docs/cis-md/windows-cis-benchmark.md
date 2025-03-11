# Table of Contents

- [Terms of Use](#terms-of-use)
- [Table of Contents](#table-of-contents)
- [Overview](#overview)
  - [Important Usage Information](#important-usage-information)
    - [Key Stakeholders](#key-stakeholders)
    - [Apply the Correct Version of a Benchmark](#apply-the-correct-version-of-a-benchmark)
    - [Exceptions](#exceptions)
    - [Remediation](#remediation)
    - [Summary](#summary)
  - [Target Technology Details](#target-technology-details)
  - [Intended Audience](#intended-audience)
  - [Consensus Guidance](#consensus-guidance)
  - [Typographical Conventions](#typographical-conventions)
- [Recommendation Definitions](#recommendation-definitions)
  - [Title](#title)
  - [Assessment Status](#assessment-status)
    - [Automated](#automated)
    - [Manual](#manual)
  - [Profile](#profile)
  - [Description](#description)
  - [Rationale Statement](#rationale-statement)
  - [Impact Statement](#impact-statement)
  - [Audit Procedure](#audit-procedure)
  - [Remediation Procedure](#remediation-procedure)
  - [Default Value](#default-value)
  - [References](#references)
  - [CIS Critical Security Controls®(CIS Controls®)](#cis-critical-security-controlscis-controls)
  - [Additional Information](#additional-information)
  - [Profile Definitions](#profile-definitions)
  - [Acknowledgements](#acknowledgements)
- [Recommendations](#recommendations)
  - [1 Account Policies](#1-account-policies)
    - [1.1 Password Policy](#11-password-policy)
      - [1.1.1 Ensure 'Enforce password history' is set to '24 or more password(s)' (Automated)](#111-ensure-enforce-password-history-is-set-to-24-or-more-passwords-automated)
      - [1.1.2 Ensure 'Maximum password age' is set to '365 or fewer days, but not 0' (Automated)](#112-ensure-maximum-password-age-is-set-to-365-or-fewer-days-but-not-0-automated)
      - [1.1.3 Ensure 'Maximum password age' is set to '60 or fewer days, but not 0' (STIG only) (Automated)](#113-ensure-maximum-password-age-is-set-to-60-or-fewer-days-but-not-0-stig-only-automated)
      - [1.1.4 Ensure 'Minimum password age' is set to '1 or more day(s)' (Automated)](#114-ensure-minimum-password-age-is-set-to-1-or-more-days-automated)
      - [1.1.5 Ensure 'Minimum password length' is set to '14 or more character(s)' (Automated)](#115-ensure-minimum-password-length-is-set-to-14-or-more-characters-automated)
      - [1.1.6 Ensure 'Password must meet complexity requirements' is set to 'Enabled' (Automated)](#116-ensure-password-must-meet-complexity-requirements-is-set-to-enabled-automated)
      - [1.1.7 Ensure 'Relax minimum password length limits' is set to 'Enabled' (Automated)](#117-ensure-relax-minimum-password-length-limits-is-set-to-enabled-automated)
      - [1.1.8 Ensure 'Store passwords using reversible encryption' is set to 'Disabled' (Automated)](#118-ensure-store-passwords-using-reversible-encryption-is-set-to-disabled-automated)

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

**NOTE:** Some tooling focuses only on the Benchmark Recommendations that can be fully automated (skipping ones marked Manual). It is important that ALL Recommendations (Automated and Manual) be addressed since all are important for properly securing systems and are typically in scope for audits.

### Key Stakeholders

Cybersecurity is a collaborative effort, and cross functional cooperation is imperative within an organization to discuss, test, and deploy Benchmarks in an effective and efficient way. The Benchmarks are developed to be best practice configuration guidelines applicable to a wide range of use cases. In some organizations, exceptions to specific Recommendations will be needed, and this team should work to prioritize the problematic Recommendations based on several factors like risk, time, cost, and labor. These exceptions should be properly categorized and documented for auditing purposes.

### Apply the Correct Version of a Benchmark

Benchmarks are developed and tested for a specific set of products and versions and applying an incorrect Benchmark to a system can cause the resulting pass/fail score to be incorrect. This is due to the assessment of settings that do not apply to the target systems. To assure the correct Benchmark is being assessed:

- **Deploy the Benchmark applicable to the way settings are managed in the environment:** An example of this is the Microsoft Windows family of Benchmarks, which have separate Benchmarks for Group Policy, Intune, and Stand-alone systems based upon how system management is deployed. Applying the wrong Benchmark in this case will give invalid results.
- **Use the most recent version of a Benchmark:** This is true for all Benchmarks, but especially true for cloud technologies. Cloud technologies change frequently and using an older version of a Benchmark may have invalid methods for auditing and remediation.

### Exceptions

The guidance items in the Benchmarks are called recommendations and not requirements, and exceptions to some of them are expected and acceptable. The Benchmarks strive to be a secure baseline, or starting point, for a specific technology, with known issues identified during Benchmark development are documented in the Impact section of each Recommendation. In addition, organizational, system specific requirements, or local site policy may require changes as well, or an exception to a Recommendation or group of Recommendations (e.g. A Benchmark could Recommend that a Web server not be installed on the system, but if a system's primary purpose is to function as a Webserver, there should be a documented exception to this Recommendation for that specific server).

In the end, exceptions to some Benchmark Recommendations are common and acceptable, and should be handled as follows:

- The reasons for the exception should be reviewed cross-functionally and be well documented for audit purposes.
- A plan should be developed for mitigating, or eliminating, the exception in the future, if applicable.
- If the organization decides to accept the risk of this exception (not work toward mitigation or elimination), this should be documented for audit purposes.

It is the responsibility of the organization to determine their overall security policy, and which settings are applicable to their unique needs based on the overall risk profile for the organization.

### Remediation

CIS has developed Build Kits for many technologies to assist in the automation of hardening systems. Build Kits are designed to correspond to Benchmark's "Remediation" section, which provides the manual remediation steps necessary to make that Recommendation compliant to the Benchmark.

**When remediating systems (changing configuration settings on deployed systems as per the Benchmark's Recommendations), please approach this with caution and test thoroughly.**

The following is a reasonable remediation approach to follow:

- CIS Build Kits, or internally developed remediation methods should never be applied to production systems without proper testing.
- Proper testing consists of the following:
  - Understand the configuration (including installed applications) of the targeted systems. Various parts of the organization may need different configurations (e.g., software developers vs standard office workers).
  - Read the Impact section of the given Recommendation to help determine if there might be an issue with the targeted systems.
  - Test the configuration changes with representative lab system(s). If issues arise during testing, they can be resolved prior to deploying to any production systems.
  - When testing is complete, initially deploy to a small sub-set of production systems and monitor closely for issues. If there are issues, they can be resolved prior to deploying more broadly.
  - When the initial deployment above is completes successfully, iteratively deploy to additional systems and monitor closely for issues. Repeat this process until the full deployment is complete.

### Summary

Using the Benchmarks Certified tools, working as a team with key stakeholders, being selective with exceptions, and being careful with remediation deployment, it is possible to harden large numbers of deployed systems in a cost effective, efficient, and safe manner.

**NOTE:** As previously stated, the PDF versions of the CIS Benchmarks™ are available for free, non-commercial use on the CIS Website. All other formats of the CIS Benchmarks™ (MS Word, Excel, and Build Kits) are available for CIS SecureSuite® members.

CIS-CAT® Pro is also available to CIS SecureSuite® members.

### Target Technology Details

This document provides prescriptive guidance for establishing a secure configuration posture for Microsoft Windows.

This secure configuration guide is based on Microsoft Windows Server 2022 Security Technical Implementation Guide (STIG) and is intended for all versions of the Server 2022 operating system, including older versions. This secure configuration guide was tested against Microsoft Windows Server 2022 Datacenter.

To ensure all new and updated group policy objects (GPOs) are installed on the system, please download the newest version of the ADMX/ADML templates for Windows 11. Templates can be downloaded from Microsoft at: Download ADMX Templates for Windows 11 2023 Update [23H2] - v3.0 from Official Microsoft Download Center.

To obtain the latest version of this secure configuration guide, please visit https://www.cisecurity.org/cis-benchmarks/. If you have questions, comments, or have identified ways to improve this guide, please write us at feedback@cisecurity.org.

### Intended Audience

The Windows CIS Benchmarks are written for Active Directory domain-joined systems using Group Policy, not standalone/workgroup systems. Adjustments/tailoring to some recommendations will be needed to maintain functionality if attempting to implement CIS hardening on standalone systems or a system running in the cloud.

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

### Profile Definitions

The following configuration profiles are defined by this Benchmark:

- **Level 1 - Domain Controller**
  
  Items in this profile apply to Domain Controllers and intend to:
  - be practical and prudent;
  - provide a clear security benefit; and
  - not inhibit the utility of the technology beyond acceptable means.

- **Level 1 - Member Server**
  
  Items in this profile apply to Member Servers and intend to:
  - be practical and prudent;
  - provide a clear security benefit; and
  - not inhibit the utility of the technology beyond acceptable means.
  
  Items in this profile also apply to Member Servers that have the following Roles enabled:
  - AD Certificate Services
  - DHCP Server
  - DNS Server
  - File Server
  - Hyper-V
  - Network Policy and Access Services
  - Print Server
  - Remote Access Services
  - Remote Desktop Services
  - Web Server

- **Level 2 - Domain Controller**
  
  This profile extends the "Level 1 - Domain Controller" profile. Items in this profile exhibit one or more of the following characteristics:
  - are intended for environments or use cases where security is paramount
  - acts as defense in depth measure
  - may negatively inhibit the utility or performance of the technology

- **Level 2 - Member Server**
  
  This profile extends the "Level 1 - Member Server" profile. Items in this profile exhibit one or more of the following characteristics:
  - are intended for environments or use cases where security is paramount
  - acts as defense in depth measure
  - may negatively inhibit the utility or performance of the technology

- **Next Generation Windows Security - Domain Controller**
  
  This profile contains advanced Windows security features that have specific configuration dependencies, and may not be compatible with all systems. It therefore requires special attention to detail and testing before implementation. If your environment supports these features, they are highly recommended as they have tangible security benefits. This profile is intended to be an optional "add-on" to the Level 1 or Level 2 profiles.

- **Next Generation Windows Security - Member Server**
  
  This profile contains advanced Windows security features that have specific configuration dependencies, and may not be compatible with all systems. It therefore requires special attention to detail and testing before implementation. If your environment supports these features, they are highly recommended as they have tangible security benefits. This profile is intended to be an optional "add-on" to the Level 1 or Level 2 profiles.

- **STIG Domain Controller**
  
  This profile includes recommendations from the DoD Microsoft Windows Server 2019 Security Technical Implementation Guide. Overlap of recommendations from the CIS Level 1, Level 2, and NextGeneration profiles are present. If any of the CIS Level 1, Level 2, and NextGeneration profiles are applied, changes will need to be made since there can be a difference in configurations from the STIG profile. Note: Configuration differences are stated in the description of the recommendation, if present.
  
  Items in this profile exhibit one or more of the following characteristics:
  - are intended for environments or use cases where following STIG security is paramount;
  - acts as even greater defense in depth measure;
  - may negatively inhibit the utility or performance of the technology.

- **STIG Member Server**
  
  This profile includes recommendations from the DoD Microsoft Windows Server 2019 Security Technical Implementation Guide. Overlap of recommendations from the CIS Level 1, Level 2, and NextGeneration profiles are present. If any of the CIS Level 1, Level 2, and NextGeneration profiles are applied, changes will need to be made since there can be a difference in configurations from the STIG profile. Note: Configuration differences are stated in the description of the recommendation, if present.
  
  Items in this profile exhibit one or more of the following characteristics:
  - are intended for environments or use cases where following STIG security is paramount;
  - acts as even greater defense in depth measure;
  - may negatively inhibit the utility or performance of the technology.

### Acknowledgements

This Benchmark exemplifies the great things a community of users, vendors, and subject matter experts can accomplish through consensus collaboration. The CIS community thanks the entire consensus team with special recognition to the following individuals who contributed greatly to the creation of this guide:

The Center for Internet Security extends special recognition and thanks to Rick Munck from Microsoft, as well as Mike Harris from General Dynamics Information Technology for their collaboration developing the configuration recommendations contained in this document.

**Editor**
- Haemish Edgerton
- Jennifer Jarose

**Contributor**
- Caleb Eifert
- Aaron Margosis
- Hardeep Mehrotara
- Phil White
- Matthew Woods
- Kevin Zhang

## Recommendations

### 1 Account Policies

This section contains recommendations for account policies.

#### 1.1 Password Policy

This section contains recommendations for password policy.

##### 1.1.1 Ensure 'Enforce password history' is set to '24 or more password(s)' (Automated)

**Profile Applicability:**
- Level 1 - Domain Controller
- Level 1 - Member Server
- STIG Domain Controller
- STIG Member Server

**Description:**
This policy setting determines the number of renewed, unique passwords that have to be associated with a user account before you can reuse an old password. The value for this policy setting must be between 0 and 24 passwords. The default value for stand-alone systems is 0 passwords, but the default setting when joined to a domain is 24 passwords. To maintain the effectiveness of this policy setting, use the Minimum password age setting to prevent users from repeatedly changing their password.

The recommended state for this setting is: 24 or more password(s).

**Note:** Password Policy settings (section 1.1) and Account Lockout Policy settings (section 1.2) must be applied via the Default Domain Policy GPO in order to be globally in effect on domain user accounts as their default behavior. If these settings are configured in another GPO, they will only affect local user accounts on the computers that receive the GPO. However, custom exceptions to the default password policy and account lockout policy rules for specific domain users and/or groups can be defined using Password Settings Objects (PSOs), which are completely separate from Group Policy and most easily configured using Active Directory Administrative Center.

**Note #2:** As of the publication of this benchmark, Microsoft currently has a maximum limit of 24 saved passwords. For more information, please visit Enforce password history (Windows 10) - Windows security | Microsoft Docs

**Rationale:**
The longer a user uses the same password, the greater the chance that an attacker can determine the password through brute force attacks. Also, any accounts that may have been compromised will remain exploitable for as long as the password is left unchanged. If password changes are required but password reuse is not prevented, or if users continually reuse a small number of passwords, the effectiveness of a good password policy is greatly reduced.

If you specify a low number for this policy setting, users will be able to use the same small number of passwords repeatedly. If you do not also configure the Minimum password age setting, users might repeatedly change their passwords until they can reuse their original password.

**Impact:**
The major impact of this configuration is that users must create a new password every time they are required to change their old one. If users are required to change their passwords to new unique values, there is an increased risk of users who write their passwords somewhere so that they do not forget them. Another risk is that users may create passwords that change incrementally (for example, password01, password02, and so on) to facilitate memorization but make them easier to guess. Also, an excessively low value for the Minimum password age setting will likely increase administrative overhead, because users who forget their passwords might ask the help desk to reset them frequently.

**Audit:**
Navigate to the UI Path articulated in the Remediation section and confirm it is set as prescribed.

**Remediation:**
To establish the recommended configuration via GP, set the following UI path to 24 or more password(s):

Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Enforce password history

**Default Value:**
24 passwords remembered on domain members. 0 passwords remembered on standalone servers.

**References:**
1. https://www.cisecurity.org/white-papers/cis-password-policy-guide/

**Additional Information:**
Microsoft Windows Server 2022 Security Technical Implementation Guide:
Version 2, Release 2, Benchmark Date: November 24, 2024

Vul ID: V-254288
Rule ID: SV-254288r1000156_rule
STIG ID: WN22-AC-000040
Severity: CAT II

**CIS Controls:**

| Controls Version | Control | IG 1 | IG 2 | IG 3 |
|------------------|---------|------|------|------|
| v8 | 5.2 Use Unique Passwords<br>Use unique passwords for all enterprise assets. Best practice implementation includes, at a minimum, an 8-character password for accounts using MFA and a 14-character password for accounts not using MFA. | ● | ● | ● |
| v7 | 16.2 Configure Centralized Point of Authentication<br>Configure access for all accounts through as few centralized points of authentication as possible, including network, security, and cloud systems. | | ● | ● |

##### 1.1.2 Ensure 'Maximum password age' is set to '365 or fewer days, but not 0' (Automated)

**Profile Applicability:**
- Level 1 - Domain Controller
- Level 1 - Member Server

**Description:**
This policy setting defines how long a user can use their password before it expires.

Values for this policy setting range from 0 to 999 days. If you set the value to 0, the password will never expire.

Because attackers can crack passwords, the more frequently you change the password the less opportunity an attacker has to use a cracked password. However, the lower this value is set, the higher the potential for an increase in calls to help desk support due to users having to change their password or forgetting which password is current.

The recommended state for this setting is 365 or fewer days, but not 0.

**Note:** Password Policy settings (section 1.1) and Account Lockout Policy settings (section 1.2) must be applied via the Default Domain Policy GPO in order to be globally in effect on domain user accounts as their default behavior. If these settings are configured in another GPO, they will only affect local user accounts on the computers that receive the GPO. However, custom exceptions to the default password policy and account lockout policy rules for specific domain users and/or groups can be defined using Password Settings Objects (PSOs), which are completely separate from Group Policy and most easily configured using Active Directory Administrative Center.

**Rationale:**
The longer a password exists the higher the likelihood that it will be compromised by a brute force attack, by an attacker gaining general knowledge about the user, or by the user sharing the password. Configuring the Maximum password age setting to 0 so that users are never required to change their passwords is a major security risk because that allows a compromised password to be used by the malicious user for as long as the valid user has authorized access.

**Impact:**
If the Maximum password age setting is too low, users are required to change their passwords very often. Such a configuration can reduce security in the organization, because users might write their passwords in an insecure location or lose them. If the value for this policy setting is too high, the level of security within an organization is reduced because it allows potential attackers more time in which to discover user passwords or to use compromised accounts.

**Audit:**
Navigate to the UI Path articulated in the Remediation section and confirm it is set as prescribed.

**Remediation:**
To establish the recommended configuration via GP, set the following UI path to 365 or fewer days, but not 0:

Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Maximum password age

**Default Value:**
42 days.

**References:**
1. https://www.cisecurity.org/white-papers/cis-password-policy-guide/

**CIS Controls:**

| Controls Version | Control | IG 1 | IG 2 | IG 3 |
|------------------|---------|------|------|------|
| v8 | 5.2 Use Unique Passwords<br>Use unique passwords for all enterprise assets. Best practice implementation includes, at a minimum, an 8-character password for accounts using MFA and a 14-character password for accounts not using MFA. | ● | ● | ● |
| v7 | 16.10 Ensure All Accounts Have An Expiration Date<br>Ensure that all accounts have an expiration date that is monitored and enforced. | | ● | ● |

##### 1.1.3 Ensure 'Maximum password age' is set to '60 or fewer days, but not 0' (STIG only) (Automated)

**Profile Applicability:**
- STIG Domain Controller
- STIG Member Server

**Description:**
This policy setting defines how long a user can use their password before it expires.

Values for this policy setting range from 0 to 999 days. If you set the value to 0, the password will never expire.

Because attackers can crack passwords, the more frequently you change the password the less opportunity an attacker has to use a cracked password. However, the lower this value is set, the higher the potential for an increase in calls to help desk support due to users having to change their password or forgetting which password is current.

The recommended STIG state for this setting is 60 or fewer days, but not 0.

**Note:** The CIS recommended state for this setting is: 365 or fewer days, but not 0, which differs from the STIG recommended state.

**Note:** Password Policy settings (section 1.1) and Account Lockout Policy settings (section 1.2) must be applied via the Default Domain Policy GPO in order to be globally in effect on domain user accounts as their default behavior. If these settings are configured in another GPO, they will only affect local user accounts on the computers that receive the GPO. However, custom exceptions to the default password policy and account lockout policy rules for specific domain users and/or groups can be defined using Password Settings Objects (PSOs), which are completely separate from Group Policy and most easily configured using Active Directory Administrative Center.

**Rationale:**
The longer a password exists the higher the likelihood that it will be compromised by a brute force attack, by an attacker gaining general knowledge about the user, or by the user sharing the password. Configuring the Maximum password age setting to 0 so that users are never required to change their passwords is a major security risk because that allows a compromised password to be used by the malicious user for as long as the valid user has authorized access.

**Impact:**
If the Maximum password age setting is too low, users are required to change their passwords very often. Such a configuration can reduce security in the organization, because users might write their passwords in an insecure location or lose them. If the value for this policy setting is too high, the level of security within an organization is reduced because it allows potential attackers more time in which to discover user passwords or to use compromised accounts.

**Audit:**
Navigate to the UI Path articulated in the Remediation section and confirm it is set as prescribed.

**Remediation:**
To establish the recommended configuration via GP, set the following UI path to 60 or fewer days, but not 0:

Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Maximum password age

**Default Value:**
42 days.

**References:**
1. https://www.cisecurity.org/white-papers/cis-password-policy-guide/

**Additional Information:**
Microsoft Windows Server 2022 Security Technical Implementation Guide:
Version 2, Release 2, Benchmark Date: November 24, 2024

Vul ID: V-254289
Rule ID: SV-254289r1016476_rule
STIG ID: WN22-AC-000050
Severity: CAT II

**CIS Controls:**

| Controls Version | Control | IG 1 | IG 2 | IG 3 |
|------------------|---------|------|------|------|
| v8 | 5.2 Use Unique Passwords<br>Use unique passwords for all enterprise assets. Best practice implementation includes, at a minimum, an 8-character password for accounts using MFA and a 14-character password for accounts not using MFA. | ● | ● | ● |
| v7 | 16.10 Ensure All Accounts Have An Expiration Date<br>Ensure that all accounts have an expiration date that is monitored and enforced. | | ● | ● |

##### 1.1.4 Ensure 'Minimum password age' is set to '1 or more day(s)' (Automated)

**Profile Applicability:**
- Level 1 - Domain Controller
- Level 1 - Member Server
- STIG Domain Controller
- STIG Member Server

**Description:**
This policy setting determines the number of days that you must use a password before you can change it. The range of values for this policy setting is between 1 and 999 days. (You may also set the value to 0 to allow immediate password changes.) The default value for this setting is 0 days.

The recommended state for this setting is: 1 or more day(s).

**Note:** Password Policy settings (section 1.1) and Account Lockout Policy settings (section 1.2) must be applied via the Default Domain Policy GPO in order to be globally in effect on domain user accounts as their default behavior. If these settings are configured in another GPO, they will only affect local user accounts on the computers that receive the GPO. However, custom exceptions to the default password policy and account lockout policy rules for specific domain users and/or groups can be defined using Password Settings Objects (PSOs), which are completely separate from Group Policy and most easily configured using Active Directory Administrative Center.

**Rationale:**
Users may have favorite passwords that they like to use because they are easy to remember and they believe that their password choice is secure from compromise. Unfortunately, passwords are compromised and if an attacker is targeting a specific individual user account, with foreknowledge of data about that user, reuse of old passwords can cause a security breach. To address password reuse a combination of security settings is required. Using this policy setting with the Enforce password history setting prevents the easy reuse of old passwords. For example, if you configure the Enforce password history setting to ensure that users cannot reuse any of their last 12 passwords, they could change their password 13 times in a few minutes and reuse the password they started with, unless you also configure the Minimum password age setting to a number that is greater than 0. You must configure this policy setting to a number that is greater than 0 for the Enforce password history setting to be effective.

**Impact:**
If an administrator sets a password for a user but wants that user to change the password when the user first logs on, the administrator must select the User must change password at next logon check box, or the user will not be able to change the password until the next day.

**Audit:**
Navigate to the UI Path articulated in the Remediation section and confirm it is set as prescribed.

**Remediation:**
To establish the recommended configuration via GP, set the following UI path to 1 or more day(s):

Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Minimum password age

**Default Value:**
1 day on domain members. 0 days on stand-alone servers.

**References:**
1. https://www.cisecurity.org/white-papers/cis-password-policy-guide/

**Additional Information:**
Microsoft Windows Server 2022 Security Technical Implementation Guide:
Version 2, Release 2, Benchmark Date: November 24, 2024

Vul ID: V-254290
Rule ID: SV-254290r1016477_rule
STIG ID: WN22-AC-000060
Severity: CAT II

**CIS Controls:**

| Controls Version | Control | IG 1 | IG 2 | IG 3 |
|------------------|---------|------|------|------|
| v8 | 5.2 Use Unique Passwords<br>Use unique passwords for all enterprise assets. Best practice implementation includes, at a minimum, an 8-character password for accounts using MFA and a 14-character password for accounts not using MFA. | ● | ● | ● |
| v7 | 16.10 Ensure All Accounts Have An Expiration Date<br>Ensure that all accounts have an expiration date that is monitored and enforced. | | ● | ● |

##### 1.1.5 Ensure 'Minimum password length' is set to '14 or more character(s)' (Automated)

**Profile Applicability:**
- Level 1 - Domain Controller
- Level 1 - Member Server
- STIG Domain Controller
- STIG Member Server

**Description:**
This policy setting determines the least number of characters that make up a password for a user account. There are many different theories about how to determine the best password length for an organization, but perhaps "passphrase" is a better term than "password." In Microsoft Windows 2000 or newer, passphrases can be quite long and can include spaces. Therefore, a phrase such as "I want to drink a $5 milkshake" is a valid passphrase; it is a considerably stronger password than an 8 or 10 character string of random numbers and letters, and yet is easier to remember. Users must be educated about the proper selection and maintenance of passwords, especially around password length. In enterprise environments, the ideal value for the Minimum password length setting is 14 characters, however you should adjust this value to meet your organization's business requirements.

The recommended state for this setting is: 14 or more character(s).

**Note:** In Windows Server 2016 and older versions of Windows Server, the GUI of the Local Security Policy (LSP), Local Group Policy Editor (LGPE) and Group Policy Management Editor (GPME) would not let you set this value higher than 14 characters. However, starting with Windows Server 2019, Microsoft changed the GUI to allow up to a 20 character minimum password length.

**Note #2:** Password Policy settings (section 1.1) and Account Lockout Policy settings (section 1.2) must be applied via the Default Domain Policy GPO in order to be globally in effect on domain user accounts as their default behavior. If these settings are configured in another GPO, they will only affect local user accounts on the computers that receive the GPO. However, custom exceptions to the default password policy and account lockout policy rules for specific domain users and/or groups can be defined using Password Settings Objects (PSOs), which are completely separate from Group Policy and most easily configured using Active Directory Administrative Center.

**Rationale:**
Types of password attacks include dictionary attacks (which attempt to use common words and phrases) and brute force attacks (which try every possible combination of characters). Also, attackers sometimes try to obtain the account database so they can use tools to discover the accounts and passwords.

**Impact:**
Requirements for extremely long passwords can actually decrease the security of an organization, because users might leave the information in an insecure location or lose it. If very long passwords are required, mistyped passwords could cause account lockouts and increase the volume of help desk calls. If your organization has issues with forgotten passwords due to password length requirements, consider teaching your users about passphrases, which are often easier to remember and, due to the larger number of character combinations, much harder to discover.

**Note:** Older versions of Windows such as Windows 98 and Windows NT 4.0 do not support passwords that are longer than 14 characters. Computers that run these older operating systems are unable to authenticate with computers or domains that use accounts that require long passwords.

**Audit:**
Navigate to the UI Path articulated in the Remediation section and confirm it is set as prescribed.

**Remediation:**
To establish the recommended configuration via GP, set the following UI path to 14 or more character(s):

Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Minimum password length

**Default Value:**
7 characters on domain members. 0 characters on stand-alone servers.

**References:**
1. https://www.cisecurity.org/white-papers/cis-password-policy-guide/

**Additional Information:**
Microsoft Windows Server 2022 Security Technical Implementation Guide:
Version 2, Release 2, Benchmark Date: November 24, 2024

Vul ID: V-254291
Rule ID: SV-254291r1016478_rule
STIG ID: WN22-AC-000070
Severity: CAT II

**CIS Controls:**

| Controls Version | Control | IG 1 | IG 2 | IG 3 |
|------------------|---------|------|------|------|
| v8 | 5.2 Use Unique Passwords<br>Use unique passwords for all enterprise assets. Best practice implementation includes, at a minimum, an 8-character password for accounts using MFA and a 14-character password for accounts not using MFA. | ● | ● | ● |
| v7 | 4.4 Use Unique Passwords<br>Where multi-factor authentication is not supported (such as local administrator, root, or service accounts), accounts will use passwords that are unique to that system. | | ● | ● |

##### 1.1.6 Ensure 'Password must meet complexity requirements' is set to 'Enabled' (Automated)

**Profile Applicability:**
- Level 1 - Domain Controller
- Level 1 - Member Server
- STIG Domain Controller
- STIG Member Server

**Description:**
This policy setting checks all new passwords to ensure that they meet basic requirements for strong passwords.

When this policy is enabled, passwords must meet the following minimum requirements:
- Not contain the user's account name or parts of the user's full name that exceed two consecutive characters
- Be at least six characters in length
- Contain characters from three of the following categories:
  - English uppercase characters (A through Z)
  - English lowercase characters (a through z)
  - Base 10 digits (0 through 9)
  - Non-alphabetic characters (for example, !, $, #, %)
  - A catch-all category of any Unicode character that does not fall under the previous four categories. This fifth category can be regionally specific.

Each additional character in a password increases its complexity exponentially. For instance, a seven-character, all lower-case alphabetic password would have 26 to the power of 7 (approximately 8 x 10 to the power of 9 or 8 billion) possible combinations. At 1,000,000 attempts per second (a capability of many password-cracking utilities), it would only take 133 minutes to crack. A seven-character alphabetic password with case sensitivity has 52 to the power of 7 combinations. A seven-character case-sensitive alphanumeric password without punctuation has 62 to the power of 7 combinations. An eight-character password has 26 to the power of 8 (or 2 x 10^11) possible combinations. Although this might seem to be a large number, at 1,000,000 attempts per second it would take only 59 hours to try all possible passwords. Remember, these times will significantly increase for passwords that use ALT characters and other special keyboard characters such as "!" or "@". Proper use of the password settings can help make it difficult to mount a brute force attack.

The recommended state for this setting is: Enabled.

**Note:** Password Policy settings (section 1.1) and Account Lockout Policy settings (section 1.2) must be applied via the Default Domain Policy GPO in order to be globally in effect on domain user accounts as their default behavior. If these settings are configured in another GPO, they will only affect local user accounts on the computers that receive the GPO. However, custom exceptions to the default password policy and account lockout policy rules for specific domain users and/or groups can be defined using Password Settings Objects (PSOs), which are completely separate from Group Policy and most easily configured using Active Directory Administrative Center.

**Rationale:**
Passwords that contain only alphanumeric characters are extremely easy to discover with several publicly available tools.

**Impact:**
If the default password complexity configuration is retained, additional help desk calls for locked-out accounts could occur because users might not be accustomed to passwords that contain non-alphabetic characters. However, all users should be able to comply with the complexity requirement with minimal difficulty.

If your organization has more stringent security requirements, you can create a custom version of the Passfilt.dll file that allows the use of arbitrarily complex password strength rules. For example, a custom password filter might require the use of non-upper row characters. (Upper row characters are those that require you to hold down the SHIFT key and press any of the digits between 1 and 0.) A custom password filter might also perform a dictionary check to verify that the proposed password does not contain common dictionary words or fragments.

Also, the use of ALT key character combinations can greatly enhance the complexity of a password. However, such stringent password requirements can result in unhappy users and an extremely busy help desk. Alternatively, your organization could consider a requirement for all administrator passwords to use ALT characters in the 0128 - 0159 range. (ALT characters outside of this range can represent standard alphanumeric characters that would not add additional complexity to the password.)

**Audit:**
Navigate to the UI Path articulated in the Remediation section and confirm it is set as prescribed.

**Remediation:**
To establish the recommended configuration via GP, set the following UI path to Enabled:

Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Password must meet complexity requirements

**Default Value:**
Enabled on domain members. Disabled on stand-alone servers.

**References:**
1. https://www.cisecurity.org/white-papers/cis-password-policy-guide/

**Additional Information:**
Microsoft Windows Server 2022 Security Technical Implementation Guide:
Version 2, Release 2, Benchmark Date: November 24, 2024

Vul ID: V-254292
Rule ID: 254292r1016479_rule
STIG ID: WN22-AC-000080
Severity: CAT II

**CIS Controls:**

| Controls Version | Control | IG 1 | IG 2 | IG 3 |
|------------------|---------|------|------|------|
| v8 | 5.2 Use Unique Passwords<br>Use unique passwords for all enterprise assets. Best practice implementation includes, at a minimum, an 8-character password for accounts using MFA and a 14-character password for accounts not using MFA. | ● | ● | ● |
| v7 | 4.4 Use Unique Passwords<br>Where multi-factor authentication is not supported (such as local administrator, root, or service accounts), accounts will use passwords that are unique to that system. | | ● | ● |

##### 1.1.7 Ensure 'Relax minimum password length limits' is set to 'Enabled' (Automated)

**Profile Applicability:**
- Level 1 - Member Server

**Description:**
This policy setting determines whether the minimum password length setting can be increased beyond the legacy limit of 14 characters. For more information please see the following Microsoft Security Blog.

The recommended state for this setting is: Enabled.

**Note:** This setting only affects local accounts on the computer. Domain accounts are only affected by settings on the Domain Controllers, because that is where domain accounts are stored.

**Rationale:**
This setting will enable the enforcement of longer and generally stronger passwords or passphrases where MFA is not in use.

**Impact:**
The Minimum password length setting may be configured higher than 14 characters.

If very long passwords are required, mistyped passwords could cause account lockouts and increase the volume of help desk calls. If your organization has issues with forgotten passwords due to password length requirements, consider teaching your users about passphrases, which are often easier to remember and, due to the larger number of character combinations, much harder to discover.

**Audit:**
Navigate to the UI Path articulated in the Remediation section and confirm it is set as prescribed. This group policy setting is backed by the following registry location with a REG_DWORD value of 1.

HKLM\System\CurrentControlSet\Control\SAM:RelaxMinimumPasswordLengthLimits

**Remediation:**
To establish the recommended configuration via GP, set the following UI path to Enabled:

Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Relax minimum password length limits

**Note:** This setting is only available within the built-in OS security template of Windows 10 Release 2004 and Server 2022 (or newer), and is not available via older versions of the OS, or via downloadable Administrative Templates (ADMX/ADML). Therefore, you must use a Windows 10 Release 2004 or Server 2022 system (or newer) to view or edit this setting with the Group Policy Management Console (GPMC) or Group Policy Management Editor (GPME).

**Default Value:**
Disabled. (The Minimum password length may be configured to a maximum of 14 characters.)

**References:**
1. https://www.cisecurity.org/white-papers/cis-password-policy-guide/
2. https://support.microsoft.com/en-us/topic/minimum-password-length-auditing-and-enforcement-on-certain-versions-of-windows-5ef7fecf-3325-f56b-cc10-4fd565aacc59

**CIS Controls:**

| Controls Version | Control | IG 1 | IG 2 | IG 3 |
|------------------|---------|------|------|------|
| v8 | 5.2 Use Unique Passwords<br>Use unique passwords for all enterprise assets. Best practice implementation includes, at a minimum, an 8-character password for accounts using MFA and a 14-character password for accounts not using MFA. | ● | ● | ● |
| v7 | 4.4 Use Unique Passwords<br>Where multi-factor authentication is not supported (such as local administrator, root, or service accounts), accounts will use passwords that are unique to that system. | | ● | ● |

##### 1.1.8 Ensure 'Store passwords using reversible encryption' is set to 'Disabled' (Automated)

**Profile Applicability:**
- Level 1 - Domain Controller
- Level 1 - Member Server
- STIG Domain Controller
- STIG Member Server

**Description:**
This policy setting determines whether the operating system stores passwords in a way that uses reversible encryption, which provides support for application protocols that require knowledge of the user's password for authentication purposes. Passwords that are stored with reversible encryption are essentially the same as plaintext versions of the passwords.

The recommended state for this setting is: Disabled.

**Note:** Password Policy settings (section 1.1) and Account Lockout Policy settings (section 1.2) must be applied via the Default Domain Policy GPO in order to be globally in effect on domain user accounts as their default behavior. If these settings are configured in another GPO, they will only affect local user accounts on the computers that receive the GPO. However, custom exceptions to the default password policy and account lockout policy rules for specific domain users and/or groups can be defined using Password Settings Objects (PSOs), which are completely separate from Group Policy and most easily configured using Active Directory Administrative Center.

**Rationale:**
Enabling this policy setting allows the operating system to store passwords in a weaker format that is much more susceptible to compromise and weakens your system security.

**Impact:**
If your organization uses either the CHAP authentication protocol through remote access or IAS services or Digest Authentication in IIS, you must configure this policy setting to Enabled. This setting is extremely dangerous to apply through Group Policy on a user-by-user basis, because it requires the appropriate user account object to be opened in Active Directory Users and Computers.

**Audit:**
Navigate to the UI Path articulated in the Remediation section and confirm it is set as prescribed.

**Remediation:**
To establish the recommended configuration via GP, set the following UI path to Disabled:

Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Store passwords using reversible encryption

**Default Value:**
Disabled.

**References:**
1. https://www.cisecurity.org/white-papers/cis-password-policy-guide/

**Additional Information:**
Microsoft Windows Server 2022 Security Technical Implementation Guide:
Version 2, Release 2, Benchmark Date: November 24, 2024

Vul ID: V-254293
Rule ID: SV-254293r1016480_rule
STIG ID: WN22-AC-000090
Severity: CAT I

**CIS Controls:**

| Controls Version | Control | IG 1 | IG 2 | IG 3 |
|------------------|---------|------|------|------|
| v8 | 3.11 Encrypt Sensitive Data at Rest<br>Encrypt sensitive data at rest on servers, applications, and databases containing sensitive data. Storage-layer encryption, also known as server-side encryption, meets the minimum requirement of this Safeguard. Additional encryption methods may include application-layer encryption, also known as client-side encryption, where access to the data storage device(s) does not permit access to the plain-text data. | | ● | ● |
| v7 | 16.4 Encrypt or Hash all Authentication Credentials<br>Encrypt or hash with a salt all authentication credentials when stored. | | ● | ● |