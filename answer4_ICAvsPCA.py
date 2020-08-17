import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import FastICA, PCA
from sklearn.preprocessing import StandardScaler

set1 = pd.read_csv("path to dataset", sep = " |\t", header = None, engine='python')
set2 = pd.read_csv("path to dataset", sep = " |\t", header = None, engine='python')
final = [set1, set2]
total = pd.concat(final)

#standardize the data
x = StandardScaler().fit_transform(total.transpose())

#apply ica on dataset
ica = FastICA()
ica_result = ica.fit_transform(total.transpose())

#apply pca on dataset
pca = PCA()
pca_result = pca.fit_transform(x)


plt.plot(total.iloc[:, :].values.tolist())
plt.title('Original Dataset')
plt.show()
plt.title('Data obtained after PCA')
plt.plot(pca_result)
plt.show()
plt.title('Data obtained after ICA')
plt.plot(ica_result)
plt.show()
