from os import environ

from pyrogram import filters
from pyrogram.client import Client
from pyrogram.types.messages_and_media import Message

from .database import await_for_database_load


def get_telegram_client() -> Client:
    telegram_api_id = environ.get("TELEGRAM_API_ID")
    telegram_api_hash = environ.get("TELEGRAM_API_HASH")
    if not telegram_api_id:
        raise ValueError(
            "TELEGRAM_API_ID is not set in the environment variables or .env file"
        )
    if not telegram_api_hash:
        raise ValueError(
            "TELEGRAM_API_HASH is not set in the environment variables or .env file"
        )
    telegram_client = Client(
        "telegram_filter_notifai",
        api_id=telegram_api_id,
        api_hash=telegram_api_hash,
    )

    @telegram_client.on_message(filters.private & filters.me)
    @await_for_database_load
    async def my_handler(client: Client, message: Message):
        print(message.text)

    return telegram_client
