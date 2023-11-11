import random
import matplotlib.pyplot as plt
from Point import Point
from tests import *

endCoords = 10 ** 4

def genaratePoints(countPoinst):
    points = []
    for _ in range(countPoinst):
        points.append(Point(random.randint(0, endCoords), random.randint(0, endCoords), random.randint(0, endCoords)))
    return points


def showPoints(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = [point.x for point in points]
    y = [point.y for point in points]
    z = [point.z for point in points]

    ax.scatter(x, y, z, c = "red", alpha=1.0)

    plt.show()


unittest.main()



