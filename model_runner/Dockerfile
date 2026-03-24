FROM nvidia/cuda:12.1.1-devel-ubuntu22.04

RUN apt-get update && \
    apt-get install -y \
    curl \
    git \
    build-essential \
    cmake \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# HOMEBREW =============================================
## Create a non-root user
RUN useradd -m -s /bin/bash developer && \
    echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
## Switch to non-root user
USER developer
WORKDIR /home/developer
## Install Homebrew non-interactively
ENV NONINTERACTIVE=1
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
## Add Homebrew to PATH
ENV PATH="/home/linuxbrew/.linuxbrew/bin:/home/developer/.linuxbrew/bin:${PATH}"
# Verify installation
RUN brew --version
# =======================================================

RUN brew install llama.cpp

# # Models downloading
# RUN pip install huggingface_hub[cli]
# # # TODO: SECURE TOKEN
# RUN hf download DmitryGalich/saiga_yandexgpt_8b.Q4_K_M --token=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 --local-dir /model_handler/models


# CMD ["./server"]