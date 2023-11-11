import random
import matplotlib.pyplot as plt
from Point import Point

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

    ax.scatter(x, y, z)

    plt.show()

points = genaratePoints(100)
showPoints(points)



