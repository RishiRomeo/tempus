init:
	python3 setup.py install
	pip3 install -r requirements.txt

test:
	python3 -m pytest -s tests --junitxml=build/tests.xml --cov-report term --cov-report xml:build/coverage.xml --cov-branch tests

run:
	docker-compose -f docker/docker-compose.yml build && \
	docker-compose -f docker/docker-compose.yml run tempus-rwd-enrichment-interview-exercise