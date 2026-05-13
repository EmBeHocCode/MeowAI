"""Dieu phoi chatbot: intent -> tim du lieu -> tao cau tra loi."""

from apps.bot.src.intent_rules import detect_intent
from apps.bot.src.product_search import (
    find_cheapest_product,
    find_product,
    find_products_by_need,
    is_lowest_price_question,
    load_products,
)
from apps.bot.src.response_templates import (
    answer_consult,
    answer_fallback,
    answer_lowest_price,
    answer_policy,
    answer_price,
    answer_stock,
)


class ChatEngine:
    """Chatbot rule-based ban dau cua MeowAI."""

    def __init__(self) -> None:
        self.products = load_products()

    def reply(self, message: str) -> str:
        """Nhan cau hoi cua khach va tra ve cau tra loi."""
        intent = detect_intent(message)

        if intent == "hoi_gia":
            if is_lowest_price_question(message):
                product = find_cheapest_product(self.products)
                return answer_lowest_price(product)

            product = find_product(message, self.products)
            return answer_price(product)

        if intent == "hoi_ton_kho":
            product = find_product(message, self.products)
            return answer_stock(product)

        if intent == "tu_van_san_pham":
            products = find_products_by_need(message, self.products)
            return answer_consult(products)

        if intent in {"thanh_toan", "giao_hang", "doi_tra", "bao_hanh", "khuyen_mai", "thong_tin_shop"}:
            return answer_policy(intent)

        return answer_fallback()
