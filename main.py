import random
import matplotlib.pyplot as plt
from Point import Point
from tests import *

import matplotlib.lines as mlines
import matplotlib.pyplot as plt

endCoords = 10 ** 4 * 2

def genaratePoints(countPoints):
    m = random.uniform(0.2, 2.0)
    b = random.uniform(0, endCoords)
    points = []

    for _ in range(countPoints // 2):
        x = random.uniform(0, endCoords)
        y = m * x + b + random.uniform(-4000, 3500)
        points.append(Point(x, y, random.randint(1500, 2500)))

    for _ in range(countPoints // 2):
        x = random.uniform(6000, endCoords - 6000)
        y = m * x + b + random.uniform(-1000, 1000)
        points.append(Point(x, y, random.randint(2000, 2500)))
    return points

def showPoints(points):
    clusters = getClusters(points)
    largestClaster = max(clusters, key = len)
    clusters.remove(largestClaster)

    countRed = len(largestClaster)
    countBlue = len(points) - countRed
    colors = ["red"] * countRed + ["blue"] * countBlue

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

    coords = [0, 5000, 10000, 15000, 20000]
    ax.set_xticks(coords)
    ax.set_yticks(coords)
    ax.set_zticks(coords)

    redBall = mlines.Line2D([], [], color='red', marker='o', linestyle='None',
                            markersize=5, label='Самый крупный кластер')
    
    blueBall = mlines.Line2D([], [], color='blue', marker='o', linestyle='None',
                            markersize=5, label='Остальные точки')
    

    plt.legend(handles=[redBall, blueBall], bbox_to_anchor=(1.3, 1.1))

    ax.scatter(x, y, z, c = colors, alpha=1.0, s = 5)
    ax.view_init(elev=40, azim=120)

    plt.show()




points = genaratePoints(100)
showPoints(points)

