import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math



a=1741
b=2731
m=12960
xi=2
theta=1
D = np.array([])
sns.set_theme(); np.random.seed(0)

N=[10,100,1000,10000,100000]
for n in N:
  D = np.array([])
  X=np.array([])
  xi=2
  for i in range(n+1):    
    xi=(xi*a+b)%m
    ui= xi/m
    val = np.sin(math.pi*ui/2)*np.sin(math.pi*ui/2)
    D=np.insert(D,len(D),val)
    X=np.insert(X,len(X),ui)

  xt, counts = np.unique(D, return_counts=True)
  cusum = np.cumsum(counts)
  cusum = cusum / cusum[-1]
  # print(cusum)
  plt.step(x=xt, y=cusum)
  xf = np.linspace(0, np.amax(xt), 1000)
  yf=np.array([])
  for xtt in xf:
    yf=np.insert(yf,len(yf),(2/(math.pi))*np.arcsin(math.sqrt(xtt)))
  sns.lineplot(x=xf,y=yf)
  plt.show()
  print('For n = %d'%n + ': Experimental Mean = %f'%(np.average(xt)) + ', Theoritical Mean = 0.5')
  print('For n = %d'%n + ': Experimental Variance = %f'%(np.var(xt)) + ', Theoritical Variance = %f'%(1/8))

