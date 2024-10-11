set-env-local:
	cp .env.local .env

install:
	python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

run:
	source .venv/bin/activate && \
	pip install -r requirements.txt && \
	(grep -v '^#' .env | xargs -I {} echo "export {}" | source /dev/stdin) && \
	python -c "import os; print('LLM_PROVIDER:', os.getenv('LLM_PROVIDER'))" && \
	streamlit run main.py

db-start:
	docker-compose up -d db

db-stop:
	docker-compose down

docker-run:
	docker-compose up --build

docker-stop:
	docker-compose down

docker-remove-image:
	docker rmi docu-mentor-app

