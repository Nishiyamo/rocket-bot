from telegram.ext import CommandHandler, InlineQueryHandler, MessageHandler, filters

from backend.bot.bot_stagges import s001_start, s002_first_picture, s003_key_listener, unknown


def bot_message_manager(my_bot):
    my_bot.add_handler(CommandHandler("start", s001_start))
    my_bot.add_handler(CommandHandler("game", s002_first_picture))
    my_bot.add_handler(MessageHandler(filters.TEXT, s003_key_listener))
    my_bot.add_handler(MessageHandler(filters.COMMAND, unknown))
