import random
import math
import matplotlib.pyplot as plt
import saveToJSON as JSON
from operator import itemgetter
import DisplayRoute as Display


# Creates the initial population by creating random routes
def CreateRoutes(populationSize, locations):
	numberOfLocations = len(locations)
	routes = []

	for x in range(populationSize):
		tempLocations = []

		for y in locations:
			tempLocations.append(y)

		currentRoute = []

		for z in range(numberOfLocations):
			temp = tempLocations[random.randint(0, len(tempLocations)-1)]

			currentRoute.append(temp)
			tempLocations.remove(temp)

		routes.append(currentRoute)

	return routes


# Initialises the population
def Init(populationSize, locations):
	routes = CreateRoutes(populationSize, locations)
	return routes


def Distance(a, b):
    tempA = (a[0] - b[0]) ** 2
    tempB = (a[1] - b[1]) ** 2
    return math.sqrt(tempA + tempB)


def TotalDistance(inputList):
	total = 0
	for x in range(len(inputList) - 1):
		total += Distance(inputList[x], inputList[x + 1])
	total += Distance(inputList[len(inputList) - 1], inputList[0])
	return total


# Evaluates the routes, gives them a score based on their efficiency
def Evaluation(routes):
	if type(routes) is dict:
		for (x,y) in routes.items():
			temp = (TotalDistance(y[1]), y[1])
			routes[x] = temp
		return routes

	counter = 0
	routeDictionary = {}

	for x in routes:
		tempTuple = (TotalDistance(x),x)
		routeDictionary[counter] = tempTuple
		counter += 1

	return routeDictionary


def CrossOver(routes, mutationRate):
	length = 0

	populationTargetSize = len(routes) * 1.5
	currentPopulationSize = len(routes)

	tempRouteDict = {}
	offspring = []

	# Lower route lengths are better: 1/route makes the shorter
	# routes have a higher score (needed for this stage)
	for (x,y) in routes.items():
		temp = (1/y[0],y[1])
		tempRouteDict[x] = temp

	while currentPopulationSize < populationTargetSize:

		probabilities = []
		keys = []
		chosenKeys = []

		for (x,y) in tempRouteDict.items():
			probabilities.append(y[0])
			keys.append(x)

		totalProbability = sum(probabilities)
		for a in range(len(probabilities)):
			probabilities[a] = ((probabilities[a]/totalProbability) * 100)

		chosenKeys.append(random.choices(keys, probabilities, k=1))

		temp = (random.choices(keys, probabilities, k=1))
		while temp == chosenKeys[0][0]:
			temp = (random.choices(keys, probabilities, k=1))
		chosenKeys.append(temp)

		parent1 = routes.get(chosenKeys[0][0])[1]
		parent2 = routes.get(chosenKeys[1][0])[1]

		crossOverPoint = random.randint(1, len(parent1) - 1)
		child1,child2 = [],[]

		child1 = parent1[0:crossOverPoint]
		for x in parent2:
			if x not in child1:
				child1.append(x)

		child2 = parent2[0:crossOverPoint]
		for x in parent1:
			if x not in child2:
				child2.append(x)

		offspring.append(child1)
		offspring.append(child2)

		currentPopulationSize += 2

	toBeEvaluated = []
	for (x,y) in routes.items():
		toBeEvaluated.append(y[1])
	for x in Mutation(offspring, mutationRate):
		toBeEvaluated.append(x)

	return Evaluation(toBeEvaluated)


# this needs to be fixed
def Mutation(routes, probability):
	for y in range(len(routes)):
		x = routes[y]

		if random.randint(0,100) <= probability:
			mutationPoint = random.randint(0, len(x) - 1)
			mutationPoint2 = random.randint(0, len(x) - 1)

			temp = x[mutationPoint]
			x[mutationPoint] = x[mutationPoint2]
			x[mutationPoint2] = temp

		routes[y] = x
	return routes


def Selection(routes, populationSize):
	output = {}
	for (x,y) in sorted(routes.items(), key=itemgetter(1)):
		if len(output) < populationSize:
			output[x] = y
	return output





def Start(settings, locations, iterations, problem):
	shortestScore = 10000000
	shortestRoute = []
	scores = []

	for s in range(iterations):
		currentShortestScore = 10000000
		populationSize = settings.populationSize
		numberOfGenerations = settings.numberOfGenerations
		mutationRate = settings.mutationRate

		initialRoutes = Init(populationSize, locations)
		routes = Evaluation(initialRoutes)

		for k in range(numberOfGenerations):
			routes = CrossOver(routes, mutationRate)
			routes = Selection(routes, populationSize)
			routes = Evaluation(routes)

			totalDistance = 0
			for (x,y) in routes.items():
				totalDistance += TotalDistance(y[1])
				if TotalDistance(y[1]) < currentShortestScore:
					currentShortestScore = TotalDistance(y[1])
				if TotalDistance(y[1]) < shortestScore:
					shortestScore = TotalDistance(y[1])
					shortestRoute = y[1]

			print("Generation ", k)
			print("Mean score of generation: ",totalDistance/len(routes),"\n best score of this generation: ",currentShortestScore)
			print("best route found across all runs: ",shortestScore)
			print("\n")

		JSON.WriteToFile("EA", problem, str(currentShortestScore))
		scores.append(currentShortestScore)

	# Standard deviation stuff
	if iterations > 1:
		sd = 0
		mean = sum(scores) / len(scores)
		for p in scores:
			sd += (mean - p) * (mean - p)
		sd /= len(scores)
		sd = math.sqrt(sd)
		print("Mean score across runs: ", mean)
		print("Standard deviation: ", sd)
	print("Shortest path found: ", shortestScore)

	shortestRoute.append(shortestRoute[0])
	Display.DisplayRoute(shortestRoute)
