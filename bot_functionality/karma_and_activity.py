# Тима Минский tg: https://t.me/tima_minski

import json
import os
import sys
import time

from loader import bot


def karma(message):
    group_id = message.chat.id  # id группы
    message_user = message.from_user.id
    print(message_user)

    with open(f'groups/{str(group_id)}/{str(group_id)}.json', "r", encoding="utf-8") as f:
        list = json.loads(f.read())

        f.close()

    with open(f'groups/{str(group_id)}/chat_history.json', "r", encoding="utf-8") as r:
        chat_history = json.loads(r.read())
        r.close()

        # добавляем сообщение в количество сообщений у пользователя
        list_message = []
        for x in chat_history["chat_text"]:
            if x['user'] == message_user:
                list_message.append(x)
        for y in list['subscribers']:
            if y['id_user'] == message_user:
                y['karma']['all_messages'] = len(list_message)
        with open(f'groups/{str(group_id)}/{str(group_id)}.json', "w", encoding="utf-8") as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
            f.close()



def active(message):
    group_id = message.chat.id  # id группы
    message_user = message.from_user.id
    message_time = message.date
    with open('groups/' + str(group_id) + '/list_banned_words.json', "r", encoding="utf-8") as g:
        list_active = json.loads(g.read())
        g.close()
    with open(f'groups/{str(group_id)}/{str(group_id)}.json', "r", encoding="utf-8") as f:
        list = json.loads(f.read())
        f.close()
        for i in list["subscribers"]:
            if i["karma"]["last_message"]+list_active["active"]["time"]<= time.time():
                i["karma"]["last_message"] = time.time()+60*60*12
                i["karma"]["reputation"] = i["karma"]["reputation"] - list_active["active"]["no_messages"]
                bot.send_message(message.chat.id, f' 🕘 Пользователь: @{i["user_name"]} не был активен 24 часа! \n'
                                                  f'🚶Интересно, куда он пропал?\n'
                                                  f'🔊Проверка активности: {int(list_active["active"]["time"]/60/60)} ч.\n'
                                                  f'🚫Если ее нет: <b>-{list_active["active"]["no_messages"]}⭐️</b> к репутации ',parse_mode="html")



        for x in list["subscribers"]:
            if message_user == x["id_user"]:
                x["karma"]["reputation"] = x["karma"]["reputation"] + list_active["active"]["new_messages"]

            with open(f'groups/{str(group_id)}/{str(group_id)}.json', "w", encoding="utf-8") as f:
                json.dump(list, f, ensure_ascii=False, indent=4)
                f.close()