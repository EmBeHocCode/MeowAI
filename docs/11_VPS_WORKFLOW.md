# 11 - Workflow VPS Và VS Code Remote SSH

File này ghi lại cách làm việc với MeowAI trên VPS.

## Đường Dẫn Project

Máy local:

```text
D:\MeowAI
```

VPS:

```text
/var/www/MeowAI
```

## Cách Mở VPS Bằng VS Code Remote SSH

1. Mở VS Code.
2. Bấm góc trái dưới màn hình vào biểu tượng màu xanh `><` hoặc `SSH`.
3. Chọn `Connect to Host...`.
4. Chọn:

```text
meow-server
```

5. Sau khi kết nối thành công, góc trái dưới sẽ hiện:

```text
SSH: meow-server
```

6. Vào menu:

```text
File -> Open Folder
```

7. Nhập đường dẫn:

```text
/var/www/MeowAI
```

Lúc này em đang sửa trực tiếp project MeowAI trên VPS.

## Cách Mở Terminal Đúng Thư Mục

Trong VS Code đang kết nối SSH, mở terminal:

```text
Terminal -> New Terminal
```

Cần thấy terminal đang ở:

```text
root@meow-server:/var/www/MeowAI#
```

Nếu chưa đúng, chạy:

```bash
cd /var/www/MeowAI
```

## Nguyên Tắc Làm Việc

- Code chính của MeowAI nằm trong `D:\MeowAI` và `/var/www/MeowAI`.
- Không sửa MeowAI trong `E:\ZALO-BotChat`.
- Nếu sửa local xong thì đồng bộ lên VPS.
- Nếu sửa trên VPS xong thì sau này cần đồng bộ ngược về local hoặc push GitHub.

## Lệnh Kiểm Tra Nhanh Trên VPS

```bash
cd /var/www/MeowAI
ls
find . -maxdepth 2 -type f | sort
```

## Bot Chạy Thường Trực Trên VPS

MeowAI API đang chạy bằng systemd:

```bash
systemctl status meowai-api.service
```

Thông tin chính:

- Service API: `meowai-api.service`
- API nội bộ: `http://127.0.0.1:8010`
- Health check: `GET /health`
- Chat endpoint: `POST /chat`

Test health trên VPS:

```bash
cd /var/www/MeowAI
curl http://127.0.0.1:8010/health
```

Test chat trên VPS:

```bash
cd /var/www/MeowAI
curl -X POST http://127.0.0.1:8010/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"VPS Ryzen Basic giá bao nhiêu?"}'
```

Xem log service:

```bash
journalctl -u meowai-api.service -f
```

## Cơ Chế Auto Reload

Service đang chạy bằng lệnh:

```bash
/var/www/MeowAI/.venv/bin/python -m uvicorn apps.bot.src.api:app --host 127.0.0.1 --port 8010 --reload
```

Ý nghĩa:

- Bot luôn chạy nền trên VPS.
- Khi mình đồng bộ file `.py` lên `/var/www/MeowAI`, Uvicorn tự phát hiện thay đổi.
- App tự reload nhanh để nhận code mới.
- Em không cần tự restart service sau mỗi lần sửa code.

Ghi chú: đây là chế độ phù hợp cho giai đoạn học, demo và làm đồ án. Khi lên production thật, mình sẽ đổi sang cách chạy ổn định hơn và restart có kiểm soát.

## Quy Trình Làm Việc Từ Bây Giờ

1. Sửa code ở local Windows `D:\MeowAI`.
2. Test local nếu phần đó không phụ thuộc VPS.
3. Đồng bộ file thay đổi lên VPS `/var/www/MeowAI`.
4. Vì service có `--reload`, bot tự cập nhật code mới.
5. Test lại API trên VPS.
6. Cập nhật `docs/07_BUILD_LOG.md`.

## Ghi Chú

MeowAI đã có chatbot terminal rule-based và API nội bộ chạy thường trực trên VPS.
