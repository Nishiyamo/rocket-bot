from telegram.ext import ApplicationBuilder

from backend.bot.bot_message_handler import bot_message_manager
from settings import TELEGRAM_TOKEN


def main() -> None:
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    bot_message_manager(app)
    app.run_polling()


if __name__ == '__main__':
    main()
