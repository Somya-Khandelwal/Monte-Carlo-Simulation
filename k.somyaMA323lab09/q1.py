import numpy as np
import matplotlib.pyplot as plt

T=5

def b(step):
    dt = T/step
    w = np.ones(step)
    w[0]=0
    for i in range(1,step):
        # Sampling from the Normal distribution
        yi = np.random.normal()
        w[i]=w[i-1]+np.sqrt(dt)*yi

    return w


for i in range(10):
    plt.plot(b(5000))
plt.show()