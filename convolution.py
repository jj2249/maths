import numpy as np
import matplotlib.pyplot as plt
# specify file location here and define as matrix A
A = plt.imread("")
plt.imshow(A, cmap='gray')
plt.show()


def term_eval(i, j, A, G, d):
    term = 0
    for k in range(G.shape[0]):
        for l in range(G.shape[1]):
            term += G[k][l] * A[i+k-d][j+l-d]
    return term


def convolution(A, G):
    B = np.zeros(A.shape)
    d = int(G.shape[0]/2)
    for i in range (d, A.shape[0]-d):
        col = []
        for j in range(d, A.shape[1]-d):
            term = term_eval(i, j, A, G, d)
            col.append(term)
        for m in range(d):
            col.append(0)
            col.insert(0, 0)
        B[i] = col
    return B


# Choose Kernel

#edge detection
#G = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

#box blur
#G = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])

#sharpen
G = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

#Unsharp masking
"""G = np.array([[-1/256, -4/256, -6/256, -4/256, -1/256],
     [-4/256, -16/256, -24/256, -16/256, -4/256],
     [-6/256, -24/256, 476/256, -24/256, -6/256],
     [-4/256, -16/256, -24/256, -16/256, -4/256],
     [-1/256, -4/256, -6/256, -4/256, -1/256]])  """

B = convolution(A, G)
plt.imshow(B, cmap='gray')
plt.show()