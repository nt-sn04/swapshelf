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
                "🆕 Yangi, ishlatilmagan", callback_data="add_book:status:New"
            )
        ],
        [
            InlineKeyboardButton(
                "👍 Yaxshi holatda", callback_data="add_book:status:Good"
            )
        ],
        [
            InlineKeyboardButton(
                "👌 O'rtacha holatda", callback_data="add_book:status:Fair"
            )
        ],
        [
            InlineKeyboardButton(
                "📄 Ko'p ishlatilgan", callback_data="add_book:status:Worn"
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_type_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🔄 Vaqtincha (30 kun muddatli)", callback_data="add_book:type:Borrow"
            )
        ],
        [
            InlineKeyboardButton(
                "🎁 Doimiy berib yuborish", callback_data="add_book:type:Permanent"
            )
        ],
        [
            InlineKeyboardButton(
                "🔀 Ikkalasi ham mumkin", callback_data="add_book:type:Both"
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_book_action_keyboard(book_id):
    keyboard = [
        [InlineKeyboardButton("🎁 Kitobni Ulashish", callback_data=f"share:{book_id}")],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_book_request_keyboard(book_id):
    keyboard = [
        [
            InlineKeyboardButton(
                "✅ Kitobni olish uling", callback_data=f"request:{book_id}"
            ),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
