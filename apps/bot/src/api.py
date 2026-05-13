"""HTTP API cho MeowAI."""

from fastapi import FastAPI
from pydantic import BaseModel, Field

from apps.bot.src.chat_engine import ChatEngine
from apps.bot.src.intent_rules import detect_intent


app = FastAPI(
    title="MeowAI",
    description="Chatbot tư vấn shop chạy bằng rule-based engine.",
    version="0.1.0",
)


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="Câu hỏi của khách hàng")


class ChatResponse(BaseModel):
    reply: str
    intent: str


@app.get("/health")
def health_check() -> dict:
    """Endpoint kiểm tra service còn sống."""
    return {"status": "ok", "service": "MeowAI"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """Nhận câu hỏi từ website và trả lời bằng ChatEngine."""
    engine = ChatEngine()
    intent = detect_intent(request.message)
    reply = engine.reply(request.message)
    return ChatResponse(reply=reply, intent=intent)
