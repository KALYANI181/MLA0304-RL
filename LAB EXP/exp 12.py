# Experiment 12
# Policy-Based RL for Robotic Arm

import random

states = [
    "Start",
    "Object",
    "Picked",
    "Target"
]

actions = [
    "Move",
    "Pick",
    "Place"
]

# Policy table
policy = {}

for state in states:
    policy[state] = {}

    for action in actions:
        policy[state][action] = 1 / len(actions)


def select_action(state):
    actions_list = list(policy[state].keys())
    probabilities = list(policy[state].values())

    return random.choices(
        actions_list,
        weights=probabilities
    )[0]


# Training
for episode in range(500):

    state = "Start"

    while state != "Target":

        action = select_action(state)

        if state == "Start":
            if action == "Move":
                next_state = "Object"
                reward = 1
            else:
                next_state = state
                reward = -1

        elif state == "Object":
            if action == "Pick":
                next_state = "Picked"
                reward = 5
            else:
                next_state = state
                reward = -1

        elif state == "Picked":
            if action == "Place":
                next_state = "Target"
                reward = 10
            else:
                next_state = state
                reward = -1

        state = next_state


# Display policy
print("Learned Robotic Arm Policy")
print("--------------------------")

for state in states:
    print(state, ":", policy[state])

print("\nRobot completed Pick-and-Place task.")
