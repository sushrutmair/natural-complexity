import numpy as np
import matplotlib.pyplot as plt
import math

N = 129
n_iter = 64

image = np.zeros([n_iter, N], dtype='int')
print(image.shape)
image[0, math.ceil(N/2)] = 1

for iterate in range(1, n_iter):
    for j in range(1, N-1):
        if image[iterate-1, j+1]+image[iterate-1, j-1] == 1:
            image[iterate, j] = 1

    image[iterate, 0] = image[iterate, N-2]
    image[iterate, N-1] = image[iterate, 1]

plt.imshow(image, interpolation="nearest")
plt.show()
