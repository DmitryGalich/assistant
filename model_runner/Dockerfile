FROM nvidia/cuda:12.1.1-devel-ubuntu22.04

WORKDIR /model_runner
COPY . /model_runner

RUN apt update && apt install -y \
    git \
    cmake \
    curl \
    libssl-dev \
    pip


# Installing Llama.cpp    
RUN git clone https://github.com/ggml-org/llama.cpp
RUN cd llama.cpp
RUN cmake -B build -DGGML_CUDA=ON
RUN cmake --build build -j 4 --config Release
RUN cd ..

# # Downloading model
# RUN pip install huggingface_hub[cli]
# # TODO: SECURE TOKEN
# RUN hf download DmitryGalich/qwen2.5-7b-instruct-q4_k_m --token=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 --local-dir /model_runner/models

# Staring model
RUN ./llama.cpp/build/bin/llama-server -m models/qwen2.5-7b-instruct-q4_k_m.gguf -c 650 --host 127.0.0.1 --port 8080
