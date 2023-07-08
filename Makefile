IMAGE_NAME=sls-fast-api

build:
	docker build . -t $(IMAGE_NAME):latest -f Dockerfile.local

run:
	docker run  -p 80:80 $(IMAGE_NAME):latest