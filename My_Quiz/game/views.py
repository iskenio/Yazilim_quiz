from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from string import digits
from .models import Questions
import telebot
from telebot import types
import random
# https://api.telegram.org/bot883353222:AAGBt8lNOYwUhMX1EzXpUGL48fSz_hRiuYQ/setWebhook?url=https://0b0b7915.ngrok.io/game
token = 'bot883353222:AAGBt8lNOYwUhMX1EzXpUGL48fSz_hRiuYQ'
bot = telebot.TeleBot(token)


@csrf_exempt
def get_answer(request):
    r = request
    # print("method: " + repr(r.method))

    json_string = request.body.decode('utf-8')

    update = telebot.types.Update.de_json(json_string)

    bot.process_new_updates([update])

    @bot.message_handler(regexp="AA")
    def handle_message(message):
        bot.send_message(chat_id=message.chat.id, text='ASdasda')

    @bot.message_handler(content_types=["text"])
    def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
        print(message.text)
        if message.text == '1':
            print('YES')
        q = Questions.objects.first()
        answ = q.question
        if answ == message.text:
            print('TRIE')
    return HttpResponse(repr(r.method))


# TOKEN = '883353222:AAGBt8lNOYwUhMX1EzXpUGL48fSz_hRiuYQ'
# STICKER_ID = 'CAADAgADcggAAnlc4gkMbqeDXAz88QI'
#
# bot = telebot.TeleBot(TOKEN)
#
# @bot.message_handler(commands=['start', 'help'])
# def command_hadler(message: Message):
#     bot.reply_to(message, 'Здравствуйте')
#     markup = types.ReplyKeyboardMarkup(row_width=2)
#     itembtn1 = types.KeyboardButton('Старт')
#     itembtn2 = types.KeyboardButton('Закончить игру')
#     itembtn3 = types.KeyboardButton('Рейтинг')
#     markup.add(itembtn1, itembtn2, itembtn3)
#     bot.send_message(chat_id=message.chat.id, text="Я бот для игры в квиз", reply_markup=markup)
#
#     # or add KeyboardButton one row at a time:
#     markup = types.ReplyKeyboardMarkup()
#     itembtna = types.KeyboardButton('Start')
#     itembtnv = types.KeyboardButton('End Game')
#     itembtnc = types.KeyboardButton('Рейтинг')
#     itembtnd = types.KeyboardButton('Помощь')
#
#     markup.row(itembtna, itembtnv)
#     markup.row(itembtnc, itembtnd)
#     bot.send_message(chat_id=message.chat.id, text="Разреши мне читать все сообщения в этой группе, чтобы начать играть.", reply_markup=markup)
#
# @bot.message_handler(content_types=['text'])
# def echo_digits(message: Message):
#     if 'Start' in message.text:
#         bot.reply_to(message, 'Я – бот для игры в квиз.'
#                               'Разреши мне читать все сообщения в этой беседе, чтобы начать играть.')
#         arr_quiz = ['Первый президент Казахстана', 'Продолжите фразу: "делу время потехе...', 'В каком году произошло Андижанское восстание?']
#         bot.send_message(chat_id=message.chat.id, text=random.choice(arr_quiz))
#
#         return
#     #bot.reply_to(message, 'Каниет')
#
# @bot.message_handler(content_types=['sticker'])
# def sticker_handler(message: Message):
#     bot.send_sticker(message.chat.id, STICKER_ID)
#
# bot.polling(timeout=10)
