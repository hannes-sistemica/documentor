# Local development commands
install-local:
	python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

run-local:
	cp .env.local .env && \
	source .venv/bin/activate && \
	pip install -r requirements.txt && \
	streamlit run main.py

db-start-local:
	docker-compose up -d db

db-stop-local:
	docker-compose down

# Docker commands
docker-build:
	docker-compose build

docker-run:
	cp .env.docker .env && \
	docker-compose up

docker-stop:
	docker-compose down

docker-remove-image:
	docker rmi docu-mentor-app

# Cleanup
clean:
	rm -f .env

