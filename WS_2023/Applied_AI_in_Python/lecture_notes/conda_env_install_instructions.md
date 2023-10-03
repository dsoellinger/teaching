# *Anaconda* environment setup guide

This tutorial provides a brief overview of how to setup a new conda environment and install the packages we will need for the course.


### Prerequisite

This tutorial assumes a working installation of the *Anaconda* python distribution. If you haven't installed it yet, please follow the official [installation instructions](https://docs.anaconda.com/anaconda/install/) on their website.



### 1 - Create a dedicated environment for the PS

The following command creates an anaconda environment named `applied_ai`.

```shell
conda create --name applied_ai
```
To verify whether you environment has been installed correctly run the following command and check whether the environment is shown in the list.

```shell
conda env list

```
After the environment has been created successfully we still need to switch from `base` environment to the `applied_ai` environment.

```shell
conda activate applied_ai
```



### 2 - Install important packages

Below you will find a list of packages which I would recommend to install. Execute the following commands to install the packages **in the newly created environment**.

```shell
conda install -c anaconda jupyter
conda install -c anaconda scikit-image
conda install -c anaconda scikit-learn
conda install -c conda-forge seaborn
conda install -c anaconda tqdm
conda install -c anaconda tensorboard

```

At at later stage we will also need PyTorch which can also be installed with conda. However, the exact command you have to execute depends on your machine's capabilities.
Therefore I will only refer you to the official installation instructions: https://pytorch.org/get-started/locally/


### 2 - Launch a Jupyter Notebook

To launch the Jupyter notebook run the following command inside the directory which should become our working directory. Executing the command will launch the Jupyer's web editor.

```
jupyter notebook
```

Copy & Paste the link shown in terminal in our browser or simply click on the link in the shell to launch your browser (if supported by our terminal).



**Note:** In case you prefer with an IDE instead of the web editor, [PyCharm](https://www.jetbrains.com/pycharm/) also provides supports for Jupyter Notebooks.
