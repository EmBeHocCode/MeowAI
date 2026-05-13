# 09 - Từ Điển Giải Thích

## Intent

Ý định của người dùng.

Ví dụ:

```text
"gói nào rẻ nhất" -> intent hoi_gia
```

## Entity

Thông tin quan trọng trong câu hỏi.

Ví dụ:

```text
"gói VPS dưới 300k" -> entity: category=VPS, budget=300000
```

## Preprocess

Bước làm sạch và chuẩn hóa câu hỏi trước khi đưa vào model.

Ví dụ:

```text
"ck dc k" -> "chuyển khoản được không"
```

## Dataset

Tập dữ liệu dùng để train/test model.

## Model

Thành phần học từ dataset để dự đoán intent mới.

## Confidence

Độ tự tin của model khi đưa ra kết quả.

## Fallback

Cách xử lý khi bot không hiểu hoặc không chắc.

## API

Cầu nối để web gọi MeowAI.
