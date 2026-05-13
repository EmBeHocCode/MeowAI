# 12 - Trạng Thái Hiện Tại

File này là bản tóm tắt ngắn để không bị loạn khi quay lại project.

## Hiện Tại Đã Làm Tới Đâu

MeowAI đang ở cuối Phase 1.

Đã có:

- Chatbot rule-based chạy được.
- API `/chat` chạy được trên VPS.
- Service `meowai-api.service` chạy nền trên VPS.
- Auto reload khi code Python thay đổi trên VPS.
- GitHub repo đã có code.
- Cấu trúc đã tách `apps/bot` và `apps/web`.

## Cấu Trúc Cần Nhớ

```text
MeowAI/
├─ apps/
│  ├─ bot/   # Phần bot thật: API, thuật toán, test
│  └─ web/   # Dashboard quản lý, chưa xây ở phase này
├─ data/     # Dữ liệu sản phẩm, chính sách, dataset intent
├─ docs/     # Tài liệu project
├─ models/   # Model train sau này
└─ deploy/   # File service VPS
```

## Bot Đang Chạy Kiểu Gì

Trên VPS, bot chạy bằng systemd service:

```bash
systemctl status meowai-api.service
```

Service chạy API nội bộ:

```text
http://127.0.0.1:8010
```

File service:

```text
deploy/meowai-api.service
```

Lệnh service đang dùng:

```bash
/var/www/MeowAI/.venv/bin/python -m uvicorn apps.bot.src.api:app --host 127.0.0.1 --port 8010 --reload
```

## Test Nhanh Trên VPS

Terminal đúng:

```bash
cd /var/www/MeowAI
```

Kiểm tra bot còn sống:

```bash
curl http://127.0.0.1:8010/health
```

Hỏi thử bot:

```bash
curl -X POST http://127.0.0.1:8010/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"VPS Ryzen Basic giá bao nhiêu?"}'
```

## File Code Chính

```text
apps/bot/src/preprocess.py          # Chuẩn hóa câu hỏi
apps/bot/src/intent_rules.py        # Nhận diện intent bằng rule
apps/bot/src/product_search.py      # Tìm sản phẩm trong CSV
apps/bot/src/response_templates.py  # Mẫu câu trả lời
apps/bot/src/chat_engine.py         # Ghép các bước thành chatbot
apps/bot/src/api.py                 # FastAPI /health và /chat
apps/bot/run_chat.py                # Chạy chatbot trong terminal
```

## Cách Chạy Terminal Chatbot

Local Windows:

```powershell
cd D:\MeowAI
$env:PYTHONIOENCODING='utf-8'
python apps\bot\run_chat.py
```

VPS:

```bash
cd /var/www/MeowAI
source .venv/bin/activate
PYTHONIOENCODING=utf-8 python apps/bot/run_chat.py
```

## Cách Test

Local Windows:

```powershell
cd D:\MeowAI
$env:PYTHONIOENCODING='utf-8'
python -m unittest discover -s apps\bot\tests
```

VPS:

```bash
cd /var/www/MeowAI
PYTHONIOENCODING=utf-8 .venv/bin/python -m unittest discover -s apps/bot/tests
```

## Quy Trình Làm Việc Từ Giờ

1. Sửa code ở local `D:\MeowAI`.
2. Test local.
3. Commit và push lên GitHub.
4. VPS pull code mới.
5. Service auto reload.
6. Test API trên VPS.
7. Cập nhật `docs/07_BUILD_LOG.md`.

## Bước Tiếp Theo

Bước tiếp theo nên làm là Phase 2 nhẹ:

- Thêm nhiều sản phẩm mẫu vào `data/shop/products.csv`.
- Làm tìm kiếm sản phẩm thông minh hơn một chút.
- Thêm endpoint API để xem danh sách sản phẩm.

Chưa cần xây dashboard web ngay. Mình nên làm bot chắc trước, rồi dashboard sau.
