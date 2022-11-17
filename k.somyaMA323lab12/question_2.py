import numpy as np
import matplotlib.pyplot as plt

def Solution():
    ls1 = []
    ls2 = []
    ls3 = []

    def g(x):
        return x*np.exp(-x)

    def acf(ans,lg):
        list1=list()
        list2=list()
        n=len(ans)
        for i in range(0,n-lg):
            list1.append(ans[i])
        for i in range(lg,n):
            list2.append(ans[i])
        var1=np.var(list1)
        var2=np.var(list2)
        matrix = np.cov(list1, list2)
        return matrix[0][1]/np.sqrt(matrix[0][0]*matrix[1][1])

    def plot(ans):
        n=len(ans)
        plt.plot(np.arange(1, n+1, 1),ans, color = "green")
        plt.show()

    def norm(x):
        return np.exp(-x*x/2)/np.sqrt(2*np.pi)

    def condition(A, u):
        if A>1-A:
            if u>1-A:
                return True
        else:
            if u<=A:
                return True

    def independent():
        
        x=0.5
        chain_length=0
        while chain_length<5000:
                y=np.random.normal()
                A=min(1,g(y)*norm(x)/g(x)*norm(y))
                u=np.random.uniform()
                if condition(A, u):
                    x=y
                    chain_length=chain_length+1
                    ls2.append(x)  

    

    def symmetric():        
        x=0.5
        chain_length=0
        while chain_length<5000:
                y=np.random.normal()
                A=min(1,g(y)*norm(x)/g(x)*norm(y))
                u=np.random.uniform()
                if condition(A, u):
                    x=y
                    chain_length=chain_length+1
                    ls1.append(x)

    def randomwalk():        
        x=0.5
        chain_length=0
        while chain_length<5000:
                y=x+np.random.normal()
                A=min(1,g(y)/g(x))
                u=np.random.uniform()
                if condition(A,u):
                    x=y
                    chain_length=chain_length+1
                    ls3.append(x)

    symmetric()
    independent()
    randomwalk()
    plot(ls1)
    plot(ls2)
    plot(ls3)


    print("Acf - lag 0 - symmetric mcmc:", acf(ls1 , 0))
    print("Acf - lag 100 - symmetric mcmc:", acf(ls1 , 100))
    print("Acf - lag 200 - symmetric mcmc:", acf(ls1 , 200))
    
    print("Acf - lag 0 - independent mcmc:", acf(ls2 , 0))
    print("Acf - lag 100 - independent mcmc:", acf(ls2 , 100))
    print("Acf - lag 200 - independent mcmc:", acf(ls2 , 200))
    
    print("Acf - lag 0 - random walk mcmc:", acf(ls3 , 0))
    print("Acf - lag 100 - random walk mcmc:", acf(ls3 , 100))
    print("Acf - lag 200 - random walk mcmc:", acf(ls3 , 20))


Solution()