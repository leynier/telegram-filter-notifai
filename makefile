install:
	uv sync --all-extras

listen:
	uv run telegram-filter-notifai listen

broadcast:
	uv run telegram-filter-notifai broadcast
