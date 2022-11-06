from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import multivariate_normal
import random
import numpy as np
import math
import time

def LCG(a,b,m,seed):
  xi=seed  
  xi=(xi*a+b)%m
  return xi

ValuesOfA= [-0.5, 0, 0.5, 1]
E= np.array([[5], [8]]) 
VC= np.array([[0, 0], [0, 0]])
A= np.array([[0, 0], [0, 0]])

Z1= []
Z2= []
seed_u1=3
seed_u2=5
for i in range(0, 10000):
  seed_u1=LCG(1741,2731,12960,seed_u1)
  seed_u2=LCG(1741,2731,12960,seed_u2)
  U1=seed_u1/12960
  U2=seed_u2/12960
  if(U1!=0):
    R= -2*math.log(U1)
  V= 2*math.pi*U2
  z1= math.sqrt(R)*math.cos(V)
  z2= math.sqrt(R)*math.sin(V)  
  Z1.append(z1)
  Z2.append(z2)

for a in ValuesOfA:
  X= []

  VC[0][0]= 1
  VC[0][1]= 2*a
  VC[1][0]= 2*a
  VC[1][1]= 4

  Sigma1= math.sqrt(VC[0][0])
  Sigma2= math.sqrt(VC[1][1])
  Raw= (VC[0][1]*1.00)/(Sigma1*Sigma2*1.00)

  A[0][0]= Sigma1
  A[0][1]= 0
  A[1][0]= Raw*Sigma2
  A[1][1]= math.sqrt(1.0-math.pow(Raw,2))*Sigma2
  
  X1= []
  X2= []
  for i in range(0, 10000):
    x1= E[0][0]+ Z1[i]*A[0][0]
    x2= E[1][0]+ A[1][0]*Z1[i]+ A[1][1]* Z2[i] 
    X1.append(x1)
    X2.append(x2)

  sns.histplot(x =X1, y = X2)

  sns.kdeplot(x =X1, y = X2,color="yellow")
  plt.show()


