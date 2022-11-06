import numpy as np
import pandas as pd
from scipy.stats import norm
N = 1000
h = 0.5
def genInvTrans():
    seq = []
    for i in range(N):
        u = np.random.uniform(0,1)
        seq.append(-np.log(u))
    return seq
print("Estimate generated using Inverse Transform method = ", np.mean(genInvTrans()))
print("Variance of estimator generated using Inverse Transform method = ", np.var(genInvTrans()))
print()
def genEstimator():
    seq = []
    for i in range(N):
        u = np.random.uniform(0,1)
        seq.append(np.log(u)/(h-1))
    return np.exp(np.multiply(-h,seq))/(1-h)
print("Estimate generated using Importance Sampling method = ", np.mean(genEstimator()))
print("Variance of estimator generated using Importance Sampling method = ", np.var(genEstimator()))
print()
var1 = np.var(genEstimator())
var2 = np.var(genInvTrans())
print("Amount of reduction in variance = ", (var2-var1)/var2 * 100)
