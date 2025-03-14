# Gitflow Workflow

Dự án này sử dụng mô hình Gitflow được điều chỉnh cho phù hợp với quy mô dự án.

## Branch Chính

- `main`: Branch production, chỉ chứa code đã được kiểm tra và sẵn sàng deployment
- `develop`: Branch phát triển chính, nơi tích hợp tất cả các feature

## Branch Tạm Thời

- `feature/*`: Branch cho tính năng mới (ví dụ: `feature/user-authentication`)
- `bugfix/*`: Branch để sửa lỗi
- `hotfix/*`: Branch sửa lỗi khẩn cấp (từ `main`)
- `release/*`: Branch chuẩn bị phát hành

## Quy Trình Làm Việc

### Phát Triển Tính Năng Mới

1. Tạo feature branch từ `develop`:
   ```
   git checkout develop
   git pull origin develop
   git checkout -b feature/new-feature-name
   ```

2. Phát triển và commit thay đổi:
   ```
   git add .
   git commit -m "feat: add new feature"
   ```

3. Push và tạo Pull Request:
   ```
   git push origin feature/new-feature-name
   ```

4. Sau khi review và CI passes, merge vào `develop`.

### Phát Hành

1. Tạo release branch từ `develop`:
   ```
   git checkout develop
   git pull origin develop
   git checkout -b release/1.0.0
   ```

2. Sửa lỗi cuối nếu cần, cập nhật version và changelog.

3. Merge vào `main` và `develop`:
   ```
   # Merge vào main
   git checkout main
   git merge --no-ff release/1.0.0
   git tag -a v1.0.0 -m "Version 1.0.0"
   git push origin main --tags
   
   # Merge lại vào develop
   git checkout develop
   git merge --no-ff release/1.0.0
   git push origin develop
   
   # Xóa branch release
   git branch -d release/1.0.0
   ```

### Hotfix

1. Tạo hotfix branch từ `main`:
   ```
   git checkout main
   git pull origin main
   git checkout -b hotfix/critical-bug
   ```

2. Sửa và commit:
   ```
   git add .
   git commit -m "fix: critical bug"
   ```

3. Merge vào `main` và `develop`:
   ```
   # Merge vào main
   git checkout main
   git merge --no-ff hotfix/critical-bug
   git tag -a v1.0.1 -m "Version 1.0.1"
   git push origin main --tags
   
   # Merge vào develop
   git checkout develop
   git merge --no-ff hotfix/critical-bug
   git push origin develop
   
   # Xóa hotfix branch
   git branch -d hotfix/critical-bug
   ```

---