# AGENTS - Luật Làm Việc Với MeowAI

File này dành cho Codex hoặc bất kỳ dev nào mở project MeowAI.

Trước khi sửa code, bắt buộc đọc:

1. `rules/README.md`
2. `rules/CORE_PROMPT.md`
3. `rules/PHASE_GATES.md`
4. `rules/FILE_EDITING_RULES.md`
5. `rules/RTK_USAGE_RULES.md`
6. `docs/12_CURRENT_STATUS.md`

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
- Khi chạy terminal, ưu tiên dùng `rtk` nếu phù hợp để giảm output và tiết kiệm token.

## RTK / Token-saving command rules

When running terminal commands, use RTK where useful to reduce token usage.

On Windows, avoid `rtk ls` because native `ls` may not exist in PATH.

Prefer:

- `rtk git status`
- `rtk read README.md`
- `rtk find . -name package.json`
- `rtk find apps -type f`
- `rtk npm test` / `rtk pnpm test` when applicable
- `rtk tsc`
- `rtk next build`
- `rtk lint`

Do not use RTK if it hides information needed to debug a problem. In that case, run the normal command after explaining why.

## Lệnh Kiểm Tra Nhanh

```powershell
cd D:\MeowAI
$env:PYTHONIOENCODING='utf-8'
python -m unittest discover -s apps\bot\tests
```
