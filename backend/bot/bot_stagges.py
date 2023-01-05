from uuid import uuid4

from telegram import Update, KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup, InputTextMessageContent, \
    InlineQueryResultArticle
from telegram.ext import ContextTypes

from backend.utils.framex.bisector import Bisector


async def s001_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Wellcome, in this bot we are going to try to know when the "
        "Falcon Heavy liftoff, Do you want to start the /game?"
    )


async def s002_first_picture(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Load out the frame for send it to the bot
    bisector = Bisector()
    image = bisector.image
    message = "Did he the rocket liftoff?"
    reply_keyboard = [["Yes", "No"]]
    await update.effective_message.reply_photo(
        photo=image, caption=message, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )


async def s003_key_listener(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.effective_message.text
    if not query:
        await update.message.reply_text(
            "I don't have any answer. Do you want to try my /game of rockets?."
        )
    if query != 'Yes' and query != 'No':
        await update.message.reply_text(
            "I don't understand you, I only accept a Yes or No answer.\n"
            "Sorry :-("
        )
    else:
        await s002_first_picture(update, context)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
