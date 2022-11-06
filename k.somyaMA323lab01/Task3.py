import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a=1229
b=1
m=2048

xo=5
print("For a=1229, b=1, m=2048, Xo=5:")
X=np.array([])
Y=np.array([])
prev=-1
for i in range(1,10001):
  xo=(xo*a+b)%m
  ui= xo/m
  if(i!=1):
    X=np.insert(X,0,prev)
    Y=np.insert(Y,0,ui)
  prev=ui
sns.scatterplot(x=X,y=Y)
plt.show()