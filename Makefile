DOCKER_COMPOSE_COMMAND = docker compose -f docker-compose.yml


.PHONY: create_network
create_network:
	docker network create test_network

.PHONY: up
up:
	$(DOCKER_COMPOSE_COMMAND) up -d 

.PHONY: restart
restart:
	$(DOCKER_COMPOSE_COMMAND) restart 

.PHONY: bash
bash:
	$(DOCKER_COMPOSE_COMMAND) exec -it web bash
	
.PHONY: clean
clean:
	$(DOCKER_COMPOSE_COMMAND) down

.PHONY: stop
stop:
	$(DOCKER_COMPOSE_COMMAND) stop

.PHONY: shell
shell:
	$(DOCKER_COMPOSE_COMMAND) exec web ./manage.py shell


.PHONY: psql
psql:
	docker exec -it project-db-1 psql -U postgres 
