# Experiment 21
# Smart Energy Management using Q-Learning

import random

states = ["Cold", "Comfortable", "Hot"]

actions = [
    "Heater_ON",
    "AC_ON",
    "OFF"
]

# Q-table
Q = {}

for state in states:
    Q[state] = {
        action: 0
        for action in actions
    }


def get_next_state(state, action):

    if state == "Cold":

        if action == "Heater_ON":
            return "Comfortable"
        else:
            return "Cold"

    elif state == "Hot":

        if action == "AC_ON":
            return "Comfortable"
        else:
            return "Hot"

    else:
        return "Comfortable"


def get_reward(state, action):

    if state == "Comfortable" and action == "OFF":
        return 10

    elif action == "Heater_ON" or action == "AC_ON":
        return 3

    return -5


alpha = 0.1
gamma = 0.9
epsilon = 0.2

# Training
for episode in range(500):

    state = random.choice(states)

    for step in range(20):

        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = max(
                Q[state],
                key=Q[state].get
            )

        next_state = get_next_state(
            state,
            action
        )

        reward = get_reward(
            state,
            action
        )

        best_next = max(
            Q[next_state].values()
        )

        Q[state][action] += alpha * (
            reward
            + gamma * best_next
            - Q[state][action]
        )

        state = next_state


# Display policy
print("Smart Energy Management Policy")
print("------------------------------")

for state in states:

    best_action = max(
        Q[state],
        key=Q[state].get
    )

    print(
        state,
        "->",
        best_action
    )
