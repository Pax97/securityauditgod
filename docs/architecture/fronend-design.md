# Thiết kế Giao diện Ứng dụng Phân tích CIS Benchmark

Dựa trên tài liệu thiết kế và yêu cầu từ dự án, tôi đã tạo mockup giao diện cho ứng dụng phân tích CIS Benchmark với kiến trúc monolithic. Giao diện này đảm bảo hỗ trợ đầy đủ các chức năng đã được nêu trong thiết kế tổng thể.

## Tổng quan giao diện

Giao diện được thiết kế với bố cục nhất quán và trực quan, bao gồm:

1. **Menu điều hướng chính** (bên trái)
2. **Thanh tiêu đề** (trên cùng) với thông tin người dùng và tìm kiếm
3. **Khu vực nội dung chính** (trung tâm) thay đổi theo chức năng
4. **Thanh trạng thái** (dưới cùng) hiển thị thông tin hệ thống

## Các màn hình chính

### 1. Dashboard (Trang tổng quan)

```
+----------------------------------------------------------------------------------------------------------------------+
|  LOGO  | Dashboard | Projects | Assets | Assessments | Reports | Settings |                      User ▼ | ? | ⚙ |     |
+--------+-----------+----------+--------+-------------+---------+----------+------------------------------+---+---+-----+
|        |                                                                                                              |
|        |  DASHBOARD                                                                             ⟳ | Filter ▼ | Export |
|        |  +--------------------------+  +------------------------+  +------------------------+                         |
|        |  | PROJECTS                 |  | ASSESSMENTS            |  | COMPLIANCE OVERVIEW   |                         |
|        |  |                          |  |                        |  |                       |                         |
| MENU   |  | Active: 5                |  | Last 24h: 3            |  |  [DONUT CHART]        |                         |
|        |  | Total: 12                |  | Last 7d: 12            |  |                       |                         |
|        |  |                          |  | Total: 35              |  |  Pass: 75%            |                         |
|        |  | [VIEW ALL]               |  |                        |  |  Fail: 15%            |                         |
|        |  +--------------------------+  | [VIEW ALL]             |  |  Unknown: 10%         |                         |
|        |                                +------------------------+  +------------------------+                         |
|        |  +-----------------------------------------------------------------------------+                            |
|        |  | RECENT ASSESSMENTS                                                          |                            |
|        |  |                                                                             |                            |
|        |  | Project     | Asset           | Benchmark       | Date       | Score | Status |                          |
|        |  |-------------|-----------------|-----------------|------------|-------|--------|                          |
|        |  | Web App     | web1.example.com| Ubuntu 24.04 L1 | 2025-03-17 | 85.7% | ✓     |                          |
|        |  | Database    | db-master       | MySQL 8.4       | 2025-03-16 | 92.3% | ✓     |                          |
|        |  | API Servers | api02.internal  | Ubuntu 24.04 L1 | 2025-03-15 | 67.8% | ⚠     |                          |
|        |  |                                                                             |                            |
|        |  | [VIEW ALL]                                                                  |                            |
|        |  +-----------------------------------------------------------------------------+                            |
|        |                                                                                                              |
|        |  +-------------------------------------+  +---------------------------------------------+                    |
|        |  | TOP FAILING CONTROLS                |  | COMPLIANCE TREND                            |                    |
|        |  |                                     |  |                                             |                    |
|        |  | 1. Disable cramfs (15 assets)       |  | [LINE CHART - compliance score over time]   |                    |
|        |  | 2. SSH root login (12 assets)       |  |                                             |                    |
|        |  | 3. MySQL auth plugin (8 assets)     |  |                                             |                    |
|        |  | 4. Password policy (6 assets)       |  |                                             |                    |
|        |  |                                     |  |                                             |                    |
|        |  | [VIEW ALL]                          |  |                                             |                    |
|        |  +-------------------------------------+  +---------------------------------------------+                    |
|        |                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------+
| Status: System Ready | Last update: 2025-03-18 15:30:45                                                               |
+----------------------------------------------------------------------------------------------------------------------+
```

### 2. Projects Management (Quản lý dự án)

```
+----------------------------------------------------------------------------------------------------------------------+
|  LOGO  | Dashboard | Projects | Assets | Assessments | Reports | Settings |                      User ▼ | ? | ⚙ |     |
+--------+-----------+----------+--------+-------------+---------+----------+------------------------------+---+---+-----+
|        |                                                                                                              |
|        |  PROJECTS                                                                        + New Project | Search...    |
|        |                                                                                                              |
|        |  +-------------------------------------------------------------------------------------------+               |
|        |  | PROJECT LIST                                                                              |               |
|        |  |                                                                                           |               |
| MENU   |  | Name           | Description                | Assets | Last Assessment  | Status  | Actions              |
|        |  |----------------|----------------------------|--------|------------------|---------|---------------------|
|        |  | Web App Infra  | Web application servers    | 8      | 2025-03-17       | Active  | View | Edit | Delete |
|        |  | Database Tier  | Database servers           | 5      | 2025-03-16       | Active  | View | Edit | Delete |
|        |  | API Services   | API backend servers        | 6      | 2025-03-15       | Active  | View | Edit | Delete |
|        |  | Dev Environment| Development environment    | 12     | 2025-03-10       | Active  | View | Edit | Delete |
|        |  | Legacy Systems | Systems pending migration  | 4      | 2025-02-28       | Inactive| View | Edit | Delete |
|        |  |                                                                                           |               |
|        |  +-------------------------------------------------------------------------------------------+               |
|        |                                                                                                              |
|        |  PROJECT DETAILS: Web App Infra                                                                              |
|        |                                                                                                              |
|        |  +-------------------------------------+  +---------------------------------------------+                    |
|        |  | INFORMATION                         |  | COMPLIANCE SUMMARY                          |                    |
|        |  |                                     |  |                                             |                    |
|        |  | Created: 2025-03-01                 |  | [COMPLIANCE SCORE BAR CHART BY ASSET]       |                    |
|        |  | Owner: John Smith                   |  |                                             |                    |
|        |  | Description: Web application        |  | web1: 85.7%                                 |                    |
|        |  | infrastructure including frontend   |  | web2: 88.2%                                 |                    |
|        |  | and application servers             |  | web3: 79.5%                                 |                    |
|        |  |                                     |  | web4: 90.1%                                 |                    |
|        |  | [EDIT]                              |  |                                             |                    |
|        |  +-------------------------------------+  +---------------------------------------------+                    |
|        |                                                                                                              |
|        |  +--------------------------+ +-------------------------+ +--------------------------------+                 |
|        |  | ASSET GROUPS             | | ASSESSMENTS             | | ACTIONS                        |                 |
|        |  |                          | |                         | |                                |                 |
|        |  | ☑ Production (5)         | | Total: 12               | | [ASSESS PROJECT]               |                 |
|        |  | ☐ Staging (3)            | | Last: 2025-03-17        | | [VIEW REPORT]                  |                 |
|        |  |                          | | Scheduled: 2025-03-24   | | [EXPORT DATA]                  |                 |
|        |  | [MANAGE GROUPS]          | | [VIEW HISTORY]          | | [SCHEDULE ASSESSMENT]          |                 |
|        |  +--------------------------+ +-------------------------+ +--------------------------------+                 |
|        |                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------+
| Status: System Ready | Last update: 2025-03-18 15:31:20                                                               |
+----------------------------------------------------------------------------------------------------------------------+
```

### 3. Asset Inventory (Quản lý tài sản)

```
+----------------------------------------------------------------------------------------------------------------------+
|  LOGO  | Dashboard | Projects | Assets | Assessments | Reports | Settings |                      User ▼ | ? | ⚙ |     |
+--------+-----------+----------+--------+-------------+---------+----------+------------------------------+---+---+-----+
|        |                                                                                                              |
|        |  ASSETS                                                                            + New Asset | Search...    |
|        |                                                                                                              |
|        |  Project: Web App Infra ▼ | Type: All ▼ | Group: All ▼ | Status: All ▼ | Tags: ▼                             |
|        |                                                                                                              |
| MENU   |  +-------------------------------------------------------------------------------------------+               |
|        |  | ASSET LIST                                                                                |               |
|        |  |                                                                                           |               |
|        |  | Name           | Type   | Hostname            | IP Address    | OS/Info        | Actions               |
|        |  |----------------|--------|---------------------|---------------|----------------|----------------------|
|        |  | Web Server 1   | Linux  | web1.example.com    | 192.168.1.10  | Ubuntu 24.04   | View | Edit | Delete  |
|        |  | Web Server 2   | Linux  | web2.example.com    | 192.168.1.11  | Ubuntu 24.04   | View | Edit | Delete  |
|        |  | App Server 1   | Linux  | app1.example.com    | 192.168.1.20  | Ubuntu 24.04   | View | Edit | Delete  |
|        |  | App Server 2   | Linux  | app2.example.com    | 192.168.1.21  | Ubuntu 24.04   | View | Edit | Delete  |
|        |  | Load Balancer  | Linux  | lb.example.com      | 192.168.1.5   | Ubuntu 24.04   | View | Edit | Delete  |
|        |  | DB Server      | MySQL  | db.example.com      | 192.168.1.30  | MySQL 8.4      | View | Edit | Delete  |
|        |  |                                                                                           |               |
|        |  +-------------------------------------------------------------------------------------------+               |
|        |                                                                                                              |
|        |  ASSET DETAILS: Web Server 1                                                                                 |
|        |                                                                                                              |
|        |  +-------------------------------------+  +---------------------------------------------+                    |
|        |  | INFORMATION                         |  | COMPLIANCE HISTORY                          |                    |
|        |  |                                     |  |                                             |                    |
|        |  | Type: Linux                         |  | [LINE CHART - compliance trend]             |                    |
|        |  | Hostname: web1.example.com          |  |                                             |                    |
|        |  | IP: 192.168.1.10                    |  | Last Assessment: 2025-03-17                 |                    |
|        |  | OS: Ubuntu 24.04                    |  | Score: 85.7%                                |                    |
|        |  | Groups: Production                  |  | Changed from: 82.3% (2025-03-10)            |                    |
|        |  | Tags: Web, Frontend, Critical       |  |                                             |                    |
|        |  |                                     |  | [VIEW FULL HISTORY]                         |                    |
|        |  | [EDIT]                              |  |                                             |                    |
|        |  +-------------------------------------+  +---------------------------------------------+                    |
|        |                                                                                                              |
|        |  +-------------------------------------------------------------------+                                       |
|        |  | ACTIONS                                                            |                                       |
|        |  |                                                                    |                                       |
|        |  | [ASSESS NOW] [VIEW REPORT] [COMPARE ASSESSMENTS] [EXPORT DATA]     |                                       |
|        |  +-------------------------------------------------------------------+                                       |
|        |                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------+
| Status: System Ready | Last update: 2025-03-18 15:32:05                                                               |
+----------------------------------------------------------------------------------------------------------------------+
```

### 4. Data Import (Nhập dữ liệu)

```
+----------------------------------------------------------------------------------------------------------------------+
|  LOGO  | Dashboard | Projects | Assets | Assessments | Reports | Settings |                      User ▼ | ? | ⚙ |     |
+--------+-----------+----------+--------+-------------+---------+----------+------------------------------+---+---+-----+
|        |                                                                                                              |
|        |  IMPORT DATA                                                                                                 |
|        |                                                                                                              |
|        |  +------------------------------------------------------------------------------------------------------+    |
|        |  | IMPORT ASSESSMENT DATA                                                                               |    |
|        |  |                                                                                                      |    |
| MENU   |  | Source: File Upload ▼                                                                                |    |
|        |  |                                                                                                      |    |
|        |  | [DRAG AND DROP FILES HERE OR CLICK TO BROWSE]                                                        |    |
|        |  |                                                                                                      |    |
|        |  | Selected files:                                                                                      |    |
|        |  | • web1_assessment.json (12.5 KB) [REMOVE]                                                            |    |
|        |  | • db_assessment.json (8.3 KB) [REMOVE]                                                               |    |
|        |  |                                                                                                      |    |
|        |  | Target Project: Web App Infra ▼                                                                      |    |
|        |  |                                                                                                      |    |
|        |  | Options:                                                                                             |    |
|        |  | ☑ Auto-associate with assets based on hostname/IP                                                    |    |
|        |  | ☑ Create assets if they don't exist                                                                  |    |
|        |  | ☐ Override existing assessments for same date                                                        |    |
|        |  | ☑ Validate data before import                                                                        |    |
|        |  |                                                                                                      |    |
|        |  | [VALIDATE] [IMPORT NOW]                                                                              |    |
|        |  +------------------------------------------------------------------------------------------------------+    |
|        |                                                                                                              |
|        |  +------------------------------------------------------------------------------------------------------+    |
|        |  | VALIDATION RESULTS                                                                                   |    |
|        |  |                                                                                                      |    |
|        |  | ✅ web1_assessment.json: Valid format                                                                 |    |
|        |  | ✅ Asset match found: Web Server 1 (web1.example.com)                                                 |    |
|        |  | ✅ Benchmark match found: CIS Ubuntu Linux 24.04 LTS Benchmark                                        |    |
|        |  |                                                                                                      |    |
|        |  | ✅ db_assessment.json: Valid format                                                                   |    |
|        |  | ⚠️ No asset match found. Will create new asset: db.example.com (MySQL)                               |    |
|        |  | ✅ Benchmark match found: CIS Oracle MySQL Enterprise Edition 8.4 Benchmark                           |    |
|        |  |                                                                                                      |    |
|        |  | [PROCEED WITH IMPORT] [CANCEL]                                                                       |    |
|        |  +------------------------------------------------------------------------------------------------------+    |
|        |                                                                                                              |
|        |  +------------------------------------------------------------------------------------------------------+    |
|        |  | IMPORT HISTORY                                                                                       |    |
|        |  |                                                                                                      |    |
|        |  | Date       | User      | Files | Status  | Details                                                   |    |
|        |  |------------|-----------|-------|---------|-----------------------------------------------------------|    |
|        |  | 2025-03-15 | admin     | 3     | Success | Imported 3 files to "Web App Infra"                       |    |
|        |  | 2025-03-10 | jsmith    | 5     | Partial | Imported 4/5 files to "Database Tier" (1 validation error)|    |
|        |  | 2025-03-05 | admin     | 8     | Success | Imported 8 files to "API Services"                        |    |
|        |  |                                                                                                      |    |
|        |  | [VIEW FULL HISTORY]                                                                                  |    |
|        |  +------------------------------------------------------------------------------------------------------+    |
+----------------------------------------------------------------------------------------------------------------------+
| Status: Ready to import | Files selected: 2                                                                           |
+----------------------------------------------------------------------------------------------------------------------+
```

### 5. Assessment View (Xem đánh giá)

```
+----------------------------------------------------------------------------------------------------------------------+
|  LOGO  | Dashboard | Projects | Assets | Assessments | Reports | Settings |                      User ▼ | ? | ⚙ |     |
+--------+-----------+----------+--------+-------------+---------+----------+------------------------------+---+---+-----+
|        |                                                                                                              |
|        |  ASSESSMENT: Web Server 1 - 2025-03-17                                             Filter ▼ | Export | Print |
|        |                                                                                                              |
|        |  +---------------------------------------------------------+  +--------------------------------------+       |
|        |  | SUMMARY                                                 |  | STATS                                |       |
|        |  |                                                         |  |                                      |       |
| MENU   |  | Asset: Web Server 1 (web1.example.com)                  |  | Overall Score: 85.7%                 |       |
|        |  | Benchmark: CIS Ubuntu Linux 24.04 LTS Benchmark         |  |                                      |       |
|        |  | Profile: Level 1 - Server                               |  | Pass: 120 (80%)                      |       |
|        |  | Date: 2025-03-17 14:30:00                               |  | Fail: 15 (10%)                       |       |
|        |  | Duration: 45.8s                                         |  | Unknown: 5 (3.3%)                    |       |
|        |  | Collector: linux_collector.py v1.0.0                    |  | Not Applicable: 10 (6.7%)            |       |
|        |  |                                                         |  |                                      |       |
|        |  | [VIEW RAW DATA] [COMPARE WITH PREVIOUS]                 |  | [DONUT CHART]                        |       |
|        |  +---------------------------------------------------------+  +--------------------------------------+       |
|        |                                                                                                              |
|        |  +-------------------------------------------------------------------------------------------+               |
|        |  | CONTROLS                                                                                  |               |
|        |  |                                                                                           |               |
|        |  | ID        | Title                              | Status | Evidence                    | Actions         |
|        |  |-----------|------------------------------------|---------|-----------------------------|-----------------|
|        |  | 1.1.1.1   | Ensure cramfs kernel module...     | ✅ Pass | Module is blacklisted...    | Details | Fix  |
|        |  | 1.1.1.2   | Ensure freevxfs kernel module...   | ✅ Pass | Module is blacklisted...    | Details | Fix  |
|        |  | 1.1.1.3   | Ensure hfs kernel module...        | ✅ Pass | Module is blacklisted...    | Details | Fix  |
|        |  | 1.1.1.4   | Ensure hfsplus kernel module...    | ✅ Pass | Module is blacklisted...    | Details | Fix  |
|        |  | 1.1.1.5   | Ensure jffs2 kernel module...      | ❌ Fail | Module is loadable...       | Details | Fix  |
|        |  | 1.2.1     | Use dedicated least priv account   | ✅ Pass | MySQL user exists...        | Details | Fix  |
|        |  | 1.3.1     | Disable MySQL command history      | ❌ Fail | .mysql_history found...     | Details | Fix  |
|        |  | 1.4.1     | Verify MYSQL_PWD is not in use     | ✅ Pass | No MYSQL_PWD found...       | Details | Fix  |
|        |  |                                                                                           |               |
|        |  | [LOAD MORE] Showing 8 of 150 controls                                                     |               |
|        |  +-------------------------------------------------------------------------------------------+               |
|        |                                                                                                              |
|        |  CONTROL DETAILS: 1.1.1.5 - Ensure jffs2 kernel module is not available                                      |
|        |                                                                                                              |
|        |  +-------------------------------------------------------------------------------------------+               |
|        |  | CONTROL INFORMATION                                                                        |               |
|        |  |                                                                                            |               |
|        |  | Description: The jffs2 (journaling flash filesystem 2) filesystem type is a log-structured |               |
|        |  | filesystem used in flash memory devices.                                                   |               |
|        |  |                                                                                            |               |
|        |  | Rationale: Removing support for unneeded filesystem types reduces the local attack surface |               |
|        |  | of the system. If this filesystem type is not needed, disable it.                          |               |
|        |  |                                                                                            |               |
|        |  | Assessment Status: Automated                                                               |               |
|        |  |                                                                                            |               |
|        |  +-------------------------------------------------------------------------------------------+               |
|        |                                                                                                              |
|        |  +-------------------------------------------------------------------------------------------+               |
|        |  | ASSESSMENT RESULTS                                                                         |               |
|        |  |                                                                                            |               |
|        |  | Status: FAIL                                                                               |               |
|        |  |                                                                                            |               |
|        |  | Evidence:                                                                                  |               |
|        |  | - kernel module: "jffs2" is not loaded                                                     |               |
|        |  | - kernel module: "jffs2" is loadable                                                       |               |
|        |  | - kernel module: "jffs2" is not deny listed                                                |               |
|        |  |                                                                                            |               |
|        |  +-------------------------------------------------------------------------------------------+               |
|        |                                                                                                              |
|        |  +-------------------------------------------------------------------------------------------+               |
|        |  | REMEDIATION                                                                                |               |
|        |  |                                                                                            |               |
|        |  | Run the following script to unload and disable the jffs2 module:                           |               |
|        |  | - Create a file ending in .conf with `install jffs2 /bin/false` in the `/etc/modprobe.d/`  |               |
|        |  | - Create a file ending in .conf with `blacklist jffs2` in the `/etc/modprobe.d/` directory |               |
|        |  | - Run `modprobe -r jffs2 2>/dev/null; rmmod jffs2 2>/dev/null` to remove jffs2             |               |
|        |  |                                                                                            |               |
|        |  | [COPY COMMAND] [MARK AS FIXED]                                                             |               |
|        |  +-------------------------------------------------------------------------------------------+               |
+----------------------------------------------------------------------------------------------------------------------+
| Status: System Ready | Viewing assessment from: 2025-03-17 14:30:00                                                   |
+----------------------------------------------------------------------------------------------------------------------+
```

### 6. Reports (Báo cáo)

```
+----------------------------------------------------------------------------------------------------------------------+
|  LOGO  | Dashboard | Projects | Assets | Assessments | Reports | Settings |                      User ▼ | ? | ⚙ |     |
+--------+-----------+----------+--------+-------------+---------+----------+------------------------------+---+---+-----+
|        |                                                                                                              |
|        |  REPORTS                                                                                + New Report         |
|        |                                                                                                              |
|        |  +---------------------------------------------------------------------+                                     |
|        |  | REPORT TEMPLATES                                                     |                                     |
|        |  |                                                                      |                                     |
| MENU   |  | Template               | Description                   | Actions     |                                     |
|        |  |-----------------------|-------------------------------|-------------|                                     |
|        |  | Executive Summary     | High-level overview           | Use | Edit   |                                     |
|        |  | Detailed Assessment   | Complete assessment details    | Use | Edit   |                                     |
|        |  | Compliance Dashboard  | Visual dashboard               | Use | Edit   |                                     |
|        |  | Remediation Plan      | Focus on fixing issues         | Use | Edit   |                                     |
|        |  | Trend Analysis        | Changes over time              | Use | Edit   |                                     |
|        |  |                                                                      |                                     |
|        |  +---------------------------------------------------------------------+                                     |
|        |                                                                                                              |
|        |  Generate Report:                                                                                            |
|        |                                                                                                              |
|        |  Template: Executive Summary ▼ | Format: PDF ▼                                                               |
|        |                                                                                                              |
|        |  Scope:                                                                                                      |
|        |  ○ Project: Web App Infra ▼                                                                                  |
|        |  ○ Asset Group: Production Servers ▼                                                                         |
|        |  ○ Individual Asset: Web Server 1 ▼                                                                          |
|        |                                                                                                              |
|        |  Time Range:                                                                                                 |
|        |  ○ Latest assessment                                                                                         |
|        |  ○ Specific date: [2025-03-17] ▼                                                                             |
|        |  ○ Date range: [2025-03-01] to [2025-03-17] ▼                                                                |
|        |  ○ Compare: [2025-03-10] vs [2025-03-17] ▼                                                                   |
|        |                                                                                                              |
|        |  Options:                                                                                                    |
|        |  ☑ Include executive summary                                                                                 |
|        |  ☑ Include remediation recommendations                                                                       |
|        |  ☑ Include trend analysis                                                                                    |
|        |  ☑ Include charts and visuals                                                                                |
|        |  ☐ Include raw data                                                                                          |
|        |                                                                                                              |
|        |  [PREVIEW REPORT] [GENERATE REPORT]                                                                          |
|        |                                                                                                              |
|        |  +---------------------------------------------------------------------+                                     |
|        |  | RECENT REPORTS                                                       |                                     |
|        |  |                                                                      |                                     |
|        |  | Name                      | Generated          | By       | Actions  |                                     |
|        |  |---------------------------|-------------------|----------|----------|                                     |
|        |  | Web App Infra - Executive | 2025-03-17 16:45   | admin    | View     |                                     |
|        |  | DB Tier - Remediation     | 2025-03-16 10:30   | jsmith   | View     |                                     |
|        |  | API Services - Full       | 2025-03-15 09:15   | admin    | View     |                                     |
|        |  |                                                                      |                                     |
|        |  +---------------------------------------------------------------------+                                     |
+----------------------------------------------------------------------------------------------------------------------+
| Status: System Ready | Last report generated: 2025-03-17 16:45:23                                                     |
+----------------------------------------------------------------------------------------------------------------------+
```

### 7. Settings & Configuration

```
+----------------------------------------------------------------------------------------------------------------------+
|  LOGO  | Dashboard | Projects | Assets | Assessments | Reports | Settings |                      User ▼ | ? | ⚙ |     |
+--------+-----------+----------+--------+-------------+---------+----------+------------------------------+---+---+-----+
|        |                                                                                                              |
|        |  SETTINGS                                                                                                    |
|        |                                                                                                              |
|        |  +------------------+  +------------------------------------------------+                                    |
|        |  |                  |  |                                                |                                    |
|        |  | General          |  | GENERAL SETTINGS                               |                                    |
| MENU   |  | Benchmarks       |  |                                                |                                    |
|        |  | Users            |  | Application Name: CIS Assessment Tool          |                                    |
|        |  | Backup & Restore |  | Default Project: None ▼                        |                                    |
|        |  | Import & Export  |  | Theme: Light ▼                                 |                                    |
|        |  | Logs             |  | Date Format: YYYY-MM-DD ▼                      |                                    |
|        |  | About            |  | Time Format: 24-hour ▼                         |                                    |
|        |  |                  |  | Default Export Format: PDF ▼                    |                                    |
|        |  |                  |  |                                                |                                    |
|        |  |                  |  | Auto-refresh Dashboard: ☑                      |                                    |
|        |  |                  |  | Refresh Interval: 5 minutes ▼                  |                                    |
|        |  |                  |  |                                                |                                    |
|        |  |                  |  | Scoring Method: Weighted ▼                     |                                    |
|        |  |                  |  | Failed Control Weight: 1.0                     |                                    |
|        |  |                  |  | Unknown Control Weight: 0.5                    |                                    |
|        |  |                  |  |                                                |                                    |
|        |  |                  |  | [SAVE CHANGES] [RESTORE DEFAULTS]              |                                    |
|        |  |                  |  |                                                |                                    |
|        |  +------------------+  +------------------------------------------------+                                    |
|        |                                                                                                              |
|        |  BENCHMARK MANAGEMENT                                                                                        |
|        |                                                                                                              |
|        |  +------------------------------------------------------------------------------------------+                |
|        |  | INSTALLED BENCHMARKS                                           | + Import Benchmark | Update All          |
|        |  |                                                                                                           |
|        |  | Benchmark                          | Version  | Profiles      | Last Updated | Actions                    |
|        |  |-------------------------------------|----------|--------------|--------------|----------------------------|
|        |  | CIS Ubuntu Linux 24.04 LTS         | 1.0.0    | L1/L2 Server | 2025-03-01   | Update | Export | Delete   |
|        |  | CIS Oracle MySQL Ent. Ed. 8.4      | 1.0.0    | L1/L2        | 2025-01-29   | Update | Export | Delete   |
|        |  | CIS Microsoft Windows Server 2022  | 2.0.0    | L1/L2/STIG   | 2025-02-15   | Update | Export | Delete   |
|        |  |                                                                                                           |
|        |  | [LOAD MORE] Showing 3 of 8 benchmarks                                                                     |
|        |  +------------------------------------------------------------------------------------------+                |
|        |                                                                                                              |
|        |  +------------------------------------------------------------------------------------------+                |
|        |  | BENCHMARK REPOSITORY                                                                     |                |
|        |  |                                                                                                           |
|        |  | Source: Local Repository ▼                                     | Refresh | Check for Updates              |
|        |  |                                                                                                           |
|        |  | Name                                | Version  | Status                                                   |
|        |  |-------------------------------------|----------|----------------------------------------------------------|
|        |  | CIS Amazon Linux 2 Benchmark       | 2.1.0    | Not Installed [INSTALL]                                  |
|        |  | CIS Google Kubernetes Engine Bench | 1.5.0    | Not Installed [INSTALL]                                  |
|        |  | CIS PostgreSQL 15 Benchmark        | 1.0.0    | Not Installed [INSTALL]                                  |
|        |  |                                                                                                           |
|        |  | [LOAD MORE] Showing 3 of 15 available benchmarks                                                          |
|        |  +------------------------------------------------------------------------------------------+                |
+----------------------------------------------------------------------------------------------------------------------+
| Status: System Ready | Database: 384 MB Used                                                                          |
+----------------------------------------------------------------------------------------------------------------------+
```

## Thiết kế Responsive

Giao diện ứng dụng được thiết kế để có thể phản hồi tốt trên các kích thước màn hình khác nhau:

1. **Màn hình lớn (>1200px)**: Hiển thị đầy đủ như mockup trên
2. **Tablet (768px-1200px)**: Menu co lại thành icons, layout chuyển sang dạng cột đơn
3. **Mobile (<768px)**: Menu ẩn trong hamburger icon, các bảng scrollable ngang

## Bảng màu đề xuất

- **Màu chính (Primary)**: #1E88E5 (Blue)
- **Màu phụ (Secondary)**: #26A69A (Teal)
- **Màu nhấn (Accent)**: #FFC107 (Amber)
- **Màu thành công (Success)**: #4CAF50 (Green)
- **Màu cảnh báo (Warning)**: #FF9800 (Orange)
- **Màu lỗi (Error)**: #F44336 (Red)
- **Màu nền (Background)**: #F5F7FA (Light Gray)
- **Màu văn bản (Text)**: #37474F (Dark Gray)

## Kết luận

Thiết kế giao diện ứng dụng phân tích CIS Benchmark này đảm bảo đáp ứng đầy đủ các yêu cầu chức năng từ thiết kế tổng thể, bao gồm:

1. Quản lý và tổ chức tài sản theo dự án
2. Nhập và phân tích dữ liệu thu thập từ collector scripts
3. Đánh giá tuân thủ theo tiêu chuẩn CIS Benchmark
4. Tạo báo cáo chi tiết và tổng quan
5. Theo dõi tiến độ cải thiện theo thời gian

Giao diện được thiết kế với nguyên tắc đơn giản, trực quan và hiệu quả, phù hợp với kiến trúc monolithic của ứng dụng, tạo ra trải nghiệm người dùng tốt nhất cho việc đánh giá bảo mật theo CIS Benchmark.
