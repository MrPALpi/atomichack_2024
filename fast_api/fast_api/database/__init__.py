import os
import contextlib
from typing import Optional

from sqlalchemy.orm import declarative_base
from sqlalchemy import URL, exc
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


database_url = URL.create(
    "postgresql+asyncpg",
    username=os.environ.get('DB_USERNAME', "postgres"),
    password=os.environ.get('DB_PASSWORD', "example"),
    host=os.environ.get('DB_HOST', '127.0.0.1'),
    port=os.environ.get('DB_PORT', 5432),
    database=os.environ.get('DB_NAME', "atomic_hack")
)

Base = declarative_base()


class DatabaseSessionManager:
    def __init__(self) -> None:
        self.engine: Optional[AsyncEngine] = None
        self.session_factory: Optional[AsyncSession] = None

    def init(self) -> None:
        connect_args = {
            "statement_cache_size": 0,
            "prepared_statement_cache_size": 0,
        }
        self.engine = create_async_engine(
            url=database_url,
            pool_pre_ping=True,
            connect_args=connect_args,
            echo=True
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    async def close(self) -> None:
        if self.engine is None:
            return
        await self.engine.dispose()
        self.engine = None
        self.session_factory = None

    async def startup(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @contextlib.asynccontextmanager
    async def get_session(self) -> AsyncSession:
        if self.session_factory is None:
            raise IOError("DatabaseSessionManager is not initialized")
        session: AsyncSession = self.session_factory()
        try:
            yield session
        except exc.SQLAlchemyError as error:
            await session.rollback()
            raise
        finally:
            await session.close()


db_manager = DatabaseSessionManager()
db_manager.init()
