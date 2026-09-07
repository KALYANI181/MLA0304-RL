# Experiment 16
# Policy Gradient for Autonomous Lane Keeping

import random

states = [-2, -1, 0, 1, 2]

actions = ["LEFT", "STAY", "RIGHT"]

# Initialize policy
policy = {}

for state in states:
    policy[state] = {
        "LEFT": 1/3,
        "STAY": 1/3,
        "RIGHT": 1/3
    }


def choose_action(state):
    return random.choices(
        actions,
        weights=list(policy[state].values())
    )[0]


def move(position, action):

    if action == "LEFT":
        position -= 1

    elif action == "RIGHT":
        position += 1

    position = max(-2, min(2, position))

    return position


def get_reward(position):

    if position == 0:
        return 10
    elif abs(position) == 1:
        return 3
    else:
        return -5


# Training
for episode in range(500):

    position = random.choice(states)

    for step in range(20):

        action = choose_action(position)

        new_position = move(position, action)

        reward = get_reward(new_position)

        # Simple policy update
        if reward > 0:
            policy[position][action] += 0.01

        else:
            policy[position][action] -= 0.01

        # Keep probabilities positive
        for a in actions:
            policy[position][a] = max(
                0.01,
                policy[position][a]
            )

        # Normalize
        total = sum(policy[position].values())

        for a in actions:
            policy[position][a] /= total

        position = new_position


# Display learned policy
print("Learned Lane-Keeping Policy")
print("---------------------------")

for state in states:

    best_action = max(
        policy[state],
        key=policy[state].get
    )

    print(
        "Position:", state,
        "->", best_action
    )
