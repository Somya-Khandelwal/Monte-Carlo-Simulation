import numpy as np
import matplotlib.pyplot as plt

T=5

def bx(step):
    dt = T/step
    x = np.ones(step)
    x[0]=5
    mu=0.06
    sig=0.3
    for i in range(1,step):
        # Sampling from the Normal distribution
        yi = np.random.normal()
        x[i]=x[i-1]+mu*dt+sig*np.sqrt(dt)*yi

    return x


for i in range(10):
    plt.plot(bx(5000))
plt.show()