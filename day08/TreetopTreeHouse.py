input = open("input", "r").read().splitlines()

grid_height = len(input)
grid_width = len(input[0])


class Tree:
    def __init__(self, height):
        self.height = height
        self.is_visible = False


grid = []
for x in range(grid_width):
    tree_column = []
    for y in range(grid_height):
        tree_column.append(Tree(int(input[y][x])))
    grid.append(tree_column)

for x in range(grid_width):
    max_height_top = -1
    max_height_bottom = -1
    for y in range(grid_height):
        tree_top = grid[x][y]
        tree_bottom = grid[x][grid_height - y - 1]
        if tree_top.height > max_height_top:
            tree_top.is_visible = True
            max_height_top = tree_top.height
        if tree_bottom.height > max_height_bottom:
            tree_bottom.is_visible = True
            max_height_bottom = tree_bottom.height

for y in range(grid_height):
    max_height_left = -1
    max_height_right = -1
    for x in range(grid_width):
        tree_left = grid[x][y]
        tree_right = grid[grid_width - x - 1][y]
        if tree_left.height > max_height_left:
            tree_left.is_visible = True
            max_height_left = tree_left.height
        if tree_right.height > max_height_right:
            tree_right.is_visible = True
            max_height_right = tree_right.height


visible_count = 0
for tree_row in grid:
    for tree in tree_row:
        if tree.is_visible:
            visible_count += 1

print(visible_count)