import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import dt, fs
from loader import bot


def info_change_photo_discription(message,val):
    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton("Фото", callback_data="p1" + str(message.chat.id))
    button2 = InlineKeyboardButton("Описание", callback_data="p2"+ str(message.chat.id))
    menu = InlineKeyboardButton("Меню", callback_data="ss"+ str(message.chat.id))
    if val == "1":
        keyboard.add(menu)
    if val == "2":
        keyboard.add(button1, button2)
    return keyboard
def user_card(message):
    group_id = message.chat.id
    user_id = message.from_user.id
    g = open('groups/' + str(group_id) + '/' + str(group_id) + '.json', 'r', encoding='utf-8')
    user_list = json.load(g)
    g.close()
    if message.reply_to_message != None:
        name = message.reply_to_message.from_user.first_name
        username = message.reply_to_message.from_user.username

        user_id = message.reply_to_message.from_user.id
        for i in user_list["subscribers"]:
            if i["id_user"] == int(user_id):
                bot.send_message(message.chat.id, f'📊<b>Статистика</b> {name}\n'
                              f'🏆<b>Репутация:</b> {i["karma"]["reputation"]}⭐️\n'
                              f'👤<b>ID:</b> {user_id}\n'
                              f'🚫<b>Нарушения:</b> {i["karma"]["ban_words"]} \n\n'
                              f'   \n'
                              f'📝<b>Описание:</b> {i["description"]}\n'
                              f'📷<b>Фото:</b> 👇👇👇 \n'
                              f'👍Изменить фото или описание /info_change' ,parse_mode="html")
                photo1 = i["photo"]
                if i["photo"] != "":
                    bot.send_photo(message.chat.id, photo1)

    if message.reply_to_message == None:
        name = message.from_user.first_name
        username = message.from_user.username
        user_id = message.from_user.id
        for i in user_list["subscribers"]:
            if i["id_user"] == int(user_id):

                bot.send_message(message.chat.id, f'📊<b>Статистика</b> {name}\n'
                                          f'🏆<b>Репутация:</b> {i["karma"]["reputation"]}⭐️\n'
                                          f'👤<b>ID:</b> {user_id}\n'
                                          f'🚫<b>Нарушения:</b> {i["karma"]["ban_words"]} \n\n'
                                          f'   \n'
                                          f'📝<b>Описание:</b> {i["description"]}\n'
                                          f'📷<b>Фото:</b> 👇👇👇\n'
                                          f'👍Изменить фото или описание /info_change',parse_mode="html")
                photo1 = i["photo"]
                if i["photo"] != "":
                    bot.send_photo(message.chat.id, photo1)


    aa = []
    for x in user_list["subscribers"]:
        aa.append(x["id_user"])
    if int(user_id) not in aa:
            bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} \n'
                                      f'К сожалению данных о пользователе нет, \n'
                                      f'так как он ничего еще не написал в чат 👣')

    if message.text == "/commands":
        bot.send_message(message.chat.id, f'Команды группы: \n'
                                          f'📊 /info - просмотреть информацию о пользователе.\n'
                                          f'📷 /info_change - изменить картинку или описание')
def info_change_command(message):
        val = "2"
        bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}, выбери что хочешь добавить!"
                                                , reply_markup=info_change_photo_discription(message,val))
        bot.delete_message(message.chat.id, message.message_id)


def get_photo_user(message,call,group_id):

    g = open('groups/' + str(group_id) + '/' + str(group_id) + '.json', 'r', encoding='utf-8')
    user_list = json.load(g)
    g.close()

    if message.content_type == "photo":
        photo1 = (message.photo[-1].file_id)
        for x in user_list["subscribers"]:
            if x["id_user"] == message.from_user.id:
                x["photo"] = photo1
            with open('groups/' + str(group_id) + '/' + str(group_id) + '.json', "w", encoding="utf-8") as f:
                json.dump(user_list, f, ensure_ascii=False, indent=4)
                f.close()
            val = "1"
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                  text='Прекрасно'
                                  , reply_markup=info_change_photo_discription(message, val),
                                  parse_mode="Markdown", disable_web_page_preview=True)
    else:
        bot.delete_message(message.chat.id, message.message_id)
        message = bot.send_message(message.chat.id,
                               "что-то пошло не так, попробуй снова\n")
        bot.register_next_step_handler(message, get_photo_user, call, group_id)

def get_discr_user(message,call,group_id):
    g = open('groups/' + str(group_id) + '/' + str(group_id) + '.json', 'r', encoding='utf-8')
    user_list = json.load(g)
    g.close()

    if message.content_type == ("text"):
        text = message.text
        for x in user_list["subscribers"]:
            if x["id_user"] == message.from_user.id:
                x["description"] = text
                with open('groups/' + str(group_id) + '/' + str(group_id) + '.json', "w", encoding="utf-8") as f:
                    json.dump(user_list, f, ensure_ascii=False, indent=4)
                    f.close()
        val = "1"
        bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                          text='Прекрасно'
                                          , reply_markup=info_change_photo_discription(message,val),
                                          parse_mode="Markdown", disable_web_page_preview=True)
    else:
        bot.delete_message(message.chat.id, message.message_id)
        message = bot.send_message(message.chat.id,
                               "что-то пошло не так, попробуй снова\n")
        bot.register_next_step_handler(message, get_discr_user, call, group_id)

def handler_change_profile(call):
    data = dt(call.data)
    flag = fs(call.data)
    if flag == "p1":
        group_id = data
        message = bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                              text= f' Приветствую!'
                                    f' Загрузи сюда картинку.')
        bot.register_next_step_handler(message, get_photo_user, call, group_id)

    if flag == "p2":
        group_id = data
        message = bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        text=f' Приветствую!'
                                             f' Напиши небольшое описание себя.')
        bot.register_next_step_handler(message, get_discr_user, call, group_id)
