# development環境
.PHONY: setup
setup:
	docker-compose -f docker/docker-compose.yml build
	$(MAKE) install

.PHONY: install
install:
	docker-compose -f docker/docker-compose.yml run --rm fast_api make setup

.PHONY: start
start:
	docker-compose -f docker/docker-compose.yml up --remove-orphans

.PHONY: start.background
start.background:
	docker-compose -f docker/docker-compose.yml up -d --remove-orphans

.PHONY: status
status:
	docker-compose -f docker/docker-compose.yml ps

.PHONY: stop
stop:
	docker-compose -f docker/docker-compose.yml down

.PHONY: pytest
pytest:
	docker-compose -f docker/docker-compose.yml run --rm fast_api make test