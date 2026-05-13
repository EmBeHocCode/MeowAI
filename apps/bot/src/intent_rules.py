"""Nhan dien intent bang luat tu khoa don gian."""

from apps.bot.src.preprocess import normalize_text


INTENT_KEYWORDS = {
    "hoi_gia": ["gia", "bao nhieu", "nhieu tien", "phi", "cost", "re nhat", "goi re", "gia re"],
    "hoi_ton_kho": ["con hang", "ton kho", "het hang", "con khong", "stock"],
    "tu_van_san_pham": [
        "tu van",
        "nen mua",
        "goi nao",
        "phu hop",
        "chay web",
        "wordpress",
        "crm",
        "ten mien",
        "can email",
        "email doanh nghiep",
    ],
    "thanh_toan": ["thanh toan", "chuyen khoan", "vi dien tu", "tra tien", "ck"],
    "giao_hang": [
        "giao hang",
        "ban giao",
        "nhan hang",
        "nhan duoc",
        "bao lau nhan",
        "khi nao nhan",
        "email",
        "tai khoan",
    ],
    "doi_tra": ["doi tra", "hoan tien", "tra hang", "doi hang", "loi"],
    "bao_hanh": ["bao hanh", "ho tro loi", "sua loi"],
    "khuyen_mai": ["khuyen mai", "giam gia", "coupon", "ma giam"],
    "thong_tin_shop": ["lien he", "dia chi", "shop", "hotline", "ho tro"],
}


def detect_intent(message: str) -> str:
    """Tra ve intent dau tien khop voi tu khoa, neu khong co thi fallback."""
    normalized = normalize_text(message)

    for intent, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in normalized:
                return intent

    return "fallback"
