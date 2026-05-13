"""Test don gian cho chatbot rule-based Phase 1."""

import unittest

from apps.bot.src.chat_engine import ChatEngine
from apps.bot.src.intent_rules import detect_intent
from apps.bot.src.product_search import find_product, load_products


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

    def test_phase1_sample_questions(self) -> None:
        cases = [
            ("gói nào rẻ nhất shop", "hoi_gia", "Email Business Starter"),
            ("ck dc k", "thanh_toan", "chuyển khoản"),
            ("còn hàng không", "hoi_ton_kho", "tồn kho"),
            ("mình cần gói chạy web nhỏ", "tu_van_san_pham", "VPS Ryzen Basic"),
            ("đổi trả sao vậy", "doi_tra", "kiểm tra lỗi"),
            ("bh ntn", "bao_hanh", "bảo hành"),
            ("có coupon không", "khuyen_mai", "khuyến mãi"),
            ("shop ở đâu", "thong_tin_shop", "liên hệ"),
            ("bao lâu nhận được", "giao_hang", "bàn giao"),
            ("web mới nên dùng gói nào", "tu_van_san_pham", "Cloud Server Starter 1"),
            ("mình cần email tên miền riêng", "tu_van_san_pham", "Email Business Starter"),
        ]

        for question, expected_intent, expected_text in cases:
            with self.subTest(question=question):
                self.assertEqual(detect_intent(question), expected_intent)
                self.assertIn(expected_text, self.bot.reply(question))

    def test_phase2_product_data_has_minimum_size(self) -> None:
        self.assertGreaterEqual(len(load_products()), 10)

    def test_product_search_does_not_guess_when_question_is_vague(self) -> None:
        product = find_product("còn hàng không", load_products())
        self.assertIsNone(product)

    def test_product_answer_contains_product_link(self) -> None:
        answer = self.bot.reply("VPS Ryzen Basic giá bao nhiêu?")
        self.assertIn("/products/vps-ryzen-basic", answer)


if __name__ == "__main__":
    unittest.main()
