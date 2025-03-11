# Thiết kế schema chuẩn hoá CIS Benchmark

## Mục lục
1. [Giới thiệu](#giới-thiệu)
2. [Schema dữ liệu thu thập](#schema-dữ-liệu-thu-thập)
   - [Cấu trúc tổng quan](#cấu-trúc-tổng-quan-dữ-liệu-thu-thập)
   - [Schema JSON chi tiết](#schema-json-chi-tiết-dữ-liệu-thu-thập)
   - [Ví dụ dữ liệu thu thập](#ví-dụ-dữ-liệu-thu-thập)
3. [Schema kết quả đánh giá](#schema-kết-quả-đánh-giá)
   - [Cấu trúc tổng quan](#cấu-trúc-tổng-quan-kết-quả-đánh-giá)
   - [Schema JSON chi tiết](#schema-json-chi-tiết-kết-quả-đánh-giá)
   - [Ví dụ kết quả đánh giá](#ví-dụ-kết-quả-đánh-giá)
4. [Hướng dẫn sử dụng schema](#hướng-dẫn-sử-dụng-schema)
   - [Áp dụng cho Collectors](#áp-dụng-cho-collectors)
   - [Áp dụng cho Rule Engine](#áp-dụng-cho-rule-engine)
   - [Xác thực schema](#xác-thực-schema)
5. [Kết luận](#kết-luận)

## Giới thiệu

Tài liệu này mô tả chi tiết các schema JSON được sử dụng trong công cụ tự động hóa Security Audit theo CIS Benchmark. Schema này chuẩn hóa cấu trúc dữ liệu thu thập và kết quả đánh giá, đảm bảo tính nhất quán trong toàn bộ hệ thống.

## Schema dữ liệu thu thập

### Cấu trúc tổng quan dữ liệu thu thập

Schema dữ liệu thu thập bao gồm ba thành phần chính:

1. **system_info**: Thông tin về hệ thống được thu thập dữ liệu
2. **collection_info**: Thông tin về quá trình thu thập
3. **collected_data**: Dữ liệu cấu hình thu thập được, tổ chức theo loại hệ thống

### Schema JSON chi tiết dữ liệu thu thập

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CIS Collection Data Schema",
  "description": "Schema cho dữ liệu cấu hình được thu thập để đánh giá CIS benchmark",
  "type": "object",
  "required": ["system_info", "collection_info", "collected_data"],
  "properties": {
    "system_info": {
      "type": "object",
      "required": ["system_id", "system_type", "hostname", "ip_address"],
      "properties": {
        "system_id": {
          "type": "string",
          "description": "Định danh duy nhất của hệ thống"
        },
        "system_type": {
          "type": "string",
          "enum": ["os", "network", "database", "cloud"],
          "description": "Loại hệ thống được đánh giá"
        },
        "os_type": {
          "type": "string",
          "description": "Loại hệ điều hành (Windows, Linux...)"
        },
        "os_version": {
          "type": "string",
          "description": "Phiên bản hệ điều hành"
        },
        "hostname": {
          "type": "string",
          "description": "Tên máy chủ"
        },
        "ip_address": {
          "type": "string",
          "description": "Địa chỉ IP"
        },
        "fqdn": {
          "type": "string",
          "description": "Tên miền đầy đủ"
        },
        "mac_address": {
          "type": "string",
          "description": "Địa chỉ MAC"
        }
      }
    },
    "collection_info": {
      "type": "object",
      "required": ["collector_id", "timestamp", "collector_version"],
      "properties": {
        "collector_id": {
          "type": "string",
          "description": "Định danh của collector"
        },
        "collector_version": {
          "type": "string",
          "description": "Phiên bản của collector"
        },
        "timestamp": {
          "type": "string",
          "format": "date-time",
          "description": "Thời điểm thu thập dữ liệu (ISO 8601)"
        },
        "collection_method": {
          "type": "string",
          "description": "Phương thức thu thập (agent, API, SSH...)"
        },
        "collection_status": {
          "type": "string",
          "enum": ["complete", "partial", "failed"],
          "description": "Trạng thái của quá trình thu thập"
        },
        "collection_errors": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "error_code": { "type": "string" },
              "error_message": { "type": "string" },
              "control_id": { "type": "string" }
            }
          },
          "description": "Lỗi gặp phải khi thu thập"
        }
      }
    },
    "collected_data": {
      "type": "object",
      "description": "Dữ liệu cấu hình thu thập được",
      "properties": {
        "os_configuration": {
          "type": "object",
          "description": "Dữ liệu cấu hình OS",
          "properties": {
            "account_policies": { "type": "object" },
            "local_policies": { "type": "object" },
            "password_policy": { "type": "object" },
            "audit_policy": { "type": "object" },
            "system_services": { 
              "type": "array", 
              "items": { "type": "object" } 
            },
            "filesystem": { "type": "object" },
            "network_configuration": { "type": "object" },
            "kernel_parameters": { "type": "object" },
            "installed_software": { 
              "type": "array", 
              "items": { "type": "object" } 
            },
            "registry_settings": { "type": "object" }
          }
        },
        "database_configuration": {
          "type": "object",
          "description": "Dữ liệu cấu hình database",
          "properties": {
            "database_version": { "type": "string" },
            "authentication_methods": { "type": "object" },
            "network_settings": { "type": "object" },
            "permissions": { "type": "object" },
            "encryption_settings": { "type": "object" },
            "audit_settings": { "type": "object" },
            "instance_parameters": { "type": "object" },
            "users_and_roles": { 
              "type": "array", 
              "items": { "type": "object" } 
            }
          }
        },
        "raw_data": {
          "type": "object",
          "description": "Dữ liệu thô thu thập được"
        }
      }
    }
  }
}
```

### Ví dụ dữ liệu thu thập

Ví dụ cho hệ thống Ubuntu Linux:

```json
{
  "system_info": {
    "system_id": "srv-web-01",
    "system_type": "os",
    "os_type": "Linux",
    "os_version": "Ubuntu 24.04 LTS",
    "hostname": "webserver-prod-01",
    "ip_address": "192.168.1.100",
    "fqdn": "webserver-prod-01.example.com"
  },
  "collection_info": {
    "collector_id": "linux-collector",
    "collector_version": "1.0.0",
    "timestamp": "2025-03-12T10:15:30Z",
    "collection_method": "agent",
    "collection_status": "complete"
  },
  "collected_data": {
    "os_configuration": {
      "filesystem": {
        "cramfs_module": {
          "module_loaded": false,
          "module_blacklisted": true,
          "raw_command_output": "install cramfs /bin/false"
        },
        "squashfs_module": {
          "module_loaded": true,
          "module_blacklisted": false,
          "raw_command_output": ""
        }
      },
      "system_services": [
        {
          "name": "ssh",
          "status": "running",
          "enabled": true,
          "config_path": "/etc/ssh/sshd_config"
        }
      ]
    },
    "raw_data": {
      "lsmod_output": "Module Size Used by\nsquashfs 49152 0\nip_tables 28672 1 iptable_filter\n"
    }
  }
}
```

## Schema kết quả đánh giá

### Cấu trúc tổng quan kết quả đánh giá

Schema kết quả đánh giá bao gồm bốn thành phần chính:

1. **system_info**: Thông tin về hệ thống được đánh giá
2. **assessment_info**: Thông tin về quá trình đánh giá và benchmark sử dụng
3. **summary**: Tóm tắt kết quả đánh giá
4. **assessment_results**: Kết quả đánh giá chi tiết cho từng control

### Schema JSON chi tiết kết quả đánh giá

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CIS Assessment Result Schema",
  "description": "Schema cho kết quả đánh giá CIS benchmark",
  "type": "object",
  "required": ["system_info", "assessment_info", "assessment_results", "summary"],
  "properties": {
    "system_info": {
      "type": "object",
      "required": ["system_id", "system_type", "hostname"],
      "properties": {
        "system_id": {
          "type": "string",
          "description": "Định danh duy nhất của hệ thống"
        },
        "system_type": {
          "type": "string",
          "enum": ["os", "network", "database", "cloud"],
          "description": "Loại hệ thống được đánh giá"
        },
        "hostname": {
          "type": "string",
          "description": "Tên máy chủ"
        },
        "ip_address": {
          "type": "string",
          "description": "Địa chỉ IP"
        },
        "os_info": {
          "type": "object",
          "properties": {
            "os_type": { "type": "string" },
            "os_version": { "type": "string" }
          }
        },
        "db_info": {
          "type": "object",
          "properties": {
            "db_type": { "type": "string" },
            "db_version": { "type": "string" }
          }
        }
      }
    },
    "assessment_info": {
      "type": "object",
      "required": ["benchmark_id", "benchmark_version", "profile_id", "timestamp"],
      "properties": {
        "benchmark_id": {
          "type": "string",
          "description": "Định danh của CIS benchmark sử dụng"
        },
        "benchmark_version": {
          "type": "string",
          "description": "Phiên bản của CIS benchmark"
        },
        "profile_id": {
          "type": "string",
          "description": "Định danh của profile sử dụng (Level 1 Server...)"
        },
        "timestamp": {
          "type": "string",
          "format": "date-time",
          "description": "Thời điểm đánh giá"
        },
        "tool_name": {
          "type": "string",
          "description": "Tên công cụ đánh giá"
        },
        "tool_version": {
          "type": "string",
          "description": "Phiên bản công cụ đánh giá"
        }
      }
    },
    "summary": {
      "type": "object",
      "required": ["total_controls", "passed", "failed", "unknown", "not_applicable", "compliance_score"],
      "properties": {
        "total_controls": {
          "type": "integer",
          "description": "Tổng số control được đánh giá"
        },
        "passed": {
          "type": "integer",
          "description": "Số control đạt yêu cầu"
        },
        "failed": {
          "type": "integer",
          "description": "Số control không đạt yêu cầu"
        },
        "unknown": {
          "type": "integer",
          "description": "Số control có kết quả không xác định"
        },
        "not_applicable": {
          "type": "integer",
          "description": "Số control không áp dụng"
        },
        "compliance_score": {
          "type": "number",
          "minimum": 0,
          "maximum": 100,
          "description": "Điểm tuân thủ tổng thể (%)"
        },
        "section_scores": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "section_id": { "type": "string" },
              "section_title": { "type": "string" },
              "controls_count": { "type": "integer" },
              "passed_count": { "type": "integer" },
              "compliance_score": { "type": "number" }
            }
          },
          "description": "Điểm tuân thủ theo từng section"
        }
      }
    },
    "assessment_results": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["control_id", "title", "status"],
        "properties": {
          "control_id": {
            "type": "string",
            "description": "Định danh của control (1.1.1)"
          },
          "section_id": {
            "type": "string",
            "description": "Định danh của section chứa control"
          },
          "title": {
            "type": "string",
            "description": "Tiêu đề của control"
          },
          "description": {
            "type": "string",
            "description": "Mô tả của control"
          },
          "status": {
            "type": "string",
            "enum": ["pass", "fail", "unknown", "not_applicable"],
            "description": "Kết quả đánh giá"
          },
          "severity": {
            "type": "string",
            "enum": ["high", "medium", "low", "informational"],
            "description": "Mức độ nghiêm trọng"
          },
          "expected_value": {
            "type": "string",
            "description": "Giá trị mong đợi"
          },
          "actual_value": {
            "type": "string",
            "description": "Giá trị thực tế"
          },
          "remediation": {
            "type": "string",
            "description": "Hướng dẫn khắc phục"
          },
          "evidence": {
            "type": "string",
            "description": "Bằng chứng đánh giá"
          },
          "assessment_method": {
            "type": "string",
            "enum": ["automated", "manual"],
            "description": "Phương pháp đánh giá"
          },
          "cis_controls": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "version": { "type": "string" },
                "id": { "type": "string" },
                "name": { "type": "string" }
              }
            },
            "description": "Ánh xạ tới CIS Controls"
          }
        }
      }
    },
    "exceptions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "control_id": { "type": "string" },
          "exception_reason": { "type": "string" },
          "approval_info": {
            "type": "object",
            "properties": {
              "approved_by": { "type": "string" },
              "approval_date": { "type": "string", "format": "date-time" },
              "expiration_date": { "type": "string", "format": "date-time" }
            }
          }
        }
      },
      "description": "Ngoại lệ đã được phê duyệt"
    }
  }
}
```

### Ví dụ kết quả đánh giá

```json
{
  "system_info": {
    "system_id": "srv-web-01",
    "system_type": "os",
    "hostname": "webserver-prod-01",
    "ip_address": "192.168.1.100",
    "os_info": {
      "os_type": "Linux",
      "os_version": "Ubuntu 24.04 LTS"
    }
  },
  "assessment_info": {
    "benchmark_id": "CIS_Ubuntu_Linux_24.04_LTS_Benchmark",
    "benchmark_version": "1.0.0",
    "profile_id": "Level_1_Server",
    "timestamp": "2025-03-12T11:30:45Z",
    "tool_name": "CIS Audit Tool",
    "tool_version": "1.2.0"
  },
  "summary": {
    "total_controls": 185,
    "passed": 152,
    "failed": 28,
    "unknown": 3,
    "not_applicable": 2,
    "compliance_score": 82.16,
    "section_scores": [
      {
        "section_id": "1",
        "section_title": "Initial Setup",
        "controls_count": 42,
        "passed_count": 38,
        "compliance_score": 90.48
      }
    ]
  },
  "assessment_results": [
    {
      "control_id": "1.1.1.1",
      "section_id": "1.1.1",
      "title": "Ensure cramfs kernel module is not available",
      "status": "pass",
      "severity": "medium",
      "expected_value": "Module not available or blacklisted",
      "actual_value": "Module blacklisted and not loaded",
      "assessment_method": "automated",
      "evidence": "Verified module is blacklisted in /etc/modprobe.d/cramfs.conf and not loaded in kernel.",
      "cis_controls": [
        {
          "version": "8",
          "id": "4.8",
          "name": "Uninstall or Disable Unnecessary Services on Enterprise Assets and Software"
        }
      ]
    },
    {
      "control_id": "1.1.1.2",
      "section_id": "1.1.1",
      "title": "Ensure squashfs kernel module is not available",
      "status": "fail",
      "severity": "medium",
      "expected_value": "Module not available or blacklisted",
      "actual_value": "Module loaded and not blacklisted",
      "remediation": "Create a file ending in .conf with 'install squashfs /bin/false' and 'blacklist squashfs' in the /etc/modprobe.d/ directory.",
      "assessment_method": "automated",
      "evidence": "Module squashfs is currently loaded in the kernel and not blacklisted."
    }
  ],
  "exceptions": [
    {
      "control_id": "1.1.1.2",
      "exception_reason": "Required for backup system",
      "approval_info": {
        "approved_by": "Security Team",
        "approval_date": "2025-02-15T09:00:00Z",
        "expiration_date": "2025-08-15T09:00:00Z"
      }
    }
  ]
}
```

## Hướng dẫn sử dụng schema

### Áp dụng cho Collectors

Tất cả các collector phát triển cho công cụ Security Audit phải:

1. **Thu thập thông tin**: Thu thập thông tin cấu hình từ hệ thống mục tiêu (OS, Database, Network...)
2. **Chuẩn hóa dữ liệu**: Định dạng thông tin thu thập theo Schema dữ liệu thu thập
3. **Xuất dữ liệu**: Lưu dữ liệu dưới dạng JSON

#### Ví dụ implemention collector

```python
# Linux Filesystem Collector
import json
import subprocess
import platform
import socket
import datetime

def collect_cramfs_info():
    # Kiểm tra module cramfs
    module_loaded = False
    module_blacklisted = False
    
    # Kiểm tra module có được load không
    lsmod_output = subprocess.run(["lsmod"], capture_output=True, text=True).stdout
    if "cramfs" in lsmod_output:
        module_loaded = True
    
    # Kiểm tra module có bị blacklist không
    try:
        modprobe_output = subprocess.run(
            ["modprobe", "--showconfig"], 
            capture_output=True, 
            text=True
        ).stdout
        if "blacklist cramfs" in modprobe_output:
            module_blacklisted = True
    except:
        pass
    
    return {
        "module_loaded": module_loaded,
        "module_blacklisted": module_blacklisted,
        "raw_command_output": lsmod_output
    }

def collect_filesystem_data():
    return {
        "cramfs_module": collect_cramfs_info(),
        # Thêm các filesystem khác ở đây
    }

def collect_all_data():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    collection_data = {
        "system_info": {
            "system_id": hostname,
            "system_type": "os",
            "os_type": platform.system(),
            "os_version": platform.version(),
            "hostname": hostname,
            "ip_address": ip_address
        },
        "collection_info": {
            "collector_id": "linux-filesystem-collector",
            "collector_version": "1.0.0",
            "timestamp": datetime.datetime.now().isoformat(),
            "collection_method": "agent",
            "collection_status": "complete"
        },
        "collected_data": {
            "os_configuration": {
                "filesystem": collect_filesystem_data()
            }
        }
    }
    
    return collection_data

# Thu thập và lưu dữ liệu
data = collect_all_data()
with open("filesystem_data.json", "w") as f:
    json.dump(data, f, indent=2)
```

### Áp dụng cho Rule Engine

Rule Engine sẽ:

1. **Nhận dữ liệu**: Nhận dữ liệu thu thập chuẩn hóa
2. **Đánh giá dữ liệu**: So sánh với các quy tắc CIS
3. **Tạo kết quả**: Tạo báo cáo đánh giá theo Schema kết quả đánh giá

#### Ví dụ implemention rule engine

```python
# Đánh giá một control đơn giản
def evaluate_cramfs_control(data):
    try:
        # Lấy dữ liệu cramfs từ dữ liệu thu thập
        cramfs_data = data["collected_data"]["os_configuration"]["filesystem"]["cramfs_module"]
        
        # Kiểm tra theo yêu cầu CIS
        if not cramfs_data["module_loaded"] and cramfs_data["module_blacklisted"]:
            status = "pass"
            actual_value = "Module blacklisted and not loaded"
        elif not cramfs_data["module_loaded"]:
            status = "pass"
            actual_value = "Module not loaded, but not blacklisted"
        else:
            status = "fail"
            actual_value = "Module loaded and not blacklisted"
            
        # Tạo kết quả đánh giá
        result = {
            "control_id": "1.1.1.1",
            "section_id": "1.1.1",
            "title": "Ensure cramfs kernel module is not available",
            "status": status,
            "severity": "medium",
            "expected_value": "Module not available or blacklisted",
            "actual_value": actual_value,
            "assessment_method": "automated",
            "evidence": f"Module loaded: {cramfs_data['module_loaded']}, "
                        f"Module blacklisted: {cramfs_data['module_blacklisted']}",
        }
        
        if status == "fail":
            result["remediation"] = (
                "Run 'modprobe -r cramfs' to unload the module.\n"
                "Create /etc/modprobe.d/cramfs.conf with content:\n"
                "install cramfs /bin/false\n"
                "blacklist cramfs"
            )
            
        return result
    except KeyError:
        return {
            "control_id": "1.1.1.1",
            "section_id": "1.1.1",
            "title": "Ensure cramfs kernel module is not available",
            "status": "unknown",
            "severity": "medium",
            "assessment_method": "automated",
            "evidence": "Required data not found in collector output"
        }

# Tạo báo cáo đánh giá
def create_assessment_report(collected_data, benchmark_id, profile_id):
    # Đánh giá các controls
    results = []
    results.append(evaluate_cramfs_control(collected_data))
    # Thêm các đánh giá khác ở đây
    
    # Tính toán số liệu tóm tắt
    passed = sum(1 for r in results if r["status"] == "pass")
    failed = sum(1 for r in results if r["status"] == "fail")
    unknown = sum(1 for r in results if r["status"] == "unknown")
    not_applicable = sum(1 for r in results if r["status"] == "not_applicable")
    total = len(results)
    
    if total > 0:
        compliance_score = (passed / (total - not_applicable)) * 100 if (total - not_applicable) > 0 else 0
    else:
        compliance_score = 0
        
    # Tạo báo cáo
    report = {
        "system_info": collected_data["system_info"],
        "assessment_info": {
            "benchmark_id": benchmark_id,
            "benchmark_version": "1.0.0",
            "profile_id": profile_id,
            "timestamp": datetime.datetime.now().isoformat(),
            "tool_name": "CIS Rule Engine",
            "tool_version": "1.0.0"
        },
        "summary": {
            "total_controls": total,
            "passed": passed,
            "failed": failed,
            "unknown": unknown,
            "not_applicable": not_applicable,
            "compliance_score": round(compliance_score, 2)
        },
        "assessment_results": results
    }
    
    return report
```

### Xác thực schema

Sử dụng JSONSchema Validator để xác thực dữ liệu trước khi xử lý:

```python
import jsonschema
import json

# Xác thực dữ liệu thu thập
def validate_collection_data(data):
    with open('collection_schema.json', 'r') as f:
        schema = json.load(f)
    
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True, "Dữ liệu hợp lệ"
    except jsonschema.exceptions.ValidationError as e:
        return False, f"Lỗi xác thực: {e}"

# Xác thực kết quả đánh giá
def validate_assessment_result(data):
    with open('assessment_schema.json', 'r') as f:
        schema = json.load(f)
    
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True, "Dữ liệu hợp lệ"
    except jsonschema.exceptions.ValidationError as e:
        return False, f"Lỗi xác thực: {e}"
```

## Kết luận

Schema chuẩn hóa này cung cấp:

1. **Cấu trúc nhất quán** cho dữ liệu thu thập từ nhiều hệ thống khác nhau
2. **Định dạng kết quả đánh giá** thống nhất, hỗ trợ báo cáo và dashboard
3. **Khả năng xác thực** dữ liệu đầu vào và đầu ra
4. **Tính mở rộng** cho việc thêm mới các loại hệ thống và benchmark

Việc áp dụng schema này sẽ giúp:
- Chuẩn hóa quy trình thu thập và đánh giá
- Giảm thiểu lỗi do không nhất quán dữ liệu
- Đơn giản hóa phát triển các thành phần mới
- Hỗ trợ tích hợp với các hệ thống khác