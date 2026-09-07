# Experiment 18
# Meta-Reinforcement Learning

import random

tasks = [
    "Assembly",
    "Welding",
    "Packaging"
]

actions = [
    "MOVE",
    "PICK",
    "PLACE"
]

# Meta knowledge
meta_policy = {
    action: 0
    for action in actions
}


# Learn from multiple tasks
for task in tasks:

    print("\nTraining Task:", task)

    for episode in range(100):

        action = random.choice(actions)

        reward = random.randint(1, 10)

        meta_policy[action] += reward


print("\nMeta Learned Knowledge")
print("----------------------")

for action in actions:
    print(
        action,
        ":",
        meta_policy[action]
    )


# New task
new_task = "Sorting"

print("\nNew Task:", new_task)

best_action = max(
    meta_policy,
    key=meta_policy.get
)

print(
    "Quickly Selected Action:",
    best_action
)
