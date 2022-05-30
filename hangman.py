import telebot
from telebot import types
import psycopg2

replace_hire_word = "" 

bot = telebot.TeleBot("5307145956:AAF7BsexPCrLdEFbxUpABKaczESCT0uiWGQ")

@bot.message_handler(commands = ["start"])
def users_id(message):
	try:
		conn = None
		cur = None

		conn = psycopg2.connect(
				host = "localhost",
				dbname = "demo",
				user = "postgres",
				password = 256809,
				port = 5433)

		cur = conn.cursor()

		cur.execute("SELECT * FROM game")

		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item = types.KeyboardButton("Продолжить")
		markup_reply.add(item)
		mesg2 = bot.send_message(message.chat.id, "Ваш оппонент уже загадал слово, нажмите продолжить", reply_markup = markup_reply)
		bot.register_next_step_handler(mesg2, game)

	except Exception as error:
		mesg0 = bot.send_message(message.chat.id, "Привет " + str(message.from_user.first_name) + "\nВы хост этой игры, загадайте слово")
		bot.register_next_step_handler(mesg0, word)

	finally:
		if cur is not None:
			cur.close()

		if conn is not None:
			conn.close()	

@bot.message_handler(func = lambda message: message.text == "Продолжить")
def game(message):
	try:
		a = types.ReplyKeyboardRemove()
		conn = psycopg2.connect(
				host = "localhost",
				dbname = "demo",
				user = "postgres",
				password = 256809,
				port = 5433)

		cur = conn.cursor()

		cur.execute("SELECT * FROM game")
		global hire_word
		global replace_hire_word
		global tries

		hire_word = cur.fetchall()[0][1]
		replace_hire_word = len(hire_word) * "_"
		tries = len(hire_word) * 2

		mesg3 = bot.send_message(message.chat.id, replace_hire_word, reply_markup = a)
		bot.register_next_step_handler(mesg3, second_game)

		conn.commit()

	finally:
		if cur is not None:
			cur.close()

		if conn is not None:
			conn.close()

@bot.message_handler(func = lambda message: len(str(message.text)) >= 1 and message.text != "/getsecretinfo")
def second_game(message):
	if len(str(message.text)) == 1:

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

			cur.execute("SELECT * FROM game")
			global host_id
			host_id = cur.fetchall()[0][0]

			global replace_hire_word
			global tries

			if tries == 0 and replace_hire_word != hire_word:
				bot.send_message(message.chat.id, "Вы проиграли((( \nУ вас закончились попытки \nЗагаданное слово было " + hire_word + "\nВведите команду /start что бы начать заново")
				bot.send_message(host_id, "Вы выиграли))) \nУ оппонента закончились попытки \nВведите команду /start что бы начать заново")
				cur.execute("DROP TABLE game")
				tries = 0

			elif str(message.text).lower() in hire_word:

				a = 0
				if hire_word.count(str(message.text).lower()) >= 2:
					while a != hire_word.count(str(message.text).lower()):
						try:
							first = hire_word.find(str(message.text).lower(), first + 1)
							bob = list(replace_hire_word)
							bob[first] = str(message.text).lower()
							replace_hire_word = "".join(bob)
							a += 1

						except:
							first = hire_word.find(str(message.text).lower())
							bob = list(replace_hire_word)
							bob[first] = str(message.text).lower()
							replace_hire_word = "".join(bob)
							a += 1
					
					bot.send_message(message.chat.id, str(replace_hire_word) + "\nВы отгадали букву) \nУ вас осталось " + str(tries) + " попыток")
					bot.send_message(host_id, str(replace_hire_word) + "\nОппонент отгадал букву( \nУ оппонента осталось " + str(tries) + " попыток")
					tries -= 1

					if replace_hire_word == hire_word:
						bot.send_message(message.chat.id, "Вы отгадали слово))) \nВведите команду /start что бы начать заново")
						bot.send_message(host_id, "Вы проиграли \nОппонент угадал слово \nВведите команду /start что бы начать заново")
						cur.execute("DROP TABLE game")
						tries = 0

				elif hire_word.count(str(message.text).lower()) == 1:
					letter_index = hire_word.index(str(message.text).lower())
					bob = list(replace_hire_word)
					bob[letter_index] = str(message.text).lower()
					replace_hire_word = "".join(bob)

					bot.send_message(message.chat.id, str(replace_hire_word) + "\nВы отгадали букву) \nУ вас осталось " + str(tries) + " попыток")
					bot.send_message(host_id, str(replace_hire_word) + "\nОппонент отгадал букву( \nУ оппонента осталось " + str(tries) + " попыток")
					tries -= 1

					if replace_hire_word == hire_word:
						bot.send_message(message.chat.id, "Вы отгадали слово))) \nВведите команду /start что бы начать заново")
						bot.send_message(host_id, "Вы проиграли \nОппонент угадал слово \nВведите команду /start что бы начать заново")
						cur.execute("DROP TABLE game")
						tries = 0

			elif message.text not in hire_word:
				bot.send_message(message.chat.id, "Вы не отгадали букву( \nУ вас осталось " + str(tries) + " попыток")
				bot.send_message(host_id, "Оппонент не отгадал букву) \nУ оппонента осталось " + str(tries) + " попыток")
				tries -= 1

			conn.commit()

		finally:
			if cur is not None:
				cur.close()

			if conn is not None:
				conn.close()

	else:
		bot.send_message(message.chat.id, "Ты чё самый умный")
		bot.send_message(host_id, "Оппонент типо самый умный")

@bot.message_handler(commands = ["фыф"])
def word(message):
	if len(str(message.text).split()) == 1:
		cur = None
		conn = None

		try:
			conn = psycopg2.connect(
					host = "localhost",
					dbname = "demo",
					user = "postgres",
					password = 256809,
					port = 5433)

			cur = conn.cursor()

			global hire_word
			global host_id
			host_id = message.chat.id
			hire_word = message.text

			create_script = """CREATE TABLE IF NOT EXISTS game(
					users_id INT,
					word varchar(20))"""

			cur.execute(create_script)

			insert_script = "INSERT INTO game VALUES(%s, %s)"
			insert_value = (host_id, hire_word.lower())

			cur.execute(insert_script, insert_value)

			bot.send_message(host_id, "Слово загадано, ждём оппонента")

			conn.commit()

		finally:
			if cur is not None:
				cur.close()

			if conn is not None:
				conn.close()

	else:
		host_id = message.chat.id
		bot.send_message(host_id, "Вводите только одно слово")

@bot.message_handler(commands = ["getsecretinfo"])
def secretinfro(message):
	inline_murkup = types.InlineKeyboardMarkup()
	hyper_text = types.InlineKeyboardButton(text = "Ссылка", url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
	inline_murkup.add(hyper_text)
	bot.send_message(message.chat.id, "Перейди по ссылке что бы получить доступ", reply_markup = inline_murkup)

bot.polling()