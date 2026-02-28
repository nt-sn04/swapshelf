from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from db.books import get_genres


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


def get_genre_keyboard():
    genres = get_genres()
    keyboard = [
        [InlineKeyboardButton(name, callback_data=f"add_book:genre:{genre_id}")]
        for genre_id, name in genres
    ]
    return InlineKeyboardMarkup(keyboard)


def get_status_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🆕 Yangi, ishlatilmagan", callback_data="add_book:status:new"
            )
        ],
        [
            InlineKeyboardButton(
                "👍 Yaxshi holatda", callback_data="add_book:status:good"
            )
        ],
        [
            InlineKeyboardButton(
                "👌 O'rtacha holatda", callback_data="add_book:status:fair"
            )
        ],
        [
            InlineKeyboardButton(
                "📄 Ko'p ishlatilgan", callback_data="add_book:status:worn"
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_type_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🔄 Vaqtincha (30 kun muddatli)", callback_data="add_book:type:borrow"
            )
        ],
        [
            InlineKeyboardButton(
                "🎁 Doimiy berib yuborish", callback_data="add_book:type:permanent"
            )
        ],
        [
            InlineKeyboardButton(
                "🔀 Ikkalasi ham mumkin", callback_data="add_book:type:both"
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
