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


print("First 25 values of the Van der Corupt sequence, using the radical inverse function are:")
for i in range(1, 26):
  s= decimalToBinary(i)
  value= 0
  for j in range(0, len(s)):
    if s[len(s)-j-1]=='1':
      value+= 1.00/pow(2, j+1)
  print(value)

Values= []
for i in range(0, 100000):
  s= decimalToBinary(i)
  value= 0
  for j in range(0, len(s)):
    if s[len(s)-j-1]=='1':
      value+= 1.00/pow(2, j+1)
  Values.append(value)
X= []
Y= []
for i in range(0, 999):
  X.append(Values[i])
for i in range(1, 1000):
  Y.append(Values[i])
plt.scatter(X,Y)
plt.xlabel("x(i)",size= 20)
plt.ylabel("x(i+1)",size= 20)
plt.title("Graph between x(i) and x(i+1).. Used radical inverse method",size= 20)
plt.show()

N= [100, 100000]
for n in N:
    Radical= []
    LCG= []
    for i in range(0, n):
        Radical.append(Values[i])
    m= 244944
    a= 1597
    b= 51749
    x0= 1
    for i in range(0, n):
        x= (a*x0 + b)%m
        LCG.append((x*1.000)/(m*1.000))
        x0= x
    plt.hist(Radical, bins = 100, rwidth = 0.5)
    plt.xlabel('Value',size= 20)
    plt.ylabel('Frequemcy',size= 20)
    plt.title('Plotting Distribution Using Radical Inverse method',size= 20)
    # plt.legend()
    plt.show()

    plt.hist(LCG, bins = 100, rwidth = 0.5)
    plt.xlabel('Value',size= 20)
    plt.ylabel('Frequemcy',size= 20)
    plt.title('Plotting Distribution Using LCG',size= 20)
    # plt.legend()
    plt.show()