"""Tien xu ly cau hoi cua khach hang."""

import re
import unicodedata


SHORT_WORDS = {
    "ko": "khong",
    "k": "khong",
    "kh": "khong",
    "dc": "duoc",
    "đc": "duoc",
    "ck": "chuyen khoan",
    "ship": "giao hang",
}


def remove_vietnamese_accents(text: str) -> str:
    """Chuyen tieng Viet co dau ve khong dau de so khop tu khoa de hon."""
    normalized = unicodedata.normalize("NFD", text)
    without_marks = "".join(char for char in normalized if unicodedata.category(char) != "Mn")
    return without_marks.replace("đ", "d").replace("Đ", "D")


def normalize_text(text: str) -> str:
    """Lam sach cau hoi: chu thuong, bo dau, bo ky tu dac biet."""
    text = remove_vietnamese_accents(text.lower())
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    words = text.split()
    words = [SHORT_WORDS.get(word, word) for word in words]
    return " ".join(words)


def tokenize(text: str) -> list[str]:
    """Tach cau hoi thanh danh sach tu khoa don gian."""
    normalized = normalize_text(text)
    return normalized.split()
