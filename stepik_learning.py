import telebot
import datetime

bot = telebot.TeleBot("5316711648:AAFpKLwNeMcsGapHtIwhoU60qdvQbPGW5xo")

@bot.message_handler(commands = ["start"])
def function(message):
	bot.send_message(message.chat.id, "Я пробил информацию:" + "\n\n" + "Id чата: " + str(message.chat.id) + "\n" + "Id пользователя: " + str(message.from_user.id) + "\n" + "Имя: " + str(message.from_user.first_name) + "\n" + "Фамилия: " + str(message.from_user.last_name) + "\n" + "Псевдоним: " + str(message.from_user.username) + "\n\n" + "Текст сообщения: " + str(message.text))

@bot.message_handler(commands = ["time"])
def function_num2(message):
	date = message.date + 10800
	bot.send_message(message.chat.id, "Время, когда вы отправили это сообщение: " + str(datetime.datetime.utcfromtimestamp(date)))

@bot.message_handler(content_types = ["photo"])
def function_num4(message):
	photo = open("C:/Users/mahim/OneDrive/Рабочий стол/Tkinter/PIL and Image/кот.jpg", "rb")
	bot.send_photo(message.chat.id, photo)
	bot.send_photo(message.chat.id, r"https://i.ytimg.com/vi/1YdZnTiiKSY/maxresdefault.jpg")

@bot.message_handler(func = lambda message: message.text == "Привет")
def function_num3(message):
	bot.send_message(message.chat.id, "Привет")

bot.polling()