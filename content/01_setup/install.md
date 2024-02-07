# Install python and an IDE

The code in this tutorial is written in using python 3.10.13 and a number of other python data science dependencies.

## Python installation

For beginners it is is recommended that users first install 'Anaconda'. This bundles python along with a data science centric IDEs called `Jupyter Notebook` (I recommend the more modern Jupyter-Lab over basic notebook, but there is no requirement to use it.). Anaconda is available for Windows, MacOS and Linux (e.g Ubuntu).

https://www.anaconda.com/download/

```{admonition} See also
:class: tip
Anaconda includes 'conda' (a package manager).  We are going to use `conda` to create a virtual environment that includes python 3.10.13 and Jupyter-Lab 3.x
```

```{admonition} My personal preferences
:class: tip
Alternatively (and my preference) you can install substantially smaller [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and install the packages you need using the provided conda environment or by selecting them yourself.  I tend to use packages installed from [conda-forge](https://conda-forge.org/), but the packages in the Anaconda channel (defaults) are equally good.
```

## Conda virtual environment

The code examples in this tutorial have been created using a conda virtual environment called `sim`.  You can think of a virtual environment as box within your operating system.  Inside the box we install a specific version of python along with specific versions of data science and simulation libraries such as `simpy`.  You can have multiple virtual environments within one machine.

```{admonition} Video tutorial
:class: tip
[![Watch the video](https://img.youtube.com/vi/8mb_9FDK3qA/0.jpg)](https://www.youtube.com/watch?v=8mb_9FDK3qA)  
```


### Open a terminal or command prompt on your machine.

We will use `conda` via the command line interface (CLI)

```{admonition} Windows users: Anaconda Powershell Prompt
:class: tip
On Microsoft Windows, Anaconda also install "Anaconda Powershell Prompt". This will allow you to run `conda` CLI commands.  This is easy to find on Windows. Browse to the Anaconda (or miniconda) folder in programs and choose "Powershell prompt".
```

```{admonition} Mac and Linux users: built in terminal
:class: tip
MacOS and all versions of Linux include a built in terminal.  On MacOS use the "Finder" app to navigate to a directory, right click and select "New Terminal at Folder". 
```

## Getting the code on your machine.

The code is stored in GitHub: https://github.com/health-data-science-OR/simpy-streamlit-tutorial.git

You can either download the code to your machine (click on the green Code button and choose "Download as ZIP"), or you can clone the repository using the terminal and Git (this assumes you have installed Git).

```console
git clone https://github.com/health-data-science-OR/simpy-streamlit-tutorial.git
```

## Creating the conda virtual environment

In the code you have downloaded there is a file called `binder/environment.yml`.  The `yml` file contains a list of all the dependencies conda will install in the virtual environment - including the version of python and the name of the virtual environment. 

To create the `conda` environment issue the following commands line by line on a terminal/powershell prompt.

```console
cd <path_to_code>/simpy-streamlit-tutorial
```

The command above first changes directory (cd) to the directory containing the tutorial materials.  Note that the `<path_to_code>` is dependent on your own machine.

```console
conda env create -f binder/environment.yml
```

The next line is a `conda` command.  It tells conda to create a new environment and that the list of software to install is in a file called `binder/environment.yml`.  The installation time varies by machine and by operating system.  It should take between 5 to 10 minutes.

```console
conda activate sim
```

The final command activates the `sim` virtual environment.  

## Launching Jupyter Lab

Once you have activate the correct conda environment then you can launch Jupyter Lab from the command line as follows.

```console
jupyter-lab
```

