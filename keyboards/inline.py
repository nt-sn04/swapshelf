from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_confirm_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Ha", callback_data="ha"),
            InlineKeyboardButton("Yo'q", callback_data="yo'q"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("📚 Mening Javonim", callback_data="my_books")],
        [InlineKeyboardButton("➕ Kitob Qo'shish", callback_data="add_book")],
        [InlineKeyboardButton("🔍 Kitob Qidirish", callback_data="browse_books")],
        [InlineKeyboardButton("📬 Mening So'rovlaram", callback_data="my_requests")],
        [InlineKeyboardButton("🔄 Mening Almashtirishlarim", callback_data="my_swaps")],
        [InlineKeyboardButton("⭐ Mening Sahifam", callback_data="my_profile")],
    ]
    return InlineKeyboardMarkup(keyboard)
