import os
from dataclasses import dataclass
from dotenv import load_dotenv

# загружаем переменные окружения из файла .env
load_dotenv()


def create_dsn() -> str:
    """
    Создать строку для ассинхронного подключения к БД Postgres с использованием переменных окружения

    :return: строка подключения по маске "postgresql+asyncpg://{uid}:{psw}@{server}:{port}/{database}"
    """
    server: str = os.getenv("WITH_LIST_DB_SERVER")
    database: str = os.getenv("WITH_LIST_DB_DATABASE")
    port: str = os.getenv("WITH_LIST_DB_PORT")
    uid: str = os.getenv("WITH_LIST_DB_UID")
    psw: str = os.getenv("WITH_LIST_DB_PSW")
    return f"postgresql+asyncpg://{uid}:{psw}@{server}:{port}/{database}"


@dataclass
class API_BOT:
    TOKEN: str = os.getenv("WITH_LIST_BOT_TOKEN")


@dataclass
class DB:
    DSN: str = create_dsn()

