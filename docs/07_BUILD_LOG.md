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
python run_chat.py
```

### Cách Test Ở Local Windows

```powershell
cd D:\MeowAI
$env:PYTHONIOENCODING='utf-8'
python -m unittest discover -s tests
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
