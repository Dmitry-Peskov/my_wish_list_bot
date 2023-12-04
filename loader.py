from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from config import DB

db_engine = create_async_engine(url=DB.DSN,
                                echo=True,
                                pool_size=10,
                                max_overflow=5,
                                )

db_session = async_sessionmaker(db_engine,
                                expire_on_commit=False,
                                )
