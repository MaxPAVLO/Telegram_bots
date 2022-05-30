import telebot

bot = telebot.TeleBot("5393705311:AAFFd2fP7GtAk7hg0c3ewtWolHkPerTERKo")

@bot.message_handler(commands = ["start"])
def function(message):
	if message.chat.id == 1236422161:
		bot.send_message(1236422161, "Привет, " + str(message.from_user.first_name) + ", ждём отправку фотографий.")

	else:
		bot.send_message(message.chat.id, "Привет, " + str(message.from_user.first_name) + ", отправьте фото администратору.")

@bot.message_handler(content_types = ["photo"])
def sending(message):
	if message.chat.id == 1236422161:
		bot.send_message(1236422161, "У вас нет прав.")

	else:
		photo_id = message.photo[0].file_id
		bot.send_message(message.chat.id, "Успешно отправлено.")
		bot.send_photo(1236422161, photo_id)

bot.polling()