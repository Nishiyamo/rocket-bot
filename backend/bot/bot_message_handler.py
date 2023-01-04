from telegram.ext import CommandHandler

from backend.bot.bot_stagges import s001_start, s002_initilize


def bot_message_manager(my_bot):
    my_bot.add_handler(CommandHandler("start", s001_start))
    my_bot.add_handler(CommandHandler("game", s002_initilize))
