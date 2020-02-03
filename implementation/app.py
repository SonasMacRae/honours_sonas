import os
import json
import math
import sys
import time

import ACOTest as ACO
import EA as ea
import NearestNeighbour as NN
import BruteForce as BF
import CreateEnvironment as createEnvironment
import OptimalTour as Optimal


class EASettings:
	def __init__(self, populationSize, numberOfGenerations, mutationRate):
		self.populationSize = populationSize
		self.numberOfGenerations = numberOfGenerations
		self.mutationRate = mutationRate


def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./20)


def Settings(settings):
	popSize = settings.populationSize
	numGens = settings.numberOfGenerations
	mutRate = settings.mutationRate

	response = ""
	while response != "0":
		os.system('cls||clear')
		choice = False

		print("Current settings")
		print("Population size = ", popSize)
		print("Number of generations = ", numGens)
		print("Mutation rate = ", mutRate, "\n")

		print("1 - Update population size")
		print("2 - Update number of generations")
		print("3 - Update mutation rate")
		print("0 - Return to main menu")

		response = input()

		if response == "1":
			print("Population size: ")
			response = int(input())
			popSize = response

		if response == "2":
			print("Update number of generations: ")
			response = int(input())
			numGens = response

		if response == "3":
			print("Update mutation rate: ")
			response = int(input())
			mutRate = response

	return EASettings(popSize,numGens,mutRate)


algorithms = ["Evolutionary algorithm","Nearest neighbour","Brute force","Ant colony optimisation"]
def PrintAlgorithms():
	for x in range(len(algorithms)):
		print(x + 1, algorithms[x])


problems = ["berlin52","eil51","kroA100","att48","bays29","gr120","pr76","kroD100","eil76","st70"]
def PrintProblems():
	for x in range(len(problems)):
		print(x + 1, problems[x])


def ChooseAlgorithm(algorithm):

	print("Algorithm in use: ", algorithms[algorithm - 1])
	print("These are the algorithms available: ")
	PrintAlgorithms()

	response = input()

	if response == "1":
		print("You have chosen evolutionary algorithm")
		return 1

	if response == "2":
		print("You have chosen the nearest neighbour algorithm")
		return 2

	if response == "3":
		print("You have chosen the brute force algorithm")
		return 3

	if response == "4":
		print("You have chosen the ant colony optimisation algorithm")
		return 4

	return algorithm


def GenerateProblem(locations):
	response = ""
	problem = ""
	while response != "0":
		os.system('cls||clear')

		print("Generate problem menu")

		print("Current number of locations = ", len(locations),"\n")

		print("1 - Choose preset problems")
		print("2 - Update number of locations")
		print("0 - Back to main menu")

		response = input()

		if response == "1":
			print("Preset problems")
			PrintProblems()
			response = input()
			if response == "1" or response == "2" or response == "3" or response == "4":
				locations = createEnvironment.PreSetProblems(response)
			problem = problems[int(response) - 1]
			continue

		if response == "2":
			print("Enter number of locations: ")
			response = input()
			locations = createEnvironment.Start(int(response))
			problem = "custom"

		temp = (locations, problem)
	return temp


# Shows the stats from the runs
def Data():
	shortAlgorithms = ["EA","NN","BF","ACO"]
	problem = ""
	print("Choose problem")
	PrintProblems()

	response = int(input())
	problem = problems[response - 1]
	os.system('cls||clear')
	with open('data.txt') as json_file:
		data = json.load(json_file)
		for x in shortAlgorithms:
			temp = x + "-" + problem
			totalScore = 0
			counter = 0
			bestScore = 1000000
			if temp in data:
				print(temp)
				for p in data[temp]:
					totalScore += float(p['score'])
					counter += 1
				if float(p['score']) < bestScore:
					bestScore = float(p['score'])
				mean = totalScore/counter
				sd = 0
				for p in data[temp]:
					sd += (mean - float(p['score'])) * (mean - float(p['score']))
				sd /= counter
				sd = math.sqrt(sd)

				print("Best score: ", bestScore)
				print("Mean score: ", mean)
				print("Standard deviation: ", sd)
		print("\n\n Press any key to continue")
		temp = input()



def MainMenu():
	algorithm = 1
	problem = "berlin52"

	locations = createEnvironment.PreSetProblems("1")
	settings = EASettings(50, 500, 5)

	response = ""
	while response != "0":
		os.system('cls||clear')

		print("Main menu")
		print("Algorithm in use: ", algorithms[algorithm -1])
		print("Problem being solved: ", problem, "\n")
		print("1 - Generate problem")
		print("2 - Choose algorithm")
		print("3 - Data")
		print("4 - Settings")
		print("5 - View optimal tour")
		print("6 - Run once")
		# need to allow the algorithm to be run x number of times
		print("7 - Run x times")

		response = input()

		print(type(response))
		os.system('cls||clear')
		if response == "1":
			temp = GenerateProblem(locations)
			locations = temp[0]
			problem = temp[1]

		if response == "2":
			algorithm = ChooseAlgorithm(algorithm)

		if response == "3":
			Data()

		if response == "4":
			settings = Settings(settings)

		if response == "5":
			Optimal.DisplayOptimalTour(problem)

		if response == "6":
			if algorithm == 1:
				ea.Start(settings, locations, 1, problem)
			if algorithm == 2:
				NN.NearestNeighbour(locations)
			if algorithm == 3:
				BF.BruteForce(locations, 1)
			if algorithm == 4:
				ACO.Run(locations, 1, problem)

		if response == "7":
			os.system('cls||clear')
			print("Enter number of iterations: ")
			iterations = int(input())
			if algorithm == 1:
				ea.Start(settings, locations, iterations, problem)
			if algorithm == 2:
				NN.NearestNeighbour(locations)
			if algorithm == 3:
				BF.BruteForce(locations)
			if algorithm == 4:
				ACO.Run(locations, iterations, problem)

		if response == "0":
			return


def App():
	MainMenu()


App()




# Things to add
# Allow the storage of routes, allow the user to name them
# Help
# Save runs to a file using JSON, then add a section that displays data about all the runs, average fitness for each
# algorithm for each benchmark problem, show the number of runs, best score etc
# add in more algorithms to this application

# t.test do that student t test

# irace for parameter tuning
