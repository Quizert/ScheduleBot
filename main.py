import telebot
import config
import get_schedule
import time_controller
from telebot import types

schedule = get_schedule.Schedule().GetSchedule()
bot = telebot.TeleBot(config.TOKEN)

time_controller = time_controller.Timer()


@bot.message_handler(commands=['start'])
def welcome(message):
    global schedule
    time_controller.SetCurrentTime()

    if time_controller.isGood():
        schedule = get_schedule.Schedule().GetSchedule()
        time_controller.SetPrevData()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    monday = types.KeyboardButton("Понедельник")
    tuesday = types.KeyboardButton("Вторник")
    wednesday = types.KeyboardButton("Среда")
    thursday = types.KeyboardButton("Четверг")
    friday = types.KeyboardButton("Пятница")
    saturday =  types.KeyboardButton("Суббота")

    markup.add(monday, tuesday, wednesday, thursday, friday, saturday)

    bot.send_message(message.chat.id, "пися попа", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    global schedule
    time_controller.SetCurrentTime()

    if time_controller.isGood():
        schedule = get_schedule.Schedule().GetSchedule()
        time_controller.SetPrevData()

        
    string = ""

    end_line_format = '\n-----------------------------------------------------------------------\n'
    end_time_format = ':\n'

    if message.text == 'Понедельник':
        for i in schedule:
            string += i + end_time_format + ''.join(schedule[i][0]) + end_line_format
        bot.send_message(message.chat.id, string)

    if message.text == 'Вторник':
        for i in schedule:
            string += i + end_time_format + ''.join(schedule[i][1]) + end_line_format
        bot.send_message(message.chat.id, string)

    if message.text == 'Среда':
        for i in schedule:
            string += i + end_time_format + ''.join(schedule[i][2]) + end_line_format
        bot.send_message(message.chat.id, string)
        
    if message.text == 'Четверг':
        for i in schedule:
            string += i + end_time_format + ''.join(schedule[i][3]) + end_line_format
        bot.send_message(message.chat.id, string)

    if message.text == 'Пятница':
        for i in schedule:
            string += i + end_time_format + ''.join(schedule[i][4]) + end_line_format
        bot.send_message(message.chat.id, string)

    if message.text == 'Суббота':
        for i in schedule:
            string += i + end_time_format + ''.join(schedule[i][5]) + end_line_format
        bot.send_message(message.chat.id, string)

bot.polling(non_stop=True)
