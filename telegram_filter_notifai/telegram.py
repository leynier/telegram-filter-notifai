from os import environ

from pyrogram.client import Client


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

    return telegram_client
