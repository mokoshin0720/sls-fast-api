IMAGE_NAME=sls-fast-api
MAKEFILE_DIR:=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))

build:
	docker build . -t $(IMAGE_NAME):latest -f Dockerfile.local --build-arg BUILDKIT_INLINE_CACHE=1

run:
	docker run --rm -v $(MAKEFILE_DIR):/code -p 9000:9000 $(IMAGE_NAME):latest