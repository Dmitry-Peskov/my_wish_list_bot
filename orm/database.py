from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from config import DB
from models.desire import Desire
from models.user import User

ENGINE = create_async_engine(url=DB.DSN,
                             echo=True,
                             pool_size=10,
                             max_overflow=5,
                             )

SESSION = async_sessionmaker(ENGINE,
                             expire_on_commit=False,
                             )


async def add_user(telegram_id: int, fullname: str, nickname: str) -> None:
    """
    Записать в БД нового пользователя

    :param telegram_id: id пользователя в Telegram
    :param fullname: полное имя пользователя
    :param nickname: никнейм
    :return: None
    """
    async with SESSION() as session:
        async with session.begin():
            user = User(telegram_id=telegram_id, fullname=fullname, nickname=nickname)
            await session.add(user)


async def add_desire(user_id: int, title: str, url: str) -> None:
    """
    Записать в БД новое пожелание

    :param user_id: id telegram автора пожелания
    :param title: название желания
    :param url: ссылка на желание
    :return: None
    """
    async with SESSION() as session:
        async with session.begin():
            desire = Desire(user_id=user_id, title=title, url=url)
            await session.add(desire)


async def this_user_exists(telegram_id: int) -> bool:
    """
    Проверить по telegram id существует ли пользователь в БД

    :param telegram_id: id пользователя в telegram
    :return: False если пользователя нет в БД, иначе True
    """
    async with SESSION() as session:
        async with session.begin():
            user = await session.get(User, {"telegram_id": telegram_id})
            return False if user is None else True
