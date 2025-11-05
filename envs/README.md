## Windows 11

#### Create env
* Install miniconda
* Open Anaconda PowerShell Prompt
* Create and open virtual envirenment
```
    conda env create -f envs\env.yaml
    conda activate ${ENV_NAME}
    code ${PROJECT_PATH}
```
#### Remove env
```
    conda deactivate ${NAME}
    conda remove --name ${NAME} --all
```

#### GPU llama instalation

```
    conda create --name ${ENV_NAME}
    conda activate ${ENV_NAME}

    conda install conda-forge::langchain
    conda install conda-forge::langchain-community

    $env:CMAKE_ARGS="-DGGML_CUBLAS=ON"
    $env:FORCE_CMAKE=1
    $env:CUDAToolkit_ROOT="D:/libraries/cuda_12_3"
    $env:CUDA_PATH="D:/libraries/cuda_12_3"
    $env:PATH="D:/libraries/cuda_12_3/bin;$env:PATH"

    pip install llama-cpp-python --force-reinstall --no-cache-dir --no-binary=llama-cpp-python


```