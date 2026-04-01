# Model runner 

Module for only running LLM

## Development

### Copying model
Copy model into container by hands:
```
docker cp <source_path_on_host> <container_name_or_id>:<destination_path_in_container>
```
Example:
```
docker cp D:\models\qwen2.5-7b-instruct-q4_k_m.gguf 6af8ff30516c8233ccc578c03edf84eee4260008fec51485108798e2487fec73:/workspaces/assistant/model_runner/models
```

    1  ls
    2  cd model_runner/
    3  ls
    4  apt update
    5  apt install git
    6  apt install cmake
    7  git clone https://github.com/ggml-org/llama.cpp
    8  cd llama.cpp/
    9  cmake -B build -DGGML_CUDA=ON
   10  cmake --build build --config Release
   11  cd ..
   12  git clone https://github.com/ggml-org/llama.cpp
   13  cd llama.cpp
   14  cmake -B build -DGGML_CUDA=ON
   15  sudo apt-get install libssl-dev
   16  apt-get install libssl-dev
   17  cmake -B build -DGGML_CUDA=ON
   18  cmake --build build -j --config Release
   19  cmake --build build --config Release
   20  cmake -B build -DGGML_CUDA=ON
   21  cmake --build build -j 4 --config Release