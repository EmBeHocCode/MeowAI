# 04 - Kế Hoạch Train Model

## Mục Tiêu Train

MeowAI không train một LLM lớn. MeowAI train model nhỏ cho tác vụ:

```text
Câu hỏi của khách -> intent
```

Ví dụ:

```text
"gói nào rẻ nhất" -> hoi_gia
"ck dc k" -> thanh_toan
"còn hàng không" -> hoi_ton_kho
```

## Model Đề Xuất

Bản đầu dùng pipeline dễ hiểu:

```text
TF-IDF Vectorizer + Logistic Regression
```

Lý do:

- Dễ giải thích.
- Chạy nhẹ trên laptop/VPS.
- Không cần GPU.
- Train nhanh.
- Phù hợp đồ án sinh viên.

## Luồng Train

```text
training_data.jsonl
        |
        v
Tiền xử lý text
        |
        v
TF-IDF biến text thành vector số
        |
        v
Logistic Regression học phân loại intent
        |
        v
Lưu model vào models/intent_classifier.pkl
```

## Chỉ Số Đánh Giá

Cần có:

- Accuracy: tỷ lệ đoán đúng intent.
- Confusion matrix: intent nào hay bị nhầm.
- Test samples: một số câu hỏi thủ công.

## Khi Model Không Chắc

Nếu confidence thấp:

```text
Bot không đoán bừa.
Bot hỏi lại một câu ngắn gọn.
```

Ví dụ:

```text
Dạ ý anh là hỏi bảo hành hay hỏi bao giờ nhận hàng ạ?
```

## Cách Giải Thích Với Giảng Viên

> Hệ thống sử dụng tập dữ liệu câu hỏi mẫu để huấn luyện mô hình phân loại ý định. Sau khi xác định intent, chatbot truy vấn dữ liệu nội bộ và sinh câu trả lời bằng các mẫu phản hồi được thiết kế riêng cho ngữ cảnh bán hàng.
