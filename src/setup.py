# Some libraries tend to be in flux for their dependency versions
import warnings
warnings.simplefilter("ignore")

# We utilize some mglearn demo functions
import src.mglearn as mglearn

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

linf = pd.read_csv('data/linear_failure.csv', index_col=0)