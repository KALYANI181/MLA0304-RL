import random

states = [
    "Low Risk",
    "Medium Risk",
    "High Risk"
]

actions = [
    "Monitor",
    "Consult Doctor",
    "Emergency Care"
]

Q = {}

alpha = 0.1
gamma = 0.9
epsilon = 0.2


def choose_action(state):
    if random.random() < epsilon:
        return random.choice(actions)

    values = [
        Q.get((state, action), 0)
        for action in actions
    ]

    max_value = max(values)

    best = [
        action
        for action, value in zip(actions, values)
        if value == max_value
    ]

    return random.choice(best)


for episode in range(1000):

    state = random.choice(states)

    action = choose_action(state)

    # Reward based on appropriate treatment
    if state == "Low Risk" and action == "Monitor":
        reward = 10

    elif state == "Medium Risk" and action == "Consult Doctor":
        reward = 10

    elif state == "High Risk" and action == "Emergency Care":
        reward = 10

    else:
        reward = -5

    old_value = Q.get((state, action), 0)

    Q[(state, action)] = old_value + alpha * (
        reward - old_value
    )


print("Healthcare RL Training Completed\n")

for state in states:

    values = [
        Q.get((state, action), 0)
        for action in actions
    ]

    best_action = actions[values.index(max(values))]

    print("State:", state)
    print("Recommended Action:", best_action)
    print()
