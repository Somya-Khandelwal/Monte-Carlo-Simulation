import numpy as np
from scipy.special import ndtri
import random

random.seed(2)

M_list = [100, 1000, 10000, 100000]

def get_s(seq, N): 
    mu = seq[0]
    S = 0
    
    for i in range(1, N): 
        d = seq[i] - mu
        mu = mu + d/(i+1) 
        S = S + (i/(i+1))*d*d
    
    return np.sqrt(S/(N-1))

for M in M_list:
    seq = []

    while len(seq) < M: 
        ui = random.random(); 
        yi = np.exp(np.sqrt(ui))
        seq.append(yi)

    mu_tilda = np.mean(seq)
    ci_percent = 0.95
    delta = ndtri((1+ci_percent)/2)
    s = get_s(seq, M)
    L = mu_tilda - ((delta*s)/np.sqrt(M))
    U = mu_tilda + ((delta*s)/np.sqrt(M))

    print("\n**********\n")
    print(f"For M = {M}-")
    print("95 percent confidence interval is - [",L,",",U,"].")
    print("Actual value of I is 2."); 
    print(f"Estimated value of I is {mu_tilda}.")


