import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

a=1741
b=2731
m=12960
xt=2
D = np.array([])
sns.set_theme(); np.random.seed(0)
xi=xt
N=[1000,10000,100000]
for i in range(1,18):
  xi=(xi*a+b)%m
  ui= xi/m
  D=np.insert(D,len(D),ui)

for n in N:
  d=D
  for i in range(18,n+1):
    ui = d[i-18]-d[i-6]
    if(ui<0):
      ui+=1
    d=np.insert(d,len(d),ui)
  sns.histplot(data=d,bins = 10000)
  plt.show()


for n in N:
  d=D
  for i in range(18,n+1):
    ui = d[i-18]-d[i-6]
    if(ui<0):
      ui+=1
    d=np.insert(d,len(d),ui)
  d1 = np.delete(d, 0)
  d2 = np.delete(d,len(d)-1)
  sns.scatterplot(x=d2, y=d1)
  plt.show()
