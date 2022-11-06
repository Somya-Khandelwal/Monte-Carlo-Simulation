import numpy as np
import matplotlib.pyplot as plt

T=5

def y_mu(t):
     return 0.0325-(0.05*t)

def y_sig(t):
     return 0.012+0.0138*t+0.00125*t*t

def by(step):
    dt = T/step
    y = np.ones(step)
    y[0]=5
    
    
    for i in range(1,step):
        # Sampling from the Normal distribution
        yi = np.random.normal()
        y[i]=y[i-1]+y_mu(dt*i)*dt+y_sig(dt*i)*np.sqrt(dt)*yi

    return y


for i in range(10):
    plt.plot(by(5000))
plt.show()