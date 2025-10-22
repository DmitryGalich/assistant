## Windows 11

#### Create env
* Install miniconda
* Open Anaconda PowerShell Prompt
* Create and open virtual envirenment
```
    conda create --name ${NAME}
    conda activate ${NAME}
    pip install llama-cpp-python langchain langchain_community
    code ${PROJECT_PATH}
```
#### Remove env
```
    conda deactivate ${NAME}
    conda remove --name ${NAME} --all
```
