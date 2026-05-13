# 12 - Trạng Thái Hiện Tại

File này là bản tóm tắt ngắn để không bị loạn khi quay lại project.

## Hiện Tại Đã Làm Tới Đâu

MeowAI đã hoàn thành Phase 1 và Phase 2 bản nền.

Bước tiếp theo là Phase 3: mở rộng dataset intent để chuẩn bị train model.

Đã có:

- Chatbot rule-based chạy được.
- Bot hiểu các câu mẫu Phase 1, gồm viết tắt như `ck`, `dc`, `bh`, `ntn`.
- Bot trả lời được câu hỏi giá rẻ nhất, tồn kho, giao hàng, bảo hành, khuyến mãi và tư vấn sản phẩm.
- Dữ liệu sản phẩm mẫu đã có 10 sản phẩm trong `data/shop/products.csv`.
- Tìm kiếm sản phẩm đã tránh chọn bừa khi câu hỏi quá mơ hồ.
- Câu trả lời về sản phẩm có thể kèm link sản phẩm nếu dữ liệu có link.
- API `/chat` chạy được trên VPS.
- Giao diện web Next.js/TSX `/dashboard` và `/chat`.
- Service `meowai-api.service` chạy nền trên VPS.
- Service `meowai-web.service` dành cho Next.js web trên VPS.
- Auto reload khi code Python thay đổi trên VPS.
- GitHub repo đã có code.
- Cấu trúc đã tách `apps/bot` và `apps/web`.
- Bộ luật cứng cho dev/Codex trong `AGENTS.md` và `rules/`.

## Cấu Trúc Cần Nhớ

```text
MeowAI/
├─ apps/
│  ├─ bot/   # Phần bot thật: API, thuật toán, test
│  └─ web/   # Dashboard quản lý, chưa xây ở phase này
├─ data/     # Dữ liệu sản phẩm, chính sách, dataset intent
├─ rules/    # Luật cứng: prompt, phase gate, luật sửa file, luật train
├─ docs/     # Tài liệu project
├─ models/   # Model train sau này
└─ deploy/   # File service VPS
```

## File Luật Cứng Cần Đọc Trước Khi Làm

```text
AGENTS.md
rules/README.md
rules/CORE_PROMPT.md
rules/PHASE_GATES.md
rules/FILE_EDITING_RULES.md
rules/AI_TRAINING_RULES.md
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
apps/web/src/app/dashboard/page.tsx # Dashboard quản lý bot
apps/web/src/app/chat/page.tsx      # Trang chat thử bot
apps/web/src/components             # Component UI chia theo dashboard/chat/layout
apps/web/src/lib                    # API client và type TypeScript
```

## Giao Diện Web

Local:

```text
http://127.0.0.1:3020/dashboard
http://127.0.0.1:3020/chat
```

VPS:

```text
MeowAI Python API: http://127.0.0.1:8010
MeowAI Next.js web: http://127.0.0.1:3020
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

Bước tiếp theo nên làm là Phase 3 - Dataset Intent:

- Mở rộng `data/intents/training_data.jsonl` từ khoảng 40 câu lên ít nhất 200 câu.
- Mỗi intent chính nên có ít nhất 15-20 câu.
- Thêm câu đời thường, viết tắt và sai chính tả nhẹ.
- Cập nhật `data/intents/labels.md` nếu thêm intent mới.

Sau khi Phase 3 đủ dữ liệu mới sang Phase 4 để train model bằng TF-IDF + Logistic Regression.
