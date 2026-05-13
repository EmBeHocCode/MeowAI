# AI Training Rules - Luật Train MeowAI

MeowAI cần được xây theo hướng dễ hiểu, phù hợp đồ án sinh viên.

## Không Train ChatGPT Từ Đầu

Project này không cố tự tạo một mô hình ngôn ngữ lớn như ChatGPT, Gemini hay Claude.

Lý do:

- Cần dữ liệu rất lớn.
- Cần GPU mạnh.
- Chi phí cao.
- Khó giải thích và bảo trì trong đồ án sinh viên.

## Hướng Train Đúng Cho MeowAI

MeowAI sẽ train theo hướng nhỏ và thực tế:

1. Thu thập câu hỏi khách hàng.
2. Gán nhãn intent cho từng câu.
3. Train intent classifier.
4. Dùng intent để chọn dữ liệu và template trả lời.
5. Đánh giá kết quả bằng tập test.

## Model Đầu Tiên Nên Dùng

Ưu tiên:

- TF-IDF Vectorizer.
- Logistic Regression.

Lý do:

- Dễ hiểu.
- Không cần GPU.
- Chạy được trên máy sinh viên và VPS nhỏ.
- Dễ trình bày với giảng viên.

## Dataset Tối Thiểu

Trước khi train, cần:

- Ít nhất 200 câu hỏi mẫu.
- Mỗi intent chính có ít nhất 15-20 câu.
- Có câu viết tắt: `ck`, `dc`, `k`, `bh`, `ntn`.
- Có câu sai chính tả nhẹ.
- Có câu fallback không thuộc nhóm nào.

## Không Được Làm

- Không dùng OpenAI/Gemini API rồi gọi đó là tự train.
- Không train khi dataset chỉ có vài chục câu.
- Không đưa dữ liệu nhạy cảm của khách hàng vào dataset.
- Không để model trả lời bịa khi không tìm thấy dữ liệu.

## Cách Giải Thích Với Giảng Viên

MeowAI dùng machine learning ở phần phân loại ý định câu hỏi.

Luồng xử lý:

```text
Câu hỏi khách hàng
-> tiền xử lý văn bản
-> model phân loại intent
-> tìm dữ liệu sản phẩm/chính sách
-> tạo câu trả lời bằng template
```

Đây là cách làm phù hợp với chatbot tư vấn bán hàng vì bot cần trả lời đúng dữ liệu shop hơn là nói chuyện lan man.

