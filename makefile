deploy-single-start:
	COORDINATOR_EXTERNAL_PORT=7543 docker-compose -f docker-compose.single.yml up --no-start
	COORDINATOR_EXTERNAL_PORT=7543 docker-compose -f docker-compose.single.yml start
	sleep 5

deploy-single-stop:
	COORDINATOR_EXTERNAL_PORT=7543 docker-compose -f docker-compose.single.yml down

deploy-cluster-start:
	COORDINATOR_EXTERNAL_PORT=7543 docker-compose -f docker-compose.cluster.yml up --no-start
	COORDINATOR_EXTERNAL_PORT=7543 docker-compose -f docker-compose.cluster.yml start
	sleep 5

deploy-cluster-stop:
	COORDINATOR_EXTERNAL_PORT=7543 docker-compose -f docker-compose.cluster.yml down

run:
	python main.py