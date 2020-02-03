import matplotlib.pyplot as plt

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
