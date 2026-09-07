# Experiment 17
# Hierarchical Reinforcement Learning - MAXQ

import random

# Hierarchical tasks
tasks = {
    "CleanHouse": [
        "GoToRoom",
        "CleanRoom",
        "ReturnHome"
    ],

    "GoToRoom": [
        "MoveForward",
        "Turn"
    ],

    "CleanRoom": [
        "PickDirt",
        "Vacuum"
    ],

    "ReturnHome": [
        "MoveBackward",
        "Turn"
    ]
}


# Reward for subtasks
rewards = {
    "MoveForward": 2,
    "Turn": 1,
    "PickDirt": 5,
    "Vacuum": 10,
    "MoveBackward": 2
}


def execute_task(task):

    print("\nExecuting:", task)

    for subtask in tasks[task]:

        if subtask in tasks:

            execute_task(subtask)

        else:

            reward = rewards.get(subtask, 0)

            print(
                "Action:",
                subtask,
                "Reward:",
                reward
            )


print("Hierarchical Robot Task")
print("-----------------------")

execute_task("CleanHouse")

print("\nHouse cleaning completed!")
