# Experiment 22
# Q-Learning Grid Game

import random

size = 4

start = (0, 0)
goal = (3, 3)
ghost = (1, 1)

actions = [
    "UP",
    "DOWN",
    "LEFT",
    "RIGHT"
]

Q = {}

for i in range(size):
    for j in range(size):
        Q[(i, j)] = {
            action: 0
            for action in actions
        }


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

    for step in range(50):

        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = max(
                Q[state],
                key=Q[state].get
            )

        next_state = move(
            state,
            action
        )

        if next_state == goal:
            reward = 10

        elif next_state == ghost:
            reward = -10

        else:
            reward = -1

        best_next = max(
            Q[next_state].values()
        )

        Q[state][action] += alpha * (
            reward
            + gamma * best_next
            - Q[state][action]
        )

        state = next_state

        if state == goal:
            break


# Test
state = start
path = [state]

for step in range(30):

    if state == goal:
        break

    action = max(
        Q[state],
        key=Q[state].get
    )

    state = move(
        state,
        action
    )

    path.append(state)


print("Game Agent Path")
print("----------------")

print(path)

print("\nGoal Reached:",
      state == goal)
