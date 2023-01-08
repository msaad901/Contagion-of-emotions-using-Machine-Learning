
import numpy as np

def generate_table(n_rows, n_columns, zero_prob):
    table = np.zeros((n_rows, n_columns))
    for i in range(n_rows):
        for j in range(n_columns):
            if np.random.rand() > zero_prob:
                table[i][j] = np.random.uniform(0, 1)
    return table

rating_matrix = generate_table(100, 15, 0.6)
np.save('rating_matrix.npy', rating_matrix)
