IMAGE_NAME=sls-fast-api
MAKEFILE_DIR:=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))

build:
	docker build . -t $(IMAGE_NAME):latest -f Dockerfile.local

run:
	docker run --rm -v $(MAKEFILE_DIR)/app:/code/app -p 80:80 $(IMAGE_NAME):latest