# MeowAI Web Dashboard

Thư mục này chứa giao diện làm việc của MeowAI.

Giao diện dùng Next.js App Router và TSX, tham khảo cách tổ chức của `ZALO-BotChat/apps/web`.

Next.js web gọi MeowAI Python API thông qua proxy nội bộ:

```text
/api/meowai/*
```

## Trang Hiện Có

- `/dashboard`: dashboard quản lý bot, dữ liệu sản phẩm và dataset intent.
- `/chat`: giao diện chat thử với MeowAI.

## Cấu Trúc

```text
apps/web/
├─ src/
│  ├─ app/
│  │  ├─ api/meowai/[...path]/route.ts
│  │  ├─ dashboard/page.tsx
│  │  ├─ chat/page.tsx
│  │  ├─ layout.tsx
│  │  └─ globals.css
│  ├─ components/
│  │  ├─ chat/
│  │  ├─ dashboard/
│  │  └─ layout/
│  └─ lib/
│     ├─ api.ts
│     └─ types.ts
├─ package.json
├─ next.config.ts
└─ tsconfig.json
```

Chạy local:

Terminal 1 chạy Python API:

```powershell
cd D:\MeowAI
.\.venv\Scripts\python.exe -m uvicorn apps.bot.src.api:app --host 127.0.0.1 --port 8020 --reload
```

Terminal 2 chạy Next.js web:

```powershell
cd D:\MeowAI\apps\web
bun run dev -- --hostname 127.0.0.1 --port 3020
```

Sau đó mở:

```text
http://127.0.0.1:3020/dashboard
http://127.0.0.1:3020/chat
```

Dashboard hiện có:

- Tổng quan trạng thái bot.
- Số lượng sản phẩm mẫu.
- Số câu dataset intent.
- Danh sách intent.
- Bảng sản phẩm mẫu.

Dự kiến mở rộng sau:

- Quản lý chính sách shop.
- Xem log và lịch sử câu hỏi.
- Quản lý dataset intent trực tiếp trên web.
- Theo dõi model train.

Nguyên tắc:

- Dashboard không chứa thuật toán chatbot chính.
- Dashboard gọi Bot API nội bộ.
- Secret/API key nếu có phải nằm server-side, không đưa ra browser.
