"""HTTP API cho MeowAI."""

import json
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel, Field

from apps.bot.src.chat_engine import ChatEngine
from apps.bot.src.intent_rules import detect_intent
from apps.bot.src.product_search import format_price, load_products


PROJECT_ROOT = Path(__file__).resolve().parents[3]
TRAINING_DATA_FILE = PROJECT_ROOT / "data" / "intents" / "training_data.jsonl"
LABELS_FILE = PROJECT_ROOT / "data" / "intents" / "labels.md"

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


def count_training_samples() -> int:
    """Đếm số dòng dataset intent hiện có."""
    if not TRAINING_DATA_FILE.exists():
        return 0

    with TRAINING_DATA_FILE.open("r", encoding="utf-8") as file:
        return sum(1 for line in file if line.strip())


def count_intents() -> dict[str, int]:
    """Đếm số câu mẫu theo từng intent trong dataset."""
    counts: dict[str, int] = {}

    if not TRAINING_DATA_FILE.exists():
        return counts

    with TRAINING_DATA_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue

            item = json.loads(line)
            intent = item.get("intent", "unknown")
            counts[intent] = counts.get(intent, 0) + 1

    return counts


def read_intent_labels() -> list[dict[str, str]]:
    """Đọc bảng intent trong file markdown labels đơn giản."""
    labels: list[dict[str, str]] = []

    if not LABELS_FILE.exists():
        return labels

    for line in LABELS_FILE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `"):
            continue

        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) < 3:
            continue

        labels.append(
            {
                "intent": parts[0].strip("`"),
                "meaning": parts[1],
                "example": parts[2].strip('"'),
            }
        )

    return labels


@app.get("/health")
def health_check() -> dict:
    """Endpoint kiểm tra service còn sống."""
    return {"status": "ok", "service": "MeowAI"}


@app.get("/api/dashboard/summary")
def dashboard_summary() -> dict:
    """Trả dữ liệu tổng quan cho dashboard."""
    products = load_products()
    intent_counts = count_intents()
    total_stock = sum(int(product.get("stock", 0)) for product in products)

    return {
        "service": "MeowAI",
        "status": "online",
        "phase": "Phase 3 - Intent dataset baseline complete",
        "mode": "Rule-based + product CSV",
        "product_count": len(products),
        "total_stock": total_stock,
        "intent_count": len(intent_counts),
        "training_samples": count_training_samples(),
    }


@app.get("/api/products")
def products_api() -> dict:
    """Trả danh sách sản phẩm mẫu cho dashboard."""
    products = []

    for product in load_products():
        product_item = dict(product)
        product_item["formatted_price"] = format_price(product_item.get("price", "0"))
        products.append(product_item)

    return {"products": products}


@app.get("/api/intents")
def intents_api() -> dict:
    """Trả danh sách intent và số câu mẫu hiện có."""
    counts = count_intents()
    labels = []

    for label in read_intent_labels():
        label_item = dict(label)
        label_item["sample_count"] = counts.get(label_item["intent"], 0)
        labels.append(label_item)

    return {"intents": labels}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """Nhận câu hỏi từ website và trả lời bằng ChatEngine."""
    engine = ChatEngine()
    intent = detect_intent(request.message)
    reply = engine.reply(request.message)
    return ChatResponse(reply=reply, intent=intent)
