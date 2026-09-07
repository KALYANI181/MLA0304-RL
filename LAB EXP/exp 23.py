# Experiment 23
# PPO-based Autonomous Lane Changing

import random

lanes = [0, 1, 2]

actions = [
    "STAY",
    "LEFT",
    "RIGHT"
]

# Policy values
policy = {}

for lane in lanes:
    policy[lane] = {
        action: 0
        for action in actions
    }


def choose_action(lane):

    return max(
        policy[lane],
        key=policy[lane].get
    )


# Training
for episode in range(500):

    lane = random.choice(lanes)

    for step in range(20):

        action = random.choice(actions)

        # Simulated traffic
        traffic = random.choice(
            ["FAST", "SLOW"]
        )

        if traffic == "SLOW":
            reward = 5

            if action == "LEFT" and lane > 0:
                lane -= 1

            elif action == "RIGHT" and lane < 2:
                lane += 1

        else:
            reward = 2

        # Simple policy update
        policy[lane][action] += 0.01 * reward


# Display learned policy
print("Autonomous Lane Changing")
print("------------------------")

for lane in lanes:

    best_action = choose_action(lane)

    print(
        "Lane",
        lane,
        "->",
        best_action
    )
