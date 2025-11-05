FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

WORKDIR /model_handler
COPY . /model_handler

RUN apt-get update && apt-get install -y \
    python3=3.10.6 \
    python3-pip=22.0.2 \
    python3-dev=3.10.6 \
    build-essential \
    ninja-build=1.10.1 \
    cmake=3.22.1 \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

ENV CMAKE_ARGS="-DGGML_CUDA=on"
ENV FORCE_CMAKE=1
RUN pip install llama-cpp-python===0.3.16