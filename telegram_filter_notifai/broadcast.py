import asyncio
from os import environ
from random import shuffle

from pyrogram.client import Client
from pyrogram.types import (
    Chat,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)


async def wait_minutes(time_in_minutes: int, interval: int = 5):
    for i in range(0, 60 * time_in_minutes, interval):
        total_seconds = 60 * time_in_minutes - i
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        print(f"Waiting for {minutes} minutes and {seconds} seconds")
        await asyncio.sleep(interval)


async def get_message_media_list(
    app: Client,
    message: Message,
) -> list[InputMediaPhoto | InputMediaVideo | InputMediaAudio | InputMediaDocument]:
    if not message.media_group_id:
        return []
    media_list: list[
        InputMediaPhoto | InputMediaVideo | InputMediaAudio | InputMediaDocument
    ] = []
    media_group = await app.get_media_group(message.chat.id, message.id)
    for media in media_group:
        new_media = None
        if media.photo:
            new_media = InputMediaPhoto(media.photo.file_id)
        elif media.video:
            new_media = InputMediaVideo(media.video.file_id)
        if media.caption and new_media:
            new_media.caption = media.caption
            new_media.caption_entities = media.caption_entities
        if new_media:
            media_list.append(new_media)
    return media_list


def get_message_title(message: Message) -> str:
    return message.caption.splitlines()[0]


async def get_messages_with_caption_from_chat(
    app: Client,
    from_chat: int,
    limit: int = 100,
) -> list[Message]:
    messages: list[Message] = []
    async for message in app.get_chat_history(from_chat, limit):  # type: ignore
        if not message.caption:
            continue
        messages.append(message)
    messages.sort(key=lambda message: message.date)
    return messages


async def send_message(
    app: Client,
    message: Message,
    media_list: list[
        InputMediaPhoto | InputMediaVideo | InputMediaAudio | InputMediaDocument
    ],
    to_chat: int,
):
    message_title = get_message_title(message)
    chat = await app.get_chat(to_chat)
    if not isinstance(chat, Chat):
        print(f"Chat {chat.title} is only preview")
        return
    try:
        if media_list:
            await app.send_media_group(chat.id, media_list)
        else:
            await message.forward(chat.id)
        print(f"Message {message_title} has been sent to {chat.title}")
    except Exception as e:
        print(f"Failed to send message {message_title} to {chat.title}: {e}")


def broadcast(app: Client):
    from_chat = environ.get("BROADCAST_FROM_CHAT")
    if not from_chat:
        raise ValueError(
            "BROADCAST_FROM_CHAT is not set in the environment variables or .env file"
        )
    try:
        from_chat = int(from_chat)
    except ValueError:
        raise ValueError("BROADCAST_FROM_CHAT environment variable must be an integer")
    to_chats = environ.get("BROADCAST_TO_CHATS")
    if not to_chats:
        raise ValueError(
            "BROADCAST_TO_CHATS is not set in the environment variables or .env file"
        )
    to_chats = to_chats.split(",")
    try:
        to_chats = [int(to_chat) for to_chat in to_chats]
    except ValueError:
        raise ValueError(
            "BROADCAST_TO_CHATS environment variable must be a list of integers"
        )

    async def main():
        async with app:
            messages = await get_messages_with_caption_from_chat(app, from_chat)
            shuffle(messages)
            while True:
                for message in messages:
                    message_title = get_message_title(message)
                    media_list = await get_message_media_list(app, message)
                    print(f"Start to send the message: {message_title}")
                    for to_chat in to_chats:
                        await send_message(app, message, media_list, to_chat)
                    print(f"Finish to send the message: {message_title}")
                    await wait_minutes(10)

    app.run(main())
