# Inspired by Self-Driving-Car Nano Degree from Udacity

# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]

goal = [len(grid) - 1, len(grid[0]) - 1]

cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def value_function():
    # value = [[99 if i == 1 else 0 for i in range(len(grid[0]))] for j in range(len(grid))]
    value = [[99 for i in range(len(grid[0]))] for j in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):

                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        change = True  # No need of doing this as we are returning

                        # return value

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:

                            v2 = value[x2][y2] + cost
                            # print("\t", v2, "value[x][y]=", value[x][y])
                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2

    return value


value_ = value_function()

for v in value_:
    print(v)
