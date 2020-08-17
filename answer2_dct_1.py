import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA, FastICA
from sklearn.preprocessing import StandardScaler
import math

set1 = pd.read_csv("path to dataset", sep = " |\t", header = None, engine='python')
set2 = pd.read_csv("path to dataset", sep = " |\t", header = None, engine='python')
final = [set1, set2]
total = pd.concat(final)

k=100
rows=1000
cols=100

result = [[0 for i in range(cols)] for j in range(rows)]
result1 = [[0 for i in range(rows)] for j in range(cols)]
for j in range(1000):
    for i in range(100):
        if (i==0):
            a = float(math.sqrt(0.01))
        else:
            a = float(math.sqrt(0.02))
        result[j][i] = a*total.iloc[j][i]*math.cos(((2*j+1)*i*math.pi)/(2*k))

for i in range(len(result)):
   for j in range(len(result[0])):
       result1[j][i] = result[i][j]

plt.rcParams["figure.figsize"] = (12,9)
plt.plot(total.transpose())
plt.title('Original Dataset')
plt.show()
plt.plot(result1)
plt.title('Data obtained after DCT')
plt.show()
