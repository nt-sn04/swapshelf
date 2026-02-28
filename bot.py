from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler,
)

from config import settings
from utils import states
from handlers import start


def main() -> None:
    updater = Updater(settings.BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler("start", start.start)],
            states={
                states.SET_NAME: [
                    MessageHandler(Filters.text & ~Filters.command, start.set_name)
                ],
                states.SET_PHONE: [
                    MessageHandler(Filters.text & ~Filters.command, start.set_phone)
                ],
                states.CONFIRM: [
                    CallbackQueryHandler(start.register, pattern="^(ha)$"),
                    CallbackQueryHandler(start.start, pattern="^(yo'q)$"),
                ],
            },
            fallbacks=[CommandHandler("start", start.start)],
        )
    )

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
