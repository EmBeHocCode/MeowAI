'use client';

import { FormEvent, KeyboardEvent, useEffect, useRef, useState } from 'react';
import { sendChatMessage } from '@/lib/api';

type ChatMessage = {
  id: number;
  role: 'user' | 'bot';
  text: string;
  intent?: string;
};

const QUICK_QUESTIONS = [
  'gói nào rẻ nhất shop',
  'mình cần gói chạy web nhỏ',
  'VPS Ryzen Basic giá bao nhiêu?',
  'ck dc k',
];

export function ChatWorkspace() {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: 1,
      role: 'bot',
      text: 'Dạ em sẵn sàng tư vấn sản phẩm, giá, tồn kho, thanh toán, giao hàng và bảo hành nha.',
    },
  ]);
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  async function submitMessage(nextMessage: string) {
    const cleanMessage = nextMessage.trim();

    if (!cleanMessage || loading) {
      return;
    }

    setMessage('');
    setLoading(true);
    setMessages((current) => [...current, { id: Date.now(), role: 'user', text: cleanMessage }]);

    try {
      const response = await sendChatMessage(cleanMessage);
      setMessages((current) => [
        ...current,
        {
          id: Date.now() + 1,
          role: 'bot',
          text: response.reply,
          intent: response.intent,
        },
      ]);
    } catch {
      setMessages((current) => [
        ...current,
        {
          id: Date.now() + 1,
          role: 'bot',
          text: 'Dạ hiện tại web chưa gọi được MeowAI API. Em kiểm tra server Python giúp chị nha.',
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    submitMessage(message);
  }

  function handleKeyDown(event: KeyboardEvent<HTMLTextAreaElement>) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      submitMessage(message);
    }
  }

  return (
    <section className="chat-panel" aria-label="MeowAI chat">
      <header className="chat-header">
        <div>
          <p className="eyebrow">MeowAI playground</p>
          <h1>Chat thử bot bán hàng</h1>
          <p className="muted">Dùng để kiểm tra câu trả lời trước khi tích hợp vào website.</p>
        </div>
        <span className="status-pill">Online</span>
      </header>

      <div className="messages" aria-live="polite">
        {messages.map((item) => (
          <article key={item.id} className={`message ${item.role === 'user' ? 'user-message' : 'bot-message'}`}>
            <span className="avatar">{item.role === 'user' ? 'B' : 'M'}</span>
            <div className="bubble">
              <strong>{item.role === 'user' ? 'Bạn' : 'MeowAI'}</strong>
              <p>{item.text}</p>
              {item.intent ? <span className="intent">intent: {item.intent}</span> : null}
            </div>
          </article>
        ))}
        <div ref={bottomRef} />
      </div>

      <div className="quick-row" aria-label="Câu hỏi mẫu">
        {QUICK_QUESTIONS.map((question) => (
          <button key={question} type="button" onClick={() => submitMessage(question)}>
            {question}
          </button>
        ))}
      </div>

      <form className="chat-form" onSubmit={handleSubmit}>
        <textarea
          rows={2}
          placeholder="Nhập câu hỏi cho MeowAI..."
          value={message}
          onChange={(event) => setMessage(event.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button className="primary-button" type="submit" disabled={loading}>
          {loading ? 'Đợi...' : 'Gửi'}
        </button>
      </form>
    </section>
  );
}
