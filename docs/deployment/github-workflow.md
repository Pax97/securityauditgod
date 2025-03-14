# Git-Workflow-Setup.md

## 1. Thiết lập Branch Chính

Thực hiện các lệnh sau để thiết lập các branch chính:

```bash
# Khởi tạo các branch chính
git branch main  # Branch production
git branch develop  # Branch phát triển

# Đảm bảo đang ở branch develop
git checkout develop
```

## 2. Tạo thư mục cho GitHub workflows

```bash
mkdir -p .github/workflows
```

## 3. Tạo GITFLOW.md

Tạo file `.github/GITFLOW.md` với nội dung sau:

---

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

## 4. Tạo COMMIT_CONVENTION.md

Tạo file `.github/COMMIT_CONVENTION.md` với nội dung sau:

---

# Quy Ước Commit Message

Dự án này sử dụng quy ước Conventional Commits để đảm bảo lịch sử commit nhất quán và dễ đọc.

## Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Types

- `feat`: Tính năng mới
- `fix`: Sửa lỗi
- `docs`: Thay đổi tài liệu
- `style`: Thay đổi không ảnh hưởng đến code (format, semi-colons, etc)
- `refactor`: Refactor code không sửa lỗi hay thêm tính năng
- `perf`: Cải thiện hiệu suất
- `test`: Thêm hoặc sửa tests
- `build`: Thay đổi hệ thống build hoặc dependencies
- `ci`: Thay đổi CI configuration
- `chore`: Các thay đổi khác không thuộc các loại trên

## Examples

```
feat: add user authentication
```

```
fix(api): handle null response from inventory service
```

```
docs: update README with setup instructions
```

```
feat: implement assessment report generation

This implementation includes:
- PDF generation
- Chart visualization
- Summary statistics

Resolves: #123
```

---

## 5. Tạo CI Workflow

Tạo file `.github/workflows/ci.yml` với nội dung sau:

```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.8, 3.10]

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements-dev.txt
    
    - name: Run Linting
      run: |
        flake8 --count --select=E9,F63,F7,F82 --show-source --statistics webapp/
        black --check webapp/
        isort --check-only --profile black webapp/
    
    - name: Run Tests
      run: |
        cd webapp
        pytest --cov=. --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./webapp/coverage.xml
        fail_ci_if_error: true
```

## 6. Tạo Workflow cho Collector Scripts

Tạo file `.github/workflows/collectors-ci.yml` với nội dung sau:

```yaml
name: Collector Scripts CI

on:
  push:
    branches: [ main, develop ]
    paths:
      - 'collectors/**'
  pull_request:
    branches: [ main, develop ]
    paths:
      - 'collectors/**'

jobs:
  test-linux-collectors:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y shellcheck
    
    - name: Run ShellCheck
      run: |
        shellcheck collectors/linux/*.sh collectors/mysql/*.sh
    
    - name: Run Linux collector unit tests
      run: |
        bash collectors/linux/tests/run_tests.sh

  test-windows-collectors:
    runs-on: windows-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Run PSScriptAnalyzer
      shell: pwsh
      run: |
        Install-Module -Name PSScriptAnalyzer -Force
        $results = Invoke-ScriptAnalyzer -Path collectors/windows/ -Recurse
        $results | Format-Table
        if ($results) { throw "PSScriptAnalyzer found issues" }
    
    - name: Run Windows collector unit tests
      shell: pwsh
      run: |
        collectors/windows/tests/run_tests.ps1
```

## 7. Tạo Pull Request Template

Tạo file `.github/PULL_REQUEST_TEMPLATE.md` với nội dung sau:

---

## Mô tả

Mô tả ngắn gọn về Pull Request này.

## Loại thay đổi

- [ ] Bug fix (non-breaking change - sửa lỗi)
- [ ] New feature (non-breaking change - tính năng mới)
- [ ] Breaking change (fix/feature gây thay đổi hoạt động hiện tại)
- [ ] Documentation update (cập nhật tài liệu)

## Kiểm tra

- [ ] Đã kiểm tra code style với linters
- [ ] Đã chạy và pass tất cả tests
- [ ] Đã kiểm tra chức năng hoạt động đúng trên môi trường cục bộ

## Screenshots (nếu phù hợp)

## Issue liên quan

Resolves #<issue_number>

---

## 8. Tạo CODEOWNERS

Tạo file `.github/CODEOWNERS` với nội dung sau:

```
# Project maintainers
*       @team-lead @tech-lead

# Backend code
/webapp/  @backend-team
/collectors/ @security-team

# Documentation
/docs/   @documentation-team
```

## 9. Tạo .gitattributes

Tạo file `.gitattributes` ở thư mục gốc với nội dung sau:

```
# Set default behavior to automatically normalize line endings
* text=auto

# Explicitly declare text files
*.py text
*.js text
*.html text
*.css text
*.md text
*.yml text
*.yaml text
*.json text
*.sh text eol=lf
*.sql text
*.ps1 text eol=crlf

# Declare binary files
*.png binary
*.jpg binary
*.gif binary
*.ico binary
*.db binary
*.sqlite3 binary
```

## 10. Tạo Release Workflow

Tạo file `.github/workflows/release.yml` với nội dung sau:

```yaml
name: Release

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
      with:
        fetch-depth: 0
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build wheel setuptools twine
    
    - name: Build packages
      run: |
        # Build webapp package
        cd webapp
        python -m build
        
        # Package collectors
        cd ../collectors
        zip -r ../dist/linux-collectors.zip linux/
        zip -r ../dist/windows-collectors.zip windows/
        zip -r ../dist/mysql-collectors.zip mysql/
    
    - name: Generate changelog
      id: changelog
      uses: metcalfc/changelog-generator@v4.0.1
      with:
        myToken: ${{ secrets.GITHUB_TOKEN }}
    
    - name: Create GitHub Release
      uses: softprops/action-gh-release@v1
      with:
        files: |
          dist/*.whl
          dist/*.tar.gz
          dist/*.zip
        body: |
          # Release ${{ github.ref_name }}
          
          ## What's Changed
          ${{ steps.changelog.outputs.changelog }}
        draft: false
        prerelease: false
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## 11. Cập nhật README.md

Thêm phần sau vào README.md:

---

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

---

## 12. Commit các thay đổi

```bash
# Thêm các file mới
git add .github/ .gitattributes

# Commit
git commit -m "chore: set up git workflow"

# Cập nhật README
git add README.md
git commit -m "docs: update README with git workflow information"
```