# MeowAI

MeowAI là project chatbot AI tự xây cho đồ án website bán hàng.

Mục tiêu của project này không phải tạo ra một ChatGPT mới. Mục tiêu là xây dựng một chatbot có thể:

- Hiểu ý định câu hỏi của khách hàng.
- Tìm thông tin trong dữ liệu sản phẩm, chính sách và FAQ của shop.
- Trả lời tự nhiên bằng tiếng Việt theo phong cách Meow.
- Không phụ thuộc vào API AI bên ngoài trong bản nộp đồ án.
- Có tài liệu rõ ràng để giải thích với giảng viên.

## Hướng Đi

Project sẽ đi theo lộ trình dễ hiểu:

1. Rule-based chatbot: dùng từ khóa và luật để nhận diện câu hỏi.
2. Intent classifier: train model nhỏ để phân loại ý định câu hỏi.
3. Database search: bot tìm sản phẩm/chính sách từ dữ liệu nội bộ.
4. Response generator: bot tạo câu trả lời theo template tự nhiên.
5. API service: web PHP/Next.js gọi MeowAI qua API nội bộ.

## Thư Mục Chính

```text
MeowAI/
├─ data/                 # Dataset và dữ liệu shop
├─ docs/                 # Kế hoạch, giải thích, báo cáo kỹ thuật
├─ models/               # Model đã train
├─ notebooks/            # Thử nghiệm, phân tích dữ liệu
├─ reports/              # Báo cáo, hình ảnh, kết quả test
├─ src/                  # Mã nguồn MeowAI
└─ tests/                # Test đơn giản
```

## Nguyên Tắc Code

- Code ngắn, rõ tên biến, ít "ảo thuật".
- Mỗi module làm một việc rõ ràng.
- Có file note giải thích trước khi code phức tạp.
- Mỗi phase hoàn thành phải có test và ghi lại vào `docs/07_BUILD_LOG.md`.

## Trạng Thái

Đang ở phase 1: chatbot terminal rule-based.

Chạy thử ở local Windows:

```powershell
cd D:\MeowAI
$env:PYTHONIOENCODING='utf-8'
python run_chat.py
```

Chạy test:

```powershell
cd D:\MeowAI
$env:PYTHONIOENCODING='utf-8'
python -m unittest discover -s tests
```

## Chạy API Trên VPS

MeowAI API chạy nội bộ trên VPS tại:

```text
http://127.0.0.1:8010
```

Endpoint chính:

```text
GET  /health
POST /chat
```

Ví dụ test trên terminal VPS `/var/www/MeowAI`:

```bash
curl http://127.0.0.1:8010/health
curl -X POST http://127.0.0.1:8010/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"VPS Ryzen Basic giá bao nhiêu?"}'
```

Service dùng `uvicorn --reload`, nên khi mã nguồn Python thay đổi trên VPS, bot sẽ tự reload để nhận code mới mà không cần restart thủ công.
