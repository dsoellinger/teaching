# *Anaconda* environment setup guide

As mentioned in the course, all assignments must be submitted as a [Jupyter Notebook](https://jupyter.org/). This page provides a short tutorial on how to ...

- Setup dedicated *Anaconda3* environment for the PS
- Install packages will most likely require to solve the assignments
- Install and launch a Jupyter notebook



### Prerequisite

This tutorial assumes a working installation of the *Anaconda* python distribution. If you haven't installed it yet, please follow the official [installation instructions](https://docs.anaconda.com/anaconda/install/) on their website.



### 1 - Create a dedicated environment for the PS

The following command creates an anaconda environment named `ps_image_processing`.

```shell
conda create --name ps_image_processing
```
To verify whether you environment has been installed correctly run the following command and check whether the environment is shown in the list.

```shell
conda env list

```
After the environment has been created successfully we still need to switch from `base` environment to the `ps_image_processing` environment.

```shell
conda activate ps_image_processing
```



### 2 - Install important packages

Below you will find a list of packages which I would recommend to install. Execute the following commands to install the packages **in the newly created environment**.

```shell
conda install -c anaconda jupyter
conda install -c anaconda scikit-image
conda install -c anaconda scikit-learn
conda install -c conda-forge seaborn
conda install -c conda-forge opencv
```



### 2 - Launch a Jupyter Notebook

To launch the Jupyter notebook run the following command inside the directory which should become our working directory. Executing the command will launch the Jupyer's web editor.

```
jupyter notebook
```

Copy & Paste the link shown in terminal in our browser or simply click on the link in the shell to launch your browser (if supported by our terminal).



**Note:** In case you prefer with an IDE instead of the web editor, [PyCharm](https://www.jetbrains.com/pycharm/) also provides supports for Jupyter Notebooks. 
