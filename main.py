from telegram.ext.updater import Updater
from telegram.ext.updater.messagehandler import MessageHandler
from telegram.ext.filters import Filters




def select_lang(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Hindi", callback_data="Hindi"),
            InlineKeyboardButton("Spanish", callback_data="Spanish"),
            InlineKeyboardButton("German", callback_data="German")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Say Hello!', reply_markup=reply_markup)


lang = ""

def button(update: Update, context: CallbackContext) -> None:
    global lang
    lang = update.callback_query.data.lower()
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"{query.data} has been selected for translation! You can start translating your text.")



def lang_translator(user_input):
    transator = Translator(from_lang="english", to_lang=lang)
    translation = Translator.translate(user_input)
    return translation



def reply(update, context):
    user_input = update.message.text
    update.message.reply_text(lang_translator(user_input))

def main():
    api = open("api.txt", "r")
    updater = Updater(api.read(), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', select_lang))
    dp.add_handler(CommandHandler('select_lang', select_lang))
    dp.add_handler(CallblackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()


main()
