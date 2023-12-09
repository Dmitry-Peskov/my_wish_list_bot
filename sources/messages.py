from config import ADMIN


def back_to_main_menu_msg(username: str) -> str:
    msg = f'{username} добавление нового желания,\n❌<b>было отменено</b>❌!\n' \
          f'Чем займёмся теперь?'
    return msg


def about_msg() -> str:
    msg = '🤝<b>Благодарю <u>Вас</u>, за выбор @my_w1sh_list_bot!</b>🤝\n\n' \
          'Исходный код проекта находится в открытом доступе и доступен в репозитории GitHub ' \
          '🔗<a href="https://github.com/Dmitry-Peskov/my_wish_list_bot/">my_wish_list_bot</a>\n\n' \
          'Если у Вас возникли предложения или вы обнаружили ошибки в работе бота, пожалуйста, свяжитесь со мной:\n' \
          f'📱 <a href="tg://user?id={ADMIN.ID_str}">{ADMIN.NICKNAME}</a>\n' \
          f'💻 <a href="{ADMIN.VK_URL}">ВКонтакте</a>\n\n'
    return msg


def help_msg() -> str:
    msg = 'Привет✌\nЯ помогу тебе составить твой собственный 🎁<b>список желаний</b>🎁!\n' \
          'Когда мы закончим, ты сможешь поделиться им со своими 👨‍👨‍👧‍👧близкими, 🙋‍♀️друзьями или 👨‍💼коллегами.\n' \
          'Для этого я наделён следующими возомжностями:\n\n' \
          '👤<b>Регистрация</b>\nПри первом нашем общении (/start) я создал для тебя собственный профиль. Все твои желания хранятся в нём и ' \
          'останутся только <b>твоими</b>! Другие люди могут с ними ознакомиться только, если ты самостоятельно поделишься итоговым списком.\n\n' \
          '🎁<b>Загадать желание</b>\nПопрошу тебя коротко описать то, что ты хочешь и указать URL адрес на ресурс, где есть информация ' \
          'о желаемом. Сохраню твое желание в профиле.\n\n' \
          '🙅‍♀<b>Отказаться от мечты</b>\nВ личном списке желаний есть не актуальные вещи? Давай это поправим.\n\n' \
          '✍<b>Скорректировать планы</b>\nОбнаружил неточность в своих желаниях? Давай уточним этот момент\n\n' \
          '📝<b>Получить список</b>\nПора рассылать свой wish list друзьям!\nОтдам его тебе в виде:\n' \
          '<b>1.</b> <a href="https://ya.ru/">Купить Яндекс</a>\n' \
          '<b>2.</b> <a href="https://www.google.com/">Стать директором Google</a>\n' \
          '<b>3.</b> <a href="https://example.com/">...</a>\n\n' \
          'Пускай твои мечты сбудуться!'

    return msg


def get_desire_title(fullname: str) -> str:
    name = fullname.replace("/", "").replace("<", "").replace(">", "").replace("\\", "")
    msg = f'Окей, <b>{name}</b>! Давай сделаем это💪\n\n' \
          'Опиши своё желание... только пожалуйста, уложись в <i><b>120</b></i> символов.\n' \
          'Иначе, я не смогу 🤯запомнить твоё желание <b>целиком</b> и что-нибудь "почикаю"✂'
    return msg


def get_desire_url() -> str:
    msg = 'Вас понял, капитан🫡\nДавайте теперь заполним ссылку, на ваше желание.\n' \
          'Шеф, жду от Вас 🔗<b>URL</b> адресс на вашу хотелку.\n' \
          'Учтите, я проверю её на корректность☝'
    return msg


def get_confirmed_desire(title: str, url: str) -> str:
    msg = f'<b>Всё правильно?</b>\n\n' \
          f'📝{title.replace("<", "").replace(">", "").replace("/", "")}\n' \
          f'🔗<a href="{url}">{url}</a>'
    return msg


def not_valid_url_msg() -> str:
    msg = 'Это не похоже на <i>корректный</i> <b>URL</b>🤨\nДавай попробуем еще разок.'
    return msg


def add_desire_msg_completed(title: str, url: str) -> str:
    msg = 'Поздравляю, коллега🤝\nМы записали в список желаний:\n' \
          f'📝<b>{title.replace("<", "").replace(">", "").replace("/", "")}</b>\n' \
          f'🔗<a href="{url}">{url}</a>'
    return msg


def get_desire(desires: list[dict[str]], user_id: int, nickname: str) -> str:
    msg = ''
    if len(desires) == 0:
        msg += '🤷‍♂Вы пока что не загадили ни одного желания🤷‍♀\n' \
               'К сожалению мне нечего Вам показать😔'
    else:
        msg += f'Список желаний, 👤 <a href="tg://user?id={user_id}">{nickname}</a>:\n\n'
        num = 1
        for desire in desires:
            msg += f'<b>{num}.</b> <a href="{desire["url"]}">{desire["title"]}</a>\n'

            num += 1
        msg += '\nПодготовлено в @my_w1sh_list_bot'
    return msg
