FROM nvidia/cuda:12.1.1-devel-ubuntu22.04

WORKDIR /model_runner
COPY . /model_runner

RUN apt update && apt install -y \
    git \
    cmake \
    curl \
    libssl-dev \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

ENV CUDA_HOME=/usr/local/cuda
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
ENV LIBRARY_PATH=/usr/local/cuda/lib64/stubs:$LIBRARY_PATH

# Installing llama.cpp
# RUN git clone https://github.com/ggml-org/llama.cpp && \
#     cd llama.cpp && \
#     cmake -B build -DGGML_CUDA=ON -DCMAKE_EXE_LINKER_FLAGS="-Wl,--allow-shlib-undefined" && \
#     cmake --build build -j 12

RUN cd llama.cpp && \
    cmake -B build -DGGML_CUDA=ON -DCMAKE_EXE_LINKER_FLAGS="-Wl,--allow-shlib-undefined" && \
    cmake --build build -j 12

# RUN pip install huggingface_hub[cli]
# # TODO: SECURE TOKEN
# RUN hf download DmitryGalich/qwen2.5-7b-instruct-q4_k_m --token=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 --local-dir /model_runner/models

# Запуск сервера
CMD ["./llama.cpp/build/bin/llama-server", \
     "-m", "models/qwen2.5-7b-instruct-q4_k_m.gguf", \
     "-c", "650", \
     "--host", "0.0.0.0", \
     "--port", "8080"]