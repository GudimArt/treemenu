DC = docker compose
STORAGES_FILE = docker_compose/storages.yaml
EXEC = docker exec -it
DB_CONTAINER = postgres-db
LOGS = docker logs
ENV_FILE = --env-file .env
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main


.PHONY: storages-up
storages-up:
	${DC} -f ${STORAGES_FILE} ${ENV_FILE} up -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} ${ENV_FILE} down

.PHONY: postgres
postgres:
	${EXEC} ${DB_CONTAINER} psql -U admin -d main-db

.PHONY: storages-logs 
storages-logs:
	${LOGS} ${DB_CONTAINER} -f


.PHONY: app-up
app-up:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} ${ENV_FILE} up -d

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} ${ENV_FILE} down

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: app-migrate
app-migrate:
	${EXEC} ${APP_CONTAINER} python manage.py migrate

.PHONY: app-makemigrations
app-migratemigrations:
	${EXEC} ${APP_CONTAINER} python manage.py makemigrations

.PHONY: app-createsuperuser
app-createsuperuser:
	${EXEC} ${APP_CONTAINER} python manage.py createsuperuser
