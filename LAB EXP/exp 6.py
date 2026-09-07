# Experiment 6: Robot Navigation using Q-Learning

import random

# Grid size
size = 5

start = (0, 0)
goal = (4, 4)

actions = ["UP", "DOWN", "LEFT", "RIGHT"]

# Q-table
Q = {}

for i in range(size):
    for j in range(size):
        Q[(i, j)] = {a: 0 for a in actions}


def move(state, action):
    x, y = state

    if action == "UP":
        x -= 1
    elif action == "DOWN":
        x += 1
    elif action == "LEFT":
        y -= 1
    elif action == "RIGHT":
        y += 1

    x = max(0, min(size - 1, x))
    y = max(0, min(size - 1, y))

    return (x, y)


alpha = 0.1
gamma = 0.9
epsilon = 0.2

# Training
for episode in range(1000):

    state = start

    for step in range(100):

        # Epsilon-greedy selection
        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = max(Q[state], key=Q[state].get)

        next_state = move(state, action)

        if next_state == goal:
            reward = 10
        else:
            reward = -1

        best_next = max(Q[next_state].values())

        Q[state][action] += alpha * (
            reward + gamma * best_next - Q[state][action]
        )

        state = next_state

        if state == goal:
            break


# Testing
state = start
path = [state]

for step in range(30):

    if state == goal:
        break

    action = max(Q[state], key=Q[state].get)

    state = move(state, action)

    path.append(state)


print("Robot Navigation Path:")
print(path)

print("\nGoal Reached:", state == goal)
