# Lộ trình phát triển chi tiết với các đầu việc nhỏ

Dưới đây là bảng kế hoạch chi tiết với các đầu việc được bẻ nhỏ để một người có thể thực hiện tuần tự, mỗi đầu việc dự kiến hoàn thành trong 1-3 ngày:

## Giai đoạn 0: Thiết kế và chuẩn bị cơ sở (2-3 tuần)

### 0.1 Thiết kế cấu trúc dữ liệu CIS (4-5 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 0.1.1 | Thu thập và phân tích CIS benchmark cho Windows | Ghi chú phân tích, danh sách kiểm tra | Done |
| 0.1.2 | Thu thập và phân tích CIS benchmark cho Linux | Ghi chú phân tích, danh sách kiểm tra | Done |  
| 0.1.3 | Thu thập và phân tích CIS benchmark cho MySQL | Ghi chú phân tích, danh sách kiểm tra | Done |
| 0.1.4 | Xác định cấu trúc chung giữa các benchmarks | Tài liệu mô tả cấu trúc chung | 1 |
| 0.1.5 | Thiết kế mô hình dữ liệu chung | Sơ đồ cấu trúc dữ liệu | 1 |

### 0.2 Thiết kế schema chuẩn hoá (3-4 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 0.2.1 | Xác định các trường dữ liệu bắt buộc cho chuẩn hóa | Danh sách trường dữ liệu | 1 |
| 0.2.2 | Thiết kế schema JSON/YAML cho dữ liệu thu thập | File schema cơ bản | 1 |
| 0.2.3 | Thiết kế schema cho kết quả đánh giá | File schema kết quả | 1 |
| 0.2.4 | Viết tài liệu mô tả schema | Tài liệu mô tả | 1 |

### 0.3 Thiết kế kiến trúc API và giao tiếp (3-4 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 0.3.1 | Thiết kế API cho thu thập dữ liệu | Tài liệu API | 1 | 
| 0.3.2 | Thiết kế API cho chuẩn hóa dữ liệu | Tài liệu API | 1 |
| 0.3.3 | Thiết kế API cho đánh giá dữ liệu | Tài liệu API | 1 |
| 0.3.4 | Thiết kế API cho báo cáo kết quả | Tài liệu API | 1 |

### 0.4 Thiết lập môi trường phát triển (3-5 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 0.4.1 | Thiết lập môi trường phát triển Python | Cấu hình Python, virtualenv | 1 |
| 0.4.2 | Cài đặt và cấu hình các công cụ phát triển | VSCode/IDE cấu hình | 1 |
| 0.4.3 | Thiết lập cơ sở dữ liệu phát triển | DB schema, kết nối | 1 |
| 0.4.4 | Cấu hình GitHub Actions CI/CD | File workflow CI/CD | 1 |
| 0.4.5 | Thiết lập môi trường kiểm thử | Framework test, fixtures | 1 |

## Giai đoạn 1: Phát triển Tầng Thu thập (Collection Layer) (4-6 tuần)

### 1.1 Phát triển collector framework (6-8 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 1.1.1 | Thiết kế interface cơ bản cho collector | Mô hình class, interface | 1 |
| 1.1.2 | Xây dựng base collector class | Mã nguồn base class | 2 |
| 1.1.3 | Phát triển cơ chế xác thực cho collectors | Module xác thực | 1 |
| 1.1.4 | Phát triển cơ chế khởi chạy và thu thập | Module runner | 1 |
| 1.1.5 | Phát triển cơ chế lưu trữ kết quả | Module lưu trữ | 1 |
| 1.1.6 | Phát triển cơ chế xử lý lỗi | Module error handling | 1 |
| 1.1.7 | Viết unit test cho framework | Test cases | 1 |

### 1.2 Phát triển collector Linux (Ubuntu) (5-7 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 1.2.1 | Liệt kê các commands cần thu thập dữ liệu | Danh sách commands | 1 |
| 1.2.2 | Phát triển module thu thập cấu hình user và group | Module users | 1 |
| 1.2.3 | Phát triển module thu thập cấu hình quyền file | Module file permissions | 1 |
| 1.2.4 | Phát triển module thu thập cấu hình network | Module network | 1 |
| 1.2.5 | Phát triển module thu thập cấu hình service | Module services | 1 |
| 1.2.6 | Viết converter và exporter dữ liệu theo schema | Module converter | 1 |
| 1.2.7 | Viết unit test cho Linux collector | Test cases Linux | 1 |

### 1.3 Phát triển collector Windows (5-7 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 1.3.1 | Liệt kê các PowerShell/WMI commands cần dùng | Danh sách commands | 1 |
| 1.3.2 | Phát triển module thu thập Local Security Policy | Module security policy | 1 |
| 1.3.3 | Phát triển module thu thập cấu hình Registry | Module registry | 1 |
| 1.3.4 | Phát triển module thu thập cấu hình services | Module services | 1 |
| 1.3.5 | Phát triển module thu thập Windows Firewall | Module firewall | 1 |
| 1.3.6 | Viết converter và exporter dữ liệu theo schema | Module converter | 1 |
| 1.3.7 | Viết unit test cho Windows collector | Test cases Windows | 1 |

### 1.4 Phát triển collector MySQL (4-6 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 1.4.1 | Liệt kê các MySQL queries cần dùng | Danh sách queries | 1 |
| 1.4.2 | Phát triển module kết nối và xác thực MySQL | Module connection | 1 |
| 1.4.3 | Phát triển module thu thập cấu hình quyền user | Module users/privileges | 1 |
| 1.4.4 | Phát triển module thu thập cấu hình bảo mật | Module security settings | 1 |
| 1.4.5 | Viết converter và exporter dữ liệu theo schema | Module converter | 1 |
| 1.4.6 | Viết unit test cho MySQL collector | Test cases MySQL | 1 |

### 1.5 Kiểm thử tích hợp các collectors (3-4 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 1.5.1 | Xây dựng môi trường kiểm thử tích hợp | Môi trường test | 1 |
| 1.5.2 | Kiểm thử collector Linux trên môi trường thực | Báo cáo test | 1 |
| 1.5.3 | Kiểm thử collector Windows trên môi trường thực | Báo cáo test | 1 |
| 1.5.4 | Kiểm thử collector MySQL trên môi trường thực | Báo cáo test | 1 |

## Giai đoạn 2: Phát triển Tầng Chuẩn hoá (Normalization Layer) (3-4 tuần)

### 2.1 Phát triển API chuẩn hoá (3-4 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 2.1.1 | Xây dựng RESTful API endpoints | Mã nguồn API | 1 |
| 2.1.2 | Phát triển validation cho input data | Module validation | 1 |
| 2.1.3 | Phát triển xử lý lỗi và logging | Module error handling | 1 |
| 2.1.4 | Viết documentation cho API | Tài liệu API | 1 |

### 2.2 Phát triển parsers (6-7 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 2.2.1 | Phát triển base parser class | Mã nguồn base parser | 1 |
| 2.2.2 | Phát triển parser cho dữ liệu Linux | Parser Linux | 2 |
| 2.2.3 | Phát triển parser cho dữ liệu Windows | Parser Windows | 2 |
| 2.2.4 | Phát triển parser cho dữ liệu MySQL | Parser MySQL | 2 |

### 2.3 Phát triển bộ chuyển đổi schema (3-4 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 2.3.1 | Xây dựng transformer cơ bản | Mã nguồn transformer | 1 |
| 2.3.2 | Phát triển bộ ánh xạ dữ liệu từ Linux | Mã nguồn Linux mapping | 1 |
| 2.3.3 | Phát triển bộ ánh xạ dữ liệu từ Windows | Mã nguồn Windows mapping | 1 |
| 2.3.4 | Phát triển bộ ánh xạ dữ liệu từ MySQL | Mã nguồn MySQL mapping | 1 |

### 2.4 Kiểm thử tầng chuẩn hoá (3-4 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 2.4.1 | Viết unit tests cho API | Test cases API | 1 |
| 2.4.2 | Viết unit tests cho parsers | Test cases parsers | 1 |
| 2.4.3 | Viết unit tests cho transformers | Test cases transformers | 1 |
| 2.4.4 | Thực hiện integration tests | Báo cáo integration tests | 1 |