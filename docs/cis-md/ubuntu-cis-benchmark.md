# CIS Ubuntu Linux 24.04 LTS Benchmark

## Overview

All CIS Benchmarks™ focus on technical configuration settings used to maintain and/or increase the security of the addressed technology, and they should be used in conjunction with other essential cyber hygiene tasks like:
- Monitoring the base operating system and applications for vulnerabilities and quickly updating with the latest security patches.
- End-point protection (Antivirus software, Endpoint Detection and Response (EDR), etc.).
- Logging and monitoring user and system activity.

In the end, the CIS Benchmarks™ are designed to be a key component of a comprehensive cybersecurity program.

## Important Usage Information

All CIS Benchmarks™ are available free for non-commercial use from the [CIS Website](https://www.cisecurity.org/). They can be used to manually assess and remediate systems and applications. In lieu of manual assessment and remediation, there are several tools available to assist with assessment:
- CIS Configuration Assessment Tool (CIS-CAT® Pro Assessor)
- CIS Benchmarks™ Certified 3rd Party Tooling

These tools make the hardening process much more scalable for large numbers of systems and applications.

> **NOTE**: Some tooling focuses only on the CIS Benchmarks™ Recommendations that can be fully automated (skipping ones marked Manual). It is important that ALL Recommendations (Automated and Manual) be addressed, since all are important for properly securing systems and are typically in scope for audits.

In addition, CIS has developed CIS [Build Kits](https://www.cisecurity.org/cis-securesuite/cis-securesuite-membership-benefits/cis-securesuite-build-kits) for some common technologies to assist in applying CIS Benchmarks™ Recommendations.

> **When remediating systems (changing configuration settings on deployed systems as per the CIS Benchmarks™ Recommendations), please approach this with caution and test thoroughly.**

The following is a reasonable remediation approach to follow:

1. NEVER deploy a CIS Build Kit, or any internally developed remediation method, to production systems without proper testing.
2. Proper testing consists of the following:
   a. Understand the configuration (including installed applications) of the targeted systems.
   b. Read the Impact section of the given Recommendation to help determine if there might be an issue with the targeted systems.
   c. Test the configuration changes on representative lab system(s). This way if there is some issue it can be resolved prior to deploying to any production systems.
   d. When confident, initially deploy to a small sub-set of users and monitor closely for issues. This way if there is some issue it can be resolved prior to deploying more broadly.
   e. When confident, iteratively deploy to additional groups and monitor closely for issues until deployment is complete. This way if there is some issue it can be resolved prior to continuing deployment.

> **NOTE**: CIS and the CIS Benchmarks™ development communities in CIS WorkBench do their best to test and have high confidence in the Recommendations, but they cannot test potential conflicts with all possible system deployments. Known potential issues identified during CIS Benchmarks™ development are documented in the Impact section of each Recommendation.

By using CIS and/or CIS Benchmarks™ Certified tools, and being careful with remediation deployment, it is possible to harden large numbers of deployed systems in a cost effective, efficient, and safe manner.

> **NOTE**: As previously stated, the PDF versions of the CIS Benchmarks™ are available for free, non-commercial use on the [CIS Website](https://www.cisecurity.org/). All other formats of the CIS Benchmarks™ (MS Word, Excel, and [Build Kits](https://www.cisecurity.org/cis-securesuite/cis-securesuite-membership-benefits/cis-securesuite-build-kits)) are available for CIS [SecureSuite®](https://www.cisecurity.org/cis-securesuite/) members.
> 
> CIS-CAT® Pro is also available to CIS [SecureSuite®](https://www.cisecurity.org/cis-securesuite/) members.

## Target Technology Details

This document provides prescriptive guidance for establishing a secure configuration posture for Ubuntu Linux 24.04 LTS systems running on x86_64 platforms.

This guide was developed and tested against Ubuntu Linux 24.04 LTS.

The guidance within broadly assumes that operations are being performed as the <span style="color:red">root</span> user and executed under the default Bash version for the applicable distribution. Operations performed using <span style="color:red">sudo</span> instead of the <span style="color:red">root</span> user, or executed under another shell, may produce unexpected results, or fail to make the intended changes to the system. Non-root users may not be able to access certain areas of the system, especially after remediation has been performed. It is advisable to verify <span style="color:red">root</span> users path integrity and the integrity of any programs being run prior to execution of commands and scripts included in this benchmark.

The default prompt for the <span style="color:red">root</span> user is <span style="color:red">#</span>, and as such all sample commands will have <span style="color:red">#</span> as an additional indication that it is to be executed as <span style="color:red">root</span>.

To obtain the latest version of this guide, please visit [http://workbench.cisecurity.org](http://workbench.cisecurity.org). If you have questions, comments, or have identified ways to improve this guide, please write us at [feedback@cisecurity.org](mailto:feedback@cisecurity.org).

## Intended Audience

This benchmark is intended for system and application administrators, security specialists, auditors, help desk, and platform deployment personnel who plan to develop, deploy, assess, or secure solutions that incorporate Ubuntu Linux 24.04 LTS on x86_64 platforms.

## Consensus Guidance

This CIS Benchmark™ was created using a consensus review process comprised of a global community of subject matter experts. The process combines real world experience with data-based information to create technology specific guidance to assist users to secure their environments. Consensus participants provide perspective from a diverse set of backgrounds including consulting, software development, audit and compliance, security research, operations, government, and legal.

Each CIS Benchmark undergoes two phases of consensus review. The first phase occurs during initial Benchmark development. During this phase, subject matter experts convene to discuss, create, and test working drafts of the Benchmark. This discussion occurs until consensus has been reached on Benchmark recommendations. The second phase begins after the Benchmark has been published. During this phase, all feedback provided by the Internet community is reviewed by the consensus team for incorporation in the Benchmark. If you are interested in participating in the consensus process, please visit [https://workbench.cisecurity.org/](https://workbench.cisecurity.org/).

## Typographical Conventions

The following typographical conventions are used throughout this guide:

| Convention | Meaning |
|------------|---------|
| Stylized Monospace font | Used for blocks of code, command, and script examples. Text should be interpreted exactly as presented. |
| Monospace font | Used for inline code, commands, UI/Menu selections or examples. Text should be interpreted exactly as presented. |
| \<Monospace font in brackets\> | Text set in angle brackets denote a variable requiring substitution for a real value. |
| *Italic font* | Used to reference other relevant settings, CIS Benchmarks and/or Benchmark Communities. Also, used to denote the title of a book, article, or other publication. |
| **Bold font** | Additional information or caveats things like Notes, Warnings, or Cautions (usually just the word itself and the rest of the text normal). |

## Recommendation Definitions

The following defines the various components included in a CIS recommendation as applicable. If any of the components are not applicable it will be noted or the component will not be included in the recommendation.

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

- **Level 1 - Server**  
  Items in this profile intend to:
  - be practical and prudent.
  - provide a clear security benefit; and
  - not inhibit the utility of the technology beyond acceptable means.  
  This profile is intended for servers.

- **Level 2 - Server**  
  This profile extends the "Level 1 - Server" profile. Items in this profile exhibit one or more of the following characteristics:
  - are intended for environments or use cases where security is paramount.
  - acts as defense in depth measure.
  - may negatively inhibit the utility or performance of the technology.  
  This profile is intended for servers.

- **Level 1 - Workstation**  
  Items in this profile intend to:
  - be practical and prudent.
  - provide a clear security benefit; and
  - not inhibit the utility of the technology beyond acceptable means.  
  This profile is intended for workstations.

- **Level 2 - Workstation**  
  This profile extends the "Level 1 - Workstation" profile. Items in this profile exhibit one or more of the following characteristics:
  - are intended for environments or use cases where security is paramount.
  - acts as defense in depth measure.
  - may negatively inhibit the utility or performance of the technology.  
  This profile is intended for workstations.

## Acknowledgements

This Benchmark exemplifies the great things a community of users, vendors, and subject matter experts can accomplish through consensus collaboration. The CIS community thanks the entire consensus team with special recognition to the following individuals who contributed greatly to the creation of this guide:

This benchmark is based upon previous Linux benchmarks published and would not be possible without the contributions provided over the history of all of these benchmarks. The CIS community thanks everyone who has contributed to the Linux benchmarks.

**Contributor**  
Ron Colvin, Ron Colvin  
Dave Billing  
Dominic Pace  
Koen Laevens  
Mark Birch  
Thomas Sjögren  
James Trigg  
Matthew Burket, IBM  
Marcus Burghardt  
Graham Eames  
Robert McSulla  
Chad Streck  
Ryan Jaynes CISSP  
Cory Sherman  
Simon John  
Steve Cobrin  

**Editor**  
Jonathan Lewis Christopherson  
Eric Pinnell  
Justin Brown  
Gokhan Lus  
Randie Bejar  

## Recommendations

### 1 Initial Setup

Items in this section are advised for all systems but may be difficult or require extensive preparation after the initial setup of the system.

#### 1.1 Filesystem

The file system is generally a built-in layer used to handle the data management of the storage.

##### 1.1.1 Configure Filesystem Kernel Modules

Several uncommon filesystem types are supported under Linux. Removing support for unneeded filesystem types reduces the local attack surface of the system. If a filesystem type is not needed it should be disabled. Native Linux file systems are designed to ensure that built-in security controls function as expected. Non-native filesystems can lead to unexpected consequences to both the security and functionality of the system and should be used with caution. Many filesystems are created for niche use cases and are not maintained and supported as the operating systems are updated and patched. Users of non-native filesystems should ensure that there is attention and ongoing support for them, especially in light of frequent operating system changes.

Standard network connectivity and Internet access to cloud storage may make the use of non-standard filesystem formats to directly attach heterogeneous devices much less attractive.

**Note**: This should not be considered a comprehensive list of filesystems. You may wish to consider additions to those listed here for your environment. For the current available file system modules on the system see `/usr/lib/modules/$(uname -r)/kernel/fs`

**Start up scripts**

Kernel modules loaded directly via insmod will ignore what is configured in the relevant `/etc/modprobe.d/*.conf` files. If modules are still being loaded after a reboot whilst having the correctly configured blacklist and install command, check for insmod entries in start up scripts such as `.bashrc`.

You may also want to check `/lib/modprobe.d/`. Please note that this directory should not be used for user defined module loading. Ensure that all such entries resides in `/etc/modprobe.d/*.conf` files.

**Return values**

Using `/bin/false` as the command in disabling a particular module serves two purposes; to convey the meaning of the entry to the user and cause a non-zero return value. The latter can be tested for in scripts. Please note that insmod will ignore what is configured in the relevant `/etc/modprobe.d/*.conf` files. The preferred way to load modules is with modprobe.

###### 1.1.1.1 Ensure cramfs kernel module is not available (Automated)

**Profile Applicability:**
- Level 1 - Server
- Level 1 - Workstation

**Description:**  
The cramfs filesystem type is a compressed read-only Linux filesystem embedded in small footprint systems. A cramfs image can be used without having to first decompress the image.

**Rationale:**  
Removing support for unneeded filesystem types reduces the local attack surface of the system. If this filesystem type is not needed, disable it.

**Audit:**  
Run the following script to verify:
- IF - the cramfs kernel module is available in ANY installed kernel, verify:
  - An entry including `/bin/true` or `/bin/false` exists in a file within the `/etc/modprobe.d/` directory
  - The module is deny listed in a file within the `/etc/modprobe.d/` directory
  - The module is not loaded in the running kernel
- IF - the cramfs kernel module is not available on the system, or pre-compiled into the kernel, no additional configuration is necessary

```bash
#!/usr/bin/env bash
{
 a_output=() a_output2=() a_output3=() l_dl="" l_mod_name="cramfs" 
l_mod_type="fs"
 l_mod_path="$(readlink -f /lib/modules/**/kernel/$l_mod_type | sort -u)"
 f_module_chk()
 {
 l_dl="y" a_showconfig=()
 while IFS= read -r l_showconfig; do
 a_showconfig+=("$l_showconfig")
 done < <(modprobe --showconfig | grep -P --
'\b(install|blacklist)\h+'"${l_mod_chk_name//-/_}"'\b')
 if ! lsmod | grep "$l_mod_chk_name" &> /dev/null; then
 a_output+=(" - kernel module: \"$l_mod_name\" is not loaded")
 else
 a_output2+=(" - kernel module: \"$l_mod_name\" is loaded")
 fi
 if grep -Pq -- '\binstall\h+'"${l_mod_chk_name//-
/_}"'\h+(\/usr)?\/bin\/(true|false)\b' <<< "${a_showconfig[*]}"; then
 a_output+=(" - kernel module: \"$l_mod_name\" is not loadable")
 else
 a_output2+=(" - kernel module: \"$l_mod_name\" is loadable")
 fi
 if grep -Pq -- '\bblacklist\h+'"${l_mod_chk_name//-/_}"'\b' <<< 
"${a_showconfig[*]}"; then
 a_output+=(" - kernel module: \"$l_mod_name\" is deny listed")
 else
 a_output2+=(" - kernel module: \"$l_mod_name\" is not deny listed")
 fi
 }
 for l_mod_base_directory in $l_mod_path; do
 if [ -d "$l_mod_base_directory/${l_mod_name/-/\/}" ] && [ -n "$(ls -A 
"$l_mod_base_directory/${l_mod_name/-/\/}")" ]; then
 a_output3+=(" - \"$l_mod_base_directory\"")
 l_mod_chk_name="$l_mod_name"
 [[ "$l_mod_name" =~ overlay ]] && l_mod_chk_name="${l_mod_name::-2}" 
 [ "$l_dl" != "y" ] && f_module_chk
 else
 a_output+=(" - kernel module: \"$l_mod_name\" doesn't exist in 
\"$l_mod_base_directory\"")
 fi
 done
 [ "${#a_output3[@]}" -gt 0 ] && printf '%s\n' "" " -- INFO --" " - module: 
\"$l_mod_name\" exists in:" "${a_output3[@]}"
 if [ "${#a_output2[@]}" -le 0 ]; then
 printf '%s\n' "" "- Audit Result:" " ** PASS **" "${a_output[@]}"
 else
 printf '%s\n' "" "- Audit Result:" " ** FAIL **" " - Reason(s) for 
audit failure:" "${a_output2[@]}"
 [ "${#a_output[@]}" -gt 0 ] && printf '%s\n' "- Correctly set:" 
"${a_output[@]}"
 fi
}
```

**Remediation:**  
Run the following script to unload and disable the cramfs module:
- IF - the cramfs kernel module is available in ANY installed kernel:
  - Create a file ending in .conf with `install cramfs /bin/false` in the `/etc/modprobe.d/` directory
  - Create a file ending in .conf with `blacklist cramfs` in the `/etc/modprobe.d/` directory
  - Run `modprobe -r cramfs 2>/dev/null; rmmod cramfs 2>/dev/null` to remove cramfs from the kernel
- IF - the cramfs kernel module is not available on the system, or pre-compiled into the kernel, no remediation is necessary

```bash
#!/usr/bin/env bash
{
 a_output2=() a_output3=() l_dl="" l_mod_name="cramfs" l_mod_type="fs"
 l_mod_path="$(readlink -f /lib/modules/**/kernel/$l_mod_type | sort -u)"
 f_module_fix()
 {
 l_dl="y" a_showconfig=()
 while IFS= read -r l_showconfig; do
 a_showconfig+=("$l_showconfig")
 done < <(modprobe --showconfig | grep -P --
'\b(install|blacklist)\h+'"${l_mod_chk_name//-/_}"'\b')
 if lsmod | grep "$l_mod_chk_name" &> /dev/null; then
 a_output2+=(" - unloading kernel module: \"$l_mod_name\"")
 modprobe -r "$l_mod_chk_name" 2>/dev/null; rmmod "$l_mod_name" 
2>/dev/null
 fi
 if ! grep -Pq -- '\binstall\h+'"${l_mod_chk_name//-
/_}"'\h+(\/usr)?\/bin\/(true|false)\b' <<< "${a_showconfig[*]}"; then
 a_output2+=(" - setting kernel module: \"$l_mod_name\" to 
\"$(readlink -f /bin/false)\"")
 printf '%s\n' "install $l_mod_chk_name $(readlink -f /bin/false)" >> 
/etc/modprobe.d/"$l_mod_name".conf
 fi
 if ! grep -Pq -- '\bblacklist\h+'"${l_mod_chk_name//-/_}"'\b' <<< 
"${a_showconfig[*]}"; then
 a_output2+=(" - denylisting kernel module: \"$l_mod_name\"")
 printf '%s\n' "blacklist $l_mod_chk_name" >> 
/etc/modprobe.d/"$l_mod_name".conf
 fi
 }
 for l_mod_base_directory in $l_mod_path; do # Check if the module exists 
on the system
 if [ -d "$l_mod_base_directory/${l_mod_name/-/\/}" ] && [ -n "$(ls -A 
"$l_mod_base_directory/${l_mod_name/-/\/}")" ]; then
 a_output3+=(" - \"$l_mod_base_directory\"")
 l_mod_chk_name="$l_mod_name"
 [[ "$l_mod_name" =~ overlay ]] && l_mod_chk_name="${l_mod_name::-2}" 
 [ "$l_dl" != "y" ] && f_module_fix
 else
 printf '%s\n' " - kernel module: \"$l_mod_name\" doesn't exist in 
\"$l_mod_base_directory\""
 fi
 done
 [ "${#a_output3[@]}" -gt 0 ] && printf '%s\n' "" " -- INFO --" " - module: 
\"$l_mod_name\" exists in:" "${a_output3[@]}"
 [ "${#a_output2[@]}" -gt 0 ] && printf '%s\n' "" "${a_output2[@]}" || 
printf '%s\n' "" " - No changes needed"
 printf '%s\n' "" " - remediation of kernel module: \"$l_mod_name\" 
complete" ""
}
```

**References:**
1. NIST SP 800-53 Rev. 5: CM-7

**CIS Controls:**

| Controls Version | Control | IG 1 | IG 2 | IG 3 |
|------------------|---------|------|------|------|
| v8 | 4.8 Uninstall or Disable Unnecessary Services on Enterprise Assets and Software<br>Uninstall or disable unnecessary services on enterprise assets and software, such as an unused file sharing service, web application module, or service function. | | ● | ● |
| v7 | 9.2 Ensure Only Approved Ports, Protocols and Services Are Running<br>Ensure that only network ports, protocols, and services listening on a system with validated business needs, are running on each system. | | ● | ● |

**MITRE ATT&CK Mappings:**

| Techniques / Subtechniques | Tactics | Mitigations |
|----------------------------|---------|-------------|
| T1005, T1005.000 | TA0005 | M1050 |

###### 1.1.1.3 Ensure hfs kernel module is not available (Automated)

**Profile Applicability:**
- Level 1 - Server
- Level 1 - Workstation

**Description:**  
The hfs filesystem type is a hierarchical filesystem that allows you to mount Mac OS filesystems.

**Rationale:**  
Removing support for unneeded filesystem types reduces the local attack surface of the system. If this filesystem type is not needed, disable it.

**Audit:**  
Run the following script to verify:
- IF - the hfs kernel module is available in ANY installed kernel, verify:
  - An entry including `/bin/true` or `/bin/false` exists in a file within the `/etc/modprobe.d/` directory
  - The module is deny listed in a file within the `/etc/modprobe.d/` directory
  - The module is not loaded in the running kernel
- IF - the hfs kernel module is not available on the system, or pre-compiled into the kernel, no additional configuration is necessary

```bash
#!/usr/bin/env bash
{
 a_output=() a_output2=() a_output3=() l_dl="" l_mod_name="hfs" 
l_mod_type="fs"
 l_mod_path="$(readlink -f /lib/modules/**/kernel/$l_mod_type | sort -u)"
 f_module_chk()
 {
 l_dl="y" a_showconfig=()
 while IFS= read -r l_showconfig; do
 a_showconfig+=("$l_showconfig")
 done < <(modprobe --showconfig | grep -P --
'\b(install|blacklist)\h+'"${l_mod_chk_name//-/_}"'\b')
 if ! lsmod | grep "$l_mod_chk_name" &> /dev/null; then
 a_output+=(" - kernel module: \"$l_mod_name\" is not loaded")
 else
 a_output2+=(" - kernel module: \"$l_mod_name\" is loaded")
 fi
 if grep -Pq -- '\binstall\h+'"${l_mod_chk_name//-
/_}"'\h+(\/usr)?\/bin\/(true|false)\b' <<< "${a_showconfig[*]}"; then
 a_output+=(" - kernel module: \"$l_mod_name\" is not loadable")
 else
 a_output2+=(" - kernel module: \"$l_mod_name\" is loadable")
 fi
 if grep -Pq -- '\bblacklist\h+'"${l_mod_chk_name//-/_}"'\b' <<< 
"${a_showconfig[*]}"; then
 a_output+=(" - kernel module: \"$l_mod_name\" is deny listed")
 else
 a_output2+=(" - kernel module: \"$l_mod_name\" is not deny listed")
 fi
 }
 for l_mod_base_directory in $l_mod_path; do
 if [ -d "$l_mod_base_directory/${l_mod_name/-/\/}" ] && [ -n "$(ls -A 
"$l_mod_base_directory/${l_mod_name/-/\/}")" ]; then
 a_output3+=(" - \"$l_mod_base_directory\"")
 l_mod_chk_name="$l_mod_name"
 [[ "$l_mod_name" =~ overlay ]] && l_mod_chk_name="${l_mod_name::-2}" 
 [ "$l_dl" != "y" ] && f_module_chk
 else
 a_output+=(" - kernel module: \"$l_mod_name\" doesn't exist in 
\"$l_mod_base_directory\"")
 fi
 done
 [ "${#a_output3[@]}" -gt 0 ] && printf '%s\n' "" " -- INFO --" " - module: 
\"$l_mod_name\" exists in:" "${a_output3[@]}"
 if [ "${#a_output2[@]}" -le 0 ]; then
 printf '%s\n' "" "- Audit Result:" " ** PASS **" "${a_output[@]}"
 else
 printf '%s\n' "" "- Audit Result:" " ** FAIL **" " - Reason(s) for 
audit failure:" "${a_output2[@]}"
 [ "${#a_output[@]}" -gt 0 ] && printf '%s\n' "- Correctly set:" 
"${a_output[@]}"
 fi
}
```

**Remediation:**  
Run the following script to unload and disable the hfs module:
- IF - the hfs kernel module is available in ANY installed kernel:
  - Create a file ending in .conf with `install hfs /bin/false` in the `/etc/modprobe.d/` directory
  - Create a file ending in .conf with `blacklist hfs` in the `/etc/modprobe.d/` directory
  - Run `modprobe -r hfs 2>/dev/null; rmmod hfs 2>/dev/null` to remove hfs from the kernel
- IF - the hfs kernel module is not available on the system, or pre-compiled into the kernel, no remediation is necessary

```bash
#!/usr/bin/env bash
{
 a_output2=() a_output3=() l_dl="" l_mod_name="hfs" l_mod_type="fs"
 l_mod_path="$(readlink -f /lib/modules/**/kernel/$l_mod_type | sort -u)"
 f_module_fix()
 {
 l_dl="y" a_showconfig=()
 while IFS= read -r l_showconfig; do
 a_showconfig+=("$l_showconfig")
 done < <(modprobe --showconfig | grep -P --
'\b(install|blacklist)\h+'"${l_mod_chk_name//-/_}"'\b')
 if lsmod | grep "$l_mod_chk_name" &> /dev/null; then
 a_output2+=(" - unloading kernel module: \"$l_mod_name\"")
 modprobe -r "$l_mod_chk_name" 2>/dev/null; rmmod "$l_mod_name" 
2>/dev/null
 fi
 if ! grep -Pq -- '\binstall\h+'"${l_mod_chk_name//-
/_}"'\h+(\/usr)?\/bin\/(true|false)\b' <<< "${a_showconfig[*]}"; then
 a_output2+=(" - setting kernel module: \"$l_mod_name\" to 
\"$(readlink -f /bin/false)\"")
 printf '%s\n' "install $l_mod_chk_name $(readlink -f /bin/false)" >> 
/etc/modprobe.d/"$l_mod_name".conf
 fi
 if ! grep -Pq -- '\bblacklist\h+'"${l_mod_chk_name//-/_}"'\b' <<< 
"${a_showconfig[*]}"; then
 a_output2+=(" - denylisting kernel module: \"$l_mod_name\"")
 printf '%s\n' "blacklist $l_mod_chk_name" >> 
/etc/modprobe.d/"$l_mod_name".conf
 fi
 }
 for l_mod_base_directory in $l_mod_path; do # Check if the module exists 
on the system
 if [ -d "$l_mod_base_directory/${l_mod_name/-/\/}" ] && [ -n "$(ls -A 
"$l_mod_base_directory/${l_mod_name/-/\/}")" ]; then
 a_output3+=(" - \"$l_mod_base_directory\"")
 l_mod_chk_name="$l_mod_name"
 [[ "$l_mod_name" =~ overlay ]] && l_mod_chk_name="${l_mod_name::-2}" 
 [ "$l_dl" != "y" ] && f_module_fix
 else
 printf '%s\n' " - kernel module: \"$l_mod_name\" doesn't exist in 
\"$l_mod_base_directory\""
 fi
 done
 [ "${#a_output3[@]}" -gt 0 ] && printf '%s\n' "" " -- INFO --" " - module: 
\"$l_mod_name\" exists in:" "${a_output3[@]}"
 [ "${#a_output2[@]}" -gt 0 ] && printf '%s\n' "" "${a_output2[@]}" || 
printf '%s\n' "" " - No changes needed"
 printf '%s\n' "" " - remediation of kernel module: \"$l_mod_name\" 
complete" ""
}
```

**References:**
1. NIST SP 800-53 Rev. 5: CM-7

**CIS Controls:**

| Controls Version | Control | IG 1 | IG 2 | IG 3 |
|------------------|---------|------|------|------|
| v8 | 4.8 Uninstall or Disable Unnecessary Services on Enterprise Assets and Software<br>Uninstall or disable unnecessary services on enterprise assets and software, such as an unused file sharing service, web application module, or service function. | | ● | ● |
| v7 | 9.2 Ensure Only Approved Ports, Protocols and Services Are Running<br>Ensure that only network ports, protocols, and services listening on a system with validated business needs, are running on each system. | | ● | ● |

**MITRE ATT&CK Mappings:**

| Techniques / Subtechniques | Tactics | Mitigations |
|----------------------------|---------|-------------|
| T1005, T1005.000 | TA0005 | M1050 |

###### 1.1.1.4 Ensure hfsplus kernel module is not available (Automated)

**Profile Applicability:**
- Level 1 - Server
- Level 1 - Workstation

**Description:**  
The hfsplus filesystem type is a hierarchical filesystem designed to replace hfs that allows you to mount Mac OS filesystems.

**Rationale:**  
Removing support for unneeded filesystem types reduces the local attack surface of the system. If this filesystem type is not needed, disable it.

**Audit:**  
Run the following script to verify:
- IF - the hfsplus kernel module is available in ANY installed kernel, verify:
  - An entry including `/bin/true` or `/bin/false` exists in a file within the `/etc/modprobe.d/` directory
  - The module is deny listed in a file within the `/etc/modprobe.d/` directory
  - The module is not loaded in the running kernel
- IF - the hfsplus kernel module is not available on the system, or pre-compiled into the kernel, no additional configuration is necessary

```bash
#!/usr/bin/env bash
{
 a_output=() a_output2=() a_output3=() l_dl="" l_mod_name="hfsplus" 
l_mod_type="fs"
 l_mod_path="$(readlink -f /lib/modules/**/kernel/$l_mod_type | sort -u)"
 f_module_chk()
 {
 l_dl="y" a_showconfig=()
 while IFS= read -r l_showconfig; do
 a_showconfig+=("$l_showconfig")
 done < <(modprobe --showconfig | grep -P --
'\b(install|blacklist)\h+'"${l_mod_chk_name//-/_}"'\b')
 if ! lsmod | grep "$l_mod_chk_name" &> /dev/null; then
 a_output+=(" - kernel module: \"$l_mod_name\" is not loaded")
 else
 a_output2+=(" - kernel module: \"$l_mod_name\" is loaded")
 fi
 if grep -Pq -- '\binstall\h+'"${l_mod_chk_name//-
/_}"'\h+(\/usr)?\/bin\/(true|false)\b' <<< "${a_showconfig[*]}"; then
 a_output+=(" - kernel module: \"$l_mod_name\" is not loadable")
 else
 a_output2+=(" - kernel module: \"$l_mod_name\" is loadable")
 fi
 if grep -Pq -- '\bblacklist\h+'"${l_mod_chk_name//-/_}"'\b' <<< 
"${a_showconfig[*]}"; then
 a_output+=(" - kernel module: \"$l_mod_name\" is deny listed")
 else
 a_output2+=(" - kernel module: \"$l_mod_name\" is not deny listed")
 fi
 }
 for l_mod_base_directory in $l_mod_path; do
 if [ -d "$l_mod_base_directory/${l_mod_name/-/\/}" ] && [ -n "$(ls -A 
"$l_mod_base_directory/${l_mod_name/-/\/}")" ]; then
 a_output3+=(" - \"$l_mod_base_directory\"")
 l_mod_chk_name="$l_mod_name"
 [[ "$l_mod_name" =~ overlay ]] && l_mod_chk_name="${l_mod_name::-2}" 
 [ "$l_dl" != "y" ] && f_module_chk
 else
 a_output+=(" - kernel module: \"$l_mod_name\" doesn't exist in 
\"$l_mod_base_directory\"")
 fi
 done
 [ "${#a_output3[@]}" -gt 0 ] && printf '%s\n' "" " -- INFO --" " - module: 
\"$l_mod_name\" exists in:" "${a_output3[@]}"
 if [ "${#a_output2[@]}" -le 0 ]; then
 printf '%s\n' "" "- Audit Result:" " ** PASS **" "${a_output[@]}"
 else
 printf '%s\n' "" "- Audit Result:" " ** FAIL **" " - Reason(s) for 
audit failure:" "${a_output2[@]}"
 [ "${#a_output[@]}" -gt 0 ] && printf '%s\n' "- Correctly set:" 
"${a_output[@]}"
 fi
}
```

**Remediation:**  
Run the following script to unload and disable the hfsplus module:
- IF - the hfsplus kernel module is available in ANY installed kernel:
  - Create a file ending in .conf with `install hfsplus /bin/false` in the `/etc/modprobe.d/` directory
  - Create a file ending in .conf with `blacklist hfsplus` in the `/etc/modprobe.d/` directory
  - Run `modprobe -r hfsplus 2>/dev/null; rmmod hfsplus 2>/dev/null` to remove hfsplus from the kernel
- IF - the hfsplus kernel module is not available on the system, or pre-compiled into the kernel, no remediation is necessary

```bash
#!/usr/bin/env bash
{
 a_output2=() a_output3=() l_dl="" l_mod_name="hfsplus" l_mod_type="fs"
 l_mod_path="$(readlink -f /lib/modules/**/kernel/$l_mod_type | sort -u)"
 f_module_fix()
 {
 l_dl="y" a_showconfig=()
 while IFS= read -r l_showconfig; do
 a_showconfig+=("$l_showconfig")
 done < <(modprobe --showconfig | grep -P --
'\b(install|blacklist)\h+'"${l_mod_chk_name//-/_}"'\b')
 if lsmod | grep "$l_mod_chk_name" &> /dev/null; then
 a_output2+=(" - unloading kernel module: \"$l_mod_name\"")
 modprobe -r "$l_mod_chk_name" 2>/dev/null; rmmod "$l_mod_name" 
2>/dev/null
 fi
 if ! grep -Pq -- '\binstall\h+'"${l_mod_chk_name//-
/_}"'\h+(\/usr)?\/bin\/(true|false)\b' <<< "${a_showconfig[*]}"; then
 a_output2+=(" - setting kernel module: \"$l_mod_name\" to 
\"$(readlink -f /bin/false)\"")
 printf '%s\n' "install $l_mod_chk_name $(readlink -f /bin/false)" >> 
/etc/modprobe.d/"$l_mod_name".conf
 fi
 if ! grep -Pq -- '\bblacklist\h+'"${l_mod_chk_name//-/_}"'\b' <<< 
"${a_showconfig[*]}"; then
 a_output2+=(" - denylisting kernel module: \"$l_mod_name\"")
 printf '%s\n' "blacklist $l_mod_chk_name" >> 
/etc/modprobe.d/"$l_mod_name".conf
 fi
 }
 for l_mod_base_directory in $l_mod_path; do # Check if the module exists 
on the system
 if [ -d "$l_mod_base_directory/${l_mod_name/-/\/}" ] && [ -n "$(ls -A 
"$l_mod_base_directory/${l_mod_name/-/\/}")" ]; then
 a_output3+=(" - \"$l_mod_base_directory\"")
 l_mod_chk_name="$l_mod_name"
 [[ "$l_mod_name" =~ overlay ]] && l_mod_chk_name="${l_mod_name::-2}" 
 [ "$l_dl" != "y" ] && f_module_fix
 else
 printf '%s\n' " - kernel module: \"$l_mod_name\" doesn't exist in 
\"$l_mod_base_directory\""
 fi
 done
 [ "${#a_output3[@]}" -gt 0 ] && printf '%s\n' "" " -- INFO --" " - module: 
\"$l_mod_name\" exists in:" "${a_output3[@]}"
 [ "${#a_output2[@]}" -gt 0 ] && printf '%s\n' "" "${a_output2[@]}" || 
printf '%s\n' "" " - No changes needed"
 printf '%s\n' "" " - remediation of kernel module: \"$l_mod_name\" 
complete" ""
}
```

**References:**
1. NIST SP 800-53 Rev. 5: CM-7

**CIS Controls:**

| Controls Version | Control | IG 1 | IG 2 | IG 3 |
|------------------|---------|------|------|------|
| v8 | 4.8 Uninstall or Disable Unnecessary Services on Enterprise Assets and Software<br>Uninstall or disable unnecessary services on enterprise assets and software, such as an unused file sharing service, web application module, or service function. | | ● | ● |
| v7 | 9.2 Ensure Only Approved Ports, Protocols and Services Are Running<br>Ensure that only network ports, protocols, and services listening on a system with validated business needs, are running on each system. | | ● | ● |

**MITRE ATT&CK Mappings:**

| Techniques / Subtechniques | Tactics | Mitigations |
|----------------------------|---------|-------------|
| T1005, T1005.000 | TA0005 | M1050 |

###### 1.1.1.5 Ensure jffs2 kernel module is not available (Automated)

**Profile Applicability:**
- Level 1 - Server
- Level 1 - Workstation

**Description:**  
The jffs2 (journaling flash filesystem 2) filesystem type is a log-structured filesystem used in flash memory devices.

**Rationale:**  
Removing support for unneeded filesystem types reduces the local attack surface of the system. If this filesystem type is not needed, disable it.

**Audit:**  
Run the following script to verify:
- IF - the jffs2 kernel module is available in ANY installed kernel, verify:
  - An entry including `/bin/true` or `/bin/false` exists in a file within the `/etc/modprobe.d/` directory
  - The module is deny listed in a file within the `/etc/modprobe.d/` directory
  - The module is not loaded in the running kernel
- IF - the jffs2 kernel module is not available on the system, or pre-compiled into the kernel, no additional configuration is necessary

```bash
#!/usr/bin/env bash
{
 a_output=() a_output2=() a_output3=() l_dl="" l_mod_name="jffs2" 
l_mod_type="fs"
 l_mod_path="$(readlink -f /lib/modules/**/kernel/$l_mod_type | sort -u)"
 f_module_chk()
 {
 l_dl="y" a_showconfig=()
 while IFS= read -r l_showconfig; do
 a_showconfig+=("$l_showconfig")
 done < <(modprobe --showconfig | grep -P --
'\b(install|blacklist)\h+'"${l_mod_chk_name//-/_}"'\b')
 if ! lsmod | grep "$l_mod_chk_name" &> /dev/null; then
 a_output+=(" - kernel module: \"$l_mod_name\" is not loaded")
 else
 a_output2+=(" - kernel module: \"$l_mod_name\" is loaded")
 fi
 if grep -Pq -- '\binstall\h+'"${l_mod_chk_name//-
/_}"'\h+(\/usr)?\/bin\/(true|false)\b' <<< "${a_showconfig[*]}"; then
 a_output+=(" - kernel module: \"$l_mod_name\" is not loadable")
 else
 a_output2+=(" - kernel module: \"$l_mod_name\" is loadable")
 fi
 if grep -Pq -- '\bblacklist\h+'"${l_mod_chk_name//-/_}"'\b' <<< 
"${a_showconfig[*]}"; then
 a_output+=(" - kernel module: \"$l_mod_name\" is deny listed")
 else
 a_output2+=(" - kernel module: \"$l_mod_name\" is not deny listed")
 fi
 }
 for l_mod_base_directory in $l_mod_path; do
 if [ -d "$l_mod_base_directory/${l_mod_name/-/\/}" ] && [ -n "$(ls -A 
"$l_mod_base_directory/${l_mod_name/-/\/}")" ]; then
 a_output3+=(" - \"$l_mod_base_directory\"")
 l_mod_chk_name="$l_mod_name"
 [[ "$l_mod_name" =~ overlay ]] && l_mod_chk_name="${l_mod_name::-2}" 
 [ "$l_dl" != "y" ] && f_module_chk
 else
 a_output+=(" - kernel module: \"$l_mod_name\" doesn't exist in 
\"$l_mod_base_directory\"")
 fi
 done
 [ "${#a_output3[@]}" -gt 0 ] && printf '%s\n' "" " -- INFO --" " - module: 
\"$l_mod_name\" exists in:" "${a_output3[@]}"
 if [ "${#a_output2[@]}" -le 0 ]; then
 printf '%s\n' "" "- Audit Result:" " ** PASS **" "${a_output[@]}"
 else
 printf '%s\n' "" "- Audit Result:" " ** FAIL **" " - Reason(s) for 
audit failure:" "${a_output2[@]}"
 [ "${#a_output[@]}" -gt 0 ] && printf '%s\n' "- Correctly set:" 
"${a_output[@]}"
 fi
}
```

**Remediation:**  
Run the following script to unload and disable the jffs2 module:
- IF - the jffs2 kernel module is available in ANY installed kernel:
  - Create a file ending in .conf with `install jffs2 /bin/false` in the `/etc/modprobe.d/` directory
  - Create a file ending in .conf with `blacklist jffs2` in the `/etc/modprobe.d/` directory
  - Run `modprobe -r jffs2 2>/dev/null; rmmod jffs2 2>/dev/null` to remove jffs2 from the kernel
- IF - the jffs2 kernel module is not available on the system, or pre-compiled into the kernel, no remediation is necessary

```bash
#!/usr/bin/env bash
{
 a_output2=() a_output3=() l_dl="" l_mod_name="jffs2" l_mod_type="fs"
 l_mod_path="$(readlink -f /lib/modules/**/kernel/$l_mod_type | sort -u)"
 f_module_fix()
 {
 l_dl="y" a_showconfig=()
 while IFS= read -r l_showconfig; do
 a_showconfig+=("$l_showconfig")
 done < <(modprobe --showconfig | grep -P --
'\b(install|blacklist)\h+'"${l_mod_chk_name//-/_}"'\b')
 if lsmod | grep "$l_mod_chk_name" &> /dev/null; then
 a_output2+=(" - unloading kernel module: \"$l_mod_name\"")
 modprobe -r "$l_mod_chk_name" 2>/dev/null; rmmod "$l_mod_name" 
2>/dev/null
 fi
 if ! grep -Pq -- '\binstall\h+'"${l_mod_chk_name//-
/_}"'\h+(\/usr)?\/bin\/(true|false)\b' <<< "${a_showconfig[*]}"; then
 a_output2+=(" - setting kernel module: \"$l_mod_name\" to 
\"$(readlink -f /bin/false)\"")
 printf '%s\n' "install $l_mod_chk_name $(readlink -f /bin/false)" >> 
/etc/modprobe.d/"$l_mod_name".conf
 fi
 if ! grep -Pq -- '\bblacklist\h+'"${l_mod_chk_name//-/_}"'\b' <<< 
"${a_showconfig[*]}"; then
 a_output2+=(" - denylisting kernel module: \"$l_mod_name\"")
 printf '%s\n' "blacklist $l_mod_chk_name" >> 
/etc/modprobe.d/"$l_mod_name".conf
 fi
```

**References:**  
1. NIST SP 800-53 Rev. 5: CM-7
2. STIG Finding ID: V-230498

**CIS Controls:**

| Controls Version | Control | IG 1 | IG 2 | IG 3 |
|------------------|---------|------|------|------|
| v8 | 4.8 Uninstall or Disable Unnecessary Services on Enterprise Assets and Software<br>Uninstall or disable unnecessary services on enterprise assets and software, such as an unused file sharing service, web application module, or service function. | | ● | ● |
| v7 | 9.2 Ensure Only Approved Ports, Protocols and Services Are Running<br>Ensure that only network ports, protocols, and services listening on a system with validated business needs, are running on each system. | | ● | ● |

**MITRE ATT&CK Mappings:**

| Techniques / Subtechniques | Tactics | Mitigations |
|----------------------------|---------|-------------|
| T1005, T1005.000 | TA0005 | M1050 |