# https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/rel-23-04.html#rel-23-04
FROM nvcr.io/nvidia/pytorch:23.04-py3
LABEL maintainer="Stelios Papadopoulos <spapadop@bcm.edu>"

RUN apt-get update --yes && \
    apt-get upgrade --yes && \
    apt-get install --yes --no-install-recommends

# uncomment below for latest jupyterlab. may interfere with jupyter configuration from base image
# RUN python3 -m pip install --no-cache-dir --upgrade jupyterlab

WORKDIR /root
COPY . /src/at-image
RUN pip install -e /src/at-image