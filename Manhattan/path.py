with open("data.txt", "r") as file:
    initial_state = [list(map(int, line.split())) for line in file]

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def manhattan_distance(state):
    total = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                value = state[i][j]
                goal_i = (value - 1) // 3
                goal_j = (value - 1) % 3
                total += abs(i - goal_i) + abs(j - goal_j)
    return total

def copy_state(state):
    return [row[:] for row in state]

def is_goal(state):
    return state == goal_state

def a_star(initial_state):
    queue = [(manhattan_distance(initial_state), 0, initial_state, [initial_state])]
    visited = {tuple(map(tuple, initial_state))}
    while queue:
        queue.sort()
        _, cost, state, path = queue.pop(0)
        if is_goal(state):
            return path
        x, y = find_zero(state)
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = copy_state(state)
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                state_tuple = tuple(map(tuple, new_state))
                if state_tuple not in visited:
                    visited.add(state_tuple)
                    new_cost = cost + 1
                    new_f = new_cost + manhattan_distance(new_state)
                    queue.append((new_f, new_cost, new_state, path + [new_state]))
    return None

path = a_star(initial_state)

if path:
    print("Solution found:")
    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in state:
            print(" ".join(map(str, row)))
        print()
    print(f"Total steps: {len(path) - 1}")
else:
    print("No solution found.")