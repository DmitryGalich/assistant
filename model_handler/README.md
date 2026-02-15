# Model handler 

## Development

### Installing llama-cpp-python with CUDA support
After creating container run in terminal:
```
CMAKE_ARGS="-DGGML_CUDA=on" FORCE_CMAKE=1 pip install --no-cache-dir llama-cpp-python==0.3.16 --verbose
```

### Copying model
Copy model into container by hands:
```
docker cp <source_path_on_host> <container_name_or_id>:<destination_path_in_container>
```
Example:
```
docker cp D:\models\saiga_yandexgpt_8b.Q4_K_M.gguf 6af8ff30516c8233ccc578c03edf84eee4260008fec51485108798e2487fec73:/workspaces/assistant/model_handler/models
```
