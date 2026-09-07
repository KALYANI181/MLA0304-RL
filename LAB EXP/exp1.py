# Experiment 1: Simple MDP for Chess-like Game

states = ["Start", "Middle", "NearGoal", "Goal"]

actions = {
    "Start": ["Move_Right", "Move_Left"],
    "Middle": ["Move_Right", "Move_Left"],
    "NearGoal": ["Move_Right", "Move_Left"]
}

rewards = {
    ("Start", "Move_Right"): -1,
    ("Start", "Move_Left"): -2,

    ("Middle", "Move_Right"): -1,
    ("Middle", "Move_Left"): -2,

    ("NearGoal", "Move_Right"): 10,
    ("NearGoal", "Move_Left"): -2
}

# Initial state
state = "Start"

print("MDP Game Started")
print("----------------")

total_reward = 0

while state != "Goal":

    print("\nCurrent State:", state)

    # Select action with maximum reward
    available_actions = actions[state]

    best_action = max(
        available_actions,
        key=lambda a: rewards[(state, a)]
    )

    reward = rewards[(state, best_action)]

    print("Selected Action:", best_action)
    print("Reward:", reward)

    total_reward += reward

    # State transition
    if state == "Start" and best_action == "Move_Right":
        state = "Middle"

    elif state == "Middle" and best_action == "Move_Right":
        state = "NearGoal"

    elif state == "NearGoal" and best_action == "Move_Right":
        state = "Goal"

    else:
        print("Bad move!")
        break

print("\nGame Finished!")
print("Final State:", state)
print("Total Reward:", total_reward)
