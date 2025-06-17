FROM nvidia/cuda:12.2.2-base-ubuntu22.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    wget \
    curl \
    build-essential \
    cmake \
    git \
    ninja-build \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir fire cupy-cuda12x

RUN CUDACXX=/usr/local/cuda/bin/nvcc \
    CMAKE_ARGS="-DGGML_CUDA=on -DCMAKE_CUDA_ARCHITECTURES=all-major" \
    pip install llama-cpp-python --no-cache-dir --force-reinstall --upgrade
