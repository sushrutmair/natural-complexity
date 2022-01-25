

# return a numpy array of shape s
import math
import matplotlib.pyplot as plt
import numpy as np


def create_numpy_array(s):
    return np.zeros(s, dtype='int')


# write a function to set all adjacent cells of a cell to 1 if the cell itself is 1.
# The function should return the modified array.

def set_adjacent_cells_to_1_if_cell_is_1(array):
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i, j] == 1:
                if (i - 1) >= 0 and (j - 1) >= 0 and (i + 1) < array.shape[0] and (j + 1) < array.shape[1]:
                    if array[i - 1, j] == 0 and array[i + 1, j] == 0 and array[i, j - 1] == 0 and array[i, j + 1] == 0:
                        array[i - 1, j] = 1
                        array[i - 1, j-1] = 1
                        array[i + 1, j + 1] = 1
                        array[i + 1, j] = 1
                        array[i, j - 1] = 1
                        array[i, j + 1] = 1
    return array


N = 129
n_iter = 64
image = create_numpy_array([n_iter, N])
image[0, math.ceil(N/2)] = 1
b = set_adjacent_cells_to_1_if_cell_is_1(image)
plt.imshow(b, cmap='gray')
plt.show()
