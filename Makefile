run:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && streamlit run main.py

start-db:
	docker-compose up -d db

stop-db:
	docker-compose down

run-docker:
	docker-compose up --build

stop-docker:
	docker-compose down
