# Experiment 3: MDP for Warehouse Robot

states = ["A", "B", "C", "D"]

actions = {
    "A": ["RIGHT"],
    "B": ["RIGHT"],
    "C": ["DOWN"]
}

rewards = {
    ("A", "RIGHT"): -1,
    ("B", "RIGHT"): -1,
    ("C", "DOWN"): 10
}

transitions = {
    ("A", "RIGHT"): "B",
    ("B", "RIGHT"): "C",
    ("C", "DOWN"): "D"
}

state = "A"
total_reward = 0

print("Warehouse Robot MDP")
print("--------------------")

while state != "D":

    print("\nCurrent State:", state)

    action = actions[state][0]

    next_state = transitions[(state, action)]

    reward = rewards[(state, action)]

    print("Action:", action)
    print("Next State:", next_state)
    print("Reward:", reward)

    total_reward += reward

    state = next_state

print("\nRobot reached delivery location!")
print("Total Reward:", total_reward)
