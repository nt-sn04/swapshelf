from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_confirm_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Ha", callback_data="ha"),
            InlineKeyboardButton("Yo'q", callback_data="yo'q"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
