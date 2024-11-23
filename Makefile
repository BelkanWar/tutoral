IMAGE_NAME="mysql_image"
CONTAINER_NAME="mysql_container"

build-image ::
	docker build --rm -f docker_and_DB/Dockerfile -t ${IMAGE_NAME} .

container-up ::
	docker run -itd --rm --name ${CONTAINER_NAME} -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -v /opt/mysql/:/var/lib/mysql/ ${IMAGE_NAME}

container-down ::
	docker stop ${CONTAINER_NAME}