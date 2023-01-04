from telegram import Update, KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup
from telegram.ext import ContextTypes


async def s001_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Wellcome, in this bot we are going to try to know when the "
        "Falcon Heavy liftoff, ¿Do you want to start the /game?"
    )


async def s002_initialize(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "Did he the rocket liftoff?"
    reply_keyboard = [["Yes", "No"]]
    # using one_time_keyboard to hide the keyboard
    await update.effective_message.reply_text(
        message, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )

