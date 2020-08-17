import numpy as np
from scipy.fftpack import dct
import pandas as pd
import matplotlib.pyplot as plt

total = []
set1 = pd.read_csv("path to dataset", sep = " |\t", header = None, engine='python')
set2 = pd.read_csv("path to dataset", sep = " |\t", header = None, engine='python')
final = [set1, set2]
total = pd.concat(final)


y = dct(total)
print plt.hist(y)