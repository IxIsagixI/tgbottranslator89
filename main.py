import telebot
from googletrans import Translator

translator = Translator()

bot = telebot.TeleBot("6955314353:AAGK-uOxeEUx-BHSKFj7WEt_KjDO06tIzd8")

user_language = {}

languages = {
    "en": {"code": "en", "name_en": "English", "name_ru": "английский"},
    "ru": {"code": "ru", "name_en": "Russian", "name_ru": "русский"},
    "fr": {"code": "fr", "name_en": "French", "name_ru": "французский"},
    "es": {"code": "es", "name_en": "Spanish", "name_ru": "испанский"},
    "de": {"code": "de", "name_en": "German", "name_ru": "немецкий"},
    "it": {"code": "it", "name_en": "Italian", "name_ru": "итальянский"},
    "zh": {"code": "zh", "name_en": "Chinese", "name_ru": "китайский"},
    "ja": {"code": "ja", "name_en": "Japanese", "name_ru": "японский"},
    "ko": {"code": "ko", "name_en": "Korean", "name_ru": "корейский"},
    "pt": {"code": "pt", "name_en": "Portuguese", "name_ru": "португальский"},
    "nl": {"code": "nl", "name_en": "Dutch", "name_ru": "голландский"},
    "sv": {"code": "sv", "name_en": "Swedish", "name_ru": "шведский"},
    "pl": {"code": "pl", "name_en": "Polish", "name_ru": "польский"},
    "tr": {"code": "tr", "name_en": "Turkish", "name_ru": "турецкий"},
    "uk": {"code": "uk", "name_en": "Ukrainian", "name_ru": "украинский"},
    "hi": {"code": "hi", "name_en": "Hindi", "name_ru": "хинди"},
    "ar": {"code": "ar", "name_en": "Arabic", "name_ru": "арабский"},
    "vi": {"code": "vi", "name_en": "Vietnamese", "name_ru": "вьетнамский"},
    "fi": {"code": "fi", "name_en": "Finnish", "name_ru": "финский"},
    "cs": {"code": "cs", "name_en": "Czech", "name_ru": "чешский"},
    "el": {"code": "el", "name_en": "Greek", "name_ru": "греческий"},
    "hu": {"code": "hu", "name_en": "Hungarian", "name_ru": "венгерский"},
    "da": {"code": "da", "name_en": "Danish", "name_ru": "датский"},
    "no": {"code": "no", "name_en": "Norwegian", "name_ru": "норвежский"},
    "ro": {"code": "ro", "name_en": "Romanian", "name_ru": "румынский"},
    "sk": {"code": "sk", "name_en": "Slovak", "name_ru": "словацкий"},
    "id": {"code": "id", "name_en": "Indonesian", "name_ru": "индонезийский"},
    "ms": {"code": "ms", "name_en": "Malay", "name_ru": "малайский"},
    "th": {"code": "th", "name_en": "Thai", "name_ru": "тайский"},
    "tl": {"code": "tl", "name_en": "Tagalog", "name_ru": "тагальский"},
    "et": {"code": "et", "name_en": "Estonian", "name_ru": "эстонский"},
    "lt": {"code": "lt", "name_en": "Lithuanian", "name_ru": "литовский"},
    "lv": {"code": "lv", "name_en": "Latvian", "name_ru": "латышский"},
    "hr": {"code": "hr", "name_en": "Croatian", "name_ru": "хорватский"},
    "sr": {"code": "sr", "name_en": "Serbian", "name_ru": "сербский"},
    "sl": {"code": "sl", "name_en": "Slovenian", "name_ru": "словенский"},
    "bg": {"code": "bg", "name_en": "Bulgarian", "name_ru": "болгарский"},
    "he": {"code": "he", "name_en": "Hebrew", "name_ru": "иврит"},
    "fa": {"code": "fa", "name_en": "Persian", "name_ru": "персидский"},
    "ur": {"code": "ur", "name_en": "Urdu", "name_ru": "урду"},
    "bn": {"code": "bn", "name_en": "Bengali", "name_ru": "бенгальский"},
    "gu": {"code": "gu", "name_en": "Gujarati", "name_ru": "гуджарати"},
    "ta": {"code": "ta", "name_en": "Tamil", "name_ru": "тамильский"},
    "te": {"code": "te", "name_en": "Telugu", "name_ru": "телугу"},
    "kn": {"code": "kn", "name_en": "Kannada", "name_ru": "каннада"},
    "ml": {"code": "ml", "name_en": "Malayalam", "name_ru": "малаялам"},
    "mr": {"code": "mr", "name_en": "Marathi", "name_ru": "маратхи"},
    "pa": {"code": "pa", "name_en": "Punjabi", "name_ru": "панджаби"},
    "si": {"code": "si", "name_en": "Sinhala", "name_ru": "сингальский"},
    "ne": {"code": "ne", "name_en": "Nepali", "name_ru": "непальский"},
    "sq": {"code": "sq", "name_en": "Albanian", "name_ru": "албанский"},
}

@bot.message_handler(commands=['start'])
def handle_start(message):
    welcome_message = (
        "Добро пожаловать в бота-переводчика!\n\n"
        "Отправьте мне сообщение в формате `/translate <код_языка> <текст>`, и я переведу его для вас.\n"
        "Пример: `/translate fr как дела?`\n\n"
        "Доступны следующие 45 языков:\n"
    )
    available_languages = "\n".join([f"- [{lang_info['name_en']}/{lang_info['name_ru']}] ({code})" for code, lang_info in languages.items()])
    bot.send_message(message.chat.id, welcome_message + available_languages, parse_mode='Markdown')


@bot.message_handler(commands=['translate'])
def handle_translate(message):

    command, *args = message.text.split()
    if len(args) < 2:
        bot.send_message(message.chat.id, "Пример: /translate <код_языка> <текст>")
        return
    lang_code = args[0]
    text_to_translate = ' '.join(args[1:])
    user_language[message.chat.id] = lang_code
    translation = translator.translate(text_to_translate, dest=lang_code)
    bot.send_message(message.chat.id, f"Translated text: {translation.text}")

@bot.message_handler(commands=['swaplang'])
def handle_swap_lang(message):
    if message.chat.id not in user_language:
        bot.send_message(message.chat.id,
                         "Перед заменой укажите язык, используя /translate <код_языка> <текст>.")
        return

    source_lang = user_language[message.chat.id]
    destination_lang = "en"
    placeholder_translation = translator.translate("placeholder", src=source_lang)
    destination_lang = placeholder_translation.src
    user_language[message.chat.id] = destination_lang
    bot.send_message(message.chat.id,
                     f"Language swapped. Source language: {destination_lang}, Destination language: {source_lang}")

bot.polling()