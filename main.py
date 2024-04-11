#bot_token = '6955314353:AAGK-uOxeEUx-BHSKFj7WEt_KjDO06tIzd8'
import telebot
from googletrans import Translator

translator = Translator()

bot = telebot.TeleBot("6955314353:AAGK-uOxeEUx-BHSKFj7WEt_KjDO06tIzd8")


user_language = {}

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать в бота-переводчика! Отправьте мне сообщение в формате /translate <код_языка> <текст>, и я переведу его для вас. Пример: /translate fr Привет")


@bot.message_handler(commands=['translate'])
def handle_translate(message):

    command, *args = message.text.split()
    if len(args) < 2:
        bot.send_message(message.chat.id, "Usage: /translate <language_code> <text>")
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
                         "Please specify a language using /translate <language_code> <text> before swapping.")
        return

    source_lang = user_language[message.chat.id]
    destination_lang = "en"  # Default to English if source language is not set
    placeholder_translation = translator.translate("placeholder", src=source_lang)
    destination_lang = placeholder_translation.src
    user_language[message.chat.id] = destination_lang
    bot.send_message(message.chat.id,
                     f"Language swapped. Source language: {destination_lang}, Destination language: {source_lang}")

bot.polling()