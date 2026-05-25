install:
	uv sync
	uv sync --dev

lint:
	docker run -it --rm hw2_annotations uv run flake8 main.py src/

typing:
	docker run -it --rm hw2_annotations uv run mypy main.py src/

docker-run:
	docker build -t hw2_annotations .
