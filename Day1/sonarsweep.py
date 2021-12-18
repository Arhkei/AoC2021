with open("input.txt") as f:
    data = list(map(int,f.readlines()))

def increaseFinder(dataset):

    previousDepth = dataset[0]
    increase = 0

    for depth in dataset:
        if depth > previousDepth:
            increase += 1
        previousDepth = depth

    return increase

answer1 = increaseFinder(data)

print(f"Increases: {answer1}")

sumData = []

for x in range(len(data)):
    if x < len(data) - 2:
        sumData += [data[x] + data[x+1] + data[x+2]]

answer2 = increaseFinder(sumData)

print(f"Sum Increases: {answer2}")
