from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from config import DB
from models.desire import Desire
from models.user import User


class DatabaseHelper:

    def __init__(self):
        self.__engine = create_async_engine(url=DB.DSN,
                                            echo=True,
                                            pool_size=10,
                                            max_overflow=5,
                                            )
        self.__session = async_sessionmaker(self.__engine,
                                            expire_on_commit=False,
                                            )

    async def add_user(self, user: User) -> None:
        """
        Регистрация нового пользователя в системе и запись его в БД

        :param user: конкретный экзепляр модели User
        :return: None
        """
        async with self.__session() as session:
            async with session.begin():
                session.add(user)

    async def add_desire(self, desire: Desire) -> None:
        """
        Добавить новое желание в БД

        :param desire: конкретный экзмепляр модели Desire
        :return: None
        """
        async with self.__session() as session:
            async with session.begin():
                session.add(desire)

    async def this_user_exists(self, telegram_id: int) -> bool:
        """
        Проверит зарегистрирован ли пользователь в системе по его Telegram ID

        :param telegram_id: ID пользователя в Telegram
        :return: True если зарегистрирован, иначе False
        """
        async with self.__session() as session:
            async with session.begin():
                user = await session.get(User, {"telegram_id": telegram_id})
                return False if user is None else True

    async def get_desires(self, telegram_id: int) -> list[dict[str]]:
        """
        Получить список "Желаний" конкретного пользователя по его Telegram ID

        :param telegram_id: ID пользователя в Telegram
        :return: список содержащий в себе "Желания"
        """
        result = list()
        stmt = select(Desire.title, Desire.url, Desire.id).where(Desire.user_id == telegram_id).order_by(Desire.created_at.desc())
        async with self.__session() as session:
            async with session.begin():
                desires = await session.execute(stmt)
                for desire in desires.all():
                    title = desire.title
                    url = desire.url
                    d_id = desire.id
                    d = {"title": title, "url": url, "id": d_id}
                    result.append(d)
        return result


# Инициализируем экземпляр помощника. В дальнейшем он будет импортирован сторонними модулями
DBHelper = DatabaseHelper()
