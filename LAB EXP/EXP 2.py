# Experiment 2: Smart Home Robot Navigation using Q-Learning

import random

# Grid size
rows = 4
cols = 4

start = (0, 0)
goal = (3, 3)

actions = ["UP", "DOWN", "LEFT", "RIGHT"]

Q = {}

# Initialize Q-table
for r in range(rows):
    for c in range(cols):
        Q[(r, c)] = {action: 0 for action in actions}


def move(state, action):

    r, c = state

    if action == "UP":
        r -= 1
    elif action == "DOWN":
        r += 1
    elif action == "LEFT":
        c -= 1
    elif action == "RIGHT":
        c += 1

    # Keep robot inside grid
    r = max(0, min(rows - 1, r))
    c = max(0, min(cols - 1, c))

    return (r, c)


alpha = 0.1
gamma = 0.9
epsilon = 0.2

# Training
for episode in range(1000):

    state = start

    for step in range(50):

        # Epsilon-greedy action selection
        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = max(Q[state], key=Q[state].get)

        next_state = move(state, action)

        if next_state == goal:
            reward = 10
        else:
            reward = -1

        # Q-learning update
        best_next = max(Q[next_state].values())

        Q[state][action] = Q[state][action] + alpha * (
            reward + gamma * best_next - Q[state][action]
        )

        state = next_state

        if state == goal:
            break


# Test learned policy
state = start

print("Learned Robot Path:")
print("-------------------")

path = [state]

for step in range(20):

    if state == goal:
        break

    action = max(Q[state], key=Q[state].get)
    state = move(state, action)

    path.append(state)

print(path)
print("\nGoal Reached:", state == goal)
