import telebot
from random import *
import json
import requests

API_TOKEN = '6488207375:AAGtkWonmV4XSnZgjUvzoy4fxL46kXsYyW8'
bot = telebot.TeleBot(API_TOKEN)

phone_book = {
        "дядя Ваня": {'pnones': 121212, 'email': "123@mail.ru"},
        "дядя Вася": {'pnones': 55555}
    }

@bot.message_handler(command = ['start'])
def start(message):
    print('Список команд: /contact, /save, /add, /deleted, /search, /replace, , /load')

    bot.send_message(message.chat.id,'Контакты были успешно загружены')

@bot.message_handler(command = ['contact'])
def show_contact(message):
    try:
        bot.send_message(message.chat.id,'Cписок всех контактов')
    except:
        bot.send_message(message.chat.id,'Нет контактов для просмотра')

@bot.message_handler(command = ['save'])
def save(message):
    with open("phonebook.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phone_book, ensure_ascii=False))
        bot.send_message(message.chat.id,'Контакты сохранены')

@bot.message_handler(command = ['add'])
def add_contact(message):
    bot.send_message(message.chat.id,'Контакт был успешно загружен')

@bot.message_handler(command = ['deleted'])
def deleted(message):
    bot.send_message(message.chat.id,'Контакт был удален')

@bot.message_handler(command = ['search'])
def search(message):
    bot.send_message(message.chat.id,'Поиск контакта')

@bot.message_handler(command = ['replace'])
def replace(message):
    bot.send_message(message.chat.id,'Контакт был изменен')


bot.polling()
# def add_contact():
#     name = input('Введите имя: ')
#     fname = input('Введите фамилию: ')
#     email = input('Введите почту: ')
#     num = input('Введите номер телефона: ')
#     phone_book[fname] = {'имя' : name,
#                       'почта': email,
#                       'телефон' : num
#                       }

# def save():
#     with open("phonebook.json", "w", encoding="utf-8") as fh:
#         fh.write(json.dumps(phone_book, ensure_ascii=False))
#     print("Наш список контактов успешно сохранен в файле phonebook.json")

# def load():
#     with open("phonebook.json", "r", encoding="utf-8") as fh:
#         phone_book = json.load(fh)
#     print("Наш список контактов успешно загружен")
#     return phone_book

# def show_contact():
#     for k, w in phone_book.items():
#         print(k, w)

# def deleted():
#     name = input('введите имя удаляемого контакта: ')
#     del phone_book[name]


# def search():
#     print(phone_book.get(input('Введите имя: ')))

# def replace():
#     name1 = input('введите имя контакта ,которое необходимо изменить: ')
#     name_2 = input('Введите новое имя абонента ')
#     phone_book[name_2] = phone_book.pop(name1)
#     print(f'Контакт успешно изменен \n{phone_book[name_2]}')

# def start():
#     print('Список команд: /contact, /search, /replace, /deleted, /add, /save, /load. ')


# while True:
#     command = input('Введите команду: ').lower()
#     if command == 'start':
#         start()
#     if command == 'contact':
#         show_contact()
#     if command == 'add':
#         add_contact()
#         print('Контакт успешно добавлен в имеющийся список')
#     if command == 'deleted':
#         deleted ()
#         print('Контакт был удален')
#     if command == 'search':
#         search()
#     if command == 'save':
#         save()
#         print('Контакт сохранен')
#     if command == 'load':
#         phonebook=load()
#     if command == 'replace':
#         replace()
