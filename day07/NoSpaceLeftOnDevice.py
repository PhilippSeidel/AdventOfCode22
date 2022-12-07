import Command as cmd
import FileSystem as fs

input = open("input", "r").read().splitlines()

# part one
commands = []

i = 0
while i < len(input):
    lineChunks = input[i].split()
    command_name = lineChunks[1]
    if command_name == "ls":
        i += 1
        lineChunks = input[i].split()
        while lineChunks[0] != '$' and i < len(input):
            component_name = lineChunks[1]
            if lineChunks[0] == "dir":
                commands.append(cmd.CreateDirectoryCommand(component_name, 0))
            else:
                file_size = int(lineChunks[0])
                commands.append(cmd.CreateFileCommand(component_name, file_size))
            i += 1
            if i < len(input):
                lineChunks = input[i].split()
        continue

    command_param = lineChunks[2]
    commands.append(cmd.ChangeDirectoryCommand(command_param))
    i += 1

root_directory = fs.Directory('/', 0, None)
root_directory.parent = root_directory
file_system = fs.FileSystem(root_directory, root_directory)

for c in commands:
    c.execute(file_system)

file_system.update_sizes()

directories = file_system.get_all_directories()

size_count = 0
for d in directories:
    if d.size <= 100000:
        size_count += d.size

print(size_count)

# part two
total_space = 70000000
needed_space = 30000000
used_up_space = root_directory.size
space_threshold = needed_space - (total_space - used_up_space)

deletion_candidates = []
for d in directories:
    if d.size >= space_threshold:
        deletion_candidates.append(d)

deletion_candidates.sort()

print(deletion_candidates[0].size)
