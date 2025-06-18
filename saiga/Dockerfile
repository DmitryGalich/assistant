FROM nvidia/cuda:12.2.2-devel-ubuntu22.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    wget \
    curl \
    build-essential \
    cmake \
    git \
    ninja-build \
    pkg-config \
    libssl-dev \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir fire cupy-cuda12x

# Set CUDA environment variables
ENV CUDA_HOME=/usr/local/cuda
ENV CUDACXX=/usr/local/cuda/bin/nvcc
ENV PATH=${CUDA_HOME}/bin:${PATH}
ENV LD_LIBRARY_PATH=${CUDA_HOME}/lib64:${LD_LIBRARY_PATH}

# Verify CUDA installation
RUN nvcc --version

# Try using pre-built CUDA wheel first
RUN pip install llama-cpp-python[cuda] --no-cache-dir --force-reinstall --upgrade --verbose || \
    # If pre-built wheel fails, try building from source with different approach
    CMAKE_ARGS="-DGGML_CUBLAS=on -DCMAKE_CUDA_ARCHITECTURES=86" \
    FORCE_CMAKE=1 \
    pip install llama-cpp-python --no-cache-dir --force-reinstall --upgrade --verbose
