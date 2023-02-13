# Тима Минский tg: https://t.me/tima_minski
# главная ветка проекта, handler и прочие обработки

from bot_functionality.karma_and_activity import karma, active
from bot_functionality.statistics_group import handler_statistic_group
from loader import bot
from config import text_start, info_text, fs
from keyboards import start_keyboard, return_keyboard
from admin_functionality.statistics_admin import handler_statistic
from bot_functionality.ban_message import message_sharing, clean_chat
from bot_functionality.ban_words import handler_ban_words
from admin_functionality.add_del_admin_user import new_memders, left_member
from admin_functionality.push_notifications import handler_notifications
from user.motivation import handler_motivation
from user.user_cards import user_card, handler_change_profile, info_change_photo_discription, info_change_command


@bot.message_handler(chat_types=['private'], commands=['start'])
def start(message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Hello , <b>{name}</b> ! ☺️', parse_mode="html")
    bot.send_message(message.chat.id, text_start, parse_mode='Markdown', disable_web_page_preview=True,
                     reply_markup=start_keyboard(user_id))


# handler работает только в супергруппах chat_types=['group'], в боте не фурычить
@bot.message_handler(chat_types=['group', 'supergroup'], commands=["info_change"])
def info_change(message):
    info_change_command(message)

@bot.message_handler(chat_types=['group', 'supergroup'], commands=["info"])
def mes_info(message):
    user_card(message)

# handler работает только в супергруппах chat_types=['group'], в боте не фурычить
@bot.message_handler(chat_types=['supergroup'], content_types=["text"])
def check_banned_message(message):
    message_sharing(message)
    clean_chat(message) # удаляет бан слова
    karma(message) #добавляет/отнимает карму
    active(message)


# handler работает только в группах chat_types=['group'], в боте не фурычить
@bot.message_handler(chat_types=['group'], content_types=["text"])
def check_banned_message(message):
    message_sharing(message)
    clean_chat(message) # удаляет бан слова
    karma(message)#добавляет/отнимает карму
    active(message)



# обрабатывает всех, кто подписался/добавили в группу
@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    new_memders(message)


# обрабатывает всех, кто удалился из группы
@bot.message_handler(content_types=['left_chat_member'])
def not_greeting(message):
    left_member(message)


@bot.callback_query_handler(func=lambda call: True)
def call_main(call):
    user_id = call.message.chat.id
    flag = fs(call.data)

    handler_statistic(call)  # на кнопку статистика в главном меню бота flag = du,bv,su,rp
    handler_ban_words(call)  # на кнопку добавить бан слова flag = rv
    handler_notifications(call)  # на кнопку уведомления в меню группы flag = cn,an,cr
    handler_statistic_group(call)  # на кнопку статистики по группе
    handler_motivation(call)  # на кнопку мотивация, для изменения системы подсчета
    handler_change_profile(call)  # на кнопки изменения карточки пользователя

    # Флаг для выброса информации кнопка "Инфо"
    if flag == 'in':
        info = "info"
        bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                              text=info_text, reply_markup=return_keyboard(info), parse_mode='Markdown',
                              disable_web_page_preview=True)

    # Флаг для возврата в меню, кнопки "выход", "Все понятно"
    if flag == "ss":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, text_start,
                         reply_markup=start_keyboard(user_id), parse_mode='Markdown',
                         disable_web_page_preview=True)


print("Ready")
bot.infinity_polling()
