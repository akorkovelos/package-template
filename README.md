# gons_test
[![PyPI version](https://badge.fury.io/py/gridfinder.svg)](https://badge.fury.io/py/gridfinder) [![Documentation Status](https://readthedocs.org/projects/gonset-test/badge/?version=latest)](https://gonset-test.readthedocs.io/en/latest/?badge=latest)

Documentation: https://gonset-test.readthedocs.io/en/latest/

The algorithm looks as follows in process, guessing the grid network for Malawi:

[![Animated algorithm](https://raw.githubusercontent.com/carderne/gridfinder/master/gridfinder-animated.gif)](#)

## Input requirements
-
-

## Model usage

To get to grips with the API and steps in the model, open the Jupyter notebook `gons_test_cli.ipynb`. This repository  includes the input data needed to do a test run for Malawi, so it should be a matter of openening the notebook and running all cells.

## Installation

**Requirements**

gons_test requires Python >= 3.5 with the following packages installed:
- backcall==0.1.0
- colorama==0.4.1
- decorator==4.4.0
- et-xmlfile==1.0.1
- ipython==7.5.0
- ipython-genutils==0.2.0
- jdcal==1.4.1
- jedi==0.13.3
- numpy==1.16.3
- openpyxl==2.6.2
- pandas==0.24.2
- parso==0.4.0
- pickleshare==0.7.5
- prompt-toolkit==2.0.9
- Pygments==2.3.1
- python-dateutil==2.8.0
- pytz==2019.1
- six==1.12.0
- traitlets==4.3.2
- wcwidth==0.1.7

**Install with pip**

```
pip install -i https://test.pypi.org/simple/ gons-test-alekordESA
```

**Install from GitHub**

Download or clone the repository and install the required packages (preferably in a virtual environment):

```
git clone https://github.com/alekordESA/gonset-example.git
cd gonset-example
pip install -r requirements.txt
```
You can run ```./test.sh``` in the directory, which will do an entire run through using the test data and confirm whether everything is set up properly.