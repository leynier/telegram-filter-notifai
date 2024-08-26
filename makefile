install:
	uv sync --all-extras

listen:
	uv run telegram-filter-notifai listen

broadcast:
	uv run telegram-filter-notifai broadcast

listen-up:
	docker-compose up --buildtelegram-filter-notifai-listen

listen-up-d:
	docker-compose up --build -d telegram-filter-notifai-listen

broadcast-up:
	docker-compose up --build telegram-filter-notifai-broadcast

broadcast-up-d:
	docker-compose up --build -d telegram-filter-notifai-broadcast
