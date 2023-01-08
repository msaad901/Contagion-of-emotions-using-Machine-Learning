
import numpy as np

# Create an array of 100 rows and 15 columns
arr = np.random.rand(100, 15)

# Set printing options to display the entire array
np.set_printoptions(threshold=np.inf)

# Print the array
#print(arr[15:])

import numpy as np

import random

matrix = []

for i in range(100):
  row = []
  for j in range(5):
    value = 0
    if random.uniform(0, 1) < 0.4:
      value = random.uniform(0.75, 1)
    elif random.uniform(0, 1) < 0.15:
      value = random.uniform(0.25, 0)
    row.append(value)
  matrix.append(row)

nu_i_matrix=matrix

print(nu_i_matrix)
np.save('nu_i_matrix_init.npy', nu_i_matrix)

