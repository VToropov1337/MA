from telethon import TelegramClient
import csv

api_id = ***
api_hash = ***
chat_id = ***






# Созданию сущность клиент и соединение с апи тг
client = TelegramClient('session_name', api_id, api_hash)
client.connect()

#Проверка на авторизацию
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))

#Посчитать кол-во сообщений в чате
# quantity_of_msgs = client.iter_messages(chat_id)
# count_messages = list()
# for i in q:
#     count_messages.append(i)
#
# print(len(count_messages))



#получить инфу о себе
# myself = client.get_me()
# print(myself)

#получить все диалоги (необходимо запустить, для инициализации чатов)
client.get_dialogs()

#узнать юзеров в чате
# users = client.iter_participants(chat_id)


словарь уникальных узеров по телеграм-ид
users_hash = dict()
for user in users:
    if user.last_name == None:
        users_hash[user.id] = str(user.first_name)
    else:
        users_hash[user.id] = str(user.first_name) + ' ' + str(user.last_name)


#получить все сообщения в чате / если есть медиа - скачать
msg = client.get_messages(chat_id)

#создаем массив для записи словаря в него
arr_data = list()
for i in msg:
    #создаем словарь с ключами на каждый интересующий нас метод из объекта client
    json_data = dict()
    if i.media:
        #создаем папку для фото с ид создателя --> ид сообщения
        client.download_media(i.media, file='path/{}/{}'.format(i.from_id,i.id))
        json_data["type of message"] = "image"
    else:
        json_data["type of message"] = "text"
    json_data["message_id"] = i.id
    if i.from_id in users_hash.keys():
        json_data["full_name"] = users_hash[i.from_id]
    json_data["user_id"] = i.from_id
    json_data["date"] = str(i.date)
    json_data["message"] = i.message.replace('\n',' ')
    if i.reply_to_msg_id == None:
        json_data["is_reply?"] = bool(0)
        json_data["reply_to_msg_id"] = ''
    else:
        json_data["is_reply?"] = bool(1)
        json_data["reply_to_msg_id"] = i.reply_to_msg_id
    arr_data.append(json_data)

#Создаем csv объект записи
users_data = open('path_to_file', 'w')
writer = csv.writer(users_data,delimiter='|')
count = 0
for i in arr_data:
      if count == 0:
          header = i.keys()
          writer.writerow(header)
          count += 1
      writer.writerow(i.values())

users_data.close()
