#!/bin/sh
# Build action server image
VERS=3.3.0
REGISTRY=<Docker organization>
IMAGE=haystack-action

time docker buildx build --platform linux/amd64,linux/arm64 --output=type=registry --tag ${REGISTRY}/${IMAGE}:${VERS} --tag ${REGISTRY}/${IMAGE}:latest .
docker push ${REGISTRY}/${IMAGE} --all-tags
