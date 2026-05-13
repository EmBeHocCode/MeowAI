# AGENTS - Luật Làm Việc Với MeowAI

File này dành cho Codex hoặc bất kỳ dev nào mở project MeowAI.

Trước khi sửa code, bắt buộc đọc:

1. `rules/README.md`
2. `rules/CORE_PROMPT.md`
3. `rules/PHASE_GATES.md`
4. `rules/FILE_EDITING_RULES.md`
5. `docs/12_CURRENT_STATUS.md`

## Vai Trò Của Project

MeowAI là chatbot AI tự xây cho đồ án website bán hàng.

Mục tiêu không phải tạo ChatGPT mới. Mục tiêu là xây một chatbot có thể:

- Hiểu ý định câu hỏi khách hàng.
- Tìm dữ liệu sản phẩm, chính sách và FAQ trong dữ liệu nội bộ.
- Trả lời bằng tiếng Việt tự nhiên, dễ hiểu.
- Có thể giải thích được với giảng viên.
- Không phụ thuộc API AI bên ngoài trong phần lõi nộp đồ án.

## Nguyên Tắc Bắt Buộc

- Không nhảy phase.
- Không tự ý đổi kiến trúc nếu chưa cập nhật lý do trong tài liệu.
- Không sửa nhiều file note cùng lúc nếu không cần.
- Không hardcode API key, token, mật khẩu hoặc dữ liệu nhạy cảm.
- Mỗi thay đổi code phải có test tương ứng nếu ảnh hưởng hành vi bot.
- Sau khi hoàn thành một mốc, cập nhật `docs/07_BUILD_LOG.md`.

## Lệnh Kiểm Tra Nhanh

```powershell
cd D:\MeowAI
$env:PYTHONIOENCODING='utf-8'
python -m unittest discover -s apps\bot\tests
```

