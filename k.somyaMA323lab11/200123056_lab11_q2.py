import math
import random
import numpy as np
import matplotlib.pyplot as plt

def decimalToBinary(n):  
  return bin(n).replace("0b", "")

def decimalToTernary (n):
  if n == 0:
    return '0'
  nums = []
  while n:
    n, r = divmod(n, 3)
    nums.append(str(r))
  return ''.join(reversed(nums))


ValuesInTernary= []
plt.rcParams['agg.path.chunksize'] = 10000
for i in range(0, 100000):
    s= decimalToTernary(i)
    value= 0
    for j in range(0, len(s)):
        if s[len(s)-j-1]=='1':
            value+= 1.00/pow(3, j+1)
        if s[len(s)-j-1]=='2':
            value+= 2.00/pow(3, j+1)
    ValuesInTernary.append(value)

for n in N:
    XAxis= []
    YAxis= []
    for i in range(0, n):
        XAxis.append(Values[i])
        YAxis.append(ValuesInTernary[i])
    print("For n=",n)
    plt.plot(XAxis,YAxis)
    plt.xlabel("Phi2(i)",size= 20)
    plt.ylabel("Phi3(i)",size= 20)
    plt.title("Generating x[i] using Halton sequence in 2-D",size= 20)
    plt.show()
