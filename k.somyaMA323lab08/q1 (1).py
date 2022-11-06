import numpy as np
import cmath
import random
import math
def lower_bound(arr, val, n):
    st=0 
    en=n
    while(st<en):
        mid=math.floor((st+en)/2)
        if(arr[mid]>val):
            en=mid
        else:
            st=mid+1
    return st

def eval(n):
    arr=np.random.normal(0,1,n)
    arr.sort()
    arr1=[]
    for i in range(0,n):
        u = random.random()
        y = -1*math.log(u)
        gen=lower_bound(arr,(1-y)/2,n)
        gen/=n
        arr1.append(gen)
    print("Expected value is {} and variance is {}".format(np.mean(arr1),np.var(arr1)))
    return np.var(arr1)
def eval_antithetic(n):
    arr=np.random.normal(0,1,n)
    arr.sort()
    arr1=[]
    for i in range(0,n):
        u = random.random()
        y = -1*math.log(u)
        y1 = -1*math.log(1-u)
        gen=lower_bound(arr,(1-y)/2,n)
        gen+=lower_bound(arr,(1-y1)/2,n)
        gen/=(2*n)
        arr1.append(gen)
    print("For antithetic, Expected value is {} and variance is {}".format(np.mean(arr1),np.var(arr1)))
    return np.var(arr1)
x1 = eval(100000)
x2 = eval_antithetic(100000)
print("Percentage varinace reduction is {}".format((1-x2/x1)*100))
