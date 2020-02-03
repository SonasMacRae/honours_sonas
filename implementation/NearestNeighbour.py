import matplotlib.pyplot as plt
import copy
import RouteScore


def NearestNeighbour(locations):
    shortDistance = 100000
    path = []
    counter = 0
    for x in locations:
        tempPath = []
        tempLocations = copy.deepcopy(locations)
        currentLocation = x
        tempLocations.remove(currentLocation)
        tempPath.append(x)
        totalDistance = 0

        while tempLocations:
            tempNearestNeighbour = currentLocation
            tempShortestDistance = 10000

            for x in tempLocations:
                if RouteScore.Distance(x, currentLocation) < tempShortestDistance and RouteScore.Distance(x, currentLocation) != 0:
                    tempShortestDistance = RouteScore.Distance(x, currentLocation)
                    tempNearestNeighbour = x
            currentLocation = tempNearestNeighbour
            tempLocations.remove(currentLocation)
            tempPath.append(currentLocation)
            totalDistance += tempShortestDistance

            if len(tempLocations) == 0:
                tempPath.append(tempPath[0])
                totalDistance += RouteScore.Distance(tempPath[len(tempPath) - 1], tempPath[len(tempPath) - 2])

        if totalDistance < shortDistance:
            shortDistance = totalDistance
            path = tempPath

    print("the total distance is ", shortDistance, " path is ",path)
    DisplayRoute(path)


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
