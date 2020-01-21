import numpy as np
import matplotlib.pyplot as plt

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return rho, phi

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return x, y

def rotate(x, y, angle=-np.pi/4):
    rho, phi = cart2pol(x, y)
    phi += angle
    return pol2cart(rho, phi)

def show(data, title="", xlab='', ylab=''):
    x, y = data[:, 0], data[:, 1]
    plt.plot(x, y, '.')
    plt.gca().set_aspect("equal")
    plt.ylim(plt.xlim())
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    
def make_data(angle=None):
    mean = [0, 0]
    cov = [[0.25, 0.0], [0, 10]]
    x, y = np.random.multivariate_normal(mean, cov, 200).T
    if angle:
        x, y = rotate(x, y, angle=angle)
    return np.c_[x, y]

data = make_data(angle=-np.pi/4)
