import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


centers = [[1,1],[5,5],[9,10]]
X, _ = make_blobs(n_samples = 200, centers = centers, cluster_std = 2)

ms = MeanShift()

#Fit a capital X at the fit
ms.fit(X)
#These are the labels the machine has assigned to the data.  They are different from defined centers.
labels = ms.labels_
#These are the estimated centers.  The higher the samples and lowe the std, the more accurate this approximation will be
cluster_centers = ms.cluster_centers_

print(cluster_centers)

#Tells you how many unique variables exist.  It will tell you how many categories the machine has found
n_clusters_ = len(np.unique(labels))

print("Number of estimated clusters:", n_clusters_)

#This list repeats itself 10 times
colors = 10*['r.','g.','b.','c,','k,','y,','m.']

#Plot the data!
for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

plt.scatter(cluster_centers[:,0], cluster_centers[:,1], marker="o", s=15, linewidths = 5, zorder=10)
plt.show()
