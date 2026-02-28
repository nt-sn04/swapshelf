from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from utils import states
from keyboards.inline import (
    get_confirm_keyboard,
    get_genre_keyboard,
    get_status_keyboard,
    get_type_keyboard,
)
from db.books import create_book, get_my_books


def ask_title(update: Update, context: CallbackContext) -> int:
    update.callback_query.answer()
    update.callback_query.edit_message_text("Kitob nomini kiriting:")
    return states.AddBookStates.SET_TITLE


def set_title(update: Update, context: CallbackContext) -> int:
    context.user_data["title"] = update.message.text
    update.message.reply_text("Kitob muallifini kiriting:")
    return states.AddBookStates.SET_AUTHOR


def set_author(update: Update, context: CallbackContext) -> int:
    context.user_data["author"] = update.message.text
    update.message.reply_text(
        "Kitob janrini tanlang:", reply_markup=get_genre_keyboard()
    )
    return states.AddBookStates.SET_GENRE


def set_genre(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    genre = query.data.split(":")[-1]
    context.user_data["genre"] = genre
    query.edit_message_text(
        "Kitob holatini tanlang:", reply_markup=get_status_keyboard()
    )
    return states.AddBookStates.SET_STATUS


def set_status(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    status = query.data.split(":")[-1]
    context.user_data["status"] = status
    query.edit_message_text("Kitob turini tanlang:", reply_markup=get_type_keyboard())
    return states.AddBookStates.TYPE


def set_type(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    book_type = query.data.split(":")[-1]
    context.user_data["type"] = book_type
    title = context.user_data["title"]
    author = context.user_data["author"]
    genre = context.user_data["genre"]
    status = context.user_data["status"]
    type_ = context.user_data["type"]
    query.edit_message_text(
        f"Kitob nomi: {title}\n"
        f"Muallif: {author}\n"
        f"Janr: {genre}\n"
        f"Holat: {status}\n"
        f"Tur: {type_}\n"
        "Tasdiqlaysizmi?",
        reply_markup=get_confirm_keyboard(),
    )
    return states.AddBookStates.CONFIRM


def add_book(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text("Kitob qo'shildi! Rahmat!")

    create_book(
        telegram_id=update.effective_user.id,
        title=context.user_data["title"],
        author=context.user_data["author"],
        genre_id=context.user_data["genre"],
        status=context.user_data["status"],
        type_=context.user_data["type"],
    )

    return ConversationHandler.END


def show_my_books(update: Update, context: CallbackContext) -> None:
    update.callback_query.answer()

    books = get_my_books(update.effective_user.id)
    if not books:
        update.callback_query.edit_message_text("Sizning javoningizda kitob yo'q.")
        return
    message = "Sizning javoningizdagi kitoblar:\n\n"
    for pk, title, author, genre, status, type_ in books:
        message += f"📖 {title}\n✍️ {author}\n📚 {genre}\n🔖 {status}\n🔄 {type_}\n\n"
    update.callback_query.edit_message_text(message)
