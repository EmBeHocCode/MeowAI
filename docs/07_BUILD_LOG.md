# 07 - Build Log

File này dùng để ghi lại mình đã làm gì. Mỗi lần hoàn thành một mốc nhỏ, ghi vào đây.

## 2026-05-13

### Đã Làm

- Tạo khung project `MeowAI`.
- Tạo bộ tài liệu kế hoạch ban đầu.
- Xác định hướng đi: chatbot e-commerce tự xây, không phụ thuộc API AI bên ngoài.
- Upload project lên VPS tại `/var/www/MeowAI`.
- Thêm note workflow VS Code Remote SSH.
- Soát lại tài liệu và chuyển sang tiếng Việt có dấu.

### Quyết Định Kỹ Thuật

- Bản đầu dùng Python cho phần train vì dễ học và có scikit-learn.
- Model đầu tiên sẽ là TF-IDF + Logistic Regression.
- Bot sẽ có rule-based version trước khi train model.

### Việc Tiếp Theo

- Tạo dataset intent mẫu.
- Tạo data sản phẩm mẫu.
- Viết chatbot terminal ban đầu.

### Cập Nhật Phase 1

- Tạo chatbot terminal rule-based đầu tiên.
- Thêm `src/preprocess.py` để chuẩn hóa câu hỏi: chữ thường, bỏ dấu, bỏ ký tự đặc biệt, chuẩn hóa viết tắt.
- Thêm `src/intent_rules.py` để nhận diện intent bằng từ khóa.
- Thêm `src/product_search.py` để đọc `products.csv` và tìm sản phẩm liên quan.
- Thêm `src/response_templates.py` để gom các mẫu câu trả lời.
- Thêm `src/chat_engine.py` để điều phối luồng xử lý: câu hỏi -> intent -> dữ liệu -> câu trả lời.
- Thêm `run_chat.py` để chạy bot trực tiếp trên terminal.
- Thêm `tests/test_phase1_chatbot.py` để kiểm tra nhanh intent và câu trả lời cơ bản.

### Cách Giải Thích Với Giảng Viên

- Đây là bản rule-based, nghĩa là bot chưa dùng machine learning mà dùng luật từ khóa rõ ràng.
- Mục tiêu của phase này là chứng minh luồng xử lý chatbot hoạt động end-to-end.
- Khi phase này ổn, project mới chuyển sang train intent classifier bằng TF-IDF + Logistic Regression.

### Cách Chạy Ở Local Windows

```powershell
cd D:\MeowAI
$env:PYTHONIOENCODING='utf-8'
python apps\bot\run_chat.py
```

### Cách Test Ở Local Windows

```powershell
cd D:\MeowAI
$env:PYTHONIOENCODING='utf-8'
python -m unittest discover -s apps\bot\tests
```

### Cập Nhật Chạy Thường Trực Trên VPS

- Thêm `src/api.py` để bọc ChatEngine thành HTTP API.
- Thêm endpoint `GET /health` để kiểm tra service.
- Thêm endpoint `POST /chat` để website gửi câu hỏi và nhận câu trả lời.
- Thêm `requirements.txt` gồm FastAPI và Uvicorn.
- Thêm file mẫu systemd service tại `deploy/meowai-api.service`.
- Service trên VPS sẽ chạy bằng `uvicorn --reload` tại `127.0.0.1:8010`.

### Ghi Chú Kỹ Thuật Về Auto Reload

- Python không tự thay đổi code bên trong tiến trình đang chạy.
- Cách đúng cho giai đoạn học/demo là dùng `uvicorn --reload`.
- Khi file `.py` thay đổi trên VPS, Uvicorn tự phát hiện và reload lại app.
- Em không cần restart service thủ công sau mỗi lần sửa code.

### Đã Cấu Hình Trên VPS

- Cài `python3.10-venv` để tạo môi trường Python riêng.
- Tạo virtual environment tại `/var/www/MeowAI/.venv`.
- Cài dependency từ `requirements.txt`.
- Tạo systemd service `meowai-api.service`.
- Service đang chạy nội bộ tại `http://127.0.0.1:8010`.
- Đã test `GET /health` trả về trạng thái OK.
- Đã test `POST /chat` trả lời được câu hỏi giá sản phẩm.

### Refactor Theo Cấu Trúc Bot/Web

- Tham khảo cấu trúc `ZALO-BotChat`, tách MeowAI thành dạng monorepo nhỏ.
- Chuyển code bot từ `src/` sang `apps/bot/src/`.
- Chuyển file chạy terminal từ `run_chat.py` sang `apps/bot/run_chat.py`.
- Chuyển test từ `tests/` sang `apps/bot/tests/`.
- Thêm `apps/web/README.md` để dành chỗ cho dashboard quản lý ở phase sau.
- Cập nhật service VPS để chạy API bằng `apps.bot.src.api:app`.

### Cách Giải Thích Với Giảng Viên

- Project được tách thành hai phần rõ ràng: `apps/bot` xử lý thuật toán chatbot, `apps/web` dành cho dashboard quản lý.
- Cách tách này giúp code dễ mở rộng: sau này thêm dashboard không làm rối phần thuật toán bot.
- Bot API vẫn chạy độc lập trên VPS, dashboard chỉ gọi API để quản lý và test bot.

### Dọn Lại Trạng Thái Project

- Dọn thư mục cache Python cũ trên VPS sau khi refactor, nên root không còn `src/` và `tests/` cũ.
- Thêm `docs/12_CURRENT_STATUS.md` để tóm tắt project đang ở đâu, bot chạy kiểu gì và bước tiếp theo là gì.

### Thêm Luật Cứng Cho Dev/Codex

- Thêm `AGENTS.md` ở gốc project để dev/Codex biết phải đọc luật trước khi sửa.
- Thêm thư mục `rules/` để chứa prompt cứng, phase gate, luật sửa file và luật train AI.
- Cập nhật `README.md`, `docs/12_CURRENT_STATUS.md` và `docs/01_TIMELINE.md` để nhắc rõ quy trình phát triển theo phase.
- Quyết định: trước khi train model, project phải hoàn thiện Phase 1 và có dataset đủ tốt.

### Thêm Giao Diện Chat Thử

- Thêm `apps/web/index.html` làm giao diện chat thử MeowAI trên trình duyệt.
- Thêm `apps/web/static/app.css` và `apps/web/static/app.js` cho giao diện và xử lý gọi API.
- Cập nhật `apps/bot/src/api.py` để phục vụ giao diện tại `/` và static files tại `/static`.
- Giao diện gọi cùng endpoint `POST /chat`, nên không cần nhập câu hỏi trong CMD nữa khi demo.

### Tách Web Thành Cấu Trúc Dashboard Rõ Ràng

- Tách giao diện web thành `apps/web/pages/` và `apps/web/static/`.
- Thêm trang `/dashboard` để xem trạng thái bot, số sản phẩm, số câu dataset, danh sách intent và bảng sản phẩm.
- Thêm trang `/chat` để chat thử với bot.
- Tách CSS thành `base.css`, `layout.css`, `components.css`, `dashboard.css`, `chat.css`.
- Tách JS thành `api-client.js`, `ui.js`, `dashboard-page.js`, `chat-page.js`.
- Thêm API dashboard: `/api/dashboard/summary`, `/api/products`, `/api/intents`.

### Chuyển Web Sang Next.js TSX

- Chuyển `apps/web` từ HTML tĩnh sang Next.js App Router bằng TSX.
- Thêm cấu trúc giống hướng `ZALO-BotChat/apps/web`: `src/app`, `src/components`, `src/lib`.
- Thêm trang `src/app/dashboard/page.tsx` cho dashboard.
- Thêm trang `src/app/chat/page.tsx` cho chat thử.
- Thêm proxy `src/app/api/meowai/[...path]/route.ts` để web gọi Python API qua server Next.js.
- Giữ Python FastAPI làm API backend, không phục vụ HTML tĩnh nữa.
- Thêm `deploy/meowai-web.service` để chạy web Next.js trên VPS tại `127.0.0.1:3020`.
