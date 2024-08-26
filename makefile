install:
	uv sync --all-extras

listen:
	uv run telegram-filter-notifai listen

broadcast:
	uv run telegram-filter-notifai broadcast

listen-up:
	docker-compose up --build -d telegram-filter-notifai-listen

broadcast-up:
	docker-compose up --build -d telegram-filter-notifai-broadcast
