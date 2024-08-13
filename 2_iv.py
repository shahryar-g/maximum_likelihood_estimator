import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Importing Data
df = pd.read_excel(r"C:\Users\shahryar\Desktop\Programing\python\Econometrics II\HW1.xls")

# Define the residuals function
def epsilon_i(wi, ni, psi, b):
    return ((wi / b) * (ni ** (1 - psi)) - psi) / (1 + np.log(ni) * psi)



# Define the likelihood function
def likelihood(params, w_i, n_i):
    b, psi, sigma = params
    
    # Calculate the sum of log probabilities
    log_prob_sum = np.sum(np.log((1 / (sigma * np.sqrt(2 * np.pi))))-(1/(2 * sigma**2)) * epsilon_i(w_i, n_i, psi, b))
    return -log_prob_sum
# Initial values
initial_guess = [0.5, 2, 1]

# Extracting data from DataFrame
w_i = df["w98"]
n_i = df["n98"]
# Maximize the likelihood function
result = minimize(likelihood, initial_guess, args=(w_i, n_i), method='Nelder-Mead')

# Extract the estimated parameters
b_mle, psi_mle, sigma_mle = result.x
likelihood_at_optimum = -result.fun

print("Maximum Likelihood Estimates:")
print("b:", b_mle)
print("psi:", psi_mle)
print("Sigma:", sigma_mle)
print("Likelihood at optimum parameters:", likelihood_at_optimum)

