# Thiết lập môi trường phát triển cho dự án CIS Benchmark Assessment

Dưới đây là hướng dẫn chi tiết thiết lập môi trường phát triển cho dự án tự động hóa Security Audit theo CIS Benchmark với Django cho phần phân tích và báo cáo.

## 1. Thiết lập môi trường Python và công cụ

### Yêu cầu cơ bản
- Python 3.8+ (khuyến nghị Python 3.10+)
- pip (trình quản lý package cho Python)
- virtualenv hoặc conda (quản lý môi trường ảo)

### Thiết lập môi trường ảo

```bash
# Tạo thư mục dự án
mkdir cis-benchmark-tool
cd cis-benchmark-tool

# Tạo môi trường ảo Python
python -m venv venv

# Kích hoạt môi trường ảo
# Trên Windows:
venv\Scripts\activate
# Trên Linux/macOS:
source venv/bin/activate

# Cập nhật pip
pip install --upgrade pip
```

### Cài đặt các dependencies

Tạo file `requirements.txt` với nội dung:

```
# Django và web framework
Django==4.2.10
djangorestframework==3.14.0
django-crispy-forms==2.0
django-filter==23.5
whitenoise==6.6.0
crispy-bootstrap4==2022.1

# Xử lý dữ liệu
pandas==2.1.3
numpy==1.26.3
pyyaml==6.0.1

# Trực quan hóa
matplotlib==3.8.2
seaborn==0.13.0

# Báo cáo
reportlab==4.0.8
weasyprint==60.2

# Kiểm thử
pytest==7.4.3
pytest-django==4.7.0
coverage==7.3.2
```

Tạo file `requirements-dev.txt` với nội dung:

```
# Import requirements.txt
-r requirements.txt

# Công cụ phát triển
black==23.12.0
flake8==6.1.0
isort==5.13.2
pre-commit==3.5.0

# Debug
django-debug-toolbar==4.2.0
ipython==8.18.0

# Tài liệu
sphinx==7.2.6
```

Cài đặt các dependencies:

```bash
pip install -r requirements-dev.txt
```

## 2. Thiết lập Git repository và workflow

### Khởi tạo Git repository

```bash
# Khởi tạo git repository
git init

# Tạo .gitignore
cat > .gitignore << EOL
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
media/
staticfiles/
static/

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
.env
.coverage
htmlcov/
EOL

# Commit đầu tiên
git add .gitignore requirements.txt requirements-dev.txt
git commit -m "Initial commit: Basic project setup"
```

### Thiết lập branch workflow

```bash
# Tạo branch develop
git checkout -b develop

# Tạo file hướng dẫn CONTRIBUTING.md
cat > CONTRIBUTING.md << EOL
# Contributing Guidelines

## Git Workflow

- \`main\`: branch cho production release
- \`develop\`: branch chính cho phát triển
- \`feature/*\`: branch cho tính năng mới (ví dụ: feature/user-authentication)
- \`bugfix/*\`: branch cho sửa lỗi
- \`release/*\`: branch cho chuẩn bị release

## Pull Request Process

1. Tạo branch từ \`develop\` cho tính năng mới hoặc sửa lỗi
2. Code, test và commit thay đổi của bạn
3. Push branch và tạo Pull Request vào \`develop\`
4. Đợi code review và CI passes
5. Merge sau khi được approve

## Coding Standards

- Tuân thủ PEP 8
- Sử dụng Black cho code formatting
- Viết docstrings cho functions và classes
- Viết unit tests cho code mới
EOL

git add CONTRIBUTING.md
git commit -m "Add contributing guidelines"
```

### Thiết lập pre-commit hooks

Tạo file `.pre-commit-config.yaml`:

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files

-   repo: https://github.com/psf/black
    rev: 23.12.0
    hooks:
    -   id: black

-   repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
    -   id: isort

-   repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-docstrings]
```

Cài đặt pre-commit:

```bash
pre-commit install
git add .pre-commit-config.yaml
git commit -m "Add pre-commit hooks"
```

## 3. Thiết lập môi trường kiểm thử

### Khởi tạo Django project và apps

```bash
# Tạo Django project
django-admin startproject cisbenchmark webapp

# Chuyển đến thư mục webapp
cd webapp

# Tạo các Django apps
python manage.py startapp accounts
python manage.py startapp dashboard
python manage.py startapp inventory
python manage.py startapp benchmarks
python manage.py startapp assessments
python manage.py startapp reports

# Quay lại thư mục gốc
cd ..
```

### Thiết lập pytest cho Django

Tạo file `webapp/pytest.ini`:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = cisbenchmark.settings
python_files = test_*.py
testpaths =
    accounts/tests
    dashboard/tests
    inventory/tests
    benchmarks/tests
    assessments/tests
    reports/tests
```

### Tạo tests cơ bản

Ví dụ test cho inventory app:

```bash
mkdir -p webapp/inventory/tests
touch webapp/inventory/tests/__init__.py
```

Tạo file `webapp/inventory/tests/test_models.py`:

```python
import pytest
from django.test import TestCase
from inventory.models import Project, Asset, AssetGroup

class TestProject(TestCase):
    def test_create_project(self):
        project = Project.objects.create(
            name="Test Project",
            description="This is a test project"
        )
        self.assertEqual(project.name, "Test Project")
        self.assertTrue(project.project_id)

class TestAsset(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name="Test Project",
            description="This is a test project"
        )

    def test_create_asset(self):
        asset = Asset.objects.create(
            project=self.project,
            name="Test Server",
            type="linux",
            hostname="test.example.com",
            ip_address="192.168.1.100"
        )
        self.assertEqual(asset.name, "Test Server")
        self.assertEqual(asset.project, self.project)
```

## 4. Cấu trúc cây thư mục của dự án

Tạo cấu trúc thư mục đầy đủ:

```bash
# Tạo các thư mục cho collector scripts
mkdir -p collectors/common
mkdir -p collectors/linux/modules
mkdir -p collectors/windows/modules
mkdir -p collectors/mysql

# Tạo các thư mục cho tests
mkdir -p tests/collectors
mkdir -p tests/integration

# Tạo docs và scripts
mkdir -p docs/collectors docs/webapp docs/deployment
mkdir -p scripts/setup scripts/data_migration
```

Cấu trúc cây thư mục cuối cùng sẽ như sau:

```
cis-benchmark-tool/
├── .git/
├── .github/                         # GitHub workflows (sẽ được thêm sau)
├── .gitignore
├── .pre-commit-config.yaml
├── CONTRIBUTING.md
├── collectors/                      # Collector scripts
│   ├── common/                      # Shared utility code
│   │   ├── schema_validator.py
│   │   └── utils.py
│   ├── linux/                       # Linux collector
│   │   ├── modules/                 # Module-specific collectors
│   │   ├── collector.sh
│   │   └── utils/
│   ├── windows/                     # Windows collector
│   │   ├── modules/
│   │   ├── collector.ps1
│   │   └── utils/
│   └── mysql/                       # MySQL collector
│       ├── collector.sh
│       ├── collector.ps1
│       └── collector.sql
├── docs/                            # Documentation
│   ├── collectors/
│   ├── webapp/
│   └── deployment/
├── requirements-dev.txt             # Development dependencies
├── requirements.txt                 # Python dependencies
├── scripts/                         # Utility scripts
│   ├── setup/
│   └── data_migration/
├── tests/                           # Non-Django specific tests
│   ├── collectors/
│   └── integration/
├── venv/                            # Virtual environment
└── webapp/                          # Django web application
    ├── accounts/                    # User authentication app
    ├── assessments/                 # Assessment app
    ├── benchmarks/                  # CIS Benchmarks app
    ├── cisbenchmark/                # Project settings
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── dashboard/                   # Dashboard app
    ├── inventory/                   # Inventory Manager app
    ├── manage.py
    ├── pytest.ini
    ├── reports/                     # Reporting app
    └── templates/                   # Shared templates
```

## 5. Thiết lập models cơ bản

### Models cho inventory app

Tạo file `webapp/inventory/models.py`:

```python
from django.db import models
import uuid

class Project(models.Model):
    """Model representing a project."""
    project_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Asset(models.Model):
    """Model representing an IT asset to be assessed."""
    ASSET_TYPES = (
        ('linux', 'Linux'),
        ('windows', 'Windows'),
        ('mysql', 'MySQL'),
        ('other', 'Other'),
    )

    asset_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='assets')
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=ASSET_TYPES)
    hostname = models.CharField(max_length=255, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    os_info = models.JSONField(blank=True, null=True)
    db_info = models.JSONField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.hostname})"

class AssetGroup(models.Model):
    """Model representing a group of assets."""
    group_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assets = models.ManyToManyField(Asset, related_name='groups')

    def __str__(self):
        return f"{self.name} (in {self.project.name})"
```

### Models cho benchmarks app

Tạo file `webapp/benchmarks/models.py`:

```python
from django.db import models

class Benchmark(models.Model):
    """Model representing a CIS Benchmark."""
    benchmark_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    publication_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} v{self.version}"

class Profile(models.Model):
    """Model representing a profile within a benchmark (e.g., Level 1, Level 2)."""
    profile_id = models.CharField(primary_key=True, max_length=100)
    benchmark = models.ForeignKey(Benchmark, on_delete=models.CASCADE, related_name='profiles')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.benchmark.name})"

class Section(models.Model):
    """Model representing a section within a benchmark."""
    section_id = models.CharField(primary_key=True, max_length=100)
    benchmark = models.ForeignKey(Benchmark, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subsections')
    section_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.section_number} {self.title}"

class Control(models.Model):
    """Model representing a specific control/recommendation within a benchmark."""
    ASSESSMENT_STATUS_CHOICES = (
        ('automated', 'Automated'),
        ('manual', 'Manual'),
    )

    control_id = models.CharField(primary_key=True, max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='controls')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    rationale = models.TextField(blank=True)
    impact = models.TextField(blank=True)
    audit_procedure = models.TextField(blank=True)
    remediation = models.TextField(blank=True)
    default_value = models.TextField(blank=True)
    assessment_status = models.CharField(max_length=20, choices=ASSESSMENT_STATUS_CHOICES)
    control_number = models.CharField(max_length=20, blank=True)
    profiles = models.ManyToManyField(Profile, related_name='controls')

    def __str__(self):
        return f"{self.control_number} {self.title}"
```

### Models cho assessments app

Tạo file `webapp/assessments/models.py`:

```python
from django.db import models
import uuid

class Assessment(models.Model):
    """Model representing an assessment of an asset against a benchmark."""
    assessment_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4)
    project = models.ForeignKey('inventory.Project', on_delete=models.CASCADE, related_name='assessments')
    asset = models.ForeignKey('inventory.Asset', on_delete=models.CASCADE, related_name='assessments')
    benchmark = models.ForeignKey('benchmarks.Benchmark', on_delete=models.CASCADE, related_name='assessments')
    profile = models.ForeignKey('benchmarks.Profile', on_delete=models.CASCADE, related_name='assessments')
    timestamp = models.DateTimeField(auto_now_add=True)
    summary = models.JSONField(blank=True, null=True)
    compliance_score = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.asset.name} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

class Result(models.Model):
    """Model representing a single control result within an assessment."""
    STATUS_CHOICES = (
        ('pass', 'Pass'),
        ('fail', 'Fail'),
        ('unknown', 'Unknown'),
        ('not_applicable', 'Not Applicable'),
    )

    result_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='results')
    control = models.ForeignKey('benchmarks.Control', on_delete=models.CASCADE, related_name='results')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    actual_value = models.TextField(blank=True)
    expected_value = models.TextField(blank=True)
    evidence = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.control.control_number} - {self.status}"

class CollectedData(models.Model):
    """Model storing the raw collected data from collector scripts."""
    collection_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4)
    asset = models.ForeignKey('inventory.Asset', on_delete=models.CASCADE, related_name='collected_data')
    collector_type = models.CharField(max_length=20)
    collection_date = models.DateTimeField()
    raw_data = models.JSONField()

    def __str__(self):
        return f"{self.asset.name} data - {self.collection_date.strftime('%Y-%m-%d')}"
```

## 6. Cập nhật Django settings

Cập nhật file `webapp/cisbenchmark/settings.py` để đăng ký các apps:

```python
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'crispy_forms',
    'crispy_bootstrap4',

    # Local apps
    'accounts',
    'dashboard',
    'inventory',
    'benchmarks',
    'assessments',
    'reports',
]

# Crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"
```

## 7. README.md

Tạo file `README.md` ở thư mục gốc:

```markdown
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

## Cấu trúc dự án

- `collectors/`: Collector scripts cho các nền tảng khác nhau
- `webapp/`: Ứng dụng Django cho phân tích và báo cáo
- `docs/`: Tài liệu
- `tests/`: Tests

## Collector Scripts

### Sử dụng

#### Linux
```bash
cd collectors/linux
sudo ./collector.sh --output /tmp/linux_assessment.json
```

#### Windows
```powershell
cd collectors/windows
.\collector.ps1 -OutputPath C:\Temp\windows_assessment.json
```

#### MySQL
```bash
cd collectors/mysql
./collector.sh --output /tmp/mysql_assessment.json --user <username> --password <password>
```

## Phát triển

Vui lòng tham khảo [CONTRIBUTING.md](CONTRIBUTING.md) để biết thêm về quy trình phát triển.

## License

[MIT License](LICENSE)
```

## 8. Commit các thay đổi

```bash
# Add các files đã tạo
git add .

# Commit
git commit -m "Set up Django project structure with models"

# Push (nếu bạn có remote repository)
# git push origin develop
```

---

Với các bước thiết lập trên, bạn đã có một môi trường phát triển đầy đủ cho dự án CIS Benchmark Assessment với kiến trúc monolithic. Môi trường bao gồm:

1. **Môi trường Python với virtualenv** và các dependencies cần thiết
2. **Git repository** với workflow và pre-commit hooks
3. **Django project** với các apps và models cơ bản
4. **Framework kiểm thử** với pytest và Django tests
5. **Cấu trúc cây thư mục** rõ ràng cho collector scripts và ứng dụng web

Bước tiếp theo sẽ là bắt đầu phát triển collector scripts và các chức năng chính của ứng dụng Django.
