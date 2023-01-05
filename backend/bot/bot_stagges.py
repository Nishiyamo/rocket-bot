from uuid import uuid4

from telegram import Update, KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup, InputTextMessageContent, \
    InlineQueryResultArticle, ReplyKeyboardRemove
from telegram.ext import ContextTypes

from backend.api.framex import FrameX
from backend.utils.framex.bisector import Bisector
from settings import VIDEO_NAME


async def s001_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Wellcome, in this bot we are going to try to know when the "
        "Falcon Heavy liftoff, Do you want to start the /game?"
    )


async def s002_first_picture(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Load out the frame for send it to the bot
    bisector = Bisector()
    image = bisector.image
    context.user_data['bisector'] = bisector
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
        await s004_game_manager(update, context)


async def s004_game_manager(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass_mid = True if update.effective_message.text == 'Yes' else False
    bisector = context.user_data['bisector']
    if bisector.lift_off_frame():
        await s005_end_game(update, context)
    bisector.bisect(pass_mid=pass_mid)
    bisector.calculed_frame = bisector.get_half_frames()
    image = FrameX.get_video_frame(VIDEO_NAME, bisector.calculed_frame)
    message = "Did the rocket liftoff?"
    reply_keyboard = [["Yes", "No"]]
    await update.effective_message.reply_photo(
        photo=image, caption=message, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )


async def s005_end_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Congrats, WE HAVE A LIFT OFF!!", reply_markup=ReplyKeyboardRemove()
    )


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
