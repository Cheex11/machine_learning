import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

x = [1,5,1.5,8,1,9]
y = [2,8,1.8,8,0.6,11]

plt.scatter(x,y)
plt.show()

#make an array of the data (it is a list of lists)

X = np.array([[1,2],
              [5,18],
              [1.5,1.8],
              [8,8],
              [1,0.6],
              [9,11]])

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

#c. and y. are other possible colors
colors = ["g.","r."]

for i in range(len(X)):
    print("coordinate:",X[i], "label:", labels[i])
    plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)

#s for size
plt.scatter(centroids[:,0], centroids[:,1], marker="x", s=150, linewidths=5, zorder=10)

plt.show()
