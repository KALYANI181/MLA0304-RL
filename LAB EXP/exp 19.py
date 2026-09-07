# Experiment 19
# Multi-Agent Reinforcement Learning

import random

robots = [
    "Robot 1",
    "Robot 2",
    "Robot 3"
]

tasks = [
    "Task A",
    "Task B",
    "Task C"
]

# Rewards
reward_table = {
    "Task A": 10,
    "Task B": 8,
    "Task C": 6
}

assignments = {}

available_tasks = tasks.copy()

print("Multi-Agent Warehouse System")
print("----------------------------")

for robot in robots:

    if available_tasks:

        task = random.choice(available_tasks)

        assignments[robot] = task

        available_tasks.remove(task)


total_reward = 0

for robot, task in assignments.items():

    reward = reward_table[task]

    total_reward += reward

    print(
        robot,
        "->",
        task,
        "Reward:",
        reward
    )


print("\nTotal Cooperative Reward:",
      total_reward)

print("All robots completed their tasks.")
