# 01 - Timeline Phát Triển

Timeline này chia thành các phase nhỏ để mỗi bước đều có kết quả rõ ràng.

## Phase 0 - Lập Kế Hoạch Và Khung Project

Mục tiêu:

- Tạo cấu trúc project.
- Viết tài liệu tổng quan.
- Xác định luồng xử lý của chatbot.

Kết quả cần có:

- `README.md`
- `docs/00_PROJECT_OVERVIEW.md`
- `docs/01_TIMELINE.md`
- `docs/02_ARCHITECTURE.md`
- `docs/03_DATASET_PLAN.md`
- `AGENTS.md`
- `rules/`

Trạng thái: Gần hoàn thành.

## Phase 1 - Chatbot Rule-Based Đầu Tiên

Mục tiêu:

- Bot nhận câu hỏi text.
- Chuẩn hóa câu hỏi: viết tắt, chữ thường, dấu câu.
- Nhận diện intent bằng từ khóa.
- Trả lời bằng template.

Ví dụ:

```text
User: gói nào rẻ nhất shop
Bot: Dạ gói rẻ nhất hiện tại là Cloud Server Starter 1, giá 179.000đ/tháng nha.
```

Kết quả cần có:

- `apps/bot/src/preprocess.py`
- `apps/bot/src/intent_rules.py`
- `apps/bot/src/response_templates.py`
- `apps/bot/src/chat_engine.py`
- Test bằng terminal.

Điều kiện qua phase:

- Bot hiểu đủ 10 câu hỏi mẫu trong `docs/10_NEXT_STEPS.md`.
- Có test tự động cho các câu quan trọng.
- Viết tắt phổ biến như `ck`, `dc`, `bh`, `ntn` được xử lý.
- Không còn lỗi chọn sản phẩm quá bừa ở các câu hỏi mơ hồ.

## Phase 2 - Dữ Liệu Shop Mẫu

Mục tiêu:

- Tạo dữ liệu sản phẩm mẫu.
- Tạo chính sách shop.
- Cho bot tìm sản phẩm theo giá, danh mục, nhu cầu.

Kết quả cần có:

- `data/shop/products.csv`
- `data/shop/policies.md`
- `apps/bot/src/product_search.py`

## Phase 3 - Dataset Intent

Mục tiêu:

- Tạo dataset câu hỏi khách hàng.
- Mỗi câu có nhãn intent.
- Có nhiều cách nói đời thường, viết tắt, sai chính tả nhẹ.

Kết quả cần có:

- `data/intents/training_data.jsonl`
- `data/intents/labels.md`
- Ít nhất 200 câu mẫu ban đầu.

## Phase 4 - Train Intent Classifier

Mục tiêu:

- Train model nhỏ để phân loại intent.
- Lưu model vào `models/`.
- Đo độ chính xác bằng tập test.

Công nghệ đề xuất:

- Python
- scikit-learn
- TF-IDF
- Logistic Regression hoặc Linear SVM

Kết quả cần có:

- `apps/bot/src/train_intent.py`
- `models/intent_classifier.pkl`
- Báo cáo kết quả trong `reports/intent_metrics.md`

Lưu ý:

- Không được bắt đầu train nếu dataset chưa đủ ít nhất 200 câu.
- Không dùng API AI bên ngoài để thay thế phần train intent classifier.

## Phase 5 - API Nội Bộ

Mục tiêu:

- Tạo API `/chat`.
- Web gọi MeowAI qua HTTP.
- Không gọi OpenAI/Gemini/Groq.

Công nghệ đề xuất:

- FastAPI
- Uvicorn

Kết quả cần có:

- `apps/bot/src/api.py`
- Endpoint `POST /chat`
- Hướng dẫn tích hợp web.

## Phase 6 - Tích Hợp Website

Mục tiêu:

- Web gửi câu hỏi của khách sang MeowAI.
- MeowAI trả câu trả lời.
- Giao diện chat hiển thị kết quả.

Kết quả cần có:

- Chat widget hoạt động.
- Có log hỏi/đáp.
- Có fallback khi bot không hiểu.

## Phase 7 - Báo Cáo Và Trình Bày

Mục tiêu:

- Viết thuyết minh hệ thống.
- Vẽ sơ đồ kiến trúc.
- Chuẩn bị demo.
- Chuẩn bị câu trả lời khi giảng viên hỏi.

Kết quả cần có:

- `reports/final_report_outline.md`
- `docs/08_PRESENTATION_GUIDE.md`
