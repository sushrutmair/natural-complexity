import math
from venv import create
import matplotlib.pyplot as plt
import numpy as np


def create_numpy_array(shape):
    return np.zeros(shape, dtype='int')


# write a function to set a cell of the numpy array to 1 if one and only one of its adjacent cells are 1.


def set_cell_if_one_of_its_adjacent_cells_is_1(array):
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i, j] == 0:
                if (i - 1) >= 0 and (j - 1) >= 0 and (i + 1) < array.shape[0] and (j + 1) < array.shape[1]:
                    if array[i - 1, j] == 1 and array[i + 1, j] == 0 and array[i, j - 1] == 0 and array[i, j + 1] == 0:
                        array[i, j] = 1
                    elif array[i - 1, j] == 0 and array[i + 1, j] == 1 and array[i, j - 1] == 0 and array[i, j + 1] == 0:
                        array[i, j] = 1
                    elif array[i - 1, j] == 0 and array[i + 1, j] == 0 and array[i, j - 1] == 1 and array[i, j + 1] == 0:
                        array[i, j] = 1
                    elif array[i - 1, j] == 0 and array[i + 1, j] == 0 and array[i, j - 1] == 0 and array[i, j + 1] == 1:
                        array[i, j] = 1
    return array


N = 129
n_iter = 64

image = create_numpy_array([n_iter, N])
image[0, math.ceil(N/2)] = 1

# call rule 3 on the array coded by copilot!
b = set_cell_if_one_of_its_adjacent_cells_is_1(image)
plt.imshow(b, cmap='gray')
plt.show()
