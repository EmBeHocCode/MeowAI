# 06 - Kế Hoạch API Và Tích Hợp Web

## Mục Tiêu

Sau khi MeowAI chạy được bằng terminal, mình bọc nó thành API để web gọi.

## API Dự Kiến

```text
POST /chat
```

Request:

```json
{
  "message": "gói nào rẻ nhất shop",
  "session_id": "customer-001"
}
```

Response:

```json
{
  "reply": "Dạ gói rẻ nhất hiện tại là Cloud Server Starter 1, giá 179.000đ/tháng nha.",
  "intent": "hoi_gia",
  "confidence": 0.92
}
```

## Khi Web Và MeowAI Cùng VPS

Web gọi nội bộ:

```text
http://127.0.0.1:9000/chat
```

Ưu điểm:

- An toàn hơn.
- Không mở API ra internet.
- Tốc độ tốt.

## Khi Web Ở Host Khác

Cần proxy qua Nginx:

```text
https://ai-domain.com/chat
```

Cần thêm:

- API key nội bộ.
- Rate limit.
- Log lỗi.
- Không public endpoint quản trị.

## Điều Cần Ghi Trong Báo Cáo

> Website và MeowAI giao tiếp với nhau thông qua REST API nội bộ. Điều này giúp tách riêng phần giao diện web và phần xử lý AI, giúp hệ thống dễ bảo trì và mở rộng.
