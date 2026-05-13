"""Test don gian cho chatbot rule-based Phase 1."""

import unittest

from apps.bot.src.chat_engine import ChatEngine
from apps.bot.src.intent_rules import detect_intent


class Phase1ChatbotTest(unittest.TestCase):
    def setUp(self) -> None:
        self.bot = ChatEngine()

    def test_detect_price_intent(self) -> None:
        self.assertEqual(detect_intent("VPS Ryzen Basic gia bao nhieu?"), "hoi_gia")

    def test_detect_payment_intent(self) -> None:
        self.assertEqual(detect_intent("Shop co thanh toan chuyen khoan khong?"), "thanh_toan")

    def test_answer_price_from_product_data(self) -> None:
        answer = self.bot.reply("VPS Ryzen Basic giá bao nhiêu?")
        self.assertIn("329.000đ", answer)

    def test_answer_fallback(self) -> None:
        answer = self.bot.reply("cau hoi la la")
        self.assertIn("chưa hiểu rõ", answer)


if __name__ == "__main__":
    unittest.main()
