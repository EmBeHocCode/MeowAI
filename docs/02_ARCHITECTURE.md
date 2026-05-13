# 02 - Kiến Trúc Hệ Thống

## Kiến Trúc Tổng Quan

```text
Người dùng trên website
        |
        v
Chat Widget
        |
        v
Backend Web
        |
        v
MeowAI API
        |
        +--> Preprocess: chuẩn hóa câu hỏi
        +--> Intent Detector: nhận diện ý định
        +--> Entity Extractor: lấy từ khóa sản phẩm, giá, nhu cầu
        +--> Knowledge/Search: tìm dữ liệu shop
        +--> Response Generator: tạo câu trả lời
        |
        v
Trả lời về website
```

## Các Module Chính

### 1. Preprocess

Làm sạch câu hỏi của khách:

- Đưa về chữ thường.
- Xóa dấu câu không cần thiết.
- Chuẩn hóa viết tắt: `ko -> không`, `dc -> được`, `ck -> chuyển khoản`.
- Tách từ khóa quan trọng.

### 2. Intent Detector

Nhận diện khách đang muốn hỏi gì.

Ví dụ intent:

- `hoi_gia`
- `hoi_ton_kho`
- `tu_van_san_pham`
- `thanh_toan`
- `giao_hang`
- `doi_tra`
- `bao_hanh`
- `khuyen_mai`
- `fallback`

### 3. Entity Extractor

Lấy thông tin quan trọng trong câu hỏi.

Ví dụ:

```text
"gói VPS nào dưới 300k chạy web ổn"
```

Có thể rút ra:

- Nhóm sản phẩm: VPS
- Ngân sách: dưới 300k
- Nhu cầu: chạy web

### 4. Knowledge/Search

Tìm trong dữ liệu nội bộ:

- Sản phẩm.
- Danh mục.
- Giá.
- Tồn kho.
- Chính sách.
- Coupon.

### 5. Response Generator

Tạo câu trả lời tự nhiên theo phong cách Meow.

Nguyên tắc:

- Ngắn gọn.
- Không bịa.
- Nếu không chắc thì hỏi lại.
- Nếu có sản phẩm phù hợp thì đưa tên, giá, lý do.

## Vì Sao Kiến Trúc Này Phù Hợp Đồ Án

- Dễ giải thích với giảng viên.
- Mỗi module có vai trò riêng.
- Có thể làm từng bước.
- Không cần GPU mạnh.
- Có thể chứng minh "tự xây AI" thông qua model phân loại intent và logic xử lý nội bộ.
