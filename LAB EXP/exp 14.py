# Experiment 14
# Actor-Critic for Smart Elevator Scheduling

import random

# Floors
floors = [1, 2, 3, 4, 5]

# Initial values
value = {
    floor: 0
    for floor in floors
}

# Actor policy
policy = {
    floor: random.choice(floors)
    for floor in floors
}


def reward(current, target):

    distance = abs(current - target)

    return 10 - distance


# A2C training
for episode in range(100):

    current_floor = random.choice(floors)
    target_floor = random.choice(floors)

    selected_floor = policy[current_floor]

    r = reward(selected_floor, target_floor)

    # Critic update
    value[current_floor] += (
        0.1 * (r - value[current_floor])
    )

    # Actor update
    if r > 0:
        policy[current_floor] = target_floor


print("A2C Elevator Policy")
print("-------------------")

for floor in floors:
    print(
        "Current Floor:",
        floor,
        "-> Target:",
        policy[floor]
    )


# Simple A3C demonstration
print("\nA3C Simulation")
print("--------------")

workers = 4

for worker in range(workers):

    current = random.choice(floors)
    target = random.choice(floors)

    print(
        "Worker",
        worker + 1,
        ": Elevator",
        current,
        "->",
        target
    )
