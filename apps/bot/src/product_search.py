"""Doc va tim kiem san pham tu file CSV mau."""

import csv
from pathlib import Path

from apps.bot.src.preprocess import normalize_text


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PRODUCTS_FILE = PROJECT_ROOT / "data" / "shop" / "products.csv"
SEARCH_STOPWORDS = {
    "anh",
    "chi",
    "ban",
    "co",
    "con",
    "duoc",
    "em",
    "gia",
    "hang",
    "hoi",
    "khong",
    "la",
    "minh",
    "muon",
    "nhieu",
    "san",
    "shop",
    "toi",
    "tu",
    "van",
}


def load_products(file_path: Path = PRODUCTS_FILE) -> list[dict]:
    """Doc danh sach san pham tu CSV."""
    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def format_price(price: str) -> str:
    """Dinh dang gia tien VND de bot tra loi de doc."""
    try:
        value = int(price)
    except ValueError:
        return price

    return f"{value:,}".replace(",", ".") + "đ"


def meaningful_words(message: str) -> list[str]:
    """Lay cac tu co y nghia de tim san pham, bo cac tu qua chung."""
    return [word for word in normalize_text(message).split() if word not in SEARCH_STOPWORDS]


def find_product(message: str, products: list[dict]) -> dict | None:
    """Tim san pham phu hop nhat bang ten, danh muc, mo ta va nhu cau."""
    words = meaningful_words(message)

    if not words:
        return None

    best_product = None
    best_score = 0

    for product in products:
        searchable_text = " ".join(
            [
                product.get("name", ""),
                product.get("category", ""),
                product.get("description", ""),
                product.get("use_cases", ""),
            ]
        )
        normalized_product = normalize_text(searchable_text)
        score = sum(1 for word in words if word in normalized_product)

        if score > best_score:
            best_score = score
            best_product = product

    return best_product if best_score > 0 else None


def is_lowest_price_question(message: str) -> bool:
    """Kiem tra khach co dang hoi san pham/goi re nhat khong."""
    normalized_message = normalize_text(message)
    lowest_keywords = ["re nhat", "goi re", "gia re", "re hon"]
    return any(keyword in normalized_message for keyword in lowest_keywords)


def find_cheapest_product(products: list[dict]) -> dict | None:
    """Tim san pham co gia thap nhat trong danh sach."""
    if not products:
        return None

    def price_value(product: dict) -> int:
        try:
            return int(product.get("price", 0))
        except ValueError:
            return 0

    return min(products, key=price_value)


def find_products_by_need(message: str, products: list[dict], limit: int = 3) -> list[dict]:
    """Lay mot vai san pham lien quan de tu van."""
    words = meaningful_words(message)
    if not words:
        return []

    scored_products = []

    for product in products:
        searchable_text = " ".join(
            [
                product.get("name", ""),
                product.get("category", ""),
                product.get("description", ""),
                product.get("use_cases", ""),
            ]
        )
        normalized_product = normalize_text(searchable_text)
        score = sum(1 for word in words if word in normalized_product)

        if score > 0:
            scored_products.append((score, product))

    scored_products.sort(key=lambda item: item[0], reverse=True)
    return [product for _, product in scored_products[:limit]]
