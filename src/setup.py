# Some libraries tend to be in flux for their dependency versions
import sys
import warnings
warnings.simplefilter("ignore")

from os.path import join
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

try:
    from sklearnex import patch_sklearn
    patch_sklearn()
except:
    print("Intel accelerator not installed (not required)", file=sys.stderr)

linf = pd.read_csv('data/linear_failure.csv', index_col=0)

def heatmap(data, title="", xticklabels=None, yticklabels=None):
    from matplotlib import cm
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(data, cmap=cm.viridis_r)

    if not xticklabels:
        xticklabels = [str(l) for l in range(data.shape[1])]
    if not yticklabels:
        yticklabels = [str(l) for l in range(data.shape[0])]
    
    # We want to show all ticks...
    ax.set_xticks(range(len(xticklabels)))
    ax.set_xticklabels(xticklabels)
    
    # There is something weird in y range; manually fix it
    ticks = yticklabels*2
    ticks[:] = [''] * len(ticks)
    ticks[1::2] = yticklabels
    ax.set_yticklabels(ticks)

    # Loop over data dimensions and create text annotations.
    for i in range(len(yticklabels)):
        for j in range(len(xticklabels)):
            text = ax.text(j, i, "%.2f" % data[i, j],
                           ha="center", va="center", color="white")

    ax.set_title(title)

