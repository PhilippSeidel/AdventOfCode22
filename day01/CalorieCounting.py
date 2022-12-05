input = open("input1", "r").read().splitlines()

splitIndices = [0]
for i in range(len(input)):
    if input[i] == "":
        splitIndices.append(i)
splitIndices.append(len(input))

inventories = []
for i in range(len(splitIndices) - 1):
    inventories.append(input[splitIndices[i] + 1:splitIndices[i + 1]])

calories = []
for i in inventories:
    calories.append(sum(map(int, i)))

print(max(calories))
