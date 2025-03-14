# CIS Benchmark Assessment Tool

Tool tự động hóa Security Audit theo CIS Benchmark với kiến trúc monolithic.

## Tính năng

- Thu thập thông tin cấu hình từ hệ thống (Linux, Windows, MySQL)
- Đánh giá tuân thủ theo tiêu chuẩn CIS Benchmark
- Quản lý tài sản (inventory) theo dự án
- Tạo báo cáo chi tiết và tổng quan
- Theo dõi tiến độ cải thiện theo thời gian

## Cài đặt

### Yêu cầu

- Python 3.8+
- Git

### Thiết lập môi trường phát triển

```bash
# Clone repository
git clone <repository-url>
cd cis-benchmark-tool

# Tạo và kích hoạt môi trường ảo
python -m venv venv
source venv/bin/activate  # Linux/macOS
# hoặc
venv\Scripts\activate  # Windows

# Cài đặt dependencies
pip install -r requirements-dev.txt

# Khởi tạo database
cd webapp
python manage.py migrate

# Chạy server
python manage.py runserver

```

## Git Workflow

Dự án này sử dụng mô hình Gitflow được điều chỉnh:

- `main`: Branch production, code đã sẵn sàng phát hành
- `develop`: Branch phát triển, tích hợp tính năng mới
- `feature/*`: Branch cho tính năng mới
- `bugfix/*`: Branch sửa lỗi
- `hotfix/*`: Branch sửa lỗi khẩn cấp
- `release/*`: Branch chuẩn bị phát hành

### Quy tắc Commit

Dự án sử dụng Conventional Commits:

```
<type>[optional scope]: <description>
```

Ví dụ:
- `feat: add user authentication`
- `fix(api): handle null response`

### Pull Requests

Tất cả thay đổi cần được tạo Pull Request vào `develop` và nhận approval trước khi merge.