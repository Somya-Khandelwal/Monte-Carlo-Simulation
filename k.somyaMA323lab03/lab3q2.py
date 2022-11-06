import numpy as np
import matplotlib.pyplot as plt
import cmath 
import math 
from numpy import random

get_ipython().run_line_magic('matplotlib', 'inline')

# Acceptance Rejection Method

a = 23
b = 1
m = 4096
x0 = 29
N = 10000


def f(x, alpha): 
    return (np.sign(x)*np.power(np.abs(x), (alpha-1))*np.power(math.e,-x))/math.gamma(alpha) 



class Generator: 
    def __init__(self, a, b, m, x0):
        self.a = a
        self.b = b
        self.m = m
        self.x0 = x0
    
    def generate(self): 
        self.x0 = (self.x0*self.a + self.b)%self.m
        return self.x0/self.m
     

gen = Generator(a, b, m, x0)

def alpha_less_than_1(x, alpha): 
    A = 1/alpha + 1/math.e

    if(x > 0 and x <1): 
        return (np.power(x,alpha-1))/A
    elif(x >= 1): 
        return ((math.e)**(-x))
    else:
        return 0

def inv_alpha_less_than_1(u, alpha):
    A = 1/alpha + 1/math.e

    if(u > 0 and u < 1/(alpha*A)): 
        return -np.log(A) - np.log(1-u)
    elif(u >= 1/(alpha*A) and u < 1): 
        return np.power((alpha*A*u),(1/alpha)) 


def solve_alpha_less_than_1(alpha, seq_len): 
    seq = []
    A = 1/alpha + 1/math.e 
    c = A/math.gamma(alpha)

    while(len(seq) < seq_len): 
        X_u = gen.generate()
        X = inv_alpha_less_than_1(X_u, alpha)
        U = gen.generate()

        if(U*c*alpha_less_than_1(X, alpha) <= f(X, alpha)): 
            seq.append(X)
    return seq

def alpha_integer_generate(alpha): 
    Y = 0 
    n = alpha
    while(n != 0): 
        U = gen.generate() 
        X = -np.log(U)
        Y += X
        n -= 1
    return Y

def solve_alpha_integer(alpha, seq_len): 
    seq = []
    while(len(seq) < seq_len): 
        seq.append(alpha_integer_generate(alpha))
    
    return seq

def solve_alpha_greater_than_1(alpha, seq_len): 
    f_alpha, i_alpha = np.modf(alpha)

    seq1 = np.array(solve_alpha_less_than_1(f_alpha, seq_len))
    seq2 = np.array(solve_alpha_integer(i_alpha, seq_len))

    seq = np.add(seq1, seq2)

    return seq


# part A

print("Part A\n")
resA = np.array(solve_alpha_less_than_1(0.7, N))

print("Mean : ", np.mean(resA))
print("Variance : ", np.var(resA))
plt.hist(resA)
plt.show()

# part B

print("Part B\n")
resB = np.array(solve_alpha_integer(3, N))

print("Mean : ", np.mean(resB))
print("Variance : ", np.var(resB))
plt.hist(resB)
plt.show()

# part C

print("Part C\n")
resC = np.array(solve_alpha_greater_than_1(3.7, N))

print("Mean : ", np.mean(resC))
print("Variance : ", np.var(resC))
plt.hist(resC)
plt.show()

