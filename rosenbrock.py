import numpy as np

class Rosenbrock():
    def __init__(self, a, b, tol, x0, x1):
        self.a = a
        self.b = b
        self.tol = tol
        self.x0 = x0
        self.x1 = x1

    def f(self, x):
        return (self.a - x[0])**2 + self.b*(x[1] - x[0]**2)**2

    def J(self, x):
        return np.array([[2 + 5 * self.b * x[0] ** 2 - 4 * self.b * x[1], -4 * self.b * x[0]], [4 * self.b * x[0] ** 2, 2 * self.b]])

    def g(self, x):
        return np.array([2 * x[0] - 2 * self.a - 4 * self.b * x[0] * (x[1] - x[0] ** 2), 2 * self.b * (x[1] - x[0] ** 2)])

    def JinvG(self, J, g):
        return np.linalg.solve(J, g)

    def error(self, g, gzero):
        return abs(np.linalg.norm(g) / np.linalg.norm(gzero))

    def iterate(self, J, g, x, tol):
        gzero = self.g(x)
        error = 1
        while error > tol:
            xnew = x - self.JinvG(J, g)
            x = xnew
            g = self.g(x)
            error = self.error(g, gzero)
            print(error)
        return x

    def minimise(self):
        x = [self.x0, self.x1]
        J = self.J(x)
        g = self.g(x)
        xmin = self.iterate(J, g, x, self.tol)
        fmin = self.f(xmin)
        return xmin, fmin

minimiser = Rosenbrock(2, 100, 1e-9, 1.1, 1.1)
print(minimiser.minimise())
