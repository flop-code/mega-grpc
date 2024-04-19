all: build up
build: build-protos build-services build-tests
test: run_tests organize_test_logs

copy_env_files:
	@echo [Copying templates to .env files]
	cp user_service/.env-template user_service/.env
	cp post_service/.env-template post_service/.env
	cp user_service/tests/.env-template user_service/tests/.env
	cp post_service/tests/.env-template post_service/tests/.env

build-tests:
	@echo [Building tests]
	docker compose -f post_service/tests/docker-compose.yml build
	docker compose -f user_service/tests/docker-compose.yml build

build-protos: protobufs
	@echo [Building protos]
	(cd protobufs && make)

build-services: post_service/Dockerfile post_service/docker-compose.yml \
				user_service/Dockerfile user_service/docker-compose.yml
	@echo [Building images]
	docker compose -f user_service/docker-compose.yml build
	docker compose -f post_service/docker-compose.yml build

run_tests:
	@echo [Running tests]
	COMPOSE_IGNORE_ORPHANS=True docker compose -f user_service/tests/docker-compose.yml \
		up --abort-on-container-exit --exit-code-from test_user_app

	COMPOSE_IGNORE_ORPHANS=True docker compose -f post_service/tests/docker-compose.yml \
		up --abort-on-container-exit --exit-code-from test_post_app

	docker compose -f post_service/tests/docker-compose.yml down
	docker compose -f user_service/tests/docker-compose.yml down

up:
	@echo [Setting up containers]
	COMPOSE_IGNORE_ORPHANS=True docker compose -f user_service/docker-compose.yml up -d --wait
	COMPOSE_IGNORE_ORPHANS=True docker compose -f post_service/docker-compose.yml up -d --wait

down:
	@echo [Setting down containers]
	docker compose -f post_service/docker-compose.yml down
	docker compose -f user_service/docker-compose.yml down

restart:
	@echo [Restarting containers]
	docker compose -f post_service/docker-compose.yml restart
	docker compose -f user_service/docker-compose.yml restart

organize_test_logs:
	@echo [Organizing test logs]
	mkdir -p test_results

	cp user_service/test_results.log test_results/user_service.log
	cp post_service/test_results.log test_results/post_service.log

clear_all:  # Warning! This will also delete DB & Redis volumes (data).
	@echo [Cleaning]
	rm -rf --ignore-unmatch post_service/proto/*
	rm -rf --ignore-unmatch user_service/rpc/proto/*
	rm -rf --ignore-unmatch test_results/

	docker image rm $(shell docker compose -f user_service/docker-compose.yml config --images) || true
	docker image rm $(shell docker compose -f post_service/docker-compose.yml config --images) || true
	docker image rm $(shell docker compose -f post_service/tests/docker-compose.yml config --images) || true
	docker image rm $(shell docker compose -f user_service/tests/docker-compose.yml config --images) || true

	docker volume rm $(shell docker compose -f user_service/docker-compose.yml config --volumes) || true
	docker volume rm $(shell docker compose -f post_service/docker-compose.yml config --volumes) || true
	docker volume rm $(shell docker compose -f post_service/tests/docker-compose.yml config --volumes) || true
	docker volume rm $(shell docker compose -f user_service/tests/docker-compose.yml config --volumes) || true
