# COS-451 - Artificial Intelligence
## Installation

Note that this repository uses submodules. To clone use with submodules:

```bash
git clone --recurse-submodules https://github.com/Jeff-Russ/COS-451.git
cd COS-451
git submodule init
git submodule update
```

When updating, make sure your pull includes submodules (`COS-451/` directory):

```bash
git pull --recurse-submodules
```

### Setting up `aima-python` submodule

You may also need to do the following for the `aima-python` submodule:


Install the basic dependencies to run the project on your system:

```bash
cd aima-python
pip3 install -r requirements.txt
```

You may need to fetch the datasets from the [`aima-data`](https://github.com/aimacode/aima-data) repository:

```bash
git submodule init
git submodule update
```

Wait for the datasets to download, it may take a while. Once they are downloaded, you need to install `pytest`, so that you can run the test suite:

`pip install pytest`

Then to run the tests:

`py.test`


#### Install Jupyter

`.ipynb` files Jupyter. Recommend installing [Anaconda 3](https://www.anaconda.com/download/#windows), which includes Jupyter and JupyterLab. **It is not recommended to install Anaconda for "All Users", otherwise you will have to run the Anaconda Prompt as an Administrator!**

The AIMA visualization are available on the [aima-javascript page](http://aimacode.github.io/aima-javascript/).

## Using the `aima-python` library

If you create a python script in the project directory and want to import from  the `COS-451/aima-python/` library (submodule), add this to your script:

```python
import sys
sys.path.append(sys.path[0]+"/aima-python") 
```

The second line add  the `aima-python` is the directory to path so we can import any files from `aima-python/` directly. This way of of doing things corrects  an issue of import statements from within `aima-python/` failing. Here are some examples of imports you can have after the two lines above. 

```python
from csp import Sudoku 
from search import *
```

In other words, you can import from `COS-541/` just as if you are in `COS-451/aima-python/`.