import json

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import dt, fs
from loader import bot


def keyboard_nov(group_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    punishment_ban_words = InlineKeyboardButton("Бан-слово", callback_data="m1" + str(group_id))
    punishment_bad_comment = InlineKeyboardButton("Плохой коммент", callback_data="m2" + str(group_id))
    good_comment_reward = InlineKeyboardButton("Хороший коммент", callback_data="m3" + str(group_id))
    new_messages = InlineKeyboardButton("Новое сообщение", callback_data="m4" + str(group_id))
    no_messages = InlineKeyboardButton("Неактивность", callback_data="m5" + str(group_id))
    time = InlineKeyboardButton("Время", callback_data="m6" + str(group_id))
    exitbutton = InlineKeyboardButton(text="выход ✖️", callback_data="ss")
    backbutton = InlineKeyboardButton('назад', callback_data="st:" + str(group_id))
    keyboard.add(punishment_ban_words, punishment_bad_comment, good_comment_reward, new_messages, no_messages, time,
                 exitbutton, backbutton)
    return keyboard


def main_motivation(call, group_id):
    f = open('groups/' + str(group_id) + '/list_banned_words.json', 'r', encoding='utf-8')
    list = json.load(f)

    bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                          text=f'📋Меню редактирования мотивации.\n'
                               f'✏️Выберите из списка, что хотите изменить.\n\n'
                               f'🚫Понизить за БАН-СЛОВА: <b>{list["karma"]["punishment_ban_words"]}</b>\n'
                               f'👎Понизить за ПЛОХОЙ КОММЕНТ: <b>{list["karma"]["punishment_bad_comment"]}</b>\n'
                               f'👍Повысить за ХОРОШИЙ КОММЕНТ: <b>{list["karma"]["good_comment_reward"]}</b>\n'
                               f'\n'
                               f'📝Повысить за НОВОЕ СООБЩЕНИЕ: <b>{list["active"]["new_messages"]}</b> \n'
                               f'⛔Понизить за НЕАКТИВНОСТЬ: <b>{list["active"]["no_messages"]}</b>\n'
                               f'🕜ВРЕМЯ неактивности в течении: <b>{int(list["active"]["time"] / 60 / 60)}</b> часов.',
                          reply_markup=keyboard_nov(group_id),
                          parse_mode="html", disable_web_page_preview=True)


def edit_motivation(message, call, group_id, val):
    f = open('groups/' + str(group_id) + '/list_banned_words.json', 'r', encoding='utf-8')
    list_on = json.load(f)

    if message.content_type == ("text") and message.text.replace(" ", "") and message.text.isdigit():
        bot.delete_message(message.chat.id, message.message_id - 1)
        if val == "1":
            list_on["karma"]["punishment_ban_words"] = int(message.text)
            with open('groups/' + str(group_id) + '/list_banned_words.json', "w", encoding="utf-8") as f:
                json.dump(list_on, f, ensure_ascii=False, indent=4)
                f.close()
            f = open('groups/' + str(group_id) + '/list_banned_words.json', 'r', encoding='utf-8')
            list = json.load(f)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                  text=f'📋Меню редактирования мотивации.\n'
                                       f'✏️Выберите из списка, что хотите изменить.\n\n'
                                       f'🚫Понизить за БАН-СЛОВА: <b>{list["karma"]["punishment_ban_words"]}</b>\n'
                                       f'👎Понизить за ПЛОХОЙ КОММЕНТ: <b>{list["karma"]["punishment_bad_comment"]}</b>\n'
                                       f'👍Повысить за ХОРОШИЙ КОММЕНТ: <b>{list["karma"]["good_comment_reward"]}</b>\n'
                                       f'\n'
                                       f'📝Повысить за НОВОЕ СООБЩЕНИЕ: <b>{list["active"]["new_messages"]}</b> \n'
                                       f'⛔Понизить за НЕАКТИВНОСТЬ: <b>{list["active"]["no_messages"]}</b>\n'
                                       f'🕜ВРЕМЯ неактивности в течении: <b>{int(list["active"]["time"] / 60 / 60)}</b> часов.',
                                  reply_markup=keyboard_nov(group_id),
                                  parse_mode="html", disable_web_page_preview=True)
            bot.delete_message(message.chat.id, message.message_id)
        if val == "2":
            list_on["karma"]["punishment_bad_comment"] = int(message.text)
            with open('groups/' + str(group_id) + '/list_banned_words.json', "w", encoding="utf-8") as f:
                json.dump(list_on, f, ensure_ascii=False, indent=4)
                f.close()
            f = open('groups/' + str(group_id) + '/list_banned_words.json', 'r', encoding='utf-8')
            list = json.load(f)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                  text=f'📋Меню редактирования мотивации.\n'
                                       f'✏️Выберите из списка, что хотите изменить.\n\n'
                                       f'🚫Понизить за БАН-СЛОВА: <b>{list["karma"]["punishment_ban_words"]}</b>\n'
                                       f'👎Понизить за ПЛОХОЙ КОММЕНТ: <b>{list["karma"]["punishment_bad_comment"]}</b>\n'
                                       f'👍Повысить за ХОРОШИЙ КОММЕНТ: <b>{list["karma"]["good_comment_reward"]}</b>\n'
                                       f'\n'
                                       f'📝Повысить за НОВОЕ СООБЩЕНИЕ: <b>{list["active"]["new_messages"]}</b> \n'
                                       f'⛔Понизить за НЕАКТИВНОСТЬ: <b>{list["active"]["no_messages"]}</b>\n'
                                       f'🕜ВРЕМЯ неактивности в течении: <b>{int(list["active"]["time"] / 60 / 60)}</b> часов.',
                                  reply_markup=keyboard_nov(group_id),
                                  parse_mode="html", disable_web_page_preview=True)
            bot.delete_message(message.chat.id, message.message_id)
        if val == "3":
            list_on["karma"]["good_comment_reward"] = int(message.text)
            with open('groups/' + str(group_id) + '/list_banned_words.json', "w", encoding="utf-8") as f:
                json.dump(list_on, f, ensure_ascii=False, indent=4)
                f.close()
            f = open('groups/' + str(group_id) + '/list_banned_words.json', 'r', encoding='utf-8')
            list = json.load(f)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                  text=f'📋Меню редактирования мотивации.\n'
                                       f'✏️Выберите из списка, что хотите изменить.\n\n'
                                       f'🚫Понизить за БАН-СЛОВА: <b>{list["karma"]["punishment_ban_words"]}</b>\n'
                                       f'👎Понизить за ПЛОХОЙ КОММЕНТ: <b>{list["karma"]["punishment_bad_comment"]}</b>\n'
                                       f'👍Повысить за ХОРОШИЙ КОММЕНТ: <b>{list["karma"]["good_comment_reward"]}</b>\n'
                                       f'\n'
                                       f'📝Повысить за НОВОЕ СООБЩЕНИЕ: <b>{list["active"]["new_messages"]}</b> \n'
                                       f'⛔Понизить за НЕАКТИВНОСТЬ: <b>{list["active"]["no_messages"]}</b>\n'
                                       f'🕜ВРЕМЯ неактивности в течении: <b>{int(list["active"]["time"] / 60 / 60)}</b> часов.',
                                  reply_markup=keyboard_nov(group_id),
                                  parse_mode="html", disable_web_page_preview=True)
            bot.delete_message(message.chat.id, message.message_id)
        if val == "4":
            list_on["active"]["new_messages"] = int(message.text)
            with open('groups/' + str(group_id) + '/list_banned_words.json', "w", encoding="utf-8") as f:
                json.dump(list_on, f, ensure_ascii=False, indent=4)
                f.close()
            f = open('groups/' + str(group_id) + '/list_banned_words.json', 'r', encoding='utf-8')
            list = json.load(f)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                  text=f'📋Меню редактирования мотивации.\n'
                                       f'✏️Выберите из списка, что хотите изменить.\n\n'
                                       f'🚫Понизить за БАН-СЛОВА: <b>{list["karma"]["punishment_ban_words"]}</b>\n'
                                       f'👎Понизить за ПЛОХОЙ КОММЕНТ: <b>{list["karma"]["punishment_bad_comment"]}</b>\n'
                                       f'👍Повысить за ХОРОШИЙ КОММЕНТ: <b>{list["karma"]["good_comment_reward"]}</b>\n'
                                       f'\n'
                                       f'📝Повысить за НОВОЕ СООБЩЕНИЕ: <b>{list["active"]["new_messages"]}</b> \n'
                                       f'⛔Понизить за НЕАКТИВНОСТЬ: <b>{list["active"]["no_messages"]}</b>\n'
                                       f'🕜ВРЕМЯ неактивности в течении: <b>{int(list["active"]["time"] / 60 / 60)}</b> часов.',
                                  reply_markup=keyboard_nov(group_id),
                                  parse_mode="html", disable_web_page_preview=True)
            bot.delete_message(message.chat.id, message.message_id)
        if val == "5":
            list_on["active"]["no_messages"] = int(message.text)
            with open('groups/' + str(group_id) + '/list_banned_words.json', "w", encoding="utf-8") as f:
                json.dump(list_on, f, ensure_ascii=False, indent=4)
                f.close()
            f = open('groups/' + str(group_id) + '/list_banned_words.json', 'r', encoding='utf-8')
            list = json.load(f)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                  text=f'📋Меню редактирования мотивации.\n'
                                       f'✏️Выберите из списка, что хотите изменить.\n\n'
                                       f'🚫Понизить за БАН-СЛОВА: <b>{list["karma"]["punishment_ban_words"]}</b>\n'
                                       f'👎Понизить за ПЛОХОЙ КОММЕНТ: <b>{list["karma"]["punishment_bad_comment"]}</b>\n'
                                       f'👍Повысить за ХОРОШИЙ КОММЕНТ: <b>{list["karma"]["good_comment_reward"]}</b>\n'
                                       f'\n'
                                       f'📝Повысить за НОВОЕ СООБЩЕНИЕ: <b>{list["active"]["new_messages"]}</b> \n'
                                       f'⛔Понизить за НЕАКТИВНОСТЬ: <b>{list["active"]["no_messages"]}</b>\n'
                                       f'🕜ВРЕМЯ неактивности в течении: <b>{int(list["active"]["time"] / 60 / 60)}</b> часов.',
                                  reply_markup=keyboard_nov(group_id),
                                  parse_mode="html", disable_web_page_preview=True)
            bot.delete_message(message.chat.id, message.message_id)
        if val == "6":
            list_on["active"]["time"] = int(message.text) * 60 * 60
            with open('groups/' + str(group_id) + '/list_banned_words.json', "w", encoding="utf-8") as f:
                json.dump(list_on, f, ensure_ascii=False, indent=4)
                f.close()
            f = open('groups/' + str(group_id) + '/list_banned_words.json', 'r', encoding='utf-8')
            list = json.load(f)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                  text=f'📋Меню редактирования мотивации.\n'
                                       f'✏️Выберите из списка, что хотите изменить.\n\n'
                                       f'🚫Понизить за БАН-СЛОВА: <b>{list["karma"]["punishment_ban_words"]}</b>\n'
                                       f'👎Понизить за ПЛОХОЙ КОММЕНТ: <b>{list["karma"]["punishment_bad_comment"]}</b>\n '
                                       f'👍Повысить за ХОРОШИЙ КОММЕНТ: <b>{list["karma"]["good_comment_reward"]}</b>\n'
                                       f'\n'
                                       f'📝Повысить за НОВОЕ СООБЩЕНИЕ: <b>{list["active"]["new_messages"]}</b> \n'
                                       f'⛔Понизить за НЕАКТИВНОСТЬ: <b>{list["active"]["no_messages"]}</b>\n'
                                       f'🕜ВРЕМЯ неактивности в течении: <b>{int(list["active"]["time"] / 60 / 60)}</b> часов.',
                                  reply_markup=keyboard_nov(group_id),
                                  parse_mode="html", disable_web_page_preview=True)
            bot.delete_message(message.chat.id, message.message_id)
    else:
        f = open('groups/' + str(group_id) + '/list_banned_words.json', 'r', encoding='utf-8')
        list = json.load(f)
        bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                              text=f'📋Меню редактирования мотивации.\n'
                                   f'✏️Выберите из списка, что хотите изменить.\n\n'
                                   f'🚫Понизить за БАН-СЛОВА: <b>{list["karma"]["punishment_ban_words"]}</b>\n'
                                   f'👎Понизить за ПЛОХОЙ КОММЕНТ: <b>{list["karma"]["punishment_bad_comment"]}</b>\n'
                                   f'👍Повысить за ХОРОШИЙ КОММЕНТ: <b>{list["karma"]["good_comment_reward"]}</b>\n'
                                   f'\n'
                                   f'📝Повысить за НОВОЕ СООБЩЕНИЕ: <b>{list["active"]["new_messages"]}</b> \n'
                                   f'⛔Понизить за НЕАКТИВНОСТЬ: <b>{list["active"]["no_messages"]}</b>\n'
                                   f'🕜ВРЕМЯ неактивности в течении: <b>{int(list["active"]["time"] / 60 / 60)}</b> часов.'
                                   '\n\n ⚠️ Ошибка при вводе значения! еще раз внимательно введи '
                                   'значение ЧИСЛОМ ⚠️',
                              reply_markup=keyboard_nov(group_id),
                              parse_mode="html", disable_web_page_preview=True)
        bot.delete_message(message.chat.id, message.message_id)


def handler_motivation(call):
    idx = call.message.chat.id
    user_id = call.message.chat.id
    data = dt(call.data)
    flag = fs(call.data)

    # на Бан-слово
    if flag == "m1":
        val = "1"
        group_id = data
        message = bot.send_message(call.message.chat.id, "Введите ЧИСЛОМ на сколько понизить репутацию за БАН-СЛОВА")
        bot.register_next_step_handler(message, edit_motivation, call, group_id, val)

    # на Плохой коммент
    if flag == "m2":
        val = "2"
        group_id = data
        message = bot.send_message(call.message.chat.id, "Введите ЧИСЛОМ на сколько понизить репутацию за ПЛОХОЙ "
                                                         "КОММЕНТАРИЙ")
        bot.register_next_step_handler(message, edit_motivation, call, group_id, val)

    # на Хороший коммент
    if flag == "m3":
        val = "3"
        group_id = data
        message = bot.send_message(call.message.chat.id, "Введите ЧИСЛОМ на сколько увеличить репутацию за ХОРОШИЙ "
                                                         "КОММЕНТАРИЙ")
        bot.register_next_step_handler(message, edit_motivation, call, group_id, val)

    # на Новое сообщение
    if flag == "m4":
        val = "4"
        group_id = data
        message = bot.send_message(call.message.chat.id, "Введите ЧИСЛОМ на сколько увеличить репутацию за НОВОЕ "
                                                         "СООБЩЕНИЕ")
        bot.register_next_step_handler(message, edit_motivation, call, group_id, val)

    # на неактивность
    if flag == "m5":
        val = "5"
        group_id = data
        message = bot.send_message(call.message.chat.id, "Введите ЧИСЛОМ на сколько понизить репутацию за НЕАКТИВНОСТЬ")
        bot.register_next_step_handler(message, edit_motivation, call, group_id, val)

    # на Время
    if flag == "m6":
        val = "6"
        group_id = data
        message = bot.send_message(call.message.chat.id, "Введите ЧИСЛОМ какой промежуток времени неактивности.")
        bot.register_next_step_handler(message, edit_motivation, call, group_id, val)
