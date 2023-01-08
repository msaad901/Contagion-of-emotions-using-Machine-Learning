
import numpy as np

beta_i_matrix_init_cas_police = np.load('nu_i_matrix_init_cas_panique.npy')
predicted_beta_i_matrix_cas_police = np.load('beta_i_matrix_init_cas_police.npy')

# Set printing options to display the entire array
np.set_printoptions(threshold=np.inf)

#matrix_scaled = (predicted_nu_i_matrix_cas_police - predicted_nu_i_matrix_cas_police.min()) / (predicted_nu_i_matrix_cas_police.max() - predicted_nu_i_matrix_cas_police.min())


#print(rating_matrix[:10,:5])
#print(beta_i_matrix_init_cas_police[:10,:5])
print("Voila la nouvelle matrice obtenue")
print(predicted_beta_i_matrix_cas_police[:10,:5])