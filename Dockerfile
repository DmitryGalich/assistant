FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    git-lfs \
    build-essential \
    cmake \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better layer caching
COPY requirements.txt /app/

# Install Python dependencies with specific build options for llama-cpp-python
ENV CMAKE_ARGS="-DLLAMA_CUBLAS=OFF"
ENV FORCE_CMAKE=1
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt --verbose

# Copy application code
COPY . /app/

# Download the model (if not already included in the repository)
# Uncomment and modify the following lines if you need to download the model
# RUN mkdir -p /app/models/saiga_7b_ggml
# RUN cd /app/models/saiga_7b_ggml && \
#     wget https://huggingface.co/IlyaGusev/saiga_7b_ggml/resolve/main/ggml-model-q4_1.bin

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["python", "models/saiga_7b_ggml/interact_llamacpp.py", "models/saiga_7b_ggml/ggml-model-q4_1.bin"]