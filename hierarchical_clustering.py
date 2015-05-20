import numpy as np
from sklearn.cluster import MeanShift as ms
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt

centers = [[1,1],[5,5]]

# "_" is not labeled.  It is "y"
#MeanShift is accurate up to 10,000
X, _ = make_blobs(n_samples = 200, centers = centers, cluster_std = 1)

plt.scatter(X[:,0], X[:,1])
plt.show()

#Fit a capital X at the fit
ms.fit(X)
#These are the labels the machine has assigned to the data.  They are different from defined centers.
labels = ms.labels_
#These are the estimated centers.  The higher the samples and lowe the std, the more accurate this approximation will be
cluster_centers = ms.cluster_centers_

#Tells you how many unique variables exist.  It will tell you how many categories the machine has found
n_clusters_ = len(np.unique(labels))

print("Number of estimated clusters:", n_clusters_)

#This list repeats itself 10 times
colors = 10*['r.','g.','b.','c,','k,','y,','m.']

print(colors)
print(labels)


