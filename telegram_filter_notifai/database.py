from datetime import UTC, datetime
from os import environ, makedirs
from types import EllipsisType
from typing import Any, cast
from uuid import uuid4

from pydbantic import Database, DataBaseModel, ModelField, PrimaryKey


def cast_to_ellipsis(x: Any) -> EllipsisType:
    """
    This function is used to cast the type of default
    values of ModelFields in order to avoid the error
    of linter and avoid the use of type: ignore
    """
    return cast(EllipsisType, x)


__data_base_is_already_loaded = False


async def load_database():
    global __data_base_is_already_loaded
    if __data_base_is_already_loaded:
        return
    default_database_url = "sqlite:///./data/telegram-filter-notifai.db"
    database_url = environ.get(
        "DATABASE_URL",
        default_database_url,
    )
    if database_url == default_database_url:
        makedirs("data", exist_ok=True)
    await Database.create(
        database_url,
        tables=[Message],
    )
    __data_base_is_already_loaded = True
    print("Database loaded")


def await_for_database_load(func):
    """
    This function is a decorator that will be used to
    load the database before the decorated function is
    executed. The function must be an async function.
    """

    async def wrapper(*args, **kwargs):
        await load_database()
        return await func(*args, **kwargs)

    return wrapper


class Message(DataBaseModel):
    id: str = PrimaryKey(
        default=cast_to_ellipsis(lambda: str(uuid4())),
    )
    chat_id: str
    user_id: str
    content_hash: str
    content: str
    created_at: str = ModelField(
        default=cast_to_ellipsis(lambda: datetime.now(UTC).isoformat()),
    )
