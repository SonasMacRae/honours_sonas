import math

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
