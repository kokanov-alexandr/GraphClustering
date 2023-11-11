import random
import matplotlib.pyplot as plt
from Point import Point
from tests import *

import matplotlib.lines as mlines
import matplotlib.pyplot as plt

endCoords = 10 ** 4

def genaratePoints(countPoinst):
    points = []
    for _ in range(countPoinst):
        points.append(Point(random.randint(0, endCoords), random.randint(0, endCoords), random.randint(0, endCoords)))
    return points


def showPoints(points):
    clusters = getClusters(points)
    largestClaster = max(clusters, key = len)
    clusters.remove(largestClaster)

    countRed = len(largestClaster)
    countBlue = len(points) - countRed
    colors = ["red"] * countRed + ["blue"] * countBlue

    print(largestClaster)
    fig = plt.figure()  
    ax = fig.add_subplot(111, projection='3d')

    x = [points[i].x for i in largestClaster]
    y = [points[i].y for i in largestClaster]
    z = [points[i].z for i in largestClaster]
    
    for c in clusters:
        for j in c:
            x.append(points[j].x)
            y.append(points[j].y)
            z.append(points[j].z)

    coords = [0, 3000, 6000, 9000]
    ax.set_xticks(coords)
    ax.set_yticks(coords)
    ax.set_zticks(coords)

    redBall = mlines.Line2D([], [], color='red', marker='o', linestyle='None',
                            markersize=5, label='Самый крупный кластер')
    
    blueBall = mlines.Line2D([], [], color='blue', marker='o', linestyle='None',
                            markersize=5, label='Остальные точки')
    

    plt.legend(handles=[redBall, blueBall], bbox_to_anchor=(1.3, 1.1))

    ax.scatter(x, y, z, c = colors, alpha=1.0)
    ax.view_init(elev=40, azim=30)  # Например, повернуть по оси Z на 30 градусов

    plt.show()



points = genaratePoints(50)
showPoints(points)

unittest.main()



