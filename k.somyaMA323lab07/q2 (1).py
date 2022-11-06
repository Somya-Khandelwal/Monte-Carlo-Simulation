import numpy as np
from scipy.special import ndtri
import random

random.seed(2)

def f(X): 
    return np.exp(np.sqrt(X)) 

def get_s(seq, N): 
        mu = seq[0]
        S = 0
        
        for i in range(1, N): 
            d = seq[i] - mu
            mu = mu + d/(i+1) 
            S = S + (i/(i+1))*d*d
        
        return np.sqrt(S/(N-1))


def find_CI(seq, M):
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


M_list = [100, 1000, 10000, 100000]

for M in M_list: 
    seqY1 = []
    seqY2 = []

    while(len(seqY1) < M): 
        U = random.random()
        seqY1.append(f(U)) 
        seqY2.append(f(1-U))

    seqY1 = np.array(seqY1)
    seqY2 = np.array(seqY2)

    seqY = (seqY1 + seqY2)/2
    find_CI(seqY, M)

    var_new = np.var(seqY)
    var_old = np.var(seqY1)
    var_red_pc = ((var_old-var_new)*100)/var_old

    print(f"The reduction in variance is {var_red_pc} %");


