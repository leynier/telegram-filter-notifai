import uvloop
from dotenv import load_dotenv
from typer import Typer

from .listen import listen as listen_messages
from .telegram import get_telegram_client

load_dotenv()
uvloop.install()

telegram_client = get_telegram_client()

app = Typer(no_args_is_help=True)


@app.command()
def listen():
    listen_messages(telegram_client)

