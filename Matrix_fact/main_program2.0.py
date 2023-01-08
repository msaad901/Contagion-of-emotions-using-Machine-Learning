import numpy as np
import matplotlib.pyplot as plt

import time

# Start timer
start_time = time.time()

def matrix_factorization(R, P, Q, K, steps=30000, alpha=0.0002, beta=0.02):
    errors = []
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] != 0:  # Check for non-zero ratings
                    eij = R[i][j] - np.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        errors.append(rmse(R, P, Q))
        print("Pourcentage d'accomplissement:", 100 * (step+1) / steps, "%")  # Print percentage complete
    final_rmse = rmse(R, P, Q)  # Calculate final RMSE
    print("Final RMSE:", final_rmse)  # Print final RMSE
    return P, Q.T, errors

def rmse(R, P, Q):
    non_zeros = [(i, j) for i in range(len(R)) for j in range(len(R[i])) if R[i][j] != 0]
    e = 0
    for i, j in non_zeros:
        e += pow(R[i][j] - np.dot(P[i,:],Q[:,j]), 2)
    return np.sqrt(e / len(non_zeros))

R = np.load('nu_i_matrix_init_cas_panique.npy')

R = np.array(R)

N = len(R)
M = len(R[0])
K = 8

P = np.random.rand(N,K)
Q = np.random.rand(M,K)

P, Q, errors = matrix_factorization(R, P, Q, K)
predicted_rating_matrix = np.dot(P, Q.T)

np.save('predicted_nu_i_matrix_cas_panique.npy', predicted_rating_matrix)
print(predicted_rating_matrix)

# Calculate elapsed time
elapsed_time = time.time() - start_time

# Print elapsed time
print("Temps d'execution: ", elapsed_time, "seconds")

plt.plot(range(len(errors)), errors)
plt.xlabel("Iteration")
plt.ylabel("RMSE")
plt.title("Evolution de la RMSE pour la prediction des nu_i pour le deuxieme scenario")
plt.show()
