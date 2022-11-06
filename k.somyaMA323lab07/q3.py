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
    seqX = []
    seqY = []

    while(len(seqX) < M): 
        U = random.random()
        seqX.append(f(U)) 
        seqY.append(np.sqrt(U))

    cov_mat = np.cov(seqX, seqY)
    cov = cov_mat[0][1]

    varY = np.var(seqY)
    c_hat = -cov/varY
    mu_y = np.mean(seqY)

    seqX_new = seqX + np.multiply(c_hat, seqY - mu_y)

    find_CI(seqX_new, M)

    varX = np.var(seqX)
    varX_new = np.var(seqX_new)

    var_red_pc = ((varX-varX_new)*100)/varX

    print(f"The reduction in variance is {var_red_pc} %");


