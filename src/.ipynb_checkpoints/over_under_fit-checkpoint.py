"""Slightly modified from:
http://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html
http://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html
http://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_iris.html

This example demonstrates the problems of underfitting and overfitting and how we can use 
linear regression with polynomial features to approximate nonlinear functions. The plot 
shows the function that we want to approximate, which is a part of the cosine function. 
In addition, the samples from the real function and the approximations of different models 
are displayed. The models have polynomial features of different degrees. We can see that 
a linear function (polynomial with degree 1) is not sufficient to fit the training samples. 
This is called underfitting. A polynomial of degree 4 approximates the true function almost 
perfectly. However, for higher degrees the model will overfit the training data, i.e. it 
learns the noise of the training data. We evaluate quantitatively overfitting / underfitting 
by using cross-validation. We calculate the mean squared error (MSE) on the validation set, 
the higher, the less likely the model generalizes correctly from the training data.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.cluster import k_means

def true_fun(X):
    return np.cos(1.5 * np.pi * X)

np.random.seed(0)

def show(n_samples=25, degrees=[1,4,15]):
    X = np.sort(np.random.rand(n_samples))
    y = true_fun(X) + np.random.randn(n_samples) * 0.1
    plt.figure(figsize=(8, 12))
    
    for i in range(len(degrees)):
        ax = plt.subplot(len(degrees), 1, i + 1)
        plt.setp(ax, xticks=(), yticks=())

        polynomial_features = PolynomialFeatures(degree=degrees[i],
                                                 include_bias=False)
        linear_regression = LinearRegression()
        pipeline = Pipeline([("polynomial_features", polynomial_features),
                             ("linear_regression", linear_regression)])
        pipeline.fit(X[:, np.newaxis], y)

        X_test = np.linspace(0, 1, 100)
        plt.plot(X_test, pipeline.predict(X_test[:, np.newaxis]), label="Model")
        plt.plot(X_test, true_fun(X_test), label="True function")
        plt.scatter(X, y, edgecolor='b', s=20, label="Samples")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.xlim((0, 1))
        plt.ylim((-2, 2))
        plt.legend(loc="best")
        plt.title("Poly-fit degree %d" % degrees[i])

    plt.tight_layout()    
    plt.show()

def doc():
    print(__doc__)

#### the clustering parts
blobs, classes = make_blobs(n_samples=500, 
                            centers=[(-4, -4), (-2, 2), (2, 0)],
                            random_state=42)


def cluster(n_clusters, known=False):
    centers, _classes, inertia = k_means(blobs, n_clusters=n_clusters)
    if known:
        _classes = classes
    plt.figure(figsize=(6, 6))
    plt.scatter(blobs[:,0], blobs[:,1], 
                c=np.array([('bgrcmykw'*10)[n] for n in _classes]), 
                marker='.')
    plt.show()
