import telebot

bot = telebot.TeleBot("5340242308:AAGiroTtzsk6F4fHPUYhhP4z3_Cz1bnPVDM")

@bot.message_handler(content_types = ["text"])
def function(message):
	file = open("file.txt", "w+")
	file.write(message.text)
	file.close()

	file = open("file.txt", "rb")
	bot.send_document(message.chat.id, file)
	file.close()

bot.polling()