#!/bin/bash
set -e

echo "[INFO] Checking for GPU availability..."
if command -v nvidia-smi &>/dev/null; then
    echo "[INFO] NVIDIA GPU detected. Building llama-cpp-python with CUDA support..."
    CMAKE_ARGS="-DGGML_CUDA=on" FORCE_CMAKE=1 pip install --no-cache-dir llama-cpp-python==0.3.16 --verbose
else
    echo "[INFO] No GPU detected"
fi

exec "$@"
