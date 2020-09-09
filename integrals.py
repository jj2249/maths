import numpy as np

n = 10**6

def f(x, y):
    return (np.e**(x*y)) * (np.cos(y)**2) * (np.sin(x)**2)

def g(x, y):
    return (1/np.sqrt(1-x**2)) + (1/np.sqrt(1-y**2))

def monte(alow, ahigh, blow, bhigh, n, f):
    sum = 0
    for i in range(n):
        a = np.random.uniform(alow, ahigh)
        b = np.random.uniform(blow, bhigh)
        sum += f(a, b)
    return sum / n