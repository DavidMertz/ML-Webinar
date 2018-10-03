
# Machine Learning with scikit-learn

## Overall Introduction: Welcome to Machine Learning with scikit-learn

Welcome to this Safari webinar, "Machine Learning with scikit-learn."  Over the next six hours and eight lessons we introduce the main concepts and techniques used in modern machine learning and look at numerous examples written in scikit-learn.

My name is David Mertz, and I’ve been involved with the Python community for 20 years, with Data Science under various previous names, and with Machine Learning since way back when it was more likely to be called "Artificial Intelligence."  I was a director of the Python Software Foundation for six years, and continue to serve on, or chair, a variety of PSF working groups.

I have also written quite a bit about Python: the column _Charming Python_ for IBM developerWorks, for many years; the Addison-Wesley book _Text Procesing in Python_; two short books for O’Reilly.  I created the data science training program for Anaconda Inc. and was a senior trainer for them.

A few years ago, I worked for 8 years with the folks at D. E. Shaw Research.  They have built the world's fastest, highly-specialized—down to the ASICs and network layer—supercomputer for performing molecular dynamics. I am pleased to find Python has become the default high-level language for most scientific computing projects.

Nowadays, I run a training business called "KDM Training" with some amazing and accomplished colleagues. We deliver hands-on training for Data Science and Scientific Python.  We would love to hear from you, and would especially love your business for our live, on-site trainings.  Our email is `info@kdm.training` and our website is `http://kdm.training`.

--

The Scikit-learn library provides a large range of algorithms in machine learning that are unified under a common and intuitive Python API. Most of the dozens of classes provided for various kinds of models share the large majority of the same calling interface. Very often—as we will see in examples below—you can easily substitute one algorithm for another with nearly no change in your underlying code. This allows you to explore the problem space quickly, and often arrive at an optimal, or at least satisficing approach to your problem domain or datasets.

Scikit-learn is built on the foundations of the Numeric Python stack.  It uses NumPy for its fundamental data structures and optimized performance.  It plays well with Pandas and matplotlib.  It is Free Software under a BSD license.  The great bulk of machine learning programming in Python is done with scikit-learn—at least outside the specialized domain of "deep neural networks" which we will discuss briefly in the first lesson.

--

In order to get best advantage from this course, you should do a few things to prepare, or already be familiar with things mentioned.  A good basic knowledge of Python is important.  A few intuitions about statistics and linear algebra are useful, but we will not explore mathematical details underlying algorithms in any great length.  Scikit-learn packages many of the numeric niceties for you, and implements algorithms in efficient ways.

The examples we go through in this course often utilize Pandas DataFrames as containers to store data sets.  Therefore, it will be easier for you to follow this course if you have a working knowlege of Pandas.  However, we will not use particular arcane techniques in that large library; you should be able to follow even if you do not already use Pandas.  Similarly, we will occasionally visualize results using matplotlib and a few other libraries; you will not need to learn those APIs to follow this course, but also do not be surprised to see a few of those APIs used.

The course content itself is presented using Jupyter notebooks.  These are available to download from https://github.com/DavidMertz/ML-Webinar.  If you have not used Jupyter notebooks, it is worthwhile to spend a half-hour on an introductory tutorial before working through the material in this course.  All of the content present in this video will closely match that available at the GitHub repository; the repository may be updated or tweaked by the time you watch this.  The notebook and other resources associate with this course are licensed as Attribution-NonCommercial-ShareAlike 4.0 International; this video itself is made available only for registrants at Safari, and is not redistributable.

Beyond downloading the content of the GitHub repository, you should setup a suitable environment for running the Jupyter notebooks.  The repository contains a file `environment.yml` for creating an environment using the `conda` package manager and a file `requirements.txt` for creating an environment under the `pip` package manager.  Please use one of these to install a suitable environment, then launch the material using `jupyter notebook Outline.ipynb` at the command line.

--

I hope you will enjoy and learn a great deal from the next several hours of training.  Please feel free to pause the video wherever it is convenient, and play around with techniques, concepts, and code presented within the interactive Jupyter notebooks.  I hope your personally customized version of these notebooks will be a valuable resource for you to return to later.


## Lesson 1: What is Machine Learning?

* Difference between "Deep Learning" and other ML techniques
* Overview of techniques used in Machine Learning
* Classification vs. Regression vs. Clustering
* Dimensionality Reduction
* Feature Engineering
* Feature Selection, 
* Categorical vs. Ordinal vs. Continuous variables
* One-hot encoding
* Hyperparameters
* Grid Search
* Metrics

## Lesson 2: Exploring a data set

* Looking for anomalies and data integrity problems
* Cleaning data
* Massaging data format to be model-ready
* Choosing features and a target
* Train/test split

## Lesson 3: Classification

* Choosing a model
* Feature importances
* Cut points in a decision tree
* Comparing multiple classifiers

## Lesson 4: Regression

* Sample data sets in scikit-learn
* Linear regressors
* Probabilistic regressors
* Other regressors

## Lesson 4: Clustering

* Overview of (some) clustering algorithms
* Kmeans clustering
* Agglomerative clustering
* Density based clustering: DBSan and HDBScan
* n_clusters, labels, and predictions
* Visualizing results

## Lesson 5: Hyperparameters

* Understanding hyperparameters
* Manual search of parameter space
* GridsearchCV
* Attributes of grid search and wrapped model

## Lesson 6: Feature engineering and feature selection

* Principal Component Analysis (PCA)
* Non-Negative Matrix Factorization (NMF)
* Latent Dirichlet Allocation (LDA)
* Independent component analysis (ICA)
* SelectKBest
* Dimensionality expansion
* Polynomial Features
* One-Hot Encoding
* Scaling with StandardScaler, RobustScaler, MinMaxScaler, Normalizer, and others
* Binning values with quantiles or binarize

## Lesson 7: Pipelines

* Feature selection and engineering
* Grid search
* Model

## Lesson 8: Robust Train/test splits 

* cross_val_score
* ShuffleSplit
* KFold, RepeatedKFold, LeaveOneOut, LeavePOut, StratifiedKFold


## Summary

