# Lộ trình phát triển chi tiết với kiến trúc Monolithic

Dưới đây là kế hoạch chi tiết với các đầu việc được bẻ nhỏ để một người có thể thực hiện tuần tự, phù hợp với kiến trúc monolithic mới:

## Giai đoạn 0: Thiết kế và chuẩn bị cơ sở (1-2 tuần)

### 0.1 Thiết kế cấu trúc dữ liệu CIS (2-3 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 0.1.1 | Phân tích và đơn giản hóa các CIS benchmark | Danh sách kiểm tra ưu tiên | Done |
| 0.1.2 | Thiết kế mô hình dữ liệu cho SQLite | Sơ đồ cấu trúc CSDL | Done |
| 0.1.3 | Thiết kế schema JSON/YAML cho dữ liệu thu thập | File schema cơ bản | Done |

### 0.2 Thiết kế quy trình làm việc (2-3 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 0.2.1 | Thiết kế luồng làm việc collector script | Tài liệu quy trình | 1 |
| 0.2.2 | Thiết kế giao diện ứng dụng phân tích | Mockup giao diện | 1 |
| 0.2.3 | Thiết kế cấu trúc báo cáo | Mẫu báo cáo | 1 |

### 0.3 Thiết lập môi trường phát triển (1-2 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 0.3.1 | Thiết lập môi trường Python và công cụ | Môi trường cấu hình | 0.5 |
| 0.3.2 | Thiết lập Git repository và workflow | Repository cấu hình | 0.5 |
| 0.3.3 | Thiết lập môi trường kiểm thử | Framework kiểm thử | 0.5 |

## Giai đoạn 1: Phát triển Collector Scripts (2-3 tuần)

### 1.1 Phát triển framework chung cho collectors (2-3 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 1.1.1 | Xây dựng cấu trúc cơ bản cho script | Mã nguồn template | 1 |
| 1.1.2 | Phát triển module xuất JSON/YAML | Module xuất dữ liệu | 1 |
| 1.1.3 | Phát triển module xử lý tham số và lỗi | Module lỗi | 1 |

### 1.2 Phát triển collector script cho Linux (5-6 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 1.2.1 | Liệt kê và phân nhóm các commands | Danh sách commands | 1 |
| 1.2.2 | Phát triển module thu thập cơ bản (filesystem, users) | Module thu thập cơ bản | 2 |
| 1.2.3 | Phát triển module thu thập nâng cao (network, service) | Module thu thập nâng cao | 2 |
| 1.2.4 | Tối ưu hóa và unittest | Mã nguồn hoàn thiện | 1 |

### 1.3 Phát triển collector script cho Windows (5-6 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 1.3.1 | Liệt kê các PowerShell commands | Danh sách commands | 1 |
| 1.3.2 | Phát triển module thu thập cơ bản (Local policy, registry) | Module thu thập cơ bản | 2 |
| 1.3.3 | Phát triển module thu thập nâng cao (services, firewall) | Module thu thập nâng cao | 2 |
| 1.3.4 | Tối ưu hóa và unittest | Mã nguồn hoàn thiện | 1 |

### 1.4 Phát triển collector script cho MySQL (3-4 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 1.4.1 | Liệt kê các SQL queries cần thiết | Danh sách queries | 1 |
| 1.4.2 | Phát triển module kết nối và thu thập | Module thu thập | 2 |
| 1.4.3 | Tối ưu hóa và unittest | Mã nguồn hoàn thiện | 1 |

### 1.5 Đóng gói và cài đặt collectors (2-3 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 1.5.1 | Tạo installers/packages đơn giản | Installers | 1 |
| 1.5.2 | Viết tài liệu hướng dẫn sử dụng | Tài liệu | 1 |
| 1.5.3 | Kiểm thử trên môi trường thực tế | Báo cáo kiểm thử | 1 |

## Giai đoạn 2: Phát triển Ứng dụng Phân tích (3-4 tuần)

### 2.1 Xây dựng cơ sở dữ liệu (4-5 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 2.1.1 | Tạo schema SQLite cho CIS benchmarks | Schema SQLite | 1 |
| 2.1.2 | Tạo schema SQLite cho Inventory | Schema Inventory | 1 |
| 2.1.3 | Nhập dữ liệu CIS benchmark cho Linux | Dữ liệu Linux | 1 |
| 2.1.4 | Nhập dữ liệu CIS benchmark cho Windows | Dữ liệu Windows | 1 |
| 2.1.5 | Nhập dữ liệu CIS benchmark cho MySQL | Dữ liệu MySQL | 1 |

### 2.2 Phát triển module Inventory Manager (4-5 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 2.2.1 | Xây dựng module quản lý dự án | Module dự án | 1 |
| 2.2.2 | Phát triển module quản lý tài sản (máy chủ, DB...) | Module tài sản | 1 |
| 2.2.3 | Phát triển module nhóm và phân loại tài sản | Module nhóm | 1 |
| 2.2.4 | Phát triển giao diện người dùng cho Inventory | UI Inventory | 1 |
| 2.2.5 | Phát triển chức năng gắn thẻ và tìm kiếm | Module thẻ | 1 |

### 2.3 Phát triển module nhập và chuẩn hóa dữ liệu (4-5 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 2.3.1 | Xây dựng module đọc file JSON/YAML | Module đọc file | 1 |
| 2.3.2 | Phát triển module validate dữ liệu | Module validation | 1 |
| 2.3.3 | Phát triển module chuẩn hóa dữ liệu | Module chuẩn hóa | 1 |
| 2.3.4 | Phát triển module liên kết với tài sản | Module liên kết | 1 |
| 2.3.5 | Phát triển module lưu trữ lịch sử | Module lịch sử | 1 |

### 2.4 Phát triển Rule Engine (4-5 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 2.4.1 | Xây dựng cấu trúc rule engine | Framework rule | 1 |
| 2.4.2 | Phát triển module đánh giá Linux | Module Linux | 1 |
| 2.4.3 | Phát triển module đánh giá Windows | Module Windows | 1 |
| 2.4.4 | Phát triển module đánh giá MySQL | Module MySQL | 1 |
| 2.4.5 | Phát triển module tính điểm và phân loại | Module scoring | 1 |

### 2.5 Phát triển Dashboard và Báo cáo (5-6 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 2.5.1 | Thiết kế giao diện dashboard theo dự án | UI dashboard | 1 |
| 2.5.2 | Phát triển biểu đồ và visualizations | Biểu đồ | 1 |
| 2.5.3 | Phát triển module báo cáo theo dự án/nhóm | Module báo cáo theo nhóm | 2 |
| 2.5.4 | Phát triển module xuất báo cáo HTML/PDF | Module báo cáo | 1 |
| 2.5.5 | Phát triển chức năng so sánh giữa các tài sản/lần đánh giá | Module so sánh | 1 |

## Giai đoạn 3: Tích hợp, Kiểm thử và Hoàn thiện (1-2 tuần)

### 3.1 Tích hợp các thành phần (2-3 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 3.1.1 | Tích hợp collector output với module phân tích | Mã nguồn tích hợp | 1 |
| 3.1.2 | Tích hợp rule engine với dashboard | Mã nguồn tích hợp | 1 |
| 3.1.3 | Tích hợp tất cả thành phần trong UI | UI hoàn chỉnh | 1 |

### 3.2 Kiểm thử hệ thống (3-4 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 3.2.1 | Kiểm thử end-to-end trên Linux | Báo cáo kiểm thử | 1 |
| 3.2.2 | Kiểm thử end-to-end trên Windows | Báo cáo kiểm thử | 1 |
| 3.2.3 | Kiểm thử end-to-end trên MySQL | Báo cáo kiểm thử | 1 |
| 3.2.4 | Kiểm thử hiệu năng và tối ưu | Báo cáo hiệu năng | 1 |

### 3.3 Hoàn thiện và đóng gói (2-3 ngày)
| STT | Công việc | Đầu ra | Thời gian (ngày) |
|-----|-----------|--------|------------------|
| 3.3.1 | Tạo installer cho ứng dụng phân tích | Installer | 1 |
| 3.3.2 | Viết tài liệu hướng dẫn sử dụng | Tài liệu | 1 |
| 3.3.3 | Chuẩn bị release và changelog | Release notes | 0.5 |
| 3.3.4 | Cài đặt thử nghiệm và fix bugs | Phiên bản ổn định | 0.5 |

## Tổng quan thời gian:

- **Giai đoạn 0**: 1-2 tuần
- **Giai đoạn 1**: 2-3 tuần
- **Giai đoạn 2**: 3-4 tuần
- **Giai đoạn 3**: 1-2 tuần

**Tổng thời gian dự kiến**: 7-11 tuần (vẫn ngắn hơn nhiều so với 3-6 tháng của thiết kế microservice)

## Ưu tiên phát triển:

1. **Ưu tiên cao nhất**: Collector scripts và chức năng nhập/xuất dữ liệu
2. **Ưu tiên cao**: Rule engine và đánh giá cơ bản
3. **Ưu tiên trung bình**: Dashboard và báo cáo
4. **Ưu tiên thấp**: Các tính năng nâng cao (so sánh, lịch sử)

## Chiến lược phát triển:
- Áp dụng phương pháp Agile/phát triển tăng dần
- Mỗi giai đoạn tạo ra sản phẩm có thể hoạt động được
- Tập trung vào một nền tảng trước (ví dụ: Linux) rồi mở rộng sang các nền tảng khác
- Kiểm thử liên tục trong quá trình phát triển