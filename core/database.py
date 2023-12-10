from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from config import DB
from models.desire import Desire
from models.user import User
from models.db_action_log import ActionLogDB


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
                log = ActionLogDB(user_id=user.telegram_id, message="Регистрация нового пользователя", details=str(user))
                session.add(user)
                session.add(log)

    async def add_desire(self, desire: Desire) -> None:
        """
        Добавить новое желание в БД

        :param desire: конкретный экзмепляр модели Desire
        :return: None
        """
        async with self.__session() as session:
            async with session.begin():
                log = ActionLogDB(user_id=desire.user_id, message="Добавлено новое желание", details=str(desire))
                session.add(desire)
                session.add(log)

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
        stmt = select(Desire.title, Desire.url, Desire.id).where(Desire.user_id == telegram_id).order_by(
            Desire.created_at.desc())
        async with self.__session() as session:
            async with session.begin():
                desires = await session.execute(stmt)
                for desire in desires.all():
                    title = desire.title
                    url = desire.url
                    d_id = desire.id
                    d = {"title": title, "url": url, "id": d_id}
                    result.append(d)
                log = ActionLogDB(user_id=telegram_id, message="Запрошен список желаний", details=str(result))
                session.add(log)
        return result

    async def delete_desire(self, user_id: int, desire_id: int) -> str:
        name_desire = str()
        async with self.__session() as session:
            async with session.begin():
                desire = await session.get(Desire, {"id": desire_id})
                log = ActionLogDB(user_id=user_id, message="Удаление желания", details=str(desire))
                session.add(log)
                name_desire += str(desire.title)
                await session.delete(desire)
                await session.commit()
        return name_desire


# Инициализируем экземпляр помощника. В дальнейшем он будет импортирован сторонними модулями
DBHelper = DatabaseHelper()
