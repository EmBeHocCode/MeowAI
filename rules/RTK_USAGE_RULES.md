# RTK Usage Rules - Luật Dùng Terminal Tiết Kiệm Token

File này quy định cách dùng RTK khi chạy terminal trong project MeowAI.

Mục tiêu là giảm lượng output dài, giúp Codex/dev đọc kết quả gọn hơn và đỡ tốn token.

## Nguyên Tắc Chính

- Ưu tiên dùng `rtk` khi chạy các lệnh terminal phù hợp.
- Dùng RTK để đọc file, kiểm tra git, tìm file và chạy test/build.
- Nếu RTK lỗi hoặc thiếu tính năng, được dùng lệnh PowerShell/Git/Bun/Python bình thường.
- Khi RTK lỗi, phải báo ngắn gọn lỗi gặp phải.

## Lệnh Nên Dùng

```powershell
rtk git status
rtk read README.md
rtk find . -name package.json
rtk find apps -type f
```

Khi phù hợp với project hiện tại, có thể dùng:

```powershell
rtk npm test
rtk pnpm test
rtk tsc
rtk next build
rtk lint
```

## Lưu Ý Trên Windows

- Tránh dùng `rtk ls` trên Windows nếu không cần.
- Ưu tiên `rtk find` để liệt kê file.
- Nếu cần tìm nhanh nội dung trong file, có thể dùng `rg`.
- Nếu cần đọc file ngắn, ưu tiên `rtk read <file>`.

## Không Bắt Buộc Dùng RTK Khi

- Lệnh cần chạy trực tiếp bằng Python, Bun, Git hoặc SSH.
- RTK không hỗ trợ đúng hành vi cần kiểm tra.
- Cần output đầy đủ để debug lỗi phức tạp.

## Ví Dụ Quy Trình

Kiểm tra trạng thái repo:

```powershell
rtk git status
```

Đọc hướng dẫn project:

```powershell
rtk read AGENTS.md
rtk read rules/README.md
```

Tìm file cấu hình web:

```powershell
rtk find apps -name package.json
```

Chạy kiểm tra web nếu phù hợp:

```powershell
rtk tsc
rtk next build
```
