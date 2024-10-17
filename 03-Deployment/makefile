include ../../../make.inc

# Build tasks

    #  build the container using DOCKER_IMAGE_NAME
build_docker_image:
	docker build -t $(DOCKER_IMAGE_NAME) .

    #  run the container using DOCKER_IMAGE_NAME
# <port on the host>:<port inside the container>
run_docker_image:
	docker run --rm -it -p 8000:8000 -e PORT=8000 $(DOCKER_IMAGE_NAME)

    #  push the container using DOCKER_IMAGE_NAME
push_docker_image:
	docker push $(DOCKER_IMAGE_NAME)

deploy_docker_image:
		gcloud run deploy lwb2-de-fastapi \
		--region=europe-west2 \
		--image=$(DOCKER_IMAGE_NAME) \
		--allow-unauthenticated
