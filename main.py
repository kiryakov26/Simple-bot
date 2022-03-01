import telebot
from telebot import types
import requests

bot = telebot.TeleBot("5179322043:AAEsVNYOTaI8-2uEcxoQdcnC0xLc33MeHb0")
city =''
appid = "7fb937de8789d8b01431fe07d10446e1"

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    bot.send_message ( message.chat.id, 'Привет! Я бот про конструктор LEGO. Если хочешь узнать что я умею жми help', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/buy", "Хочу","/check" ,"История","Обзор","/start","/weather")
    bot.send_message(message.chat.id, 'Если хочешь заказать конструктор, жми buy \n'
                                      'Хотите узнать стоимость заказа в рублях, жми check \n'
                                      'Хочешь узнать о новинках Lego, пиши Хочу \n'
                                      'Хочешь узнать про историю компании Lego, пиши История \n'
                                      'Хочешь прочитать обзоры на наборы, пиши Обзор \n'
                                      'Начать все сначала, жми start' 
                                      'Хочешь узнать погоду в городе, жми weather',reply_markup=keyboard)

@bot.message_handler(commands=['buy'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    bot.send_message ( message.chat.id, 'Тогда тебе сюда – https://lego.com')
    bot.send_message ( message.chat.id, 'Вернуться к возможностям, жми help', reply_markup=keyboard)

@bot.message_handler(commands=['weather'])
def city (message):
    bot.send_message(message.from_user.id, "В каком городе очешь узнать погоду?\n"+ 'Введи название города на английском и страну, через запятую: в формате Moscow,Ru')
    bot.register_next_step_handler(message,weather )
def weather(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/weather","/help","/weather-weak")
    global city
    city = message.text
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    bot.send_message (message.chat.id,'Город: '+str(city)+'\n'+'Погодные условия: '+str(data['weather'][0]['description'])+'\n'+"Температура: "+str(data['main']['temp'])+'\n'+
                      "Минимальная температура: "+str(data['main']['temp_min'])+'\n'+"Максимальная температура: "+str(data['main']['temp_max'])+'\n'+
                      "Скорость ветра: "+str(data['wind']['speed'])+'\n'+"Видимость: "+str(data['visibility']) )
    bot.send_message(message.chat.id ,'Хочешь узнать погоду в другом городпе, жми weather \n' +'Вернуться к возможностям, жми help', reply_markup=keyboard)

@bot.message_handler(commands=['check'])
def converter_mode_0(message):
    bot.send_message(message.chat.id, 'USD->RUB , Введите сумму заказа')
    global O
    O = 0

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mir-kubikov.ru/lego/new/')
    elif message.text.lower() == "история":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://ru.wikipedia.org/wiki/LEGO')
    elif message.text.lower() == "обзор":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – http://bricker.ru')
    elif O == 0:
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row("/help")
        bot.send_message(message.chat.id, round(float(float(message.text) * 75.24), 2))
        bot.send_message(message.chat.id, 'Чтобы продолжить, пиши следующуюю сумму: \n'
                                          'Вернуться к возможностям, жми help', reply_markup=keyboard)


bot.polling()
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mir-kubikov.ru/lego/new/')
    elif message.text.lower() == "история":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://ru.wikipedia.org/wiki/LEGO')
    elif message.text.lower() == "обзор":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – http://bricker.ru')
    elif i == 0:
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row("/help")
        bot.send_message(message.chat.id, round(float(float(message.text) * 75.24), 2))
        bot.send_message(message.chat.id, 'Чтобы продолжить, пиши следующуюю сумму: \n'
                                          'Вернуться к возможностям, жми help', reply_markup=keyboard)
bot.polling()
