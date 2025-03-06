import aiomysql
from aiomysql import Error as ConnectionError

from utils.consts import DATABASE_HOST, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD


async def get_db_connection():
    try:
        connection = await aiomysql.connect(
            host=DATABASE_HOST,
            db=DATABASE_NAME,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
        )
        return connection
    except ConnectionError as e:
        print(f"Error: {e}")
        return None


class Database:
    _pool = None

    @classmethod
    async def init_pool(cls):
        if cls._pool is None:
            cls._pool = await aiomysql.create_pool(
                host=DATABASE_HOST,
                user=DATABASE_USER,
                password=DATABASE_PASSWORD,
                db=DATABASE_NAME,
                minsize=1,
                maxsize=10,  # Ajusta según tus necesidades
            )

    @classmethod
    async def get_connection(cls):
        if cls._pool is None:
            await cls.init_pool()
        return cls._pool.acquire()

    @classmethod
    async def close_pool(cls):
        if cls._pool is not None:
            cls._pool.close()
            await cls._pool.wait_closed()
