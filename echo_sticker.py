import telebot

bot = telebot.TeleBot("5372938946:AAFc5VVbzpX3xKJvXEtH7_VC3AKmvlMsRks")

@bot.message_handler(content_types = ["sticker"])
def echo_sticker(message):
	bot.send_sticker(message.chat.id, message.sticker.file_id)

@bot.message_handler(commands = ["edit"])
def function_num5(message):
	bot.edit_message_text(chat_id = message.chat.id, message_id = message.id, text = "А вот и нет твоего сообщения")

bot.polling()