import numpy as np

rows = 3
cols = 3

goal = (2, 2)

gamma = 0.9

V = np.zeros((rows, cols))

# Goal state has value 10
V[goal] = 10

actions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]

for iteration in range(50):

    new_V = V.copy()

    for r in range(rows):
        for c in range(cols):

            if (r, c) == goal:
                continue

            values = []

            for dr, dc in actions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:

                    reward = -1
                    value = reward + gamma * V[nr][nc]

                    values.append(value)

            if values:
                new_V[r][c] = max(values)

    V = new_V


print("Optimal State Values:")
print(np.round(V, 2))


# Find optimal path
position = (0, 0)
path = [position]

while position != goal:

    r, c = position

    best_value = -float("inf")
    best_position = position

    for dr, dc in actions:

        nr = r + dr
        nc = c + dc

        if 0 <= nr < rows and 0 <= nc < cols:

            value = -1 + gamma * V[nr][nc]

            if value > best_value:
                best_value = value
                best_position = (nr, nc)

    if best_position == position:
        break

    position = best_position
    path.append(position)

print("\nOptimal Path:")
print(path)
