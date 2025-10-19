## Windows 11
* Install miniconda
* Open Anaconda PowerShell Prompt

* Create and open virtual envirenment
```
    conda create --name ${NAME}
    conda activate ${NAME}
```

* Install packages in this virtual envirenment
```
    conda install -c conda-forge cuda-toolkit
    $env:CMAKE_ARGS="-DGGML_CUDA=on"; pip install llama-cpp-python // for using GPU
    pip install --pre -U langchain // Alpha version of 1.0.0
    pip install langchain_community
```

* Open vscode in virtual env
```
    code
```

