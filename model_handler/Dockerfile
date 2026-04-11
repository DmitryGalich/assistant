# FROM nvidia/cuda:12.1.1-devel-ubuntu22.04

# WORKDIR /model_handler
# COPY . /model_handler

# RUN apt update && apt install -y \
#     python3 \
#     python3-pip \
#     python3-dev \
#     build-essential \
#     ninja-build \
#     cmake \
#     git \
#     curl \
#     wget \
#     && rm -rf /var/lib/apt/lists/*
    
# RUN ln -s /usr/bin/python3 /usr/bin/python

# # Langchain
# RUN pip install langchain===1.2.0
# RUN pip install langchain-community===0.4.1

# # # Models downloading
# # RUN pip install huggingface_hub[cli]
# # # # TODO: SECURE TOKEN
# # RUN hf download DmitryGalich/saiga_yandexgpt_8b.Q4_K_M --token=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 --local-dir /model_handler/models

FROM python:3.11-slim

WORKDIR /model_handler
COPY . /model_handler

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN apt update && apt install -y \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN pip install langchain===1.2.27
RUN pip install langchain-community===0.4.1
