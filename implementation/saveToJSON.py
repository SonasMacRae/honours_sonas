import json


def ReadFromFile(algorithm, problem):
    with open('data.txt') as json_file:
        data = json.load(json_file)
        totalScore = 0
        counter = 0
        bestScore = 1000000
        for p in data[str(algorithm + "-" + problem)]:
            totalScore += int(p['score'])
            counter += 1
            if int(p['score']) < bestScore:
                bestScore = int(p['score'])
        print("Best score", bestScore)
        print("Mean score", totalScore/counter)


# Need to update the best score
def WriteToFile(algorithm, problem, score):
    with open('data.txt') as json_file:
        data = json.load(json_file)
        if str(algorithm + "-" + problem) not in data:
            data[str(algorithm + "-" + problem)] = []
            data[str(algorithm + "-" + problem)].append({
                'score': score
            })
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)
            return
        data[str(algorithm + "-" + problem)].append({
            'score': score
        })
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)

'''
data = {}

data['ACO-eil51'] = []
data['ACO-eil51'].append({
    'score': '1',
})
data['ACO-eil51'].append({
    'score': '2',
})
data['ACO-eil51'].append({
    'score': '3',
})
data['ACO-eil51'].append({
    'score': '4',
})

data['ACO-berlin52'] = []
data['ACO-berlin52'].append({
    'score': '123',
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
with open('data.txt') as json_file:
    data = json.load(json_file)
    scores = ["123","345","321789","234"]
    for x in range(len(scores)):
        data['ACO-eil51'].append({
            'score': scores[x]
        })
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

WriteToFile("ACO", "eil52", "100")
WriteToFile("ACO", "eil52", "150")
WriteToFile("ACO", "eil52", "200")

ReadFromFile("ACO", "berlin52")'''
