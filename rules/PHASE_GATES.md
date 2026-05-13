# Phase Gates - Cổng Qua Từng Giai Đoạn

File này dùng để tránh dev làm lộn thứ tự.

Một phase chỉ được xem là xong khi có code chạy được, test cơ bản và ghi chú trong `docs/07_BUILD_LOG.md`.

## Phase 0 - Khung Project Và Tài Liệu

Mục tiêu:

- Có cấu trúc thư mục rõ ràng.
- Có README và tài liệu tổng quan.
- Có luật cứng cho dev/Codex.

Trạng thái: Hoàn thành.

Được làm:

- Sửa tài liệu kế hoạch.
- Tạo luật làm việc.
- Chỉnh cấu trúc thư mục nếu thật sự cần.

Chưa được làm:

- Train model.
- Tích hợp web phức tạp.

## Phase 1 - Bot Rule-Based Chạy Được

Mục tiêu:

- Chuẩn hóa câu hỏi khách hàng.
- Nhận diện intent bằng luật từ khóa.
- Tìm sản phẩm trong `data/shop/products.csv`.
- Trả lời bằng template.
- Có test cơ bản.

Trạng thái: Hoàn thành.

Điều kiện hoàn thành:

- Bot hiểu ít nhất 10 câu hỏi mẫu trong `docs/10_NEXT_STEPS.md`.
- Test local pass.
- Các lỗi viết tắt phổ biến như `ck`, `dc`, `bh`, `ntn` được xử lý.

## Phase 2 - Dữ Liệu Shop Và Tìm Kiếm Tốt Hơn

Mục tiêu:

- Tăng số lượng sản phẩm mẫu.
- Tìm được sản phẩm theo tên, giá, danh mục, nhu cầu.
- Trả lời được link sản phẩm nếu dữ liệu có link.

Chỉ bắt đầu khi Phase 1 đã ổn.

Trạng thái: Hoàn thành bản nền.

Điều kiện hoàn thành:

- Có ít nhất 10 sản phẩm mẫu.
- Có test cho tìm kiếm sản phẩm.
- Bot không chọn bừa sản phẩm khi câu hỏi quá mơ hồ.

## Phase 3 - Dataset Intent

Mục tiêu:

- Tạo dataset câu hỏi khách hàng để chuẩn bị train.
- Mỗi dòng có `text` và `intent`.
- Có câu đời thường, viết tắt và sai chính tả nhẹ.

Chỉ bắt đầu khi Phase 1 và Phase 2 đã ổn.

Trạng thái: Chưa bắt đầu.

Điều kiện hoàn thành:

- Có ít nhất 200 câu mẫu.
- Mỗi intent chính có ít nhất 15-20 câu.
- Có file giải thích nhãn trong `data/intents/labels.md`.

## Phase 4 - Train Intent Classifier

Mục tiêu:

- Train model nhỏ bằng TF-IDF và Logistic Regression hoặc Linear SVM.
- Lưu model vào `models/`.
- Có báo cáo độ chính xác.

Chỉ bắt đầu khi Phase 3 đủ dữ liệu.

Trạng thái: Chưa bắt đầu.

Điều kiện hoàn thành:

- Có script train.
- Có script test/evaluate.
- Có report trong `reports/intent_metrics.md`.

## Phase 5 - API Nội Bộ

Mục tiêu:

- Web gọi MeowAI qua HTTP API.
- API không lộ ra ngoài nếu chưa cần.
- Endpoint `/chat` ổn định.

Trạng thái: Đã có bản đầu, cần mở rộng sau khi bot thông minh hơn.

## Phase 6 - Tích Hợp Website

Mục tiêu:

- Chat widget hoặc web bán hàng gọi MeowAI.
- Có fallback khi bot không hiểu.
- Có log câu hỏi để cải thiện dataset.

Chỉ bắt đầu sau khi API và bot đủ ổn.

## Phase 7 - Báo Cáo Và Demo

Mục tiêu:

- Có báo cáo giải thích hệ thống.
- Có sơ đồ kiến trúc.
- Có kịch bản demo.
- Có phần giải thích vì sao đây là AI tự xây.
