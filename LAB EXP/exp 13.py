# Experiment 13
# REINFORCE for Autonomous Parking

import random

states = [
    "Far",
    "Near",
    "Aligned",
    "Parked"
]

actions = [
    "Forward",
    "Backward",
    "Left",
    "Right"
]

# Policy probabilities
policy = {}

for state in states:
    policy[state] = {
        action: 0.25
        for action in actions
    }


def choose_action(state):

    return random.choices(
        actions,
        weights=list(policy[state].values())
    )[0]


# Training
for episode in range(1000):

    state = "Far"
    episode_data = []

    for step in range(20):

        action = choose_action(state)

        if state == "Far":

            if action == "Forward":
                next_state = "Near"
                reward = 2
            else:
                next_state = "Far"
                reward = -1

        elif state == "Near":

            if action == "Forward":
                next_state = "Aligned"
                reward = 3
            else:
                next_state = "Near"
                reward = -1

        elif state == "Aligned":

            if action == "Backward":
                next_state = "Parked"
                reward = 10
            else:
                next_state = "Aligned"
                reward = -1

        else:
            break

        episode_data.append(
            (state, action, reward)
        )

        state = next_state

        if state == "Parked":
            break


# Display learned states
print("REINFORCE Parking Simulation")
print("----------------------------")

state = "Far"

for step in range(10):

    action = choose_action(state)

    print(
        "State:",
        state,
        " Action:",
        action
    )

    if state == "Far":
        state = "Near"

    elif state == "Near":
        state = "Aligned"

    elif state == "Aligned":
        state = "Parked"

    if state == "Parked":
        print("Parking Completed!")
        break
