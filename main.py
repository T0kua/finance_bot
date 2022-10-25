import telebot
from telebot import types
import sqlite3
import datetime

#подключение бд
div = (__file__[0:-7]) #путь к папке файлом
db = sqlite3.connect('test.db',check_same_thread=False)
sql = db.cursor()

#токен
bot = telebot.TeleBot("5773248805:AAGOho4xQcUUimERLyXK6T4LsziXWpxwMDk")
selfid = 1302569962 #вставте свой id
def swet(r): #получение даты
	time = datetime.datetime.today()
	together = str(time)[:10]#age   month     day
	#2022-10-24
	#12345678910
	together = [int(together[:4]),int(together[5:7]),int(together[8:10])]
	if r == "day" :
		return (together[2])
	if r == "month" :
		return (together[1])
	else:
		return(together[0])

@bot.message_handler(commands=['stat'])
def start(message):
	money = 0 #прибыль
	buy = 0   #траты
	for val in sql.execute(f"SELECT * from tabl WHERE age = {swet('age')}"):
		if val[2] == swet('day') and val[3] == swet('month') :
			if val[0] > 0 :
				money += val[0]
			else :
				buy += val[0]
	bot.send_message(message.chat.id,f"за сегодняшний день вы:\nпотратили {-buy}\nзаработали {money}\nитого: {buy + money}")

@bot.message_handler(content_types=['text'])
def start(message):
	if message.from_user.id == selfid :
		text = message.text
		text= text.split("%")
		if True:
			text[0] = int(text[0])
			sql.execute(f"INSERT INTO tabl VALUES (?,?,?,?,?)",(text[0],text[1],swet("day"),swet("month"),swet("age")))
			db.commit()
			bot.send_message(message.chat.id,"сохранено")
		else:
			bot.send_message(message.chat.id,"ошибка")
bot.polling()