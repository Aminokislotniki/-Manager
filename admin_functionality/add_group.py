# Тима Минский tg: https://t.me/tima_minski


from loader import bot, id_bot
import json
import os


# функция проверяет наличие файла с названием группы в директории "group" при подключении бота
# если файла нет, то добавляет, в файл записывает: id группы -> список администраторов, кто владелец,
# сколько подписчиков, и т.д
def check_is_group(group_id, group_title):
    # создаем файл группы
    try:
        with open(f'groups/{str(group_id)}/{str(group_id)}.json', "r", encoding="utf-8") as f:
            f.close()
        return True
    except:
        path = os.getcwd()
        os.makedirs(f'groups/{group_id}', exist_ok=True)
        list_admin_group = bot.get_chat_administrators(chat_id=group_id)  # все админы чата, включая владельца
        admin_name1 = ""
        for admin in list_admin_group:
            admin_name = admin.user.first_name
            admin_status = admin.status  # creator
            if admin_status == "creator":
                admin_name1 = admin_name
        with open(f'groups/{str(group_id)}/{str(group_id)}.json', "w", encoding="utf-8") as f:
            group_list = dict({'group_id': group_id,
                               'name_group': group_title,
                               'creator': admin_name1,
                               'admin_group': [],
                               'number_of_subscribers': 'null',
                               'subscribers': [],
                               'subscribers_ban_number': 'null',
                               'subscribers_ban': [],
                               'subscribers_del_number': 'null',
                               'subscribers_del': []
                               })
            json.dump(group_list, f, ensure_ascii=False, indent=4)

        # добавляем файл бан слов(пустой файл) и лист с -n очков кармы за слова(значения установлены по умолчанию)
        list_ban = {"banned_message": [],
                    "karma": {"punishment_ban_words": 10,
                              "punishment_bad_comment": 2,
                              "good_comment_reward": 2
                              },
                    "active": {"new_messages": 1,
                               "no_messages": 5,
                               "time": 5}
                    }

        with open(f'groups/{str(group_id)}/list_banned_words.json', "w", encoding="utf-8") as f:
            json.dump(list_ban, f, ensure_ascii=False, indent=4)
        f.close()

        # создаем файл истории чата
        text = {"number_message": "null",
                "chat_text": []}
        with open(f'groups/{str(group_id)}/chat_history.json', "a", encoding="utf-8") as f:
            json.dump(text, f, ensure_ascii=False, indent=4, )
        f.close()

        # создаем файл с уведомлениями {"text": "null", "interval": "null"}
        text_push = {"active": "",
                     "time": "",
                     "public": "",
                     "new": "null",
                     "new_time": "null",
                     "push_statistic": "",
                     "public_push_statistic": "no"}
        with open(f'groups/{str(group_id)}/push_notifications.json', "a", encoding="utf-8") as f:
            json.dump(text_push, f, ensure_ascii=False, indent=4, )
        f.close()


# функция перекидывает папку с данными группы в архив,
# если пользователь снова добавил бота в группу, то создается новая папка,
# таким образом сохраниться вся история добавления и удаления бота в группе
def group_file_archive(message, group_id):
    # Если удалили "БoтManager" из группы, весь архив остается, у админа в json группа удаляется
    # папка с данными группы (название папки - ID группы) перекидывается в архивную папку
    creator_id = message.from_user.id
    with open("administrator/" + str(creator_id) + ".json", "r", encoding="utf-8") as f:
        list = json.load(f)
        for i in range(len(list['group'])):
            if str(group_id) in str(list['group'][i]['group_id']):
                del list['group'][i]
                break
        with open("administrator/" + str(creator_id) + ".json", "w", encoding="utf-8") as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
            f.close()

    num = 1
    x = 2
    while x > 1:
        try:
            os.replace(os.getcwd() + '/groups/' + str(group_id),
                       os.getcwd() + '/archive_group/' + str(group_id))
            break
        except PermissionError:
            num = num + 1
            try:
                text = f'({num})'
                os.rename(os.getcwd() + '/groups/' + str(group_id),
                          os.getcwd() + '/archive_group/' + str(group_id) + str(text))
                break
            except FileExistsError:
                x = 2
                pass
