# Мой список желаний - wish list (Telegram бот)
Telegram бот, который позволяет составлять, управлять и делиться с окружающими своим списком желаний.
[![Telegram бот - Список желаний](https://img.shields.io/badge/my_w1sh_list_bot-blue?logo=telegram&logoColor=white)](https://t.me/my_w1sh_list_bot) - запусти  и попробуй!

#### Разработано и протестировано на ![Telegram бот - Список желаний](https://img.shields.io/badge/Python%203.10-black?logo=python&logoColor=white)

### Монтаж и инсталяция  
1. Клонируйте репозиторий на своё рабочее место
2. Создайте вирутальное окружение в корневом каталоге проекта
    ```pycon
    python -m venv venv
    ```
3. Если оно не было активировано автоматически, активируйте вручную виртуальное окружение
   ```pycon
   venv\Scripts\activate.bat
   ```
4. Создайте в корневом каталоге проекта файл **.env**
5. Укажите в файле **.env** параметры подключения к БД PostgresSQL и API токен вашего Telegram бот в соответсвии с шаблоном:
    ```dotenv
    WITH_LIST_DB_SERVER=сервер
    WITH_LIST_DB_DATABASE=база
    WITH_LIST_DB_PORT=порт
    WITH_LIST_DB_UID=логин
    WITH_LIST_DB_PSW=пароль
    WITH_LIST_BOT_TOKEN=токен
    ```
6. Установите необходимые зависимости опираясь на файл **requirements.txt**
   ```pycon
    pip install -r requirements.txt
   ```
7. Используя **alembic** примените все миграции к БД
   ```pycon
   alembic upgrade head
   ```
   После применения миграций в вашей БД (которую вы указали в **.env**) должны будут появиться таблицы:
   - **user** - информация о пользователях бота
   - **desire** - желания пользователей
   - **db_action_log** - лог рабоыт с БД
   - **alembic_version** - текущая версия миграции
8. Запустите файл **bot.py** на исполнение

### Контакт с разработчиком
[![PeskovDV](https://img.shields.io/badge/PeskovDV-blue?logo=Telegram&logoColor=white)](https://t.me/Peskov_DV)  [![Дмитрий Песков](https://img.shields.io/badge/%D0%94%D0%BC%D0%B8%D1%82%D1%80%D0%B8%D0%B9%20%D0%9F%D0%B5%D1%81%D0%BA%D0%BE%D0%B2-blue?logo=vk&logoColor=white)](https://vk.com/dmitry_peskov)
