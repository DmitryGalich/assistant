FROM nvidia/cuda:12.2.2-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    cmake \
    git \ 
    ninja-build \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

ARG LLAMA_CPP_VERSION=0.2.23
ARG LLAMA_CPP_CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS"
RUN CMAKE_ARGS=${LLAMA_CPP_CMAKE_ARGS} pip install --no-cache-dir --force-reinstall llama-cpp-python==${LLAMA_CPP_VERSION}

COPY . .

CMD ["python3", "main.py", "models/model-q4_K.gguf"]
