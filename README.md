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
