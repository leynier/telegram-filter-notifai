import pyrogram.utils as utils


def monkeypatch():
    def get_peer_type(peer_id: int) -> str:
        peer_id_str = str(peer_id)
        if not peer_id_str.startswith("-"):
            return "user"
        if peer_id_str.startswith("-100"):
            return "channel"
        return "chat"

    utils.get_peer_type = get_peer_type
