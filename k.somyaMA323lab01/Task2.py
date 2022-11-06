import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

A=[1597,51749]
m=244944
b=0

for at in A:
  for xt in range(1,6):
    D = np.array([])
    xi=xt
    for i in range(1,10001):
      xi=(xi*at+b)%m
      ui= xi/m
      D=np.insert(D,0,ui)
    print('Below is the graph for a=%d'%at + ' and Xo=%d'%xt)
    sns.histplot(data=D,bins = [0, 0.05, 0.10, 0.15,0.20, 0.25,0.30, 0.35, 0.40, 0.45,0.50, 0.55,0.60, 0.65, 0.70, 0.75,0.80, 0.85,0.90, 0.95, 1.00],shrink=.8)
    plt.show()