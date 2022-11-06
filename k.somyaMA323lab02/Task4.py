import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math


X=[]
a=1
b=19568
m=19647
xi=2
theta=1
U=np.array([])
for i in range(100000+1):    
  xi=(xi*a+b)%m
  ui= xi/m
  U=np.insert(U,len(U),ui)
  temp=math.floor(U[i]*5000)
  X.append(2*temp+1)

sns.displot(X,bins=10000)
plt.show()
