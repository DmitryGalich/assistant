# Assistant

Chat bot for businesses based on LLMs.

## Features
- Ability of adding new info about products
- Communicating with customers for helping to with products choice
- Sending notifications about new orders

## Running with Docker

### Prerequisites
- Docker and Docker Compose installed on your system
- At least 10GB of RAM (as per model requirements)

### Setup and Run
1. Download the model file:
   ```
   mkdir -p models/saiga_7b_ggml
   # Download the model file to models/saiga_7b_ggml/ggml-model-q4_1.bin
   # You can get it from https://huggingface.co/IlyaGusev/saiga_7b_ggml
   ```

2. Build and start the Docker container:
   ```
   docker-compose up --build
   ```
   Note: The first build may take some time as it compiles the llama-cpp-python package from source.

3. Interact with the assistant through the terminal

### Configuration
- You can modify environment variables in the docker-compose.yml file
- Model parameters can be adjusted in the Dockerfile CMD line
- Python dependencies are managed in requirements.txt

### Troubleshooting
If you encounter build issues with llama-cpp-python:
- The Dockerfile includes necessary build dependencies (build-essential, cmake)
- You can adjust CMAKE_ARGS in the Dockerfile for specific compilation options

## Components
- [LLM](#llm)
- [Tool for connecting with social media](#social-media)

## LLM

### Requirements
* Open source
* Fluent russian language
* Easy to train
* Fast response time
* Not talking about anything else than business

### Talking requirements
* Answering questions about products
* Responding in a friendly and helpful manner
* Recommending products based on user's preferences
* Asking for more information if needed (e.g. size, color)
* Providing links to product pages or other relevant resources

## Social media
  ### Telegram
  ### Whatsapp
  ### Instagram