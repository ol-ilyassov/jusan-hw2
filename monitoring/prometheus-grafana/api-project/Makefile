############
# Variables
############

DOCKER_CONTAINER_NAME:=fastapi-app

DOCKER_IMAGE_NAME:=fastapi-app-image

.SILENT:

##############
# Development
##############

.PHONY: run
run:
	clear && uvicorn main:app --reload

#########
# Docker
#########

.PHONY: docker/build
docker/build:
	docker build -t ${DOCKER_IMAGE_NAME} .

.PHONY: docker/run
docker/run: docker/build
	docker run -d -p 8080:8080 --name ${DOCKER_CONTAINER_NAME} ${DOCKER_IMAGE_NAME}

.PHONY: docker/logs
docker/logs:
	docker logs ${DOCKER_CONTAINER_NAME}

.PHONY: docker/stop
docker/stop:
	docker stop ${DOCKER_CONTAINER_NAME}

.PHONY: docker/rm
docker/rm:
	docker rm ${DOCKER_CONTAINER_NAME}

.PHONY: docker/rmi
docker/rmi:
	docker rmi ${DOCKER_IMAGE_NAME}