# Тима Минский tg: https://t.me/tima_minski
from loader import name_bot


#делит call_data  на флаг в два символа и дату
def dt(s):
    s = s[2:]
    return s
#делит call_data  на флаг в два символа и дату
def fs(st):
    return(st[0:2])


# текст выдается на старте, при запуске бота
text_start = f'БотManager — самый популярный бот в Telegram \nдля управления группами. \n' \
             f'Аналитика, модерация, система репутации, \nтриггеры, отчеты и многое другое.\n\n' \
             f'Добавьте [БотManager](https://t.me/manager_chat_tim_bot?startgroup=hbase) в группу, ' \
             f'\nили назначьте его администратором.'


# текст выдается когда бот не добавлен ни в какую группу, а пользователь хочет уже посмотреть статистику
loser_text = f' К сожалению [БотManager](https://t.me/manager_chat_tim_bot?startgroup=hbase)' \
             f' не назначен администратором ни в какой Вашей группе... 😔 \n' \
             f' Вы можете сперва назначить его, и после смотреть "статистику" 😉'


# информация о функционале бота
info_text = f'Информация о функционале бота: {name_bot} \n\n' \
            f'Самый популярный бот в Telegram для управления группами.\n' \
            f'Уведомления по заданному времени.\n' \
            f'Статистика о пользователе и информации группы.\n' \
            f'Система поощрения и наказания.\n'



