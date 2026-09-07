# Experiment 8: Monte Carlo Control
# Robot Vacuum Cleaner

import random

states = ["A", "B", "C"]

actions = ["LEFT", "RIGHT"]

Q = {}
returns = {}

for state in states:
    Q[state] = {}

    for action in actions:
        Q[state][action] = 0
        returns[(state, action)] = []


def next_state(state, action):

    if state == "A":
        if action == "RIGHT":
            return "B"
        else:
            return "A"

    if state == "B":
        if action == "RIGHT":
            return "C"
        else:
            return "A"

    if state == "C":
        if action == "LEFT":
            return "B"
        else:
            return "C"


# Training
for episode in range(500):

    state = "A"

    episode_data = []

    for step in range(10):

        action = random.choice(actions)

        new_state = next_state(state, action)

        # Reward
        if new_state == "C":
            reward = 10
        else:
            reward = -1

        episode_data.append(
            (state, action, reward)
        )

        state = new_state

        if state == "C":
            break

    # Calculate returns
    G = 0

    for state, action, reward in reversed(episode_data):

        G = reward + 0.9 * G

        returns[(state, action)].append(G)

        Q[state][action] = sum(
            returns[(state, action)]
        ) / len(returns[(state, action)])


# Display learned values
print("Learned Q Values")
print("----------------")

for state in states:
    print(state, Q[state])


print("\nBest Policy")

for state in states:

    best_action = max(
        Q[state],
        key=Q[state].get
    )

    print(state, "->", best_action)
