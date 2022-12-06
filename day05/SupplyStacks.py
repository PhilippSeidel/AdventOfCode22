import re


input = open("input", "r").read().splitlines()


# part one
def execute_instruction(instruction, stacks):
    crate = stacks[instruction.take].pop()
    stacks[instruction.put].append(crate)
    return stacks


def construct_stacks(start_configuration_lines):
    start_configuration_lines.reverse()
    line_length = len(start_configuration_lines[0])
    stacks = []
    for i in range(0, line_length, 4):
        stacks.append([])
        for l in start_configuration_lines:
            if l[i + 1] != " ":
                stacks[len(stacks) - 1].append(l[i + 1])
    return stacks


def construct_instructions(instruction_lines):
    instructions = []
    for i in instruction_lines:
        m = re.findall('\d+', i)
        for i in range(int(m[0])):
            instructions.append(Instruction(int(m[1]) - 1, int(m[2]) - 1))
    return instructions

class Instruction:
    def __init__(self, take, put):
        self.take = take
        self.put = put


start_configuration_lines = []
instruction_lines = []
for i in range(len(input)):
    if input[i] == "":
        start_configuration_lines = input[:(i - 1)]
        instruction_lines = input[(i + 1):]
        break

stacks = construct_stacks(start_configuration_lines)
instructions = construct_instructions(instruction_lines)

for i in instructions:
    execute_instruction(i, stacks)

uppermost_crates = ""
for s in stacks:
    uppermost_crates += s[len(s) - 1]

print(uppermost_crates)