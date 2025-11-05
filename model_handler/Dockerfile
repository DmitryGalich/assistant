FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

WORKDIR /model_handler
COPY . /model_handler

RUN apt update && apt install -y \
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

# llama-cpp-python for GPU
ENV CMAKE_ARGS="-DGGML_CUDA=on"
ENV FORCE_CMAKE=1
RUN pip install llama-cpp-python===0.3.16

# Langchain
RUN pip install langchain===1.0.3
RUN pip install langchain-community===0.4.1

# Models downloading
RUN pip install huggingface-hub===1.1.0
# TODO: SECURE TOKEN
ENV HF_TOKEN="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"
RUN huggingface-cli download DmitryGalich/saiga_yandexgpt_8b.Q4_K_M --token=${HF_TOKEN} --local-dir /model_handler/models