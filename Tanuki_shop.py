import telebot
from telebot import types

bot = telebot.TeleBot("5301445112:AAFJN5KGpQ01Cl6tQJa6IkuN8GVCIbrKReI")

@bot.message_handler(commands = ["start"])
def say_hello_to_new_user(message):
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	ok = types.KeyboardButton("ОК")
	markup_reply.add(ok)
	bot.send_message(message.chat.id, "Привет " + str(message.from_user.first_name) + " " + str(message.from_user.last_name) + "😝\nТы попал в онлайн магазин сеть ресторанов Тануки🍥\nТочки разположения наших ресторанов раположены по всей Росии, в частности в Москве и в Подмосковье🏢\nВ нашем ресторане огромный ассортимент различных блюд, начиная от японской кухни и заканчиваю итяльянской🍕", reply_markup = markup_reply)

@bot.message_handler(content_types = ["text"])
def main_menu(message):
	if message.text == "ОК": 
		menu = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True)
		rolli = types.KeyboardButton("Роллы")
		sushi = types.KeyboardButton("Суши")
		pizza = types.KeyboardButton("Пицца")
		soup = types.KeyboardButton("Супы")
		not_soft_drinks = types.KeyboardButton("Газированные напитки")
		alcohol_drinks = types.KeyboardButton("Алкогольные напитки")
		menu.add(rolli, sushi, pizza, soup, not_soft_drinks, alcohol_drinks)
		bot.send_message(message.chat.id, "Что вы хотите купить?", reply_markup = menu)

	elif message.text == "Роллы":
		menu_of_rolli = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
		item1 = types.KeyboardButton("Лосось гриль терияки")
		item2 = types.KeyboardButton("Марбл Грин Ролл")
		item3 = types.KeyboardButton("Макуро")
		item4 = types.KeyboardButton("Спайс микс")
		item5 = types.KeyboardButton("Калифорния с угрем")
		item6 = types.KeyboardButton("Филадельфия лайт")
		back = types.KeyboardButton("Вернуться")
		menu_of_rolli.add(item1, item2, item3, item4, item5, item6, back)
		bot.send_message(message.chat.id, "Что бы вы хотели приобрести?", reply_markup = menu_of_rolli)
		
	elif message.text == "Пицца":
		menu_of_rolli = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
		item1 = types.KeyboardButton("Гриль с колбасками")
		item2 = types.KeyboardButton("Мексиканская")
		item3 = types.KeyboardButton("Гавайская")
		item4 = types.KeyboardButton("Цезарь")
		item5 = types.KeyboardButton("Тай-фри")
		item6 = types.KeyboardButton("Жульен")
		back = types.KeyboardButton("Вернуться")
		menu_of_rolli.add(item1, item2, item3, item4, item5, item6, back)
		bot.send_message(message.chat.id, "Что бы вы хотели приобрести?", reply_markup = menu_of_rolli)		

	elif message.text == "Сушы":
		pass

	elif message.text == "Супы":
		pass

	elif message.text == "Газированные напитки":
		pass

	elif message.text == "Алкогольные напитки":
		pass

	elif message.text == "Вернуться":
		menu = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True)
		rolli = types.KeyboardButton("Роллы")
		sushi = types.KeyboardButton("Суши")
		pizza = types.KeyboardButton("Пицца")
		soup = types.KeyboardButton("Супы")
		not_soft_drinks = types.KeyboardButton("Газированные напитки")
		alcohol_drinks = types.KeyboardButton("Алкогольные напитки")
		menu.add(rolli, sushi, pizza, soup, not_soft_drinks, alcohol_drinks)
		bot.send_message(message.chat.id, "Что вы хотите купить?", reply_markup = menu)		

	else:
		bot.send_message(message.chat.id, "Выберите блюдо")

bot.polling()