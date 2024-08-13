from dotenv import load_dotenv

from .telegram import get_telegram_client

load_dotenv()

telegram_client = get_telegram_client()


def run():
    telegram_client.run()
