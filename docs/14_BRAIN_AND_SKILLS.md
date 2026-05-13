# 14 - Bộ Não Và Skill Của MeowAI

File này định nghĩa MeowAI như một hệ thống có nhiều tầng xử lý.

Mỗi tầng có nhiệm vụ riêng để bot tự nhiên hơn và dễ mở rộng hơn.

## Luồng Bộ Não

```text
Người dùng hỏi
↓
Chuẩn hóa câu
↓
Hiểu intent
↓
Đọc trí nhớ cuộc chat
↓
Chọn skill phù hợp
↓
Lấy dữ liệu shop
↓
Tạo câu trả lời theo phong cách MeowAI
↓
Ghi log để học lại
```

## Tầng 1 - Chuẩn Hóa Câu

Mục tiêu:

- Chuyển chữ về dạng dễ xử lý.
- Bỏ dấu khi cần.
- Hiểu viết tắt phổ biến.
- Giảm lỗi do khách gõ nhanh.

Ví dụ:

- `ck` -> `chuyển khoản`
- `dc` -> `được`
- `bh` -> `bảo hành`
- `ntn` -> `như thế nào`

## Tầng 2 - Hiểu Intent

Intent là ý định của người dùng.

Ví dụ:

- `hoi_gia`: khách hỏi giá.
- `hoi_ton_kho`: khách hỏi còn hàng không.
- `tu_van_san_pham`: khách muốn được tư vấn.
- `giao_hang`: khách hỏi thời gian bàn giao.
- `fallback`: bot chưa hiểu rõ.

Phase hiện tại dùng rule-based. Phase sau sẽ train intent classifier.

## Tầng 3 - Trí Nhớ

Trí nhớ giúp bot hiểu câu sau dựa trên câu trước.

Ví dụ:

```text
Khách: VPS Ryzen Basic giá bao nhiêu?
MeowAI: Dạ VPS Ryzen Basic hiện có giá 329.000đ nha.
Khách: gói đó còn hàng không?
```

Nếu có trí nhớ, MeowAI hiểu "gói đó" là `VPS Ryzen Basic`.

## Tầng 4 - Skill System

Skill là kỹ năng xử lý một nhóm nhiệm vụ cụ thể.

Mỗi skill nên có:

- Tên skill.
- Intent liên quan.
- Dữ liệu cần dùng.
- Kết quả trả về.
- Câu trả lời mẫu.
- Test cơ bản.

## Skill Cần Có

### `product_search`

Tìm sản phẩm theo tên, danh mục, mô tả và nhu cầu.

### `price_answer`

Trả lời giá sản phẩm hoặc gói rẻ nhất.

### `stock_check`

Kiểm tra tồn kho.

### `product_consult`

Tư vấn sản phẩm phù hợp với nhu cầu khách.

### `policy_answer`

Trả lời chính sách thanh toán, giao hàng, đổi trả, bảo hành và khuyến mãi.

### `conversation_memory`

Ghi nhớ sản phẩm hoặc nhu cầu vừa nhắc trong phiên chat.

### `unknown_question_logger`

Ghi lại câu bot chưa hiểu để admin dạy lại sau.

### `dataset_suggestion`

Gợi ý biến câu hỏi chưa hiểu thành dòng dataset mới.

## Tầng 5 - Phong Cách Trả Lời

MeowAI nên trả lời:

- Tiếng Việt tự nhiên.
- Ngắn gọn.
- Thân thiện.
- Không bịa dữ liệu.
- Biết hỏi lại khi thiếu thông tin.
- Có phong cách riêng nhưng không quá đà.

## Nguyên Tắc Không Được Làm

- Không để bot đoán giá nếu dữ liệu không có.
- Không để bot tự sửa dataset khi chưa có người duyệt.
- Không để bot truy cập dữ liệu nhạy cảm.
- Không trộn hết logic vào một file lớn.
- Không làm skill mới nếu chưa ghi rõ mục tiêu và test.

## Mốc Gần Nhất

Mốc tiếp theo là Phase 3:

- Mở rộng dataset intent.
- Thêm câu mơ hồ, câu cảm thán và câu viết tắt.
- Chuẩn bị dữ liệu cho model phân loại intent.
- Chưa train model nếu dataset chưa đủ.
