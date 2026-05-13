# 08 - Hướng Dẫn Trình Bày Với Giảng Viên

## Cách Nói Ngắn Gọn Về Project

> Đề tài của em là xây dựng chatbot tư vấn khách hàng cho website thương mại điện tử. Chatbot được xây dựng theo hướng xử lý ngôn ngữ tự nhiên nội bộ, gồm các bước tiền xử lý câu hỏi, phân loại ý định, truy vấn dữ liệu sản phẩm và sinh câu trả lời theo ngữ cảnh.

## Nếu Giảng Viên Hỏi: "Em Có Dùng API AI Không?"

Trả lời:

> Bản nộp đồ án của em không phụ thuộc vào API AI bên ngoài. Em xây dựng phần phân loại ý định và logic trả lời nội bộ. Nếu sau này mở rộng sản phẩm thực tế, em có thể thêm tùy chọn kết nối LLM API, nhưng không phải phần cốt lõi của đồ án.

## Nếu Giảng Viên Hỏi: "Train Ở Đâu?"

Trả lời:

> Em train model phân loại ý định từ tập dữ liệu câu hỏi mẫu của khách hàng. Mỗi mẫu gồm câu hỏi và nhãn intent. Model học cách phân loại câu hỏi vào các nhóm như hỏi giá, hỏi tồn kho, tư vấn sản phẩm, thanh toán, giao hàng và đổi trả.

## Nếu Giảng Viên Hỏi: "Sao Bot Trả Lời Được Giá Sản Phẩm?"

Trả lời:

> Sau khi nhận diện intent, chatbot truy vấn dữ liệu sản phẩm trong database/nội bộ. Câu trả lời không được bịa ra mà được tạo từ dữ liệu thật của hệ thống.

## Nếu Giảng Viên Hỏi: "Khác Gì Chatbot Rule Đơn Giản?"

Trả lời:

> Hệ thống có hai tầng. Tầng đầu là tiền xử lý và rule fallback để đảm bảo bot luôn hoạt động. Tầng thứ hai là model phân loại intent được train từ dataset. Nhờ vậy bot có thể hiểu nhiều cách diễn đạt khác nhau của khách hàng thay vì chỉ khớp từ khóa đơn giản.

## Demo Nên Chuẩn Bị

Nên có các câu test:

```text
gói nào rẻ nhất shop
ck được không
còn hàng không
em cần gói chạy web nhỏ
đổi trả sao vậy
bh ntn
```

Với mỗi câu, hiển thị:

- Câu hỏi gốc.
- Câu hỏi sau chuẩn hóa.
- Intent dự đoán.
- Confidence.
- Dữ liệu sản phẩm/chính sách tìm được.
- Câu trả lời cuối.
