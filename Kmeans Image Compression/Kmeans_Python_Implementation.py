import numpy as np; 
import matplotlib.pyplot as plt; 


def __init__(self) -> None:
    pass

'''Calculates the nearest centroid to each of the data points'''
def nearestCentroid(X,centroids):
    K = centroids.shape[0]; #numpy array, each centroid should have m axes
    axes = X.shape[1]; #the number of axes per data point
    n = X.shape[0]; #the total number of datapoints

    nearestIndex = np.zeros(X.shape[0],dtype=int); 

    for i in range(n):
        mindex = 0; minVal = np.linalg.norm(X[i] - centroids[0]);
        for j in range(1,K):
            curSum = np.linalg.norm(X[i] - centroids[j]); 
            if(curSum < minVal):
                minVal = curSum;
                mindex = j;
        nearestIndex[i] = mindex;
    
    return nearestIndex; 

'''Places the Centroids at the mean position of their group'''
def recomputeCentroids(X, indices, K):
    centroids = np.zeros((K,X.shape[1])); 
    for i in range(K):
        group = X[indices == i];
        if(len(group) != 0):
            centroids[i] = np.mean(group,axis=0); 
        # else:
        #     #randomly place this node somewhere
        #     centroids[i] = centroids[i]; 

    
    return centroids; 

'''initializes the centroids based on random positions of the X data'''
def initializeCentroids(X,K):
    ind = np.random.permutation(X.shape[0]); 
    centroids = X[ind[:K]]; #the first K of the random positions

    return centroids;

'''Runs the algorithm once'''
def runKmeansAlgorithm(X, initial_centroids, total_iterations = 10):
    m,n = X.shape;
    K = initial_centroids.shape[0]; #the initial_centroids would be calculated randomly and multiple times to get the optimal case
    centroids = initial_centroids;
    prev_centroids = centroids;
    indices = np.zeros(m); 

    for i in range(total_iterations):
        #can print the progress here to get information on how the algorithm is doing
        print("iteration- %d/%d" % (i, total_iterations-1))
        indices = nearestCentroid(X,centroids); #resetting the indices to their nearest centroids
        centroids = recomputeCentroids(X,indices,K); #resetting the centroids to the respective mean positions
    return centroids,indices;

'''tries out multiple different starting conditions to get the optimal case'''
def MultipleRandomStarts(X, K,trials = 10,total_iterations = 10,initial_centroids = None):
    
    currentLowestCentroids = (0,0); 
    curLowestCost = -1;  

    for i in range(trials):
        #for each such trial, we will compute the 
        initial_centroids = initializeCentroids(X,K);
        centroids,indices =  runKmeansAlgorithm(X,initial_centroids,total_iterations); 
        #now we shall calculate the cost
        if(curLowestCost == -1):
            currentLowestCentroids = (centroids,indices);
        else:
            currentCost = 0; 
            for i in X:
                currentCost += np.linalg.norm(X[i] - centroids[indices[i]]); #computes the norm with the nearest centroid
            if(currentCost < curLowestCost):
                currentLowestCentroids = (centroids,indices); 
                curLowestCost = currentCost; 
    
    return currentLowestCentroids[0], currentLowestCentroids[1];

    
