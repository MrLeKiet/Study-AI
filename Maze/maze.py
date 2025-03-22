maze = []
with open("maze1.txt", "r") as file:
    for line in file:
        row = list(line.strip())
        maze.append(row)

rows = len(maze)
if rows == 0:
    print("Error: Maze file is empty.")
    exit(1)

cols = len(maze[0])
for i in range(rows):
    if len(maze[i]) != cols:
        print(f"Error: Row {i+1} has {len(maze[i])} columns, expected {cols}.")
        exit(1)

start = None
end = None
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == "A":
            start = (i, j)
        elif maze[i][j] == "B":
            end = (i, j)

if not start or not end:
    print("Error: Start ('A') or End ('B') not found in maze.")
    exit(1)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] != "#"

def bfs(start, end):
    queue = [(start, [start])]
    visited = {start}
    while queue:
        (x, y), path = queue.pop(0)
        if (x, y) == end:
            return path
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if is_valid(next_x, next_y) and (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                queue.append(((next_x, next_y), path + [(next_x, next_y)]))
    return None

path = bfs(start, end)

if path:
    print("Path found:")
    for i in range(rows):
        for j in range(cols):
            if (i, j) in path:
                print("*", end="")
            else:
                print(maze[i][j], end="")
        print()
    print(f"Path length: {len(path)}")
else:
    print("No path found.")