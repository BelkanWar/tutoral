IMAGE_NAME="db_image"
CONTAINER_NAME="db_container"

build-image ::
	docker build --rm -f docker_and_DB/Dockerfile -t ${IMAGE_NAME} .

container-up ::
	docker run -itd --rm --name ${CONTAINER_NAME} ${IMAGE_NAME}

container-down ::
	docker stop ${CONTAINER_NAME}