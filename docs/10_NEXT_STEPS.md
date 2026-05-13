# 10 - Bước Tiếp Theo Gần Nhất

Đây là danh sách việc cần làm tiếp theo, ưu tiên theo thứ tự.

## Bước 1 - Làm Rule-Based Chatbot

Mục tiêu:

- Nhập câu hỏi trong terminal.
- Bot chuẩn hóa câu hỏi.
- Bot nhận diện intent bằng rule.
- Bot trả lời bằng template.

File sẽ tạo:

```text
src/preprocess.py
src/intent_rules.py
src/product_search.py
src/response_templates.py
src/chat_engine.py
run_chat.py
```

## Bước 2 - Test Bằng 10 Câu Mẫu

Câu test:

```text
gói nào rẻ nhất shop
ck dc k
còn hàng không
mình cần gói chạy web nhỏ
đổi trả sao vậy
bh ntn
có coupon không
shop ở đâu
bao lâu nhận được
web mới nên dùng gói nào
```

## Bước 3 - Viết Giải Thích Cho Báo Cáo

Sau khi bot terminal chạy được, thêm vào `docs/07_BUILD_LOG.md`:

- Đã tạo module nào.
- Bot xử lý luồng câu hỏi ra sao.
- Câu nào bot trả lời đúng.
- Câu nào cần cải thiện.

## Bước 4 - Mới Train Model

Chỉ train sau khi rule-based đã chạy ổn, vì lúc đó mình đã hiểu:

- Intent nào cần có.
- Dataset thiếu cái gì.
- Câu hỏi thực tế của khách thường như thế nào.
