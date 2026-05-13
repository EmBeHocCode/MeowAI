# 13 - Lộ Trình Trưởng Thành Của MeowAI

File này mô tả MeowAI như một hệ thống học dần, không phải một đoạn code trả lời cứng.

Mục tiêu là giúp project có hướng phát triển rõ ràng: từ phôi, thành đứa trẻ biết học, rồi thành trợ lý shop có kỹ năng.

## Tư Duy Chính

MeowAI không nên được xây như một chatbot chỉ có `if/else`.

MeowAI nên được xây như một hệ thống có:

- Bộ não hiểu ý định.
- Trí nhớ cuộc trò chuyện.
- Kho kiến thức của shop.
- Bộ kỹ năng để xử lý từng việc.
- Tính cách trả lời riêng.
- Vòng học lại từ câu sai.

## Giai Đoạn 1 - Phôi

Tương ứng với Phase 0, Phase 1 và Phase 2.

MeowAI có hình hài ban đầu:

- Có cấu trúc project.
- Có API.
- Có dashboard.
- Có dữ liệu sản phẩm.
- Có rule-based chatbot.
- Có test cơ bản.

Ở giai đoạn này, MeowAI biết phản hồi theo luật, nhưng chưa thật sự học từ dữ liệu.

## Giai Đoạn 2 - Trẻ Sơ Sinh

Tương ứng với Phase 3 và Phase 4.

MeowAI bắt đầu học nhận diện ý định từ dataset:

- Hỏi giá.
- Hỏi tồn kho.
- Hỏi tư vấn sản phẩm.
- Hỏi thanh toán.
- Hỏi giao hàng.
- Hỏi bảo hành.
- Hỏi khuyến mãi.
- Câu mơ hồ hoặc câu cảm thán.

Mục tiêu của giai đoạn này là bot không chỉ dò từ khóa, mà bắt đầu đoán được khách đang muốn gì.

## Giai Đoạn 3 - Trẻ Nhỏ

Tương ứng với phase trí nhớ ngắn hạn.

MeowAI bắt đầu nhớ ngữ cảnh trong một cuộc chat:

- Khách vừa hỏi sản phẩm nào.
- Khách đang so sánh sản phẩm nào.
- Khách muốn giá rẻ, cấu hình mạnh hay dễ dùng.
- Các từ như "gói đó", "cái này", "rẻ hơn không" đang nói về điều gì.

Nếu thiếu thông tin, MeowAI phải biết hỏi lại thay vì đoán bừa.

## Giai Đoạn 4 - Học Sinh

Tương ứng với phase skill system.

MeowAI có nhiều kỹ năng riêng:

- Tư vấn sản phẩm.
- Tìm sản phẩm.
- So sánh sản phẩm.
- Kiểm tra giá.
- Kiểm tra tồn kho.
- Giải thích chính sách.
- Ghi lại câu chưa hiểu.
- Gợi ý câu dataset mới để train lại.

Ở giai đoạn này, MeowAI không chỉ trả lời, mà biết chọn kỹ năng phù hợp để xử lý câu hỏi.

## Giai Đoạn 5 - Trợ Lý Shop

Tương ứng với phase hỗ trợ admin.

MeowAI bắt đầu giúp chủ shop:

- Tóm tắt khách hỏi gì nhiều.
- Gợi ý sản phẩm nên đẩy lên trang chủ.
- Gợi ý nhóm sản phẩm nên khuyến mãi.
- Báo sản phẩm sắp hết hàng.
- Đọc số liệu dashboard và đưa nhận xét dễ hiểu.

## Giai Đoạn 6 - Học Lại Từ Sai Lầm

Tương ứng với phase self-improvement có kiểm soát.

Luồng học lại:

1. Khách hỏi câu MeowAI chưa hiểu.
2. MeowAI lưu câu đó vào log.
3. Admin vào dashboard gán intent đúng.
4. Câu mới được thêm vào dataset.
5. Train lại model.
6. MeowAI hiểu tốt hơn ở lần sau.

Điểm quan trọng: MeowAI không tự ý sửa não của mình nếu chưa có người duyệt.

## Cách Giải Thích Với Giảng Viên

MeowAI được phát triển theo hướng AI có vòng đời:

- Ban đầu là rule-based để chứng minh luồng xử lý.
- Sau đó có dataset để học intent.
- Tiếp theo có model machine learning nhỏ để phân loại ý định.
- Sau đó thêm trí nhớ, skill và dashboard gán nhãn.

Đây không phải chatbot gọi API AI bên ngoài. Đây là một hệ thống chatbot tự xây theo từng lớp, phù hợp với đồ án sinh viên.
