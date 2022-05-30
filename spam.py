import telebot

bot = telebot.TeleBot("5376593442:AAHExJ0vq-9JT2EhkxAi6lNMgjL6mb0Ys44")

@bot.message_handler(func = lambda message: True)
def spam(message):
	bot.send_photo(message.chat.id, r"https://cdn-front.kwork.ru/pics/t3/20/11726931-1608538420.jpg", "Я научился писать телеграм ботов здесь - https://stepik.org/course/107302/ \nА ты чем занимался!?\nИди быстро играй в пайтон")

bot.polling()