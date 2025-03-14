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