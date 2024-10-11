set-env-local:
	cp .env.local .env

set-env-docker:
	cp .env.docker .env

install:
	python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

run:
	source .venv/bin/activate && pip install -r requirements.txt && streamlit run main.py

db-start:
	docker-compose up -d db

db-stop:
	docker-compose down

docker-run:
	docker-compose up --build

docker-stop:
	docker-compose down

docker-rm-image:
	docker rmi $(docker images -q docu-mentor-app)
