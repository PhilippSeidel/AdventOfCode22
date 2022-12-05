class Round:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.score = 0
        if b == 'X':
            self.score += 1
        elif b == 'Y':
            self.score += 2
        elif b == 'Z':
            self.score += 3
        if (a == 'A' and b == 'Y') or (a == 'B' and b == 'Z') or (a == 'C' and b == 'X'):
            self.score += 6
        elif (a == 'A' and b == 'X') or (a == 'B' and b == 'Y') or (a == 'C' and b == 'Z'):
            self.score += 3

    def __str__(self):
        return str((self.a, self.b, self.score))


input = open("input", "r").read().splitlines()

# part one
rounds = []

for i in input:
    parts = i.split()
    rounds.append(Round(parts[0], parts[1]))

score = 0
for r in rounds:
    score += r.score

print(score)


# part two
decrypted_rounds = []

for i in input:
    parts = i.split()
    neededFigure = ''
    if parts[0] == 'A':
        if parts[1] == 'X':
            neededFigure = 'Z'
        elif parts[1] == 'Y':
            neededFigure = 'X'
        else:
            neededFigure = 'Y'
    if parts[0] == 'B':
        if parts[1] == 'X':
            neededFigure = 'X'
        elif parts[1] == 'Y':
            neededFigure = 'Y'
        else:
            neededFigure = 'Z'
    if parts[0] == 'C':
        if parts[1] == 'X':
            neededFigure = 'Y'
        elif parts[1] == 'Y':
            neededFigure = 'Z'
        else:
            neededFigure = 'X'

    decrypted_rounds.append(Round(parts[0], neededFigure))

score = 0
for r in decrypted_rounds:
    score += r.score

print(score)
