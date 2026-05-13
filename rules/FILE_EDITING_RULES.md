# File Editing Rules - Luật Sửa File

File này giúp tránh tình trạng sửa note và code tùm lum.

## File Nên Đọc Trước Khi Sửa

- `docs/12_CURRENT_STATUS.md`
- `rules/PHASE_GATES.md`
- `docs/07_BUILD_LOG.md`
- File code liên quan trực tiếp đến yêu cầu.

## File Được Sửa Thường Xuyên

- `apps/bot/src/*.py`
- `apps/bot/tests/*.py`
- `data/shop/products.csv`
- `data/intents/training_data.jsonl`
- `docs/07_BUILD_LOG.md`
- `docs/12_CURRENT_STATUS.md`

## File Cần Cẩn Thận Khi Sửa

- `README.md`
- `docs/00_PROJECT_OVERVIEW.md`
- `docs/01_TIMELINE.md`
- `rules/*.md`
- `deploy/*.service`

Chỉ sửa các file này khi thay đổi thật sự ảnh hưởng đến hướng đi project.

## File Không Được Đưa Secret Vào

- Mọi file trong repo.
- Đặc biệt không đưa secret vào:
  - `README.md`
  - `docs/*.md`
  - `rules/*.md`
  - `deploy/*.service`
  - `.env.example`

Nếu cần cấu hình riêng, dùng `.env` local và không commit.

## Quy Tắc Cập Nhật Note

- `docs/07_BUILD_LOG.md`: chỉ ghi việc đã làm xong.
- `docs/10_NEXT_STEPS.md`: chỉ ghi việc sắp làm gần nhất.
- `docs/12_CURRENT_STATUS.md`: cập nhật khi trạng thái project thay đổi.
- Không sửa toàn bộ note chỉ vì đổi câu chữ.
- Không tạo quá nhiều file note mới nếu một file hiện có đã đủ.

## Quy Tắc Test

Sau khi sửa bot, chạy:

```powershell
cd D:\MeowAI
$env:PYTHONIOENCODING='utf-8'
python -m unittest discover -s apps\bot\tests
```

Nếu không chạy được test, phải ghi rõ lý do.

