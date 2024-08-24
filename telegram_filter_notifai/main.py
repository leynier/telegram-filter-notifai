import uvloop
from dotenv import load_dotenv
from typer import Typer

from .broadcast import broadcast as broadcast_messages
from .listen import listen as listen_messages
from .monkeypatch import monkeypatch
from .telegram import get_telegram_client

monkeypatch()
load_dotenv()
uvloop.install()

telegram_client = get_telegram_client()

app = Typer(no_args_is_help=True)


@app.command()
def listen():
    listen_messages(telegram_client)


@app.command()
def broadcast():
    broadcast_messages(telegram_client)
