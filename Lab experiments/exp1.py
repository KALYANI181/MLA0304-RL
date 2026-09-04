# Experiment 1: Markov Decision Process (MDP) for Simplified Chess

states = ["Start", "Middle", "Winning", "Losing", "Goal"]

actions = {
    "Start": ["Attack", "Defend"],
    "Middle": ["Attack", "Defend"],
    "Winning": ["Finish"],
    "Losing": ["Recover"]
}

transitions = {
    ("Start", "Attack"): "Middle",
    ("Middle", "Attack"): "Winning",
    ("Winning", "Finish"): "Goal",
    ("Losing", "Recover"): "Middle"
}

rewards = {
    "Middle": 10,
    "Winning": 50,
    "Goal": 100,
    "Losing": -20
}

state = "Start"
total_reward = 0

print("=== Simplified Chess MDP ===")

while state != "Goal":
    print("\nCurrent State:", state)
    action = actions[state][0]
    print("Action:", action)

    state = transitions[(state, action)]
    print("Next State:", state)

    reward = rewards.get(state, 0)
    print("Reward:", reward)

    total_reward += reward

print("\nGoal Reached!")
print("Total Reward =", total_reward)
