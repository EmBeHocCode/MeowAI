"""Cac mau cau tra loi cho chatbot ban hang."""

from src.product_search import format_price


POLICY_ANSWERS = {
    "thanh_toan": "Dạ shop hỗ trợ chuyển khoản ngân hàng và ví điện tử nếu hệ thống đã cấu hình nha.",
    "giao_hang": "Dạ với sản phẩm số, shop sẽ bàn giao qua tài khoản khách hàng hoặc email sau khi xác nhận đơn hàng nha.",
    "doi_tra": "Dạ shop hỗ trợ kiểm tra lỗi nếu sản phẩm hoặc dịch vụ không hoạt động đúng mô tả nha.",
    "bao_hanh": "Dạ thời gian bảo hành tùy từng sản phẩm. Nếu sản phẩm có thông tin bảo hành riêng, shop sẽ ưu tiên theo thông tin đó nha.",
    "khuyen_mai": "Dạ hiện dữ liệu mẫu chưa có mã khuyến mãi cụ thể. Anh/chị có thể theo dõi website để xem ưu đãi mới nha.",
    "thong_tin_shop": "Dạ anh/chị có thể liên hệ shop qua form liên hệ hoặc kênh hỗ trợ được cấu hình trên website nha.",
}


def product_summary(product: dict) -> str:
    """Tom tat ngan gon mot san pham."""
    return (
        f"{product['name']} - giá {format_price(product['price'])}, "
        f"còn {product['stock']} sản phẩm. {product['description']}."
    )


def answer_price(product: dict | None) -> str:
    if not product:
        return "Dạ anh/chị muốn hỏi giá sản phẩm nào ạ? Em chưa tìm thấy sản phẩm phù hợp trong dữ liệu."

    return f"Dạ {product['name']} hiện có giá {format_price(product['price'])} nha."


def answer_stock(product: dict | None) -> str:
    if not product:
        return "Dạ anh/chị muốn kiểm tra tồn kho sản phẩm nào ạ?"

    return f"Dạ {product['name']} hiện còn {product['stock']} sản phẩm nha."


def answer_consult(products: list[dict]) -> str:
    if not products:
        return "Dạ anh/chị cho em biết nhu cầu cụ thể hơn được không ạ? Ví dụ: chạy website, WordPress, CRM hoặc dự án sinh viên."

    lines = ["Dạ em gợi ý một vài sản phẩm phù hợp:"]
    for index, product in enumerate(products, start=1):
        lines.append(f"{index}. {product_summary(product)}")
    return "\n".join(lines)


def answer_policy(intent: str) -> str:
    return POLICY_ANSWERS.get(
        intent,
        "Dạ phần này em chưa có đủ thông tin. Anh/chị liên hệ shop để được hỗ trợ chính xác hơn nha.",
    )


def answer_fallback() -> str:
    return (
        "Dạ em chưa hiểu rõ câu hỏi này. Anh/chị có thể hỏi về giá, tồn kho, "
        "tư vấn sản phẩm, thanh toán, giao hàng, đổi trả hoặc bảo hành nha."
    )
