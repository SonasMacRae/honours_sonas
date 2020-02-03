from itertools import permutations
import RouteScore
import matplotlib.pyplot as plt

# Brute force way of getting best path
def BruteForce(locations):
    # Gets all the path combinations
    p = permutations(locations)
    p = list(p)
    smallestIndex = 0
    smallestDistance = 999999

    counter = 0
    # Go through all the paths
    for x in p:
        x = list(x)
        x.append(x[0])
        if counter % 1000 == 0:
            print("%.2f%% complete" %(counter/len(p)*100),  end='\r')
        # gets the path distance
        tempDistance = RouteScore.TotalDistance(x)
        # if this path is shorter than previous best, remember this
        if smallestDistance > tempDistance:
            smallestDistance = tempDistance
            smallestIndex = counter
        counter += 1

    path = []
    for x in p[smallestIndex]:
        path.append(x)
    path.append(p[smallestIndex][0])

    # prints smallest distance found
    print(path, " is the path, the distance is ", smallestDistance)
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
