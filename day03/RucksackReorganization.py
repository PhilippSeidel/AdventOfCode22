
class Rucksack:
    def __init__(self, first_compartment, second_compartment):
        self.first_compartment = first_compartment
        self.second_compartment = second_compartment


def get_overlap(s1, s2):
    overlap = ""
    for i in range(len(s1)):
        if (s1[i] in s2) and (s1[i] not in overlap):
            overlap += s1[i]
    return overlap


def get_priority(c):
    if ord('a') <= ord(c) <= ord('z'):
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


input = open("input", "r").read().splitlines()


# part one
rucksacks = []
for i in input:
    slice_index = int(len(i) / 2)
    rucksacks.append(Rucksack(i[:slice_index], i[slice_index:]))

priority_sum = 0
for r in rucksacks:
    priority_sum += get_priority(get_overlap(r.first_compartment, r.second_compartment))

print(priority_sum)


# part two
class Group:
    def __init__(self, inv1, inv2, inv3):
        self.inv1 = inv1
        self.inv2 = inv2
        self.inv3 = inv3


groups = []
for i in range(0, len(input), 3):
    groups.append(Group(input[i], input[i + 1], input[i + 2]))

priority_sum = 0
for g in groups:
    priority_sum += get_priority(get_overlap(g.inv1, get_overlap(g.inv2, g.inv3)))

print(priority_sum)