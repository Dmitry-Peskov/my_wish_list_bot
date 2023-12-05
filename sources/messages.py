from config import ADMIN

def about_msg() -> str:
    msg = '🤝<b>Благодарю <u>Вас</u>, за выбор @my_w1sh_list_bot!</b>🤝\n\n' \
          'Исходный код проекта находиться в открытом доступе и доступен в репозитории GitHub ' \
          '🔗<a href="https://github.com/Dmitry-Peskov/my_wish_list_bot/">my_wish_list_bot</a>\n\n' \
          'Если у Вас возникли предложения или вы обнаружили ошибки в работе бота, свяжитесь пожалуйста со мной:\n' \
          f'📱 <a href="tg://user?id={ADMIN.ID_str}">{ADMIN.NICKNAME}</a>\n' \
          f'💻 <a href="{ADMIN.VK_URL}">ВКонтакте</a>\n\n'
    return msg
