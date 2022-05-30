import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot("5183927528:AAFGfTyImzOhvYLfCADGoD1Q-pa810U6soo")

@bot.message_handler(commands = ["change_name"])
def change_user_surname(message):
	bot.send_message(message.chat.id, "Хорошо попробуем еще разок.")
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item = types.KeyboardButton("Фамилия")
	markup_reply.add(item)
	mesg = bot.send_message(message.chat.id, "Какая у вас фамилия?", reply_markup = markup_reply)
	bot.register_next_step_handler(mesg, change_user_name)

def change_user_name(message):
	global sas_surname
	sas_surname = message.text
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item = types.KeyboardButton("Имя")
	markup_reply.add(item)
	mesg = bot.send_message(message.chat.id, "Какое у вас имя?", reply_markup = markup_reply)
	bot.register_next_step_handler(mesg, update_records)

def update_records(message):
	global sas_name
	sas_name = message.text

	db = sqlite3.connect("bot_names")
	sql = db.cursor()

	sql.execute("INSERT INTO users_name VALUES(:data_surname, :data_name)",
		{
			"data_surname":sas_surname,
			"data_name":sas_name
		})

	sql.execute("SELECT * from users_name")
		
	records = sql.fetchall()
	print_records = ""

	for record in records[-1]:
		print_records += str(record) + " "
		
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item = types.KeyboardButton("Ок")
	markup_reply.add(item)
	bot.send_message(message.chat.id, "Теперь вас зовут : " + print_records + ".", reply_markup = markup_reply)

	db.commit()
	db.close()

@bot.message_handler(commands = ["start"])
def hello(message):
	try:
		db = sqlite3.connect("bot_names")
		sql = db.cursor()

		sql.execute("SELECT * from users_name")
		records = sql.fetchall()

		print_records = ""
		for record in records[-1]:
			print_records += str(record) + " "

		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton("Дарова")
		item2 = types.KeyboardButton("/change_name")
		markup_reply.add(item1, item2)
		bot.send_message(message.chat.id, "Привет " + print_records + ")", reply_markup = markup_reply)

		db.commit()
		db.close()
		
	except:
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item = types.KeyboardButton("Привет")
		markup_reply.add(item)
		bot.send_message(message.chat.id, "Привет, странник!", reply_markup = markup_reply)

@bot.message_handler(content_types = ["text"])
def IF(message):
	if message.chat.type == "private":
		if message.text == "Привет":
			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item = types.KeyboardButton("Фамилия")
			markup_reply.add(item)
			mesg = bot.send_message(message.chat.id, "Какая у вас фамилия?", reply_markup = markup_reply)
			bot.register_next_step_handler(mesg, get_user_surname)
			
		elif message.text == "Ок":
			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton("/start")
			item2 = types.KeyboardButton("/change_name")
			markup_reply.add(item1, item2)
			bot.send_message(message.chat.id, "Выберите одну из функций", reply_markup = markup_reply)

@bot.message_handler(content_types = ["text"])
def get_user_surname(message):
	global user_surname
	user_surname = message.text
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item = types.KeyboardButton("Имя")
	markup_reply.add(item)
	mesg = bot.send_message(message.chat.id, "Какое у вас имя?", reply_markup = markup_reply)
	bot.register_next_step_handler(mesg, get_user_name)

@bot.message_handler(content_types = ["text"])
def get_user_name(message):
	global user_name
	user_name = message.text

	db = sqlite3.connect("bot_names")
	sql = db.cursor()

	sql.execute("""CREATE TABLE IF NOT EXISTS users_name(
			last_name TEXT,
			first_name TEXT
		)""")
		
	sql.execute("INSERT INTO users_name VALUES(:data_surname, :data_name)",
		{
			"data_surname":user_surname,
			"data_name":user_name
		})

	sql.execute("SELECT * from users_name WHERE oid = " + str(num_records))
	records = sql.fetchall()
	global print_records
	print_records = ""
		
	for record in records[-1]:
		print_records += str(record) + " "
		
	bot.send_message(message.chat.id, "Вас зовут: " + print_records + "?" + "\nЕсли нет то введите команду /change_name")

bot.polling()