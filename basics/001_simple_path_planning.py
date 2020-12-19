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


def search():
    global grid, init, goal, cost

    x, y, g = init[0], init[1], 0

    opened_nodes = [[g, x, y]]
    closed_nodes = grid

    found = False  # Will set to true when the search is complete
    resign = False  # Will set to true if there is no more ways to expand

    while not found and not resign:

        if not opened_nodes:  # If there are no open nodes
            resign = False  # No need of doing this as we are returning
            print("Resigning. Failed to find a path")
            return None
        else:
            opened_nodes.sort()  # ascending order
            opened_nodes.reverse()  # since pop pops from the end
            next_node = opened_nodes.pop()

            g, x, y = next_node

            if x == goal[0] and y == goal[1]:
                found = True  # No need of doing this as we are returning
                print(
                    f"Successfully reached the goal x={next_node[1]}, y={next_node[2]} with Path cost of {next_node[0]}", )
                return next_node
            else:
                for current_delta in delta:
                    x2 = x + current_delta[0]
                    y2 = y + current_delta[1]

                    if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                        if closed_nodes[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            opened_nodes.append([g2, x2, y2])
                            closed_nodes[x2][y2] = 1

    return None


search()
