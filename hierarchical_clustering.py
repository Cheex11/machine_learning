import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv

start_times = []
end_times = []
production = []

with open('carwars.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        start_times.append(float(row[0]))
        end_times.append(float(row[1]))
        production.append(float(row[2]))


X = np.array(list(np.array(row) for row in zip(start_times, end_times, production)))

#print X
#exit(0)
#centers = [[1,1],[5,5],[9,10]]

# "_" is not labeled.  It is "y"
#MeanShift is accurate up to 10,000
#X, _ = make_blobs(n_samples = 200, centers = centers, cluster_std = 2)

#X,_ = [start_times[0]  end_times[0], ]
#X,_ = my_array
#convert array to nd array
#use zip function

#plt.scatter(start_times, end_times)
#plt.scatter(X[:,0], X[:,1])
#plt.scatter(X[:,0], X[:,1], X[:,2])

#plt.show()


#3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(start_times,end_times,production, c='r', marker='o')
plt.show()


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
#for i in range(len(X)):
#    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

#plt.scatter(cluster_centers[:,0], cluster_centers[:,1], marker="o", s=15, linewidths = 5, zorder=10)
#plt.show()








colors= 10*['orange','yellow','black','cyan','magenta','green']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(X)):
    ax.scatter(X[i][0],X[i][1],X[i][2], color=colors[labels[i]], marker='o')
ax.scatter(cluster_centers[:,0], cluster_centers[:,1],cluster_centers[:,2], c='r', marker='o',s=50)
plt.show()




plt.show()

