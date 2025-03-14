# Schema JSON cho dữ liệu thu thập (Collector Output)

## Mô tả tổng quan

Schema JSON này định nghĩa cấu trúc dữ liệu chuẩn cho output từ các collector scripts (Windows, Linux, MySQL). Mục đích chính là đảm bảo tính nhất quán của dữ liệu thu thập từ các hệ thống khác nhau, để có thể dễ dàng nhập vào ứng dụng phân tích và đối chiếu với các CIS Benchmark.

## Cấu trúc chính

Schema gồm 3 phần chính:

1. **system_info**: Thông tin định danh về hệ thống được thu thập
2. **collection_info**: Metadata về quá trình thu thập
3. **collected_data**: Dữ liệu thực tế được thu thập, phân cấp theo module

## Yêu cầu chi tiết

### 1. `system_info` (bắt buộc)

Chứa thông tin định danh của hệ thống:

```json
{
  "hostname": "string", // tên máy chủ (bắt buộc)
  "ip_address": "string", // địa chỉ IP chính (bắt buộc)
  "collector_type": "string", // loại collector: "windows", "linux", "mysql" (bắt buộc)
  "os_info": { // thông tin OS (tùy thuộc vào collector_type)
    "name": "string", // tên OS (bắt buộc)
    "version": "string", // phiên bản OS (bắt buộc)
    "kernel": "string", // phiên bản kernel (Linux)
    "architecture": "string", // kiến trúc: x86, x64, arm64, ... (bắt buộc)
    "build_number": "string", // build number (Windows)
    "edition": "string" // phiên bản: Home, Pro, Enterprise, ... (Windows)
  },
  "db_info": { // chỉ cho collector_type="mysql"
    "version": "string", // phiên bản MySQL
    "edition": "string" // Enterprise, Community, ...
  }
}
```

### 2. `collection_info` (bắt buộc)

Chứa metadata về quá trình thu thập:

```json
{
  "collector_version": "string", // phiên bản collector script (bắt buộc)
  "collection_date": "string", // thời điểm thu thập, định dạng ISO 8601 (bắt buộc)
  "collector_script": "string", // tên script sử dụng để thu thập (bắt buộc)
  "collection_parameters": { // tham số thu thập (tùy chọn)
    "include_all_modules": "boolean", // có thu thập tất cả module hay không
    "skip_network_scan": "boolean", // có bỏ qua scan mạng hay không
    // các tham số khác tùy vào collector
  },
  "collection_duration": "number", // thời gian thu thập (giây)
  "collector_user": "string", // user thực hiện thu thập (tùy chọn)
  "errors": [ // danh sách lỗi gặp phải (nếu có)
    {
      "module": "string", // module gặp lỗi
      "error_message": "string", // thông báo lỗi
      "error_time": "string" // thời điểm lỗi, định dạng ISO 8601
    }
  ]
}
```

### 3. `collected_data` (bắt buộc)

Chứa dữ liệu thực tế được thu thập, cấu trúc khác nhau tùy theo `collector_type`:

#### 3.1 Modules chung cho Linux và Windows:

```json
{
  "filesystem": {
    "partitions": [
      {
        "mount_point": "string", // điểm mount (Linux) hoặc drive letter (Windows)
        "device": "string", // thiết bị (Linux) hoặc volume ID (Windows)
        "fs_type": "string", // kiểu filesystem: ext4, ntfs, ...
        "mount_options": "string", // options khi mount
        "total_size_kb": "number", // tổng dung lượng (KB)
        "used_size_kb": "number", // dung lượng đã sử dụng (KB)
        "available_size_kb": "number" // dung lượng còn trống (KB)
      }
    ],
    "kernel_modules": { // chỉ cho Linux
      "module_name": {
        "loaded": "boolean", // module có đang load không
        "blacklisted": "boolean", // module có bị blacklist không
        "install_command_set": "boolean" // có lệnh install được thiết lập không
      }
    },
    "file_permissions": { // quyền của các file quan trọng
      "file_path": {
        "owner": "string", // chủ sở hữu
        "group": "string", // nhóm sở hữu
        "mode": "string", // mode (octal)
        "size": "number" // kích thước (bytes)
      }
    }
  },
  "users": {
    "accounts": [
      {
        "username": "string", // tên user
        "uid": "number", // user ID (Linux) hoặc SID (Windows)
        "gid": "number", // group ID (Linux)
        "home": "string", // thư mục home
        "shell": "string", // shell (Linux)
        "password_props": { // thông tin password
          "last_changed": "number", // ngày thay đổi gần nhất
          "min_days": "number", // số ngày tối thiểu giữa các lần đổi
          "max_days": "number", // số ngày tối đa trước khi phải đổi
          "warn_days": "number", // số ngày cảnh báo trước khi hết hạn
          "disabled": "boolean", // tài khoản bị vô hiệu hóa
          "locked": "boolean", // tài khoản bị khóa
          "expires": "string" // ngày hết hạn (nếu có)
        }
      }
    ],
    "password_policy": { // chính sách password
      // các thông số tùy thuộc OS
    }
  },
  "groups": {
    "list": [
      {
        "name": "string", // tên nhóm
        "gid": "number", // group ID (Linux) hoặc group SID (Windows)
        "members": ["string"] // danh sách thành viên
      }
    ]
  },
  "services": {
    "systemd": [ // Linux
      {
        "name": "string", // tên service
        "load_state": "string", // trạng thái load
        "active_state": "string", // trạng thái active
        "sub_state": "string", // trạng thái chi tiết
        "unit_file_state": "string" // trạng thái unit file
      }
    ],
    "windows_services": [ // Windows
      {
        "name": "string", // tên service
        "display_name": "string", // tên hiển thị
        "state": "string", // trạng thái: running, stopped, ...
        "start_type": "string", // kiểu khởi động: auto, manual, disabled
        "path": "string", // đường dẫn executable
        "account": "string" // tài khoản chạy service
      }
    ]
  },
  "network": {
    "interfaces": [
      {
        "name": "string", // tên interface
        "ip_address": "string", // địa chỉ IP
        "netmask": "string", // netmask
        "mac_address": "string", // địa chỉ MAC
        "state": "string" // trạng thái: up, down
      }
    ],
    "open_ports": [
      {
        "protocol": "string", // giao thức: tcp, udp
        "port": "number", // số port
        "process": "string", // tiến trình sử dụng port
        "pid": "number" // process ID
      }
    ],
    "firewall": {
      // thông tin firewall, tùy thuộc vào OS
    }
  },
  "security": {
    // module security, khác nhau tùy OS
  },
  "logging": {
    // thông tin logging, khác nhau tùy OS
  }
}
```

#### 3.2 Module đặc thù cho MySQL:

```json
{
  "mysql_config": {
    "config_files": [
      {
        "path": "string", // đường dẫn file config
        "parameters": {
          "parameter_name": "string" // giá trị parameter
        }
      }
    ],
    "variables": {
      "variable_name": "string" // giá trị biến
    },
    "permissions": {
      "file_path": {
        "owner": "string",
        "group": "string",
        "mode": "string"
      }
    }
  },
  "mysql_users": {
    "accounts": [
      {
        "user": "string", // tên user
        "host": "string", // host được phép kết nối
        "authentication_string": "string", // thông tin xác thực (đã hash)
        "privileges": ["string"], // danh sách quyền
        "account_locked": "boolean", // tài khoản bị khóa
        "password_expired": "boolean" // password hết hạn
      }
    ]
  },
  "mysql_databases": {
    "list": [
      {
        "name": "string", // tên database
        "character_set": "string", // character set
        "collation": "string" // collation
      }
    ]
  },
  "mysql_privileges": {
    "global": [
      {
        "user": "string",
        "host": "string",
        "privilege": "string"
      }
    ],
    "database": [
      {
        "user": "string",
        "host": "string",
        "database": "string",
        "privilege": "string"
      }
    ]
  },
  "mysql_logging": {
    "general_log": {
      "enabled": "boolean",
      "log_file": "string"
    },
    "slow_query_log": {
      "enabled": "boolean",
      "log_file": "string",
      "long_query_time": "number"
    },
    "error_log": {
      "enabled": "boolean",
      "log_file": "string"
    },
    "audit_log": {
      "enabled": "boolean",
      "log_file": "string",
      "policy": "string"
    }
  }
}
```

## Yêu cầu tổng thể

1. **Định dạng chuẩn**: Tuân thủ chuẩn JSON (RFC 8259)
2. **Tính nhất quán**: Tất cả collector phải tuân theo cấu trúc chung
3. **Linh hoạt**: Cho phép bổ sung thêm field khi cần, nhưng không làm thay đổi cấu trúc chính
4. **Đầy đủ thông tin**: Thu thập đủ dữ liệu để đối chiếu với các CIS Benchmark
5. **Kích thước tối ưu**: Chỉ thu thập dữ liệu cần thiết, tránh quá tải
6. **Bảo mật**: Không lưu trữ thông tin nhạy cảm như password dạng plain text

## Ví dụ dữ liệu

Xem file example-output.json đã cung cấp làm mẫu tham khảo.

## Quy ước đặt tên

1. Sử dụng snake_case cho tất cả tên trường
2. Sử dụng tên có ý nghĩa và rõ ràng
3. Các trường liên quan đến thời gian sử dụng định dạng ISO 8601
4. Các trường boolean sử dụng giá trị true/false (không dùng 0/1)

## Phiên bản và tương thích

Schema này hỗ trợ versioning để đảm bảo khả năng tương thích khi cần thay đổi:
- Phiên bản hiện tại: 1.0.0
- Thay đổi nhỏ sẽ tăng số thứ 3 (1.0.0 → 1.0.1)
- Thay đổi lớn sẽ tăng số thứ 2 (1.0.0 → 1.1.0)
- Thay đổi phá vỡ tương thích sẽ tăng số thứ 1 (1.0.0 → 2.0.0)