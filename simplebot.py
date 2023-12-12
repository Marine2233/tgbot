import telebot;
import json;

API_TOKEN = '6488207375:AAGtkWonmV4XSnZgjUvzoy4fxL46kXsYyW8'
bot = telebot.TeleBot(API_TOKEN)

global phone_book
phone_book = {}

def load_data():
    with open("phonebook.json", "r", encoding="utf-8") as fh:
        global phone_book
        phone_book = json.load(fh)        

def save_data():
    with open("phonebook.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phone_book, ensure_ascii=False))

def search(message):
    surname = message.text

    if surname in phone_book:
        bot.send_message(message.from_user.id, f'{phone_book[surname]}')
    else:
        bot.send_message(message.from_user.id, f"Контакт {surname} не найден")

def delete(message):
    surname = message.text
    if surname in phone_book:
        del phone_book[surname]
        bot.send_message(message.from_user.id, f"Контакт {surname} успешно удалён")
    else:
        bot.send_message(message.from_user.id, f"Контакт {surname} не найден")

def set_newname(message):
    name = message.text
    phone_book[surname]['имя'] = name
    bot.send_message(message.from_user.id, f"Имя контакта {surname} успешно изменено")    

def replace_name(message):
    global surname
    surname = message.text
    if surname in phone_book:
        bot.send_message(message.from_user.id, "Введите новое имя:")
        bot.register_next_step_handler(message, set_newname)
    else:
        bot.send_message(message.from_user.id, f"Контакт {surname} не найден")

def set_newemail(message):
    email = message.text
    phone_book[surname]['почта'] = email
    bot.send_message(message.from_user.id, f"Почта контакта {surname} успешно изменена")

def replace_email(message):
    global surname
    surname = message.text
    if surname in phone_book:
        bot.send_message(message.from_user.id, "Введите новою почту:")
        bot.register_next_step_handler(message, set_newemail)
    else:
        bot.send_message(message.from_user.id, f"Контакт {surname} не найден")

def set_newphone(message):
    phone = message.text    
    phone_book[surname]['телефон'] = phone
    bot.send_message(message.from_user.id, f"Телефон контакта {surname} успешно изменён")

def replace_phone(message):
    global surname
    surname = message.text
    if surname in phone_book:
        bot.send_message(message.from_user.id, "Введите новый телефон:")
        bot.register_next_step_handler(message, set_newphone)
    else:
        bot.send_message(message.from_user.id, f"Контакт {surname} не найден")                 

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
        bot.send_message(message.from_user.id, "Список команд: /contact, /save, /add, /delete, /search, /replace_name, /replace_email, /replace_phone, /load")

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
        bot.send_message(message.from_user.id, "Введите фамилию:")
        bot.register_next_step_handler(message, search)

    elif message.text == "/replace_name":        
        bot.send_message(message.from_user.id, "Введите фамилию:")
        bot.register_next_step_handler(message, replace_name)

    elif message.text == "/replace_email":        
        bot.send_message(message.from_user.id, "Введите фамилию:")
        bot.register_next_step_handler(message, replace_email)

    elif message.text == "/replace_phone":        
        bot.send_message(message.from_user.id, "Введите фамилию:")
        bot.register_next_step_handler(message, replace_phone)        

    elif message.text == "/delete":        
        bot.send_message(message.from_user.id, "Введите фамилию:")
        bot.register_next_step_handler(message, delete)                     

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)        