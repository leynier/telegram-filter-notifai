install:
	uv sync --frozen

install-dev:
	uv sync --all-extras

listen:
	uv run telegram-filter-notifai listen

listen-build:
	docker-compose build telegram-filter-notifai-listen

listen-run-bash:
	docker-compose run --rm telegram-filter-notifai-listen bash

listen-up-d:
	docker-compose up -d telegram-filter-notifai-listen

listen-logs:
	tail -f listen.log

broadcast:
	uv run telegram-filter-notifai broadcast

broadcast-build:
	docker-compose build telegram-filter-notifai-broadcast

broadcast-run-bash:
	docker-compose run --rm telegram-filter-notifai-broadcast bash

broadcast-up-d:
	docker-compose up -d telegram-filter-notifai-broadcast

broadcast-logs:
	tail -f broadcast.log
