# Contributing Guidelines

## Git Workflow

- `main`: branch cho production release
- `develop`: branch chính cho phát triển
- `feature/*`: branch cho tính năng mới (ví dụ: feature/user-authentication)
- `bugfix/*`: branch cho sửa lỗi
- `release/*`: branch cho chuẩn bị release

## Pull Request Process

1. Tạo branch từ `develop` cho tính năng mới hoặc sửa lỗi
2. Code, test và commit thay đổi của bạn
3. Push branch và tạo Pull Request vào `develop`
4. Đợi code review và CI passes
5. Merge sau khi được approve

## Coding Standards

- Tuân thủ PEP 8
- Sử dụng Black cho code formatting
- Viết docstrings cho functions và classes
- Viết unit tests cho code mới
