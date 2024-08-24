from pyrogram import filters
from pyrogram.client import Client
from pyrogram.types import (
    Message,
)

from .database import await_for_database_load


def listen(app: Client):
    @app.on_message(filters.private & filters.me)
    @await_for_database_load
    async def logger_me(client: Client, message: Message):
        print(message.text)

    app.run()
