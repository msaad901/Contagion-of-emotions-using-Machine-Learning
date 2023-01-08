


import random
import numpy as np
""""
matrix = []

for i in range(100):
  row = []
  for j in range(5):
    value = 0
    if random.uniform(0, 1) < 0.1:
      value = random.uniform(0.75, 1)
    elif random.uniform(0, 1) < 0.35:
      value = random.uniform(0.25, 0)
    elif random.uniform(0, 1) < 0.1:
      value = random.uniform(0.3, 0.7)
    row.append(value)
  matrix.append(row)
"""""

import numpy as np

# Generate a matrix with 100 rows and 5 columns
matrix = np.zeros((100, 5))

# Set the values for the first 40 rows
num_values = 40 * 5  # Number of values in the first 40 rows
num_values_set = int(num_values * 0.5)  # Number of values to set to a random value between 0.8 and 1
indices = np.random.choice(num_values, size=num_values_set, replace=False)  # Indices of the values to set
row_indices, col_indices = np.unravel_index(indices, (40, 5))  # Convert flat indices to (row, col) indices
matrix[row_indices, col_indices] = np.random.uniform(0.8, 1, size=num_values_set)



# Set the values for the next 15 rows
num_values = 15 * 5  # Number of values in the next 15 rows
num_values_set = int(num_values * 0.6)  # Number of values to set to a random value between 0 and 0.25
indices = np.random.choice(num_values, size=num_values_set, replace=False)  # Indices of the values to set
row_indices, col_indices = np.unravel_index(indices, (15, 5))  # Convert flat indices to (row, col) indices
matrix[40 + row_indices, col_indices] = np.random.uniform(0,0.3, size=num_values_set)



# Set the values for the remaining rows
num_values = 45 * 5  # Number of values in the remaining rows
num_values_set = int(num_values * 0.4)  # Number of values to set to a random value between 0 and 1
indices = np.random.choice(num_values, size=num_values_set, replace=False)  # Indices of the values to set
row_indices, col_indices = np.unravel_index(indices, (45, 5))  # Convert flat indices to (row, col) indices
matrix[55 + row_indices, col_indices] = np.random.uniform(0, 1, size=num_values_set)




print(matrix)
np.save('nu_i_matrix_init_cas_police.npy', matrix)