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


class TestClustering(unittest.TestCase):
    def testClustering1(self):
        points = [Point(1, 2, 6), Point(1, 3, 6), Point(7, 8, 9)]
        answer = [[0, 1], [2]]
        result = getClusters(points)
        for i in result:
            i.sort()
        self.assertEqual(result, answer)

    def testClustering2(self):
        points = [Point(1, 1, 1), Point(4, 4, 4), Point(7, 7, 7)]
        answer = [[0], [1], [2]]
        result = getClusters(points)
        for i in result:
            i.sort()
        self.assertEqual(result, answer)


