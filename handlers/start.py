from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from utils import states
from keyboards.inline import get_confirm_keyboard


def start(update: Update, context: CallbackContext) -> int:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Assalomu alaykum! Ismingizni kiriting:"
    )

    return states.SET_NAME


def set_name(update: Update, context: CallbackContext) -> int:
    context.user_data["name"] = update.message.text
    update.message.reply_text("Telefon raqamingizni kiriting:")

    return states.SET_PHONE


def set_phone(update: Update, context: CallbackContext) -> int:
    context.user_data["phone"] = update.message.text
    name = context.user_data["name"]
    phone = context.user_data["phone"]
    update.message.reply_text(
        f"Ismingiz: {name}\nTelefon raqamingiz: {phone}\nTasdiqlaysizmi?",
        reply_markup=get_confirm_keyboard(),
    )

    return states.CONFIRM


def register(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text("Ro'yxatdan o'tdingiz! Rahmat!")

    # Bu yerda ma'lumotlarni bazaga saqlash yoki boshqa amallarni bajarish mumkin

    return ConversationHandler.END
