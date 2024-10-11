.PHONY: up down logs run start-db stop-db run-docker stop-docker

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f
