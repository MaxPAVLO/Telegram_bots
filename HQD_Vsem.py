import telebot
from telebot import types
import psycopg2

global list
list = []
global list1
list1 = []
global list2
list2 = []
global Busket
Busket = ""

bot = telebot.TeleBot("5484112708:AAGmev134t-eApqMo2lsB_EKLGKsd2vPkHU")

@bot.message_handler(commands = ["start"])
def say_Hello_to_user(message):
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	OK = types.KeyboardButton("Ок")
	markup_reply.add(OK)
	mesg = bot.send_message(message.chat.id, "Привет, " + str(message.from_user.first_name) + " " + str(message.from_user.last_name) + " \nТы попал в магазин однаразок🤤 \nБудь аккуратней здесь💋", reply_markup = markup_reply)
	bot.register_next_step_handler(mesg, ChoosingOfBrand)

@bot.message_handler(func = lambda message: message.text == "uashduaHSUFYABSKDIAYSGFIYAYSGYGgysgygyuasduausdgugaf")
def ChoosingOfBrand(message):
	if message.text != "Ок":
		bot.send_message(message.chat.id, "Что бы вы не ввели продолжаем🤣")

	conn = None
	cur = None

	try:

		conn = psycopg2.connect(
				host = "localhost",
				dbname = "demo",
				user = "postgres",
				password = 256809,
				port = 5433)

		cur = conn.cursor()

		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		cur.execute("SELECT Brand FROM vapes")
		for i in set(cur.fetchall()):
			item = types.KeyboardButton(i[0])
			markup_reply.add(item)
			list.append(i[0])

		mesg = bot.send_message(message.chat.id, "Какой бренд вы предпочитаете?)", reply_markup = markup_reply)
		bot.register_next_step_handler(mesg, ChoosingOfTaste)

		conn.commit()

	finally:
		if conn is not None:
			conn.close()

		if cur is not None:
			cur.close()

@bot.message_handler(func = lambda message: message.text == "jaijuvuahsudinasuuandsuhuasduhfaushfuhasuhduoahsu fubauisbfuasuifb")
def ChoosingOfTaste(message):
	if str(message.text) not in list:
		bot.send_message(message.chat.id, "Выберите только из того что есть в списке")

		conn = None
		cur = None

		try:

			conn = psycopg2.connect(
					host = "localhost",
					dbname = "demo",
					user = "postgres",
					password = 256809,
					port = 5433)

			cur = conn.cursor()

			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
			cur.execute("SELECT Brand FROM vapes")
			for i in set(cur.fetchall()):
				item = types.KeyboardButton(i[0])
				markup_reply.add(item)
				list.append(i[0])

			mesg = bot.send_message(message.chat.id, "Какой бренд вы предпочитаете?)", reply_markup = markup_reply)
			bot.register_next_step_handler(mesg, ChoosingOfTaste)

			conn.commit()

		finally:
			if conn is not None:
				conn.close()

			if cur is not None:
				cur.close()	
	
	else:

		global Brand
		Brand = str(message.text)

		conn = None
		cur = None

		try:

			conn = psycopg2.connect(
					host = "localhost",
					dbname = "demo",
					user = "postgres",
					password = 256809,
					port = 5433)

			cur = conn.cursor()

			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
			cur.execute(f"SELECT Taste FROM vapes WHERE Brand = '{Brand}'")
			for i in set(cur.fetchall()):
				item = types.KeyboardButton(i[0])
				markup_reply.add(item)
				list1.append(i[0])

			mesg = bot.send_message(message.chat.id, "Какой вкус вы хотите?", reply_markup = markup_reply)
			bot.register_next_step_handler(mesg, ChoosingOfTimes)

			conn.commit()

		finally:
			if conn is not None:
				conn.close()

			if cur is not None:
				cur.close()

@bot.message_handler(func = lambda message: message.text == "kopasjfpijqsiafjoiaosnuifnbuoas u jubasf u ajubhj2 3j4b o2u3 oj 4h23ob42")
def ChoosingOfTimes(message):
	if str(message.text) not in list1:
		bot.send_message(message.chat.id, "Выберите из того что есть в списке")
		conn = None
		cur = None

		try:

			conn = psycopg2.connect(
					host = "localhost",
					dbname = "demo",
					user = "postgres",
					password = 256809,
					port = 5433)

			cur = conn.cursor()

			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
			cur.execute(f"SELECT Taste FROM vapes WHERE Brand = '{Brand}'")
			for i in set(cur.fetchall()):
				item = types.KeyboardButton(i[0])
				markup_reply.add(item)
				list1.append(i[0])

			mesg = bot.send_message(message.chat.id, "Какой вкус вы хотите?", reply_markup = markup_reply)
			bot.register_next_step_handler(mesg, ChoosingOfTimes)

			conn.commit()

		finally:
			if conn is not None:
				conn.close()

			if cur is not None:
				cur.close()

	else:

		global Taste
		Taste = str(message.text)

		conn = None
		cur = None

		try:

			conn = psycopg2.connect(
					host = "localhost",
					dbname = "demo",
					user = "postgres",
					password = 256809,
					port = 5433)

			cur = conn.cursor()

			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
			cur.execute(f"SELECT Times FROM vapes WHERE Brand = '{Brand}' AND Taste = '{Taste}'")
			for i in set(cur.fetchall()):
				item = types.KeyboardButton(i[0])
				markup_reply.add(item)
				list2.append(i[0])

			mesg = bot.send_message(message.chat.id, "На сколько тяжек)", reply_markup = markup_reply)
			bot.register_next_step_handler(mesg, Result)

			conn.commit()

		finally:
			if conn is not None:
				conn.close()

			if cur is not None:
				cur.close()

def check(message):
	try:
		int(message.text)

	except:
		pass

@bot.message_handler(func = lambda message: message.text == "[oiasjdoiSAFHUOSDasi uIABUs adhi UADUBhia dihuBUBHI iha d")
def Result(message):
	if int(message.text) not in list2:
		bot.send_message(message.chat.id, "Выберите из того что есть в списке")
		conn = None
		cur = None

		try:

			conn = psycopg2.connect(
					host = "localhost",
					dbname = "demo",
					user = "postgres",
					password = 256809,
					port = 5433)

			cur = conn.cursor()

			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
			cur.execute(f"SELECT Times FROM vapes WHERE Brand = '{Brand}' AND Taste = '{Taste}'")
			for i in set(cur.fetchall()):
				item = types.KeyboardButton(i[0])
				markup_reply.add(item)
				list2.append(i[0])

			mesg = bot.send_message(message.chat.id, "На сколько тяжек)", reply_markup = markup_reply)
			bot.register_next_step_handler(mesg, Result)

			conn.commit()

		finally:
			if conn is not None:
				conn.close()

			if cur is not None:
				cur.close()
	
	else:

		global Times
		Times = str(message.text)

		conn = None
		cur = None

		try:

			conn = psycopg2.connect(
					host = "localhost",
					dbname = "demo",
					user = "postgres",
					password = 256809,
					port = 5433)

			cur = conn.cursor()

			cur.execute(f"SELECT Price FROM vapes WHERE Brand = '{Brand}' AND Taste = '{Taste}' AND Times = '{Times}'")
			global Price
			Price = cur.fetchall()[0][0]

			cur.execute(f"SELECT Price FROM vapes WHERE Brand = '{Brand}' AND Taste = '{Taste}' AND Times = '{Times}' AND Price = '{Price}'")
			global len_of_result_vapes
			len_of_result_vapes = len(cur.fetchall())

			ResultOrder = "Итог: \nБренд: " + Brand + "\nВкус: " + Taste + "\nКоличество тяг: " + Times + "\nЦена за одну штуку: " + str(Price) + "\nВ наличии: " + str(len_of_result_vapes)
			mesg = bot.send_message(message.chat.id, ResultOrder, reply_markup = types.ReplyKeyboardRemove())
			bot.send_message(message.chat.id, "Сколько будете брать?")
			bot.register_next_step_handler(mesg, EndOfOrder)

			conn.commit()

		finally:
			if conn is not None:
				conn.close()

			if cur is not None:
				cur.close()

@bot.message_handler(func = lambda message: message.text == "ipanjipaSidioandoiasidn")
@bot.message_handler(func = check)
def EndOfOrder(message):
	if int(message.text) > len_of_result_vapes:

		bot.send_message(message.chat.id, "У нас столько нет в наличии)")
		global ResultOrder
		ResultOrder = "Итог: \nБренд: " + Brand + "\nВкус: " + Taste + "\nКоличество тяг: " + Times + "\nЦена за одну штуку: " + str(Price) + "\nВ наличии: " + str(len_of_result_vapes)
		mesg = bot.send_message(message.chat.id, ResultOrder, reply_markup = types.ReplyKeyboardRemove())
		bot.send_message(message.chat.id, "Сколько будете брать?")
		bot.register_next_step_handler(mesg, EndOfOrder)

	elif int(message.text) <= 0:

		bot.send_message(message.chat.id, "Буль Буль")
		ResultOrder = "Итог: \nБренд: " + Brand + "\nВкус: " + Taste + "\nКоличество тяг: " + Times + "\nЦена за одну штуку: " + str(Price) + "\nВ наличии: " + str(len_of_result_vapes)
		mesg = bot.send_message(message.chat.id, ResultOrder, reply_markup = types.ReplyKeyboardRemove())
		bot.send_message(message.chat.id, "Сколько будете брать?")
		bot.register_next_step_handler(mesg, EndOfOrder)

	else:
		global Choosen
		Choosen = str(message.text)

		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item = types.KeyboardButton("Добавить в корзину🚩")
		item1 = types.KeyboardButton("Вернуться в самое начало💫")
		markup_reply.add(item, item1)
		ResultOrder = "Бренд: " + Brand + "\nВкус: " + Taste + "\nКоличество тяг: " + Times + "\nЦена за одну штуку: " + str(Price) + "\nКоличество: " + str(message.text) + "\nК оплате: " + str(int(Price) * int(message.text))
		mesg = bot.send_message(message.chat.id, ResultOrder, reply_markup = markup_reply)
		bot.register_next_step_handler(mesg, Ask)

@bot.message_handler(func = lambda message: message.text == "posjfja0wjdnoisafo ioasninjo asjo j 2j2 3jo 4jk3j 4o2n34")
def Ask(message):
	if message.text != "Вернуться в самое начало💫" and message.text != "Добавить в корзину🚩":
		bot.send_message(message.chat.id, "Что бы вы не ввели продолжаем🤣")
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item = types.KeyboardButton("Завершить заказ🙄")
		item1 = types.KeyboardButton("Купить ещё что нибудь🥴")
		markup_reply.add(item, item1)
		global Busket
		Busket = Busket + ResultOrder + "\n"
		mesg = bot.send_message(message.chat.id, "Успешно добавлено в корзину🤑\nВыберите что-нибудь📌", reply_markup = markup_reply)
		bot.register_next_step_handler(mesg, Ask2)

	elif message.text == "Вернуться в самое начало💫":
		conn = None
		cur = None

		try:

			conn = psycopg2.connect(
					host = "localhost",
					dbname = "demo",
					user = "postgres",
					password = 256809,
					port = 5433)

			cur = conn.cursor()

			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
			cur.execute("SELECT Brand FROM vapes")
			for i in set(cur.fetchall()):
				item = types.KeyboardButton(i[0])
				markup_reply.add(item)
				list.append(i[0])

			mesg = bot.send_message(message.chat.id, "Какой бренд вы предпочитаете?)", reply_markup = markup_reply)
			bot.register_next_step_handler(mesg, ChoosingOfTaste)

			conn.commit()

		finally:
			if conn is not None:
				conn.close()

			if cur is not None:
				cur.close()

	else:
		conn = None
		cur = None

		try:

			conn = psycopg2.connect(
				host = "localhost",
				dbname = "demo",
				user = "postgres",
				password = 256809,
				port = 5433)

			cur = conn.cursor()

			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item = types.KeyboardButton("Завершить заказ🙄")
			item1 = types.KeyboardButton("Купить ещё что нибудь🥴")
			markup_reply.add(item, item1)
			Busket = Busket + ResultOrder + "\n"
			cur.execute(f"DELETE * FROM vapes WHERE Brand = '{Brand} AND Taste = '{Taste} AND Times = '{Times} AND Price = '{Price}' LIMIT '{Choosen}'")
			bot.send_message(message.chat.id, "Успешно добавлено в корзину🤑")
			mesg = bot.send_message(message.chat.id, "Выберите что-нибудь📌", reply_markup = markup_reply)
			bot.register_next_step_handler(mesg, Ask2)

			conn.commit()

		finally:
			if cur is not None:
				cur.close()

			if conn is not None:
				conn.close()

@bot.message_handler(func = lambda message: message.text == "ksi-fjaisjdauhsudhuasdh asda shd  sdaj sdh ajs dj ashd h j12 3j1 2jh3 ")
def Ask2(message):
	if message.text == "Завершить заказ🙄":
		mesg = bot.send_message(message.chat.id, "Введите номер телефона", reply_markup = types.ReplyKeyboardRemove())
		bot.register_next_step_handler(mesg, Sending)

	if message.text == "Купить ещё что нибудь🥴":

		conn = None
		cur = None

		try:

			conn = psycopg2.connect(
					host = "localhost",
					dbname = "demo",
					user = "postgres",
					password = 256809,
					port = 5433)

			cur = conn.cursor()

			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
			cur.execute("SELECT Brand FROM vapes")
			for i in set(cur.fetchall()):
				item = types.KeyboardButton(i[0])
				markup_reply.add(item)
				list.append(i[0])

			mesg = bot.send_message(message.chat.id, "Какой бренд вы предпочитаете?)", reply_markup = markup_reply)
			bot.register_next_step_handler(mesg, ChoosingOfTaste)

			conn.commit()

		finally:
			if conn is not None:
				conn.close()

			if cur is not None:
				cur.close()

@bot.message_handler(func = lambda message: message.text == "kaodsjoinoansjf askf  j j 12j 3j 12 3uio1nb2h h1 23")
def Sending(message):
	global Busket
	Busket = Busket
	
	bot.send_message(1236422161, "Новый ЗАКАЗ)))")
	bot.send_message(1236422161, Busket)
	bot.send_message(1236422161, "На этот номер телефона: " + str(message.text))
	bot.send_message(message.chat.id, "Заказ успешно сделан☑️")
	bot.send_message(message.chat.id, "Ждите пока админ свяжится с вами.")
	list = []
	list1 = []
	list2 = []
	Busket = ""

bot.polling()