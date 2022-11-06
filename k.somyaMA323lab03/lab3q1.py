#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import cmath 
import math 
from numpy import random

get_ipython().run_line_magic('matplotlib', 'inline')

#Function to calculate value of f(x)
def fx(i):
    return 20*i*math.pow(1 - i, 3)

#Distribution Function of f(x)
def F(x):
    y = 10 * x**2 - 20 * x**3 + 15 * x**4 - 4 * x**5
    return y

def generator(n,x0):
    a = 14945
    b = 6262
    m = 21089
    X = [x0]
    for i in range(1,n):
         X.append((a*X[-1]+b)%m)
    U = [x/m for x in X]
    return U


# In[2]:


C = 2.109375
X = []
Y = generator(50000,53)
U = generator(50000,47)
ctr=0 # in order to keep track of number of iterations

for i in range(50000):
    ctr+=1
    if U[i] <= fx(Y[i])/C :
        X.append(Y[i])
    if len(X)==10000 :
        break

print("The arithmetic mean for the generated random sample: ",np.mean(X)) #0.33300028925032005


# In[3]:


countprob=0
for x in X:
    if x>=0.25 and x<=0.75:
        countprob+=1
probability=countprob/len(X)
print("The probabilty P(0.25≤X≤0.75) for the generated random sample: ",probability)


# In[4]:


avgiter=ctr/len(X) 
print("The average number of iterations required for generation of each random number:",avgiter)


# In[5]:


plt.hist(X,bins=10000)
xa = np.arange(0,1,0.003)   
ya = xa*20*(1-xa)*(1-xa)*(1-xa)
plt.plot(xa,ya)
plt.show()


# In[6]:


print("For c=4, following are ther a-d observations:")
C = 4
X = []
Y = generator(50000,53)
U = generator(50000,47)
ctr=0 # in order to keep track of number of iterations

print("a)The avg number of iterations is equal to c=",C)
      
for i in range(50000):
    ctr+=1
    if U[i] <= fx(Y[i])/C :
        X.append(Y[i])
    if len(X)==10000 :
        break

print("b)The arithmetic mean for the generated random sample: ",np.mean(X)) #0.33300028925032005

countprob=0
for x in X:
    if x>=0.25 and x<=0.75:
        countprob+=1
probability=countprob/len(X)
print("c)The probabilty P(0.25≤X≤0.75) for the generated random sample: ",probability)

avgiter=ctr/len(X) # the average number of iterations required for generation of each random number
print("d)The average number of iterations required for generation of each random number:",avgiter)


# In[7]:


print("For c=7.5, following are ther a-d observations:")
C = 7.5
X = []
Y = generator(50000,53)
U = generator(50000,47)
ctr=0 # in order to keep track of number of iterations

print("a)The avg number of iterations is equal to c=",C)
      
for i in range(50000):
    ctr+=1
    if U[i] <= fx(Y[i])/C :
        X.append(Y[i])
    if len(X)==10000 :
        break

print("b)The arithmetic mean for the generated random sample: ",np.mean(X)) #0.33300028925032005

countprob=0
for x in X:
    if x>=0.25 and x<=0.75:
        countprob+=1
probability=countprob/len(X)
print("c)The probabilty P(0.25≤X≤0.75) for the generated random sample: ",probability)

avgiter=ctr/len(X) # the average number of iterations required for generation of each random number
print("d)The average number of iterations required for generation of each random number:",avgiter)

