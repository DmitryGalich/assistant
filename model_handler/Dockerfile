FROM nvidia/cuda:12.1.1-devel-ubuntu22.04

WORKDIR /model_handler
COPY . /model_handler

# Python 3.14 with actual pip
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt update && \
    apt install -y \
    python3.14 \
    python3.14-dev
RUN apt install -y wget
ENV DEBIAN_FRONTEND=
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.14 get-pip.py
RUN rm get-pip.py

# RUN ln -s /usr/bin/python3.14 /usr/bin/python3
# RUN ln -s /usr/bin/python3.14 /usr/bin/python

RUN apt install -y \
    build-essential \
    ninja-build \
    cmake \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*
    

# Langchain
RUN pip install langchain===1.2.0
RUN pip install langchain-community===0.4.1
RUN pip install deepagents===0.4.3
# RUN pip install tavily-python===0.7.21

# # Models downloading
# RUN pip install huggingface_hub[cli]
# # # TODO: SECURE TOKEN
# RUN hf download DmitryGalich/saiga_yandexgpt_8b.Q4_K_M --token=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 --local-dir /model_handler/models
