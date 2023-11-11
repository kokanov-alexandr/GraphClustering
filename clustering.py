from Point import Point
from scipy.spatial import distance
import math

def getDistancesMatrix(points):
    n = len(points)
    matrix = [[0 for j in range(n)] for i in range(n)]
    
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = points[i].getDistance(points[j])
    return matrix


def getAdjacencyMatrix(distMatrix, maxDistance):
    n = len(distMatrix)
    matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if distMatrix[i][j] < maxDistance:
               matrix[i][j] = 1 
    return matrix

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(round(matrix[i][j], 2), end=" ")
        print()


def getThresholdDistance(distMatrix):
    s = 0
    for i in distMatrix:
        for j in i:
            s += j
    s /= len(distMatrix) ** 2
    return s * 0.3

def getClusters(points):
    distanceMatrix = getDistancesMatrix(points)
    adjacencyMatrix = getAdjacencyMatrix(distanceMatrix, getThresholdDistance(distanceMatrix))

    clusters = []

    for i in range(len(points)):
        connectClusters = []
        for cluster in clusters:
            for p in cluster:
                if adjacencyMatrix[p][i]:
                    connectClusters.append(cluster)
                    break
        
        if not connectClusters:
            clusters.append([i])

        else:
            mergedClaster = [i]
            for cluster in connectClusters:
                mergedClaster.extend(cluster)
                clusters.remove(cluster)
            clusters.append(mergedClaster)
    return clusters