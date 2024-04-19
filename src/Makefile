all: build up

build: build-backend build-frontend build-nginx
up: up-backend up-nginx
down: down-backend down-nginx

build-frontend:
	@echo [Building frontend]
	(cd frontend && yarn build)

build-backend:
	@echo [Building backend]
	(cd backend && make build)

up-backend:
	@echo [Setting up backend]
	(cd backend && make up)

down-backend:
	@echo [Setting down backend]
	(cd backend && make down)

build-nginx:
	@echo [Building Nginx]
	docker compose -f nginx/docker-compose.yml build

up-nginx:
	@echo [Setting up Nginx]
	COMPOSE_IGNORE_ORPHANS=True docker compose -f nginx/docker-compose.yml up -d

down-nginx:
	@echo [Setting down Nginx]
	docker compose -f nginx/docker-compose.yml down
