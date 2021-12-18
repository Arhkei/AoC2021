with open("input.txt") as f:
    data = list(map(str.split,f.readlines()))
    for position in data:
        position[1] = int(position[1])

def distanceFinder(isAiming=False):

    depth = 0
    distance = 0
    aim = 0

    for direction, value in data:
        if direction == "forward":
            distance += value
            if isAiming:
                depth += value * aim
        elif direction == "down":
            if isAiming:
                aim += value
            else:
                depth += value
        elif direction == "up":
            if isAiming:
                aim -= value
            else:
                depth -= value

    return distance*depth

answer1 = distanceFinder()
answer2 = distanceFinder(isAiming=True)

print(f"Multiplied distance: {answer1}")
print(f"Multiplied distanc with aim: {answer2}")
