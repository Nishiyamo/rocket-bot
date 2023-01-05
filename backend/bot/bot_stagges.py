from telegram import Update, KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from backend.utils.framex.bisector import Bisector


async def s001_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Wellcome, in this bot we are going to try to know when the "
        "Falcon Heavy liftoff, Do you want to start the /game?"
    )


async def s002_initialize(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Load out the frame for send it to the bot
    bisector = Bisector()
    image = bisector.image
    message = "Did he the rocket liftoff?"
    reply_keyboard = [["Yes", "No"]]
    await update.effective_message.reply_photo(
        photo=image, caption=message, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
