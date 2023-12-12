import telebot;
import json;

API_TOKEN = '6488207375:AAGtkWonmV4XSnZgjUvzoy4fxL46kXsYyW8'
bot = telebot.TeleBot(API_TOKEN)

global phone_book
phone_book = {}
""" phone_book = {
        "дядя Ваня": {'pnones': 121212, 'email': "123@mail.ru"},
        "дядя Вася": {'pnones': 55555}
    } """

def load_data():
    with open("phonebook.json", "r", encoding="utf-8") as fh:
        global phone_book
        phone_book = json.load(fh)        

def save_data():
    with open("phonebook.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phone_book, ensure_ascii=False))

def get_phone(message):
    global phone
    phone = message.text

    phone_book[surname] = {'имя' : name,
                      'почта': email,
                      'телефон' : phone
                      }
    
    bot.send_message(message.from_user.id, 'Контакт добавлен:')

def get_email(message):
    global email
    email = message.text
    bot.send_message(message.from_user.id, 'Введите номер телефона:')
    bot.register_next_step_handler(message, get_phone)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Введите почту:')
    bot.register_next_step_handler(message, get_email)

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Введите фамилию:')
    bot.register_next_step_handler(message, get_surname)        

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "Привет" or message.text == "/help":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь? Чтобы увидеть список команд, напиши /start")
    
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Список команд: /contact, /save, /add, /delete, /search, /replace, /load")

    elif message.text == "/load":                  
        load_data()
        bot.send_message(message.from_user.id, "Наш список контактов успешно загружен")

    elif message.text == "/contact":
        if len(phone_book.items()) > 0:
            for k, w in phone_book.items():         
                bot.send_message(message.from_user.id, f"{k}: {w}")
        else:
            bot.send_message(message.from_user.id, "Список контактов пуст: выполните комаду /load или /add")        

    elif message.text == "/add":
        bot.send_message(message.from_user.id, "Введите имя:")
        bot.register_next_step_handler(message, get_name)
            
    elif message.text == "/save":
        save_data()
        bot.send_message(message.from_user.id, "Контакты сохранены")

    elif message.text == "/search":        
        bot.send_message(message.from_user.id, "Эта команда пока не реализована")

    elif message.text == "/replace":        
        bot.send_message(message.from_user.id, "Эта команда пока не реализована")

    elif message.text == "/delete":        
        bot.send_message(message.from_user.id, "Эта команда пока не реализована")                     

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)        