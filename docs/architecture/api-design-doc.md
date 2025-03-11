# Thiết kế API và giao tiếp cho hệ thống Security Audit

## Mục lục
1. [Giới thiệu](#giới-thiệu)
2. [Nguyên tắc thiết kế API](#nguyên-tắc-thiết-kế-api)
3. [Tổng quan kiến trúc API](#tổng-quan-kiến-trúc-api)
4. [API cho thu thập dữ liệu (Collection API)](#api-cho-thu-thập-dữ-liệu-collection-api)
5. [API cho chuẩn hóa dữ liệu (Normalization API)](#api-cho-chuẩn-hóa-dữ-liệu-normalization-api)
6. [API cho đánh giá dữ liệu (Evaluation API)](#api-cho-đánh-giá-dữ-liệu-evaluation-api)
7. [API cho báo cáo kết quả (Reporting API)](#api-cho-báo-cáo-kết-quả-reporting-api)
8. [Bảo mật API](#bảo-mật-api)
9. [Xử lý lỗi và Logging](#xử-lý-lỗi-và-logging)
10. [Ví dụ và Hướng dẫn tích hợp](#ví-dụ-và-hướng-dẫn-tích-hợp)

## Giới thiệu

Tài liệu này mô tả thiết kế chi tiết API cho hệ thống tự động hóa Security Audit theo CIS Benchmark. Hệ thống được chia thành bốn tầng chính, mỗi tầng cung cấp các API riêng biệt:

1. **Tầng Thu thập (Collection Layer)**: Thu thập thông tin cấu hình từ các hệ thống mục tiêu
2. **Tầng Chuẩn hóa (Normalization Layer)**: Chuyển đổi dữ liệu thu thập thành định dạng chuẩn
3. **Tầng Đánh giá (Evaluation Layer)**: Đánh giá dữ liệu so với các tiêu chuẩn CIS
4. **Tầng Báo cáo (Reporting Layer)**: Tạo báo cáo và dashboard về kết quả đánh giá

Tất cả API được thiết kế tuân theo chuẩn RESTful, sử dụng JSON làm định dạng dữ liệu chính và hỗ trợ xác thực bằng JWT (JSON Web Token).

## Nguyên tắc thiết kế API

Các API trong hệ thống tuân theo những nguyên tắc sau:

- **RESTful**: Sử dụng phương pháp thiết kế RESTful với các phương thức HTTP tiêu chuẩn (GET, POST, PUT, DELETE)
- **Stateless**: API không lưu trữ trạng thái, mỗi yêu cầu phải chứa tất cả thông tin cần thiết
- **JSON-based**: Sử dụng JSON cho cả dữ liệu đầu vào và đầu ra
- **Versioning**: Phiên bản API được nhúng trong URL để đảm bảo khả năng tương thích
- **Validation**: Kiểm tra và xác thực dữ liệu đầu vào theo schema định nghĩa trước
- **Authentication/Authorization**: Xác thực và phân quyền truy cập API
- **Rate Limiting**: Giới hạn số lượng yêu cầu trong một khoảng thời gian
- **Documentation**: API được tài liệu hóa đầy đủ với Swagger/OpenAPI

## Tổng quan kiến trúc API

```mermaid
graph TD
    C[Client] --> |1. Thu thập| CA[Collection API]
    C --> |2. Chuẩn hóa| NA[Normalization API]
    C --> |3. Đánh giá| EA[Evaluation API]
    C --> |4. Báo cáo| RA[Reporting API]
    
    subgraph "Collection Layer"
        CA --> WC[Windows Collector]
        CA --> LC[Linux Collector]
        CA --> DC[Database Collector]
        CA --> NC[Network Collector]
    end
    
    subgraph "Normalization Layer"
        NA --> NE[Normalization Engine]
        NE --> SE[Schema Validator]
    end
    
    subgraph "Evaluation Layer"
        EA --> RE[Rule Engine]
        RE --> CIS[(CIS Database)]
    end
    
    subgraph "Reporting Layer"
        RA --> RG[Report Generator]
        RA --> DS[Dashboard]
    end
```

Luồng xử lý chính:
1. Client gửi yêu cầu thu thập dữ liệu từ hệ thống mục tiêu
2. Dữ liệu thu thập được chuẩn hóa theo schema chung
3. Dữ liệu chuẩn hóa được đánh giá so với CIS Benchmark
4. Kết quả đánh giá được tổng hợp và xuất báo cáo

## API cho thu thập dữ liệu (Collection API)

### Tổng quan API thu thập dữ liệu

| Endpoint | Method | Mô tả |
|----------|--------|-------|
| `/api/v1/collection/systems` | GET | Lấy danh sách hệ thống |
| `/api/v1/collection/systems` | POST | Thêm hệ thống mới |
| `/api/v1/collection/systems/{system_id}` | GET | Xem thông tin hệ thống |
| `/api/v1/collection/systems/{system_id}` | PUT | Cập nhật thông tin hệ thống |
| `/api/v1/collection/systems/{system_id}` | DELETE | Xóa hệ thống |
| `/api/v1/collection/systems/{system_id}/collect` | POST | Bắt đầu thu thập dữ liệu |
| `/api/v1/collection/jobs` | GET | Lấy danh sách công việc thu thập |
| `/api/v1/collection/jobs/{job_id}` | GET | Xem trạng thái công việc thu thập |
| `/api/v1/collection/jobs/{job_id}/data` | GET | Lấy dữ liệu thu thập |

### Chi tiết API thu thập dữ liệu

#### 1. Lấy danh sách hệ thống

**Endpoint**: `/api/v1/collection/systems`  
**Method**: GET  
**Query Parameters**:
- `type` (optional): Lọc theo loại hệ thống (os, database, network, cloud)
- `page` (optional): Trang kết quả
- `limit` (optional): Số lượng kết quả mỗi trang

**Response**:
```json
{
  "total": 25,
  "page": 1,
  "limit": 10,
  "systems": [
    {
      "system_id": "srv-web-01",
      "system_type": "os",
      "hostname": "webserver-prod-01",
      "ip_address": "192.168.1.100",
      "os_info": {
        "os_type": "Linux",
        "os_version": "Ubuntu 24.04 LTS"
      },
      "last_collection": "2025-03-10T15:30:45Z",
      "status": "active"
    },
    ...
  ]
}
```

**Status Codes**:
- 200 OK: Thành công
- 400 Bad Request: Tham số không hợp lệ
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập

#### 2. Thêm hệ thống mới

**Endpoint**: `/api/v1/collection/systems`  
**Method**: POST  
**Body**:
```json
{
  "hostname": "webserver-prod-02",
  "ip_address": "192.168.1.101",
  "system_type": "os",
  "os_type": "Linux",
  "os_version": "Ubuntu 24.04 LTS",
  "connection_info": {
    "method": "ssh",
    "port": 22,
    "username": "collector_user",
    "authentication_type": "key",
    "key_file": "path/to/key.pem"
  }
}
```

**Response**:
```json
{
  "system_id": "srv-web-02",
  "hostname": "webserver-prod-02",
  "ip_address": "192.168.1.101",
  "system_type": "os",
  "os_info": {
    "os_type": "Linux",
    "os_version": "Ubuntu 24.04 LTS"
  },
  "status": "active",
  "creation_date": "2025-03-12T10:15:30Z"
}
```

**Status Codes**:
- 201 Created: Thành công
- 400 Bad Request: Dữ liệu không hợp lệ
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập
- 409 Conflict: Hệ thống đã tồn tại

#### 3. Bắt đầu thu thập dữ liệu

**Endpoint**: `/api/v1/collection/systems/{system_id}/collect`  
**Method**: POST  
**Path Parameters**:
- `system_id`: ID của hệ thống cần thu thập

**Body**:
```json
{
  "collector_type": "linux-collector",
  "collector_version": "1.0.0",
  "collection_params": {
    "include_sections": ["filesystem", "services", "network", "users"],
    "include_raw_data": true
  }
}
```

**Response**:
```json
{
  "job_id": "col-job-12345",
  "system_id": "srv-web-01",
  "status": "started",
  "start_time": "2025-03-12T10:30:00Z",
  "estimated_completion": "2025-03-12T10:35:00Z"
}
```

**Status Codes**:
- 202 Accepted: Công việc đã được bắt đầu
- 400 Bad Request: Tham số không hợp lệ
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập
- 404 Not Found: Hệ thống không tồn tại
- 409 Conflict: Đang có công việc khác đang chạy

#### 4. Lấy dữ liệu thu thập

**Endpoint**: `/api/v1/collection/jobs/{job_id}/data`  
**Method**: GET  
**Path Parameters**:
- `job_id`: ID của công việc thu thập

**Response**:
```json
{
  "job_id": "col-job-12345",
  "system_id": "srv-web-01",
  "collection_timestamp": "2025-03-12T10:32:15Z",
  "collection_data": {
    "system_info": {
      "system_id": "srv-web-01",
      "system_type": "os",
      "hostname": "webserver-prod-01",
      "ip_address": "192.168.1.100",
      "os_type": "Linux",
      "os_version": "Ubuntu 24.04 LTS"
    },
    "collection_info": {
      "collector_id": "linux-collector",
      "collector_version": "1.0.0",
      "timestamp": "2025-03-12T10:32:15Z",
      "collection_status": "complete"
    },
    "collected_data": {
      "os_configuration": {
        "filesystem": { ... },
        "services": [ ... ],
        "network": { ... },
        "users": [ ... ]
      }
    }
  }
}
```

**Status Codes**:
- 200 OK: Thành công
- 202 Accepted: Công việc đang chạy, dữ liệu chưa sẵn sàng
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập
- 404 Not Found: Công việc không tồn tại

## API cho chuẩn hóa dữ liệu (Normalization API)

### Tổng quan API chuẩn hóa dữ liệu

| Endpoint | Method | Mô tả |
|----------|--------|-------|
| `/api/v1/normalization/normalize` | POST | Chuẩn hóa dữ liệu thu thập |
| `/api/v1/normalization/validate` | POST | Xác thực dữ liệu so với schema |
| `/api/v1/normalization/schema` | GET | Lấy schema chuẩn hóa hiện tại |
| `/api/v1/normalization/jobs` | GET | Lấy danh sách công việc chuẩn hóa |
| `/api/v1/normalization/jobs/{job_id}` | GET | Xem trạng thái công việc chuẩn hóa |
| `/api/v1/normalization/jobs/{job_id}/data` | GET | Lấy dữ liệu đã chuẩn hóa |

### Chi tiết API chuẩn hóa dữ liệu

#### 1. Chuẩn hóa dữ liệu thu thập

**Endpoint**: `/api/v1/normalization/normalize`  
**Method**: POST  
**Body**:
- Dữ liệu thu thập từ Collection API hoặc ID công việc thu thập

```json
{
  "collection_job_id": "col-job-12345"
}
```

hoặc

```json
{
  "raw_data": {
    "system_info": { ... },
    "collection_info": { ... },
    "collected_data": { ... }
  }
}
```

**Response**:
```json
{
  "normalization_job_id": "norm-job-67890",
  "status": "processing",
  "start_time": "2025-03-12T10:40:00Z",
  "estimated_completion": "2025-03-12T10:41:00Z"
}
```

**Status Codes**:
- 202 Accepted: Công việc đã được bắt đầu
- 400 Bad Request: Dữ liệu không hợp lệ
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập
- 404 Not Found: Công việc thu thập không tồn tại

#### 2. Xác thực dữ liệu so với schema

**Endpoint**: `/api/v1/normalization/validate`  
**Method**: POST  
**Body**:
```json
{
  "data": {
    "system_info": { ... },
    "collection_info": { ... },
    "collected_data": { ... }
  },
  "schema_type": "collection_data"
}
```

**Response**:
```json
{
  "valid": true,
  "errors": []
}
```

hoặc

```json
{
  "valid": false,
  "errors": [
    {
      "path": "$.system_info.system_type",
      "message": "Required property missing",
      "schema_path": "properties/system_info/required"
    },
    {
      "path": "$.collected_data.os_configuration.filesystem",
      "message": "Invalid type. Expected object but got array",
      "schema_path": "properties/collected_data/properties/os_configuration/properties/filesystem/type"
    }
  ]
}
```

**Status Codes**:
- 200 OK: Xác thực thành công
- 400 Bad Request: Dữ liệu không hợp lệ
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập

#### 3. Lấy dữ liệu đã chuẩn hóa

**Endpoint**: `/api/v1/normalization/jobs/{job_id}/data`  
**Method**: GET  
**Path Parameters**:
- `job_id`: ID của công việc chuẩn hóa

**Response**:
```json
{
  "job_id": "norm-job-67890",
  "system_id": "srv-web-01",
  "normalization_timestamp": "2025-03-12T10:40:45Z",
  "normalized_data": {
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
    "collection_info": { ... },
    "check_items": [
      {
        "control_id": "1.1.1.1",
        "title": "Ensure cramfs kernel module is not available",
        "current_value": "Module not loaded, blacklisted",
        "expected_value": "Module not loaded and blacklisted",
        "raw_data": {
          "module_loaded": false,
          "module_blacklisted": true
        }
      },
      {
        "control_id": "1.1.1.2",
        "title": "Ensure squashfs kernel module is not available",
        "current_value": "Module loaded, not blacklisted",
        "expected_value": "Module not loaded and blacklisted",
        "raw_data": {
          "module_loaded": true,
          "module_blacklisted": false
        }
      },
      // Các control khác...
    ]
  }
}
```

**Status Codes**:
- 200 OK: Thành công
- 202 Accepted: Công việc đang chạy, dữ liệu chưa sẵn sàng
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập
- 404 Not Found: Công việc không tồn tại

## API cho đánh giá dữ liệu (Evaluation API)

### Tổng quan API đánh giá dữ liệu

| Endpoint | Method | Mô tả |
|----------|--------|-------|
| `/api/v1/evaluation/benchmarks` | GET | Lấy danh sách CIS Benchmark có sẵn |
| `/api/v1/evaluation/benchmarks/{benchmark_id}` | GET | Xem thông tin chi tiết benchmark |
| `/api/v1/evaluation/benchmarks/{benchmark_id}/profiles` | GET | Lấy danh sách profile trong benchmark |
| `/api/v1/evaluation/evaluate` | POST | Đánh giá dữ liệu chuẩn hóa theo benchmark |
| `/api/v1/evaluation/jobs` | GET | Lấy danh sách công việc đánh giá |
| `/api/v1/evaluation/jobs/{job_id}` | GET | Xem trạng thái công việc đánh giá |
| `/api/v1/evaluation/jobs/{job_id}/results` | GET | Lấy kết quả đánh giá |
| `/api/v1/evaluation/exceptions` | GET | Lấy danh sách ngoại lệ đánh giá |
| `/api/v1/evaluation/exceptions` | POST | Thêm ngoại lệ đánh giá mới |

### Chi tiết API đánh giá dữ liệu

#### 1. Lấy danh sách CIS Benchmark

**Endpoint**: `/api/v1/evaluation/benchmarks`  
**Method**: GET  
**Query Parameters**:
- `platform_type` (optional): Lọc theo loại nền tảng (windows, ubuntu, mysql...)
- `page` (optional): Trang kết quả
- `limit` (optional): Số lượng kết quả mỗi trang

**Response**:
```json
{
  "total": 8,
  "page": 1,
  "limit": 10,
  "benchmarks": [
    {
      "benchmark_id": "CIS_Ubuntu_Linux_24.04_LTS_Benchmark",
      "name": "CIS Ubuntu Linux 24.04 LTS Benchmark",
      "version": "1.0.0",
      "publication_date": "2025-01-15",
      "platform_type": "ubuntu",
      "profiles": ["Level_1_Server", "Level_2_Server", "Level_1_Workstation", "Level_2_Workstation"]
    },
    {
      "benchmark_id": "CIS_Windows_Server_2022_Benchmark",
      "name": "CIS Microsoft Windows Server 2022 Benchmark",
      "version": "1.0.0",
      "publication_date": "2024-11-20",
      "platform_type": "windows",
      "profiles": ["Level_1_DC", "Level_2_DC", "Level_1_MS", "Level_2_MS", "NextGen_Windows_Security"]
    },
    // Các benchmark khác...
  ]
}
```

**Status Codes**:
- 200 OK: Thành công
- 400 Bad Request: Tham số không hợp lệ
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập

#### 2. Đánh giá dữ liệu chuẩn hóa

**Endpoint**: `/api/v1/evaluation/evaluate`  
**Method**: POST  
**Body**:
```json
{
  "normalization_job_id": "norm-job-67890",
  "benchmark_id": "CIS_Ubuntu_Linux_24.04_LTS_Benchmark",
  "benchmark_version": "1.0.0",
  "profile_id": "Level_1_Server",
  "include_exceptions": true
}
```

hoặc

```json
{
  "normalized_data": {
    "system_info": { ... },
    "collection_info": { ... },
    "check_items": [ ... ]
  },
  "benchmark_id": "CIS_Ubuntu_Linux_24.04_LTS_Benchmark",
  "benchmark_version": "1.0.0",
  "profile_id": "Level_1_Server",
  "include_exceptions": true
}
```

**Response**:
```json
{
  "evaluation_job_id": "eval-job-24680",
  "status": "processing",
  "start_time": "2025-03-12T10:45:00Z",
  "estimated_completion": "2025-03-12T10:47:00Z"
}
```

**Status Codes**:
- 202 Accepted: Công việc đã được bắt đầu
- 400 Bad Request: Tham số không hợp lệ
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập
- 404 Not Found: Công việc chuẩn hóa hoặc benchmark không tồn tại

#### 3. Lấy kết quả đánh giá

**Endpoint**: `/api/v1/evaluation/jobs/{job_id}/results`  
**Method**: GET  
**Path Parameters**:
- `job_id`: ID của công việc đánh giá

**Response**:
```json
{
  "job_id": "eval-job-24680",
  "system_id": "srv-web-01",
  "benchmark_id": "CIS_Ubuntu_Linux_24.04_LTS_Benchmark",
  "benchmark_version": "1.0.0",
  "profile_id": "Level_1_Server",
  "evaluation_timestamp": "2025-03-12T10:46:30Z",
  "assessment_results": {
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
      "timestamp": "2025-03-12T10:46:30Z",
      "tool_name": "CIS Rule Engine",
      "tool_version": "1.0.0"
    },
    "summary": {
      "total_controls": 185,
      "passed": 152,
      "failed": 28,
      "unknown": 3,
      "not_applicable": 2,
      "compliance_score": 82.16,
      "section_scores": [ ... ]
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
        "evidence": "Verified module is blacklisted in /etc/modprobe.d/cramfs.conf and not loaded in kernel."
      },
      {
        "control_id": "1.1.1.2",
        "section_id": "1.1.1",
        "title": "Ensure squashfs kernel module is not available",
        "status": "fail",
        "severity": "medium",
        "expected_value": "Module not available or blacklisted",
        "actual_value": "Module loaded and not blacklisted",
        "remediation": "Create a file ending in .conf with 'install squashfs /bin/false' and 'blacklist squashfs' in the /etc/modprobe.d/ directory."
      },
      // Các control khác...
    ],
    "exceptions": [
      {
        "control_id": "1.1.1.2",
        "exception_reason": "Required for backup system",
        "exception_status": "approved",
        "approval_info": {
          "approved_by": "Security Team",
          "approval_date": "2025-02-15T09:00:00Z",
          "expiration_date": "2025-08-15T09:00:00Z"
        }
      }
    ]
  }
}
```

**Status Codes**:
- 200 OK: Thành công
- 202 Accepted: Công việc đang chạy, kết quả chưa sẵn sàng
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập
- 404 Not Found: Công việc không tồn tại

#### 4. Thêm ngoại lệ đánh giá

**Endpoint**: `/api/v1/evaluation/exceptions`  
**Method**: POST  
**Body**:
```json
{
  "system_id": "srv-web-01",
  "benchmark_id": "CIS_Ubuntu_Linux_24.04_LTS_Benchmark",
  "control_id": "1.1.1.2",
  "exception_reason": "Required for backup system",
  "expiration_date": "2025-08-15T09:00:00Z",
  "requested_by": "John Doe",
  "justification": "The squashfs module is needed for our backup solution which uses squashfs compressed images."
}
```

**Response**:
```json
{
  "exception_id": "exc-12345",
  "system_id": "srv-web-01",
  "benchmark_id": "CIS_Ubuntu_Linux_24.04_LTS_Benchmark",
  "control_id": "1.1.1.2",
  "exception_reason": "Required for backup system",
  "exception_status": "pending",
  "requested_by": "John Doe",
  "requested_date": "2025-03-12T11:00:00Z",
  "expiration_date": "2025-08-15T09:00:00Z"
}
```

**Status Codes**:
- 201 Created: Ngoại lệ đã được tạo
- 400 Bad Request: Dữ liệu không hợp lệ
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập
- 404 Not Found: Hệ thống hoặc control không tồn tại
- 409 Conflict: Ngoại lệ đã tồn tại

## API cho báo cáo kết quả (Reporting API)

### Tổng quan API báo cáo kết quả

| Endpoint | Method | Mô tả |
|----------|--------|-------|
| `/api/v1/reporting/reports` | GET | Lấy danh sách báo cáo |
| `/api/v1/reporting/reports` | POST | Tạo báo cáo mới |
| `/api/v1/reporting/reports/{report_id}` | GET | Xem báo cáo chi tiết |
| `/api/v1/reporting/reports/{report_id}/export` | GET | Xuất báo cáo theo định dạng |
| `/api/v1/reporting/dashboard` | GET | Lấy dữ liệu tổng quan dashboard |
| `/api/v1/reporting/metrics` | GET | Lấy metrics tổng hợp |
| `/api/v1/reporting/trends` | GET | Phân tích xu hướng theo thời gian |
| `/api/v1/reporting/compliance` | GET | Báo cáo tuân thủ theo control |

### Chi tiết API báo cáo kết quả

#### 1. Lấy danh sách báo cáo

**Endpoint**: `/api/v1/reporting/reports`  
**Method**: GET  
**Query Parameters**:
- `system_id` (optional): Lọc theo ID hệ thống
- `benchmark_id` (optional): Lọc theo ID benchmark
- `date_from` (optional): Lọc theo ngày bắt đầu (ISO 8601)
- `date_to` (optional): Lọc theo ngày kết thúc (ISO 8601)
- `page` (optional): Trang kết quả
- `limit` (optional): Số lượng kết quả mỗi trang

**Response**:
```json
{
  "total": 35,
  "page": 1,
  "limit": 10,
  "reports": [
    {
      "report_id": "rep-12345",
      "system_id": "srv-web-01",
      "system_name": "webserver-prod-01",
      "benchmark_id": "CIS_Ubuntu_Linux_24.04_LTS_Benchmark",
      "profile_id": "Level_1_Server",
      "creation_date": "2025-03-12T11:30:00Z",
      "compliance_score": 82.16,
      "status": "completed"
    },
    {
      "report_id": "rep-12346",
      "system_id": "srv-db-01",
      "system_name": "database-prod-01",
      "benchmark_id": "CIS_MySQL_Enterprise_8.4_Benchmark",
      "profile_id": "Level_1_MySQL_RDBMS",
      "creation_date": "2025-03-12T10:45:00Z",
      "compliance_score": 91.30,
      "status": "completed"
    },
    // Các báo cáo khác...
  ]
}
```

**Status Codes**:
- 200 OK: Thành công
- 400 Bad Request: Tham số không hợp lệ
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập

#### 2. Tạo báo cáo mới

**Endpoint**: `/api/v1/reporting/reports`  
**Method**: POST  
**Body**:
```json
{
  "evaluation_job_id": "eval-job-24680",
  "report_name": "Monthly Security Audit - Web Server",
  "report_description": "Regular monthly audit of production web server",
  "report_format": "pdf",
  "include_sections": ["summary", "failed_controls", "remediation"],
  "include_trending": true,
  "include_exceptions": true
}
```

**Response**:
```json
{
  "report_id": "rep-12347",
  "evaluation_job_id": "eval-job-24680",
  "report_name": "Monthly Security Audit - Web Server",
  "creation_date": "2025-03-12T12:00:00Z",
  "status": "generating",
  "estimated_completion": "2025-03-12T12:01:30Z"
}
```

**Status Codes**:
- 202 Accepted: Báo cáo đang được tạo
- 400 Bad Request: Dữ liệu không hợp lệ
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập
- 404 Not Found: Công việc đánh giá không tồn tại

#### 3. Xuất báo cáo theo định dạng

**Endpoint**: `/api/v1/reporting/reports/{report_id}/export`  
**Method**: GET  
**Path Parameters**:
- `report_id`: ID của báo cáo

**Query Parameters**:
- `format` (optional): Định dạng xuất (pdf, html, csv, json), mặc định là pdf

**Response**:
- Nếu format là `pdf` hoặc `html`: Trả về file với Content-Type tương ứng
- Nếu format là `csv` hoặc `json`: Trả về dữ liệu theo định dạng tương ứng

**Status Codes**:
- 200 OK: Thành công
- 400 Bad Request: Định dạng không hợp lệ
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập
- 404 Not Found: Báo cáo không tồn tại

#### 4. Lấy dữ liệu tổng quan dashboard

**Endpoint**: `/api/v1/reporting/dashboard`  
**Method**: GET  
**Query Parameters**:
- `time_period` (optional): Khoảng thời gian (today, week, month, quarter, year), mặc định là month
- `system_group` (optional): Nhóm hệ thống để lọc

**Response**:
```json
{
  "time_period": "month",
  "summary": {
    "total_systems": 48,
    "systems_assessed": 45,
    "average_compliance": 84.3,
    "risk_levels": {
      "high": 5,
      "medium": 12,
      "low": 31
    }
  },
  "compliance_by_benchmark": [
    {
      "benchmark_id": "CIS_Ubuntu_Linux_24.04_LTS_Benchmark",
      "systems_count": 25,
      "average_compliance": 87.5
    },
    {
      "benchmark_id": "CIS_Windows_Server_2022_Benchmark",
      "systems_count": 15,
      "average_compliance": 82.1
    },
    {
      "benchmark_id": "CIS_MySQL_Enterprise_8.4_Benchmark",
      "systems_count": 8,
      "average_compliance": 91.4
    }
  ],
  "top_failing_controls": [
    {
      "control_id": "5.2.8",
      "title": "Ensure password reuse is limited",
      "benchmark_id": "CIS_Windows_Server_2022_Benchmark",
      "failure_count": 12,
      "affected_systems": ["srv-win-01", "srv-win-03", "..."]
    },
    // Các control khác...
  ],
  "compliance_trends": {
    "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "data": [78.5, 80.1, 82.3, 81.9, 83.2, 82.8, 83.6, 84.1, 84.3]
  }
}
```

**Status Codes**:
- 200 OK: Thành công
- 400 Bad Request: Tham số không hợp lệ
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập

#### 5. Phân tích xu hướng theo thời gian

**Endpoint**: `/api/v1/reporting/trends`  
**Method**: GET  
**Query Parameters**:
- `system_id` (optional): ID hệ thống cần phân tích
- `benchmark_id` (optional): ID benchmark cần phân tích
- `control_id` (optional): ID control cần phân tích
- `period` (optional): Khoảng thời gian (day, week, month), mặc định là month
- `range` (optional): Số lượng điểm dữ liệu, mặc định là 12

**Response**:
```json
{
  "system_id": "srv-web-01",
  "benchmark_id": "CIS_Ubuntu_Linux_24.04_LTS_Benchmark",
  "period": "month",
  "range": 12,
  "trends": {
    "overall_compliance": {
      "labels": ["2024-04", "2024-05", "2024-06", "2024-07", "2024-08", "2024-09", "2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03"],
      "data": [78.5, 78.5, 80.1, 82.3, 81.9, 83.2, 82.8, 83.6, 84.1, 84.3, 83.9, 82.2]
    },
    "failed_controls": {
      "labels": ["2024-04", "2024-05", "2024-06", "2024-07", "2024-08", "2024-09", "2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03"],
      "data": [41, 41, 38, 35, 36, 33, 34, 32, 31, 30, 31, 33]
    },
    "section_compliance": {
      "Initial Setup": {
        "labels": ["2024-04", "2024-05", "2024-06", "2024-07", "2024-08", "2024-09", "2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03"],
        "data": [85.2, 85.2, 86.4, 87.1, 87.3, 88.5, 88.1, 89.2, 89.7, 90.1, 90.3, 90.5]
      },
      "Services": {
        "labels": ["2024-04", "2024-05", "2024-06", "2024-07", "2024-08", "2024-09", "2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03"],
        "data": [72.1, 72.1, 74.5, 76.8, 75.2, 78.1, 77.5, 78.3, 79.1, 79.5, 78.2, 76.4]
      }
      // Các section khác...
    }
  }
}
```

**Status Codes**:
- 200 OK: Thành công
- 400 Bad Request: Tham số không hợp lệ
- 401 Unauthorized: Chưa xác thực
- 403 Forbidden: Không có quyền truy cập
- 404 Not Found: Hệ thống hoặc benchmark không tồn tại

## Bảo mật API

### Xác thực và Ủy quyền

Tất cả API trong hệ thống đều yêu cầu xác thực qua JSON Web Token (JWT) và kiểm soát quyền truy cập dựa trên vai trò:

#### 1. Xác thực API

**Endpoint**: `/api/v1/auth/token`  
**Method**: POST  
**Body**:
```json
{
  "username": "admin",
  "password": "secure_password"
}
```

**Response**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

Sau khi nhận được token, client cần gửi token trong header của mỗi request:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

#### 2. Làm mới token

**Endpoint**: `/api/v1/auth/refresh`  
**Method**: POST  
**Body**:
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Quản lý quyền truy cập

Hệ thống cung cấp các vai trò và quyền sau:

| Vai trò | Mô tả | Quyền truy cập |
|---------|-------|---------------|
| admin | Quản trị viên hệ thống | Toàn quyền truy cập tất cả API |
| collector | Quản lý thu thập dữ liệu | Collection API |
| evaluator | Quản lý đánh giá | Normalization API, Evaluation API (đọc) |
| auditor | Người đánh giá | Evaluation API, Reporting API (đọc) |
| reporter | Người tạo báo cáo | Reporting API |

### Giới hạn tốc độ truy cập

Để tránh tình trạng quá tải, API sẽ giới hạn số lượng yêu cầu trong một khoảng thời gian nhất định:

- API công khai: 60 request/phút
- API thu thập và chuẩn hóa: 120 request/phút
- API đánh giá: 100 request/phút
- API báo cáo: 60 request/phút

Khi vượt quá giới hạn, API sẽ trả về mã lỗi 429 Too Many Requests với header:
```
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1584022800
```

## Xử lý lỗi và Logging

### Định dạng lỗi

Tất cả các lỗi API đều được trả về theo định dạng sau:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "benchmark_id",
        "message": "Benchmark ID is required"
      }
    ],
    "request_id": "req-abcd1234"
  }
}
```

Các mã lỗi phổ biến:
- `AUTHENTICATION_ERROR`: Lỗi xác thực
- `AUTHORIZATION_ERROR`: Không có quyền truy cập
- `VALIDATION_ERROR`: Dữ liệu đầu vào không hợp lệ
- `RESOURCE_NOT_FOUND`: Tài nguyên không tồn tại
- `RATE_LIMIT_EXCEEDED`: Vượt quá giới hạn tốc độ
- `INTERNAL_ERROR`: Lỗi hệ thống
- `SERVICE_UNAVAILABLE`: Dịch vụ không khả dụng

### Logging

Mọi yêu cầu API đều được ghi log với các thông tin:
- Thời gian yêu cầu
- URL yêu cầu
- Phương thức HTTP
- IP người dùng
- ID người dùng (nếu đã xác thực)
- Mã phản hồi
- Thời gian xử lý
- Request ID

Một Request ID duy nhất được tạo cho mỗi yêu cầu và trả về trong header phản hồi:
```
X-Request-ID: req-abcd1234
```

## Ví dụ và Hướng dẫn tích hợp

### Luồng xử lý hoàn chỉnh

Dưới đây là một ví dụ về luồng xử lý hoàn chỉnh từ thu thập dữ liệu đến báo cáo:

```mermaid
sequenceDiagram
    participant C as Client
    participant CA as Collection API
    participant NA as Normalization API
    participant EA as Evaluation API
    participant RA as Reporting API
    
    C ->> CA: POST /api/v1/collection/systems/{system_id}/collect
    CA -->> C: Return job_id
    
    C ->> CA: GET /api/v1/collection/jobs/{job_id}
    CA -->> C: Job status = completed
    
    C ->> CA: GET /api/v1/collection/jobs/{job_id}/data
    CA -->> C: Return collected data
    
    C ->> NA: POST /api/v1/normalization/normalize
    NA -->> C: Return normalization_job_id
    
    C ->> NA: GET /api/v1/normalization/jobs/{job_id}/data
    NA -->> C: Return normalized data
    
    C ->> EA: POST /api/v1/evaluation/evaluate
    EA -->> C: Return evaluation_job_id
    
    C ->> EA: GET /api/v1/evaluation/jobs/{job_id}/results
    EA -->> C: Return evaluation results
    
    C ->> RA: POST /api/v1/reporting/reports
    RA -->> C: Return report_id
    
    C ->> RA: GET /api/v1/reporting/reports/{report_id}
    RA -->> C: Return report data
    
    C ->> RA: GET /api/v1/reporting/reports/{report_id}/export?format=pdf
    RA -->> C: Return PDF report
```

### Ví dụ yêu cầu cURL

#### 1. Xác thực và lấy token

```bash
curl -X POST https://api.security-audit.example.com/api/v1/auth/token \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "secure_password"}'
```

#### 2. Thu thập dữ liệu

```bash
curl -X POST https://api.security-audit.example.com/api/v1/collection/systems/srv-web-01/collect \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -d '{
    "collector_type": "linux-collector",
    "collector_version": "1.0.0",
    "collection_params": {
      "include_sections": ["filesystem", "services", "network", "users"],
      "include_raw_data": true
    }
  }'
```

#### 3. Lấy kết quả đánh giá

```bash
curl -X GET https://api.security-audit.example.com/api/v1/evaluation/jobs/eval-job-24680/results \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

#### 4. Xuất báo cáo dạng PDF

```bash
curl -X GET https://api.security-audit.example.com/api/v1/reporting/reports/rep-12345/export?format=pdf \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -o report.pdf
```

### Thư viện client SDK

Dưới đây là một ví dụ sử dụng thư viện SDK Python:

```python
from security_audit_sdk import SecurityAuditClient

# Khởi tạo client
client = SecurityAuditClient(
    api_url="https://api.security-audit.example.com",
    username="admin",
    password="secure_password"
)

# Thu thập dữ liệu
collection_job = client.collection.collect_system_data(
    system_id="srv-web-01",
    collector_type="linux-collector",
    collection_params={
        "include_sections": ["filesystem", "services", "network", "users"]
    }
)

# Chờ thu thập hoàn tất
client.collection.wait_for_job(collection_job["job_id"])

# Chuẩn hóa dữ liệu
normalization_job = client.normalization.normalize_data(
    collection_job_id=collection_job["job_id"]
)

# Chờ chuẩn hóa hoàn tất
client.normalization.wait_for_job(normalization_job["normalization_job_id"])

# Đánh giá dữ liệu
evaluation_job = client.evaluation.evaluate_data(
    normalization_job_id=normalization_job["normalization_job_id"],
    benchmark_id="CIS_Ubuntu_Linux_24.04_LTS_Benchmark",
    profile_id="Level_1_Server"
)

# Chờ đánh giá hoàn tất
client.evaluation.wait_for_job(evaluation_job["evaluation_job_id"])

# Tạo báo cáo
report = client.reporting.create_report(
    evaluation_job_id=evaluation_job["evaluation_job_id"],
    report_name="Monthly Security Audit",
    report_format="pdf"
)

# Tải báo cáo
client.reporting.download_report(
    report_id=report["report_id"],
    format="pdf",
    output_path="./security_audit_report.pdf"
)

# Lấy dữ liệu dashboard
dashboard_data = client.reporting.get_dashboard(time_period="month")
print(f"Tổng hợp: {dashboard_data['summary']}")
print(f"Số hệ thống: {dashboard_data['summary']['total_systems']}")
print(f"Độ tuân thủ trung bình: {dashboard_data['summary']['average_compliance']}%")
```

