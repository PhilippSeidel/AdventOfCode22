import re


def complete_overlap(first_left, first_right, second_left, second_right):
    return (first_left <= second_left and second_right <= first_right) \
           or (second_left <= first_left and first_right <= second_right)


input = open("input", "r").read().splitlines()

# part one
pairs = []
for i in input:
    m = re.findall('\d+', i)
    pair = [[int(m[0]), int(m[1])], [int(m[2]), int(m[3])]]
    pairs.append(pair)

count = 0
for p in pairs:
    if complete_overlap(p[0][0], p[0][1], p[1][0], p[1][1]):
        count += 1

print(count)

# part two
count = 0
for p in pairs:
    if (p[0][0] <= p[1][0] <= p[0][1] <= p[1][1]) or (p[1][0] <= p[0][0] <= p[1][1] <= p[0][1]):
        count += 1
    elif complete_overlap(p[0][0], p[0][1], p[1][0], p[1][1]):
        count += 1

print(count)
