# Emerging Technologies Assessment

## Introduction

This project is done by Jeremy Yon G00330435 for 4th Year Software development GMIT, emerging technologies module.

## Description

This Github repository contains the project files for the Emerging Technologies 2018 module in GMIT. To be specific, it contains:

1. Numpy random notebook: a jupyter notebook explaining the concepts behind and the use of the numpy random package, including plots of the various distributions.
2. Iris dataset notebook: a jupyter notebook explaining the famous iris data set including the difficulty in writing an algorithm to separate the three classes of iris based on the variables in the dataset.
3. MNIST dataset notebook: a jupyter notebook explaining how to read the MNIST dataset efficiently into memory in Python.
4. Digit recognition script: a Python script that takes an image file containing a handwritten digit and identifies the digit using a supervised learning algorithm and the MNIST dataset.
5. Digit recognition notebook: a jupyter notebook explaining how the above Python script works and discussing its performance.

## Prerequisites
1. Anaconda 5.3.1, running on python 3.6.5 with subpackages:
- numpy
- matplotlib.pyplot
- pandas
- seaborn
- sklearn
- gzip
- PIL
- os
- keras
- tkinter

2. Mnist Dataset

## Running the Notebooks and Scripts

1. Git clone this project to local machine
```
git clone https://github.com/yonjeremy/emerging-technologies-assesment
```
2. Download the Mnist dataset (all four datasets)
```
http://yann.lecun.com/exdb/mnist/
```
3. Navigate to the cloned folder and create an empty directory called "data"
4. Paste the downloaded datasets into the data folder (leave it zipped)
5. In the cloned folder, open jupyter notebook
```
jupyter notebook
```

6. Run the digitrec.py script
```
python digitrec.py
```

## Running the digitrec.py script

1. The model will first be loaded and trained in real time. This will take up to 2-3 minutes.
2. When the model has been loaded, a file explorer will pop up, prompting the user to select on any digit image. (note that the image has to be a 28 by 28 picture)
3. The script will return the prediction, as well as the true value of the digit.
4. The user can rerun the program by entering "yes" into the prompt or "no" to exit the script.

## Project Plan
```
| no.   | Activity                             | Time estimate            |

| 1     | Setting up enviroments               | 1 week                   |
| 2     | Learn how to use jupyter notebook    | 1 week                   |
| 3     | Work on numpy.random notebook        | 2 weeks                  |
| 4     | Work on iris-dataset notebook        | 1 week                   |
| 5     | Work on mnist notebook               | 1 week                   |
| 6     | Work on digit recognition notebook   | 2 weeks                  |
| 7     | Create digitrec script from notebook | 1 week                   |
| 8     | Fix bugs, test, and tidy up READMe   | 1 week                   |
|                                   Total:     | 10 weeks                 |

```

## Credits

Dr Ian McLoughlin
