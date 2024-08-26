install:
	uv sync --frozen

install-dev:
	uv sync --all-extras

listen:
	uv run telegram-filter-notifai listen

broadcast:
	uv run telegram-filter-notifai broadcast

listen-up:
	docker-compose run --rm telegram-filter-notifai-listen bash

listen-up-d:
	docker-compose up --build -d telegram-filter-notifai-listen

broadcast-up:
	docker-compose run --rm telegram-filter-notifai-broadcast bash

broadcast-up-d:
	docker-compose up --build -d telegram-filter-notifai-broadcast

listen-logs:
	tail -f listen.log

broadcast-logs:
	tail -f broadcast.log
