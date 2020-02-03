import pants
import math
import random
import matplotlib.pyplot as plt
import saveToJSON as JSON

def DisplayRoute(locations):
    locationsx = []
    locationsy = []

    for x in range(len(locations)):
        locationsx.append(locations[x][0])
        locationsy.append(locations[x][1])

    plt.title('Travelling salesman problem')

    plt.scatter(locationsx,locationsy)
    plt.plot(locationsx,locationsy)

    print("\nYou must close the graph before carrying on\n")

    plt.show()

def euclidean(a, b):
    return math.sqrt(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2))


def Run(locations, iterations, problem):
    shortestPath = []
    shortestScore = 1000000
    for x in range(iterations):
        world = pants.World(locations, euclidean)
        solver = pants.Solver()
        solution = solver.solve(world)

        print(solution.distance)

        if solution.distance < shortestScore:
            shortestScore = solution.distance
            shortestPath = []
            for x in solution.tour:
                shortestPath.append(x)
            shortestPath.append(shortestPath[0])
            JSON.WriteToFile("ACO", problem, str(solution.distance))

    DisplayRoute(shortestPath)



# https://pypi.org/project/ACO-Pants/#description
