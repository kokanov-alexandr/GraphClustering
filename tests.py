import unittest
from Point import Point
from clustering import *

class TestPoint(unittest.TestCase):
    def testCreatePoint1(self):
        point = Point(3, 4, 5)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)
        self.assertEqual(point.z, 5)

    def testCreatePoint2(self):
        point = Point(0, 1, 0)
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 1)
        self.assertEqual(point.z, 0)

    def testDistance1(self):
        point = Point(1, 2, 3)
        distance = point.getDistance(Point(4, 5, 6))
        self.assertEqual(distance, 5.196152422706632)
    
    def testDistance2(self):
        point = Point(0, 0, 0)
        distance = point.getDistance(Point(0, 0, 0))
        self.assertEqual(distance, 0)



class TestGetDistanceMatrix(unittest.TestCase):
    def testEmptyMatrix(self):
        points = []
        result = getDistancesMatrix(points)
        self.assertEqual(result, [])

    def testOnePoint(self):
        points = [Point(1, 2, 6)]
        result = getDistancesMatrix(points)
        self.assertEqual(result, [[0]])
        
    def testTwoPoints(self):
        point1 = Point(1, 2, 3)
        point2 = Point(4, 5, 6)
        points = [point1, point2]
        result = getDistancesMatrix(points)
        self.assertEqual(result, [[0, 5.196152422706632], [5.196152422706632, 0]])

    def testSymmetricProperty(self):
        point1 = Point(1, 2, 3)
        point2 = Point(4, 5, 6)
        points = [point1, point2]
        result = getDistancesMatrix(points)
        self.assertEqual(result[0][1], result[1][0])


import unittest
from clustering import getAdjacencyMatrix

class TestGetAdjacencyMatrix(unittest.TestCase):
    def testEmptyMatrix(self):
        distMatrix = []
        maxDistance = 10
        result = getAdjacencyMatrix(distMatrix, maxDistance)
        self.assertEqual(result, [])

    def testOnePoint(self):
        distMatrix = [[0]]
        maxDistance = 10
        result = getAdjacencyMatrix(distMatrix, maxDistance)
        self.assertEqual(result, [[1]])

    def testTwoPoints(self):
        distMatrix = [
            [0, 5], 
            [5, 0]
        ]
        maxDistance = 10
        result = getAdjacencyMatrix(distMatrix, maxDistance)
        self.assertEqual(result, [[1, 1], [1, 1]])

    def testTwoPointsBeyondMaxDist(self):
        distMatrix = [
            [0, 15], 
            [15, 0]
        ]
        maxDistance = 10
        result = getAdjacencyMatrix(distMatrix, maxDistance)
        self.assertEqual(result, [[1, 0], [0, 1]])

    def testSymmetricProperty(self):
        distMatrix = [
            [0, 5, 10], 
            [5, 0, 15], 
            [10, 15, 0]
        ]
        maxDistance = 10
        result = getAdjacencyMatrix(distMatrix, maxDistance)
        self.assertEqual(result, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])



class TestClustering(unittest.TestCase):
    def testEmptyMatrix(self):
        result = getClusters([])
        self.assertEqual(result, [])

    def testOnePoint(self):
        points = [Point(1, 2, 6)]
        result = getClusters(points)
        self.assertEqual(result, [[0]])

    def testFarPoint(self):
        points = [Point(1, 2, 6), Point(1, 2, 6.1), Point(7, 8, 9)]
        answer = [[0, 1], [2]]
        result = getClusters(points)
        for i in result:
            i.sort()
        self.assertEqual(result, answer)

    def testDistantPoints(self):
        points = [Point(1, 1, 1), Point(4, 4, 4), Point(7, 7, 7)]
        answer = [[0], [1], [2]]
        result = getClusters(points)
        for i in result:
            i.sort()
        self.assertEqual(result, answer)

    def testTwoClusters(self):
        points = [Point(1, 1, 1), Point(1, 1, 1.5), Point(1, 1, 2), Point(10, 10, 10), Point(10, 10, 10.5), Point(10, 10, 10.5)]
        answer = [[0, 1, 2], [3, 4, 5]]
        result = getClusters(points)
        for i in result:
            i.sort()
        self.assertEqual(result, answer)



unittest.main()
