IMAGE_NAME = fastapi-template

up:
	test -f .env | cp .env.dist .env
	docker-compose build && docker-compose up --detach

down:
	docker-compose down
