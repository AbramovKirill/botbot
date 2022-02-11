#from aiogram import types
import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.token)



tel = 0
oblast = ''
city = ''
kvartira = 0
liverType = ''
fio = ''



bot = telebot.TeleBot(config.token)

#функция оброботки команды старт
@bot.message_handler(commands=['start'])#старт бота, человек первый раз запускает бота
def welcome(message):
   sti = open('static/sticker.webp', 'rb')
   bot.send_sticker(message.chat.id, sti)#отправляет приветст стикер

   # keyboard simple(под полем ввода собщ)
   # -1- создаем клаву
   markup = telebot.types.ReplyKeyboardMarkup(True, True)#тут удаляется кнопка
   item1 = types.KeyboardButton("😊Зарегистрироваться!")
   markup.add(item1)

   bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помочь вам. Перед тем как начать, пожалуйста зарегистрируйтесь 😊.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)# -2- цепляем к обычн сообщению

@bot.message_handler(content_types=['text'])
def lalala(message):
   if message.chat.type == 'private':
      if message.text == '😊Зарегистрироваться!':
         bot.send_message(message.chat.id, "Регистрация. {0.first_name}, пожалуйства поочереди введите данные для регистрации. Будьте внимательны, не делайте ошибок.".format(message.from_user, bot.get_me()), parse_mode='html')
         bot.send_message(message.chat.id, 'Введите свой номер телефона:')
         bot.register_next_step_handler(message, reg_tel)

def reg_tel(message):
   global tel
   tel = message.text
   bot.send_message(message.from_user.id, "Из Какой вы области?")
   bot.register_next_step_handler(message, reg_oblast)

def reg_oblast(message):
   global oblast
   oblast = message.text
   bot.send_message(message.from_user.id, "Из какого вы города?")
   bot.register_next_step_handler(message, reg_city)

def reg_city(message):
   global city
   city = message.text
   bot.send_message(message.from_user.id, "Из какой вы квартиры?")
   bot.register_next_step_handler(message, reg_kvartira)

def reg_kvartira(message):
   global kvartira
   kvartira = message.text

   markup = telebot.types.ReplyKeyboardMarkup(True, True)#тут удаляется кнопка
   item1 = types.KeyboardButton("власник")
   item2 = types.KeyboardButton("орендатор")
   item3 = types.KeyboardButton("мешканець")
   markup.add(item1, item2, item3)

   bot.send_message(message.from_user.id, "Який ви тип мешканця?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
   bot.register_next_step_handler(message, reg_liverType)

def reg_liverType(message):
   global liverType

   if message.text == 'власник':
      liverType = 'власник'
   elif message.text == 'орендатор':
      liverType = 'орендатор'
   elif message.text == 'мешканець':
      liverType = 'мешканець'
      
   # bot.send_message(message.from_user.id, liverType)
   bot.send_message(message.from_user.id, "Ваше ФИО через пробел.")
   bot.register_next_step_handler(message, reg_fio)

def reg_fio(message):
   global fio
   fio = message.text
   bot.send_message(message.from_user.id, "Поздравляю. Вы закончили регистрацию.\n Внимательно просмотрите собой заполн инфор, если есть ошибки, нажмите кнопку редактировать. Если всё зорошо нажмите ок" )
   bot.register_next_step_handler(message, welcome2)
#добавить кнопки и всё зафигачить в цыкл

# def check(message):
#    bot.send_message(message.from_user.id, liverType)


@bot.message_handler(content_types=['text'])
def welcome2(message):

   markup = telebot.types.ReplyKeyboardMarkup(True, True)
   item1 = types.KeyboardButton("1.-ОГОЛОШЕННЯ")
   item2 = types.KeyboardButton("1.-СОЗД_ЗАЯВ")
   markup.add(item1, item2)

   bot.send_message(message.chat.id, "{0.first_name}, выберете один из пунктов меню".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
   if message.chat.type == 'private':
      if message.text == '1.-ОГОЛОШЕННЯ':
            markup = types.ReplyKeyboardMarkup(True, True)
            item1 = types.KeyboardButton("1.1.-просмотреть")
            item2 = types.KeyboardButton("1.2.-редактирование(?)")
            markup.add(item1, item2)
            bot.send_message(message.from_user.id, "Вы может просмотреть оголошення. Или же, буду чи админом, отредактировать их.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

      elif message.text == '1.-СОЗД_ЗАЯВ':
            bot.send_message(message.from_user.id, "Вы находитесь в поле меню создания заявки. Опишите свою проблему текстом которая у вас случилась. А после выберете одну из катЕгорий.")
            #придумать как запоминать текст

            markup = types.ReplyKeyboardMarkup(True, True)
            item1 = types.KeyboardButton("проблемы c лампочкой")
            item2 = types.KeyboardButton("проблемы с соседями")
            item2 = types.KeyboardButton("проблемы с водой")
            markup.add(item1, item2, item3)
            bot.send_message(message.from_user.id, "Выберете одно из 3х полей.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)



# @bot.message_handler(content_types=['text'])
# def welcome2(message):

#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#    item1 = types.KeyboardButton("🎲 оголошення")
#    item2 = types.KeyboardButton("😊 заявки")
#    markup.add(item1, item2)

#    bot.send_message(message.chat.id, "{0.first_name}, выберете один из пунктов меню".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)



# @bot.message_handler(content_types=['text'])
# def lalala2(message):
#    if message.chat.type == 'private':
#       if message.text == '🎲 оголошення ':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             item1 = types.KeyboardButton("🎲 просмотреть")
#             item2 = types.KeyboardButton("😊 редактирование(?)")
#             markup.add(item1, item2)
#             bot.send_message(message.from_user.id, "Вы может просмотреть оголошення. Или же, буду чи админом, отредОктировать их.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)



#       elif message.text == '😊 заявки':
#             bot.send_message(message.from_user.id, "Вы находитесь в поле меню создания заявки. Опишите свою проблему текстом которая у вас случилась. А после выберете одну из катЕгорий.")
#             #придумать как запоминать текст

#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             item1 = types.KeyboardButton("проблемы c лампочкой")
#             item2 = types.KeyboardButton("проблемы с соседями")
#             item2 = types.KeyboardButton("проблемы с водой")
#             markup.add(item1, item2, item3)
#             bot.send_message(message.from_user.id, "Выберете одно из 3х полей.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)



# def problem(message):
#    if message.text == 'проблемы c лампочкой':
#       liverType = ''
#    elif message.text == 'проблемы с соседями':
#       liverType = ''
#    elif message.text == 'проблемы с водой':
#       liverType = ''


# RUN
bot.polling(none_stop=True)