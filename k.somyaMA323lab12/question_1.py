import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import gamma




def Solution(n):
    a = 2
    ls = [1]

    def g(x):
        return gamma.pdf(x, a)

    def alpha(x, y):
        return min(1, (g(y))/(g(x)))
    
    def gen():
        for i in range(n):
            y_1 = np.random.randn()+ls[-1]
            u = np.random.rand()
            alph = alpha(ls[-1], y_1)
            if alph > 1-alph:
                if u>1-alph:
                    ls.append(y_1)
            else:
                if u<=alph:
                    ls.append(y_1)
        
    def plot():
        plt.hist(ls,bins=10, density=True)
        plt.show()

    def get_mean():
        print("Mean for the distribution generated is:", np.mean(ls))

    gen()
    plot()
    get_mean()


def main():
    pos_n = [100, 200, 500]
    for n in pos_n:
        Solution(n)


main()