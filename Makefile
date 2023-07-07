IMAGE_NAME=sls-fast-api

build:
	docker build . -t $(IMAGE_NAME) -f Dockerfile.local

