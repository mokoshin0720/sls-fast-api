IMAGE_NAME=sls-fast-api-image
CONTAINER_NAME=sls-fast-api-container

start:
	docker build . -t $(IMAGE_NAME):latest
	docker run -p 80:80 --name $(CONTAINER_NAME) --rm $(IMAGE_NAME):latest