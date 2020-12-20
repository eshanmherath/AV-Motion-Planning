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

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]

goal = [len(grid) - 1, len(grid[0]) - 1]

cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search():
    global grid, init, goal, cost, heuristic

    x, y, g = init[0], init[1], 0
    h = heuristic[x][y]
    f = g + h

    opened_nodes = [[f, g, h, x, y]]
    closed_nodes = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    closed_nodes[x][y] = 1

    expansions = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]

    # To memorize which action was taken to get there
    actions = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]

    policy = [[' ' for i in range(len(grid[0]))] for j in range(len(grid))]
    policy[len(grid) - 1][len(grid[0]) - 1] = "*"

    found = False  # Will set to true when the search is complete
    resign = False  # Will set to true if there is no more ways to expand
    count = 0

    while not found and not resign:
        if not opened_nodes:  # If there are no open nodes
            resign = False  # No need of doing this as we are returning
            print("Resigning. Failed to find a path")
            return None
        else:
            opened_nodes.sort()  # ascending order
            opened_nodes.reverse()  # since pop pops from the end
            next_node = opened_nodes.pop()

            f, g, h, x, y = next_node

            expansions[x][y] = count
            count += 1

            if x == goal[0] and y == goal[1]:
                found = True  # No need of doing this as we are returning

                x_now, y_now = goal

                while x_now != init[0] or y_now != init[1]:
                    x2 = x_now - delta[actions[x_now][y_now]][0]
                    y2 = y_now - delta[actions[x_now][y_now]][1]

                    policy[x2][y2] = delta_name[actions[x_now][y_now]]
                    x_now = x2
                    y_now = y2

                for p in policy:
                    print(p)

                print(
                    f"Successfully reached the goal x={next_node[3]}, y={next_node[4]} with Path cost of {next_node[1]}", )
                return next_node
            else:
                for i, current_delta in enumerate(delta):
                    x2 = x + current_delta[0]
                    y2 = y + current_delta[1]

                    if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                        if closed_nodes[x2][y2] == 0 and grid[x2][y2] == 0:
                            h2 = heuristic[x2][y2]
                            g2 = g + cost
                            f2 = g2 + h2
                            opened_nodes.append([f2, g2, h2, x2, y2])
                            closed_nodes[x2][y2] = 1
                            actions[x2][y2] = i

    return None


search()
