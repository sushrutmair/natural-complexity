
from venv import create
import matplotlib.pyplot as plt
import numpy as np


def create_numpy_array(shape):
    return np.zeros(shape)

# write a function to set a cell of a numpy array to 1 if and only if its adjacent cells are all 1


def set_cell_if_adjacent_cells_are_all_1(array):
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i, j] == 0:
                if (i - 1) >= 0 and (j - 1) >= 0 and (i + 1) < array.shape[0] and (j + 1) < array.shape[1]:
                    if array[i - 1, j] == 1 and array[i + 1, j] == 1 and array[i, j - 1] == 1 and array[i, j + 1] == 1:
                        array[i, j] = 1
    return array


def alternate_cells(array):
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if i % 2 == 0:
                if j % 2 == 0:
                    array[i, j] = 1
            else:
                if j % 2 != 0:
                    array[i, j] = 1
    return array


# write a function to set a cell of a numpy array to 1 if one of its adjacent cells are 1
def set_cell_if_one_of_its_adjacent_cells_is_1(array):
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i, j] == 0:
                if (i - 1) >= 0 and (j - 1) >= 0 and (i + 1) < array.shape[0] and (j + 1) < array.shape[1]:
                    if array[i - 1, j] == 1 or array[i + 1, j] == 1 or array[i, j - 1] == 1 or array[i, j + 1] == 1:
                        array[i, j] = 1
    return array

# write a function to set a cell of a numpy array to 1 if its left cell is 1.


def set_cell_if_its_left_cell_is_1(array):
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i, j] == 0:
                if (j - 1) >= 0:
                    if array[i, j - 1] == 1:
                        array[i, j] = 1
    return array


# call alternate_cells function on a numpy array
""" a = alternate_cells(create_numpy_array((75, 150)))
print(a)

# display the array using pyplot
plt.imshow(a, cmap='gray')
plt.show() """

# call set_cell_if_adjacent_cells_are_all_1 function on a numpy array
b0 = create_numpy_array((75, 150))
# set 3 random cells of b0 to 1
b0[np.random.randint(0, b0.shape[0], 3),
   np.random.randint(0, b0.shape[1], 3)] = 1
b = set_cell_if_one_of_its_adjacent_cells_is_1(b0)
plt.imshow(b0, cmap='gray')
plt.show()
