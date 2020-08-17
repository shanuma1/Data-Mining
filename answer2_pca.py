import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#read the dataset
set1 = pd.read_csv("path to dataset", sep = " |\t", header = None, engine='python')
set2 = pd.read_csv("path to dataset", sep = " |\t", header = None, engine='python')
final = [set1, set2]
total = pd.concat(final)

#standardize/normalize the data
standardized_data = StandardScaler().fit_transform(total)

#find the mean along the rows
mean = np.mean(standardized_data, axis=0)

#find the covariance matrix i.e. 100 X 100
covariance = (standardized_data - mean).T.dot((standardized_data - mean)) / (standardized_data.shape[0]-1)

#calculate the eigen value and corresponding eigen vector using the function eig()
evalue, evector = np.linalg.eig(covariance)

#arrange each eigen value and vector in pairs
eig_pairs = [(np.abs(evalue[i]), evector[:,i]) for i in range(len(evalue))]

#arrange them in ascending order and reverse to get the value pairs in descending
eig_pairs.sort()
eig_pairs.reverse()

#calculate the variance or exactness of each Principle component
all = sum(evalue)
variance = [(i / all)*100 for i in sorted(evalue, reverse=True)]

#cumulative sum is calculated inorder to plot a scree graph
cumulative = np.cumsum(variance)

#calculate the no of diamensions to consider for the specified threshold to reduce the diamensions
sumOfVal = 0
threshold = 70;
sub = []
for i in variance:
    if sumOfVal < threshold:
        sumOfVal = sumOfVal + i
        sub.append(i)
        if sumOfVal > threshold:
            print len(sub)

#plot scree graph for the cumulative measure and the bar graph for the variance of each Principal component and mark the reduced diamensions
plt.xlabel('Principal components')
plt.ylabel('Variance')
plt.title('Threshold value = {}%'.format(threshold))
index = [i for i in range(1,101)]
plt.bar(index, variance)
plt.text(len(sub),threshold,len(sub),horizontalalignment='right')
plt.scatter(index, cumulative, 5,color='grey')
plt.show()