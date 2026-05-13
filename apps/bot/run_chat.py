"""Chay chatbot MeowAI tren terminal."""

from apps.bot.src.chat_engine import ChatEngine


def main() -> None:
    bot = ChatEngine()

    print("MeowAI terminal chatbot")
    print("Gõ 'exit' hoặc 'quit' để thoát.")
    print()

    while True:
        user_message = input("Bạn: ").strip()

        if user_message.lower() in {"exit", "quit", "thoat", "thoát"}:
            print("MeowAI: Dạ em tạm biệt anh/chị nha.")
            break

        if not user_message:
            print("MeowAI: Dạ anh/chị nhập câu hỏi giúp em nha.")
            continue

        answer = bot.reply(user_message)
        print(f"MeowAI: {answer}")


if __name__ == "__main__":
    main()
