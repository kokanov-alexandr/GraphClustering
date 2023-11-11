import math
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getDistance(self, otherPoint):
        return math.sqrt((otherPoint.x - self.x) ** 2 + (otherPoint.y - self.y) ** 2 + (otherPoint.z - self.z) ** 2)