# 03 - Kế Hoạch Dữ Liệu

## Dữ Liệu Cần Có

MeowAI cần 3 nhóm dữ liệu chính.

## 1. Dataset Intent

Dùng để train model phân loại ý định câu hỏi.

File dự kiến:

```text
data/intents/training_data.jsonl
```

Định dạng:

```json
{"text":"gói nào rẻ nhất shop","intent":"hoi_gia"}
{"text":"ck được không","intent":"thanh_toan"}
{"text":"còn hàng không vậy","intent":"hoi_ton_kho"}
```

## 2. Dữ Liệu Sản Phẩm

Dùng để bot tư vấn và trả lời theo database.

File dự kiến:

```text
data/shop/products.csv
```

Cột dự kiến:

```text
id,name,category,price,stock,description,use_cases,url
```

## 3. Chính Sách Shop

Dùng để trả lời những câu như giao hàng, đổi trả, thanh toán.

File dự kiến:

```text
data/shop/policies.md
```

Nội dung:

- Thanh toán.
- Giao hàng.
- Đổi trả.
- Bảo hành.
- Hoàn tiền.
- Hỗ trợ khách hàng.

## Nguyên Tắc Viết Dataset

Mỗi intent nên có nhiều cách nói:

### Intent `hoi_gia`

```text
giá bao nhiêu
bao tiền vậy shop
có gói nào rẻ nhất không
mình muốn xem bảng giá
gói này nhiêu tiền
```

### Intent `thanh_toan`

```text
ck được không
có momo không shop
thanh toán sao vậy
trả tiền bằng gì
có chuyển khoản ngân hàng không
```

### Intent `tu_van_san_pham`

```text
mình cần gói chạy web nhỏ
gói nào hợp cho sinh viên
nên mua gói nào để làm shop online
có gói nào rẻ mà ổn không
tư vấn cho mình gói phù hợp
```

## Mục Tiêu Số Lượng

Bản đầu:

- 8 intent.
- Mỗi intent 25 câu.
- Tổng khoảng 200 câu.

Sau khi test:

- Câu nào bot hiểu sai thì thêm vào dataset.
- Tăng dần lên 500-1000 câu.

## Nhóm Câu Đời Thường Cần Có

Dataset không chỉ gồm câu hỏi chuẩn. MeowAI cần học thêm các kiểu nói khách hàng thật hay dùng:

- Viết tắt: `ck`, `dc`, `k`, `ko`, `bn`, `bh`, `ntn`, `ib`, `rep`.
- Gen Z/thân mật: `ổn áp`, `xịn sò`, `slay`, `lụm`, `chốt`, `mềm hơn`, `chát`, `cấn`, `real`, `ní`.
- Câu mơ hồ: "hmm", "cái đó sao", "mình không biết hỏi sao".
- Câu do dự: "mắc quá", "mình còn phân vân", "sợ mua về không biết dùng".
- Câu hóc búa: "vì sao nên tin shop", "nếu web sập lúc nửa đêm thì sao".

Các từ/cụm từ này được ghi riêng tại:

```text
data/intents/genz_terms.md
```

## Lưu Ý Bảo Mật

Nếu dùng tin nhắn khách hàng thật:

- Xóa số điện thoại.
- Xóa email.
- Xóa địa chỉ.
- Xóa mã đơn hàng.
- Không đưa thông tin riêng tư vào repo public.
