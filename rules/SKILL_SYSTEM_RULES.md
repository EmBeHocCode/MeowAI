# Skill System Rules - Luật Xây Skill Cho MeowAI

File này là luật cứng khi thêm skill mới cho MeowAI.

## Skill Là Gì

Skill là một năng lực nhỏ, có mục tiêu rõ ràng.

Ví dụ:

- Tìm sản phẩm.
- Trả lời giá.
- Kiểm tra tồn kho.
- Tư vấn sản phẩm.
- Ghi log câu chưa hiểu.

Không gọi một khối code mơ hồ là skill nếu không mô tả được nó làm gì.

## Mỗi Skill Phải Có

Trước khi code skill mới, phải xác định:

- Skill giải quyết vấn đề gì.
- Skill nhận input gì.
- Skill dùng dữ liệu nào.
- Skill trả output gì.
- Skill thuộc phase nào.
- Skill có test tối thiểu nào.

## Không Được Làm

- Không gom tất cả skill vào một file lớn.
- Không sửa nhiều skill cùng lúc nếu không cần.
- Không thêm skill vượt phase hiện tại.
- Không để skill bịa thông tin không có trong dữ liệu.
- Không để skill tự ghi đè dataset hoặc model nếu chưa có bước duyệt.

## Thứ Tự Ưu Tiên Skill

1. Skill giúp bot hiểu đúng câu hỏi.
2. Skill giúp bot lấy đúng dữ liệu shop.
3. Skill giúp bot trả lời tự nhiên hơn.
4. Skill giúp bot học lại từ lỗi sai.
5. Skill hỗ trợ admin quản lý shop.

## Quy Tắc Test

Mỗi skill mới nên có ít nhất một test.

Nếu skill ảnh hưởng đến câu trả lời của bot, phải test qua `ChatEngine`.

Nếu skill chỉ xử lý dữ liệu, có thể test riêng function đó.

## Cách Giải Thích Với Giảng Viên

Skill system giúp chatbot không bị viết cứng thành một đống điều kiện.

Mỗi kỹ năng được tách riêng nên:

- Dễ đọc.
- Dễ sửa.
- Dễ test.
- Dễ mở rộng.
- Phù hợp để trình bày đồ án.
