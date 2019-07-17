###Really wish I could have used gpg keys....###
API_KEY = at_Zqv1oE2FQAZjtZPHdYqLdanmCoJUb
VERSION = 1.0.0
IMAGE_NAME = mac_lookup
LINT_IMAGE = mac_lookup_lint
BUILD_CMD = sudo docker build -t $(IMAGE_NAME):$(VERSION) . --build-arg API_KEY=$(API_KEY)

image:
	sudo docker build -t $(IMAGE_NAME):$(VERSION) . --build-arg API_KEY=$(API_KEY)

lint: 
	sudo docker build -f tests/linter/Dockerfile -t $(LINT_IMAGE):$(VERSION) .
	sudo docker run -t $(LINT_IMAGE):$(VERSION) 

default: image
