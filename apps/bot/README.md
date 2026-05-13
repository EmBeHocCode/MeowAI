# MeowAI Bot

Thư mục này chứa phần bot/service chính của MeowAI.

Nhiệm vụ:

- Nhận câu hỏi từ terminal hoặc HTTP API.
- Chuẩn hóa câu hỏi.
- Nhận diện intent.
- Tìm dữ liệu sản phẩm/chính sách.
- Sinh câu trả lời cho khách hàng.

Chạy chatbot terminal ở local Windows:

```powershell
cd D:\MeowAI
$env:PYTHONIOENCODING='utf-8'
python apps\bot\run_chat.py
```

Chạy test:

```powershell
cd D:\MeowAI
$env:PYTHONIOENCODING='utf-8'
python -m unittest discover -s apps\bot\tests
```

Chạy API thủ công:

```bash
uvicorn apps.bot.src.api:app --host 127.0.0.1 --port 8010 --reload
```
