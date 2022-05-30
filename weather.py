import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot('5064388730:AAEJae2PIdWwv7f-BWPkaRc5C_TqE5kPt5Q') 

@bot.message_handler(commands=['start'])
def get_user_info(message):
	bot.send_message(message.chat.id, 'Здравствуй, странник!\nЭтот телеграм бот скажет тебе погоду и поможет правильно одеться\nВведите название города:')

@bot.message_handler(content_types = ['text'])	
def get_text(message):
	owm = OWM('c2a7abaeee27d5b6bc639039d38d3ab2')
	mgr = owm.weather_manager()
	config_dict = get_default_config()
	config_dict['language'] = 'ru'
	observation = mgr.weather_at_place( message.text )
	w = observation.weather
	temp = w.temperature("celsius")['temp']
	toch = w.detailed_status
	answer = " В городе  " + message.text + " сейчас " + toch
	bot.send_message(message.chat.id, answer)

	if temp <= 10:
		bot.send_message(message.chat.id, " Температура в районе " + str(temp) + " , сейчас пипец холодно, одевайся как танк ")
	elif temp <= 15:
		bot.send_message(message.chat.id, " Температура сейчас в районе " + str(temp) + " , на улице прохладно одеввайся теплее ")
	else:
		bot.send_message(message.chat.id, " Погода хорошая в районе " + str(temp) + " , одевайся как хочешь ")

bot.polling()
