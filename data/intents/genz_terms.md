# Gen Z Terms - Từ Viết Tắt Và Cách Nói Đời Thường

File này dùng để ghi lại các từ/cụm từ khách hàng trẻ có thể dùng khi chat với MeowAI.

Mục tiêu là giúp Phase 3 có dữ liệu tự nhiên hơn, không chỉ gồm câu hỏi sách giáo khoa.

## Viết Tắt Phổ Biến

| Từ | Nghĩa gần đúng | Ghi chú |
| --- | --- | --- |
| `ck` | chuyển khoản | Liên quan thanh toán |
| `dc` | được | Có thể xuất hiện trong nhiều intent |
| `k` | không | Nên chuẩn hóa cẩn thận |
| `ko` | không | Biến thể của `không` |
| `khum` | không | Cách nói thân mật |
| `bn` | bao nhiêu | Thường dùng khi hỏi giá |
| `bh` | bảo hành | Cũng có thể là "bây giờ" tùy ngữ cảnh |
| `ntn` | như thế nào | Thường hỏi cách dùng/chính sách |
| `ib` | inbox | Thường yêu cầu liên hệ riêng |
| `rep` | trả lời | Thường là small talk hoặc yêu cầu hỗ trợ |

## Từ Gen Z / Cách Nói Thân Mật

| Từ/cụm từ | Nghĩa gần đúng | Intent có thể gặp |
| --- | --- | --- |
| `ổn áp` | ổn, đáng dùng | tư vấn, cảm xúc do dự |
| `xịn sò` | tốt, chất lượng | small talk, tư vấn |
| `slay` | khen vui, ấn tượng | small talk |
| `lụm` | mua/chọn | khuyến mãi, tư vấn |
| `chốt` | quyết định mua | thanh toán, tồn kho |
| `chốt đơn` | xác nhận mua | thanh toán |
| `mềm hơn` | rẻ hơn | hỏi rẻ hơn |
| `chát` | đắt | hỏi rẻ hơn, cảm xúc do dự |
| `cấn` | thấy chưa ổn, còn nghi ngại | cảm xúc do dự |
| `real` | thật, đúng không | hỏi giá, câu hỏi khó |
| `ní` | bạn/anh/chị theo cách thân mật | small talk |
| `bro` | bạn theo cách thân mật | small talk |

## Câu Hỏi Hóc Búa Nên Dạy Bot

- Vì sao nên tin shop?
- Nếu web bị sập lúc nửa đêm thì sao?
- Shop có đảm bảo dữ liệu không mất không?
- Nếu traffic tăng đột biến thì gói nào chịu được?
- Nếu bị tấn công DDoS thì xử lý sao?
- Shop có đọc được dữ liệu riêng của khách không?
- Gói rẻ nhất có đủ chạy production không?
- Nếu sau này nâng cấp thì có downtime không?

## Nguyên Tắc Khi Thêm Từ Mới

- Không thêm từ nhạy cảm, xúc phạm hoặc riêng tư vào dataset.
- Nếu một từ có nhiều nghĩa, ghi chú rõ ngữ cảnh.
- Mỗi từ nên có vài câu ví dụ trong `training_data.jsonl`.
- Nếu thêm intent mới, phải cập nhật `data/intents/labels.md`.
