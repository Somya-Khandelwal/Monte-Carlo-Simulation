
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
import time

M=[100,1000,10000,100000]
D = np.array([])

for m in M:
  D = np.array([])
  for i in range(m):
    ui=np.random.uniform(0,1)
    val = math.exp(math.sqrt(ui))
    D=np.insert(D,len(D),val)

  Im = np.average(D)
  Std = np.std(D)
  Delta = 1.96
  CI_min = Im - Delta*Std/math.sqrt(m)
  CI_max = Im + Delta*Std/math.sqrt(m)
  print("Confidence interval for M=",m," is [",CI_min,",",CI_max,"]")
