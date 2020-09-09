import numpy as np


def deriv(f, x, h):
    return ((f(x + h)) - f(x-h)) / (2 * h)


def newtonRaphson(n, f, h, x0, tol):
    count = 0
    x = x0
    while count < n:
        x = x - (f(x) / deriv(f, x, h))
        count += 1
    return x


def f(x):
    return np.sin(x)**2 + 2*x - np.e**-x

print(newtonRaphson(100, f, 1e-6, 0.5, 1e-3))
