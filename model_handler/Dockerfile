FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

WORKDIR /model_handler
COPY . /model_handler

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    ninja-build \
    cmake \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

# llama-cpp-python for GPU
RUN CMAKE_ARGS="-DGGML_CUDA=on" FORCE_CMAKE=1 pip install llama-cpp-python===0.3.16

# Langchain
RUN pip install langchain===1.0.3
RUN pip install langchain-community===0.4.1

# Models downloading
RUN pip install huggingface_hub[cli]
# # TODO: SECURE TOKEN
RUN hf download DmitryGalich/saiga_yandexgpt_8b.Q4_K_M --token=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 --local-dir /model_handler/models