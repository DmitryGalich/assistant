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
