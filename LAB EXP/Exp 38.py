import random

states = ["Left", "Center", "Right"]

belief = {
    "Left": 0.33,
    "Center": 0.34,
    "Right": 0.33
}

actions = ["Move Left", "Stay", "Move Right"]

print("POMDP Robot Localization")
print("------------------------")

for step in range(5):

    # Robot receives an observation
    observation = random.choice(states)

    print("\nStep:", step + 1)
    print("Observation:", observation)

    # Update belief
    for state in states:

        if state == observation:
            belief[state] += 0.2
        else:
            belief[state] -= 0.1

    # Normalize belief
    total = sum(belief.values())

    for state in states:
        belief[state] = max(0, belief[state] / total)

    # Select most probable state
    estimated_state = max(
        belief,
        key=belief.get
    )

    print("Belief:")
    for state in states:
        print(state, ":", round(belief[state], 2))

    print("Estimated State:", estimated_state)

    # Select action
    if estimated_state == "Left":
        action = "Move Right"
    elif estimated_state == "Right":
        action = "Move Left"
    else:
        action = "Stay"

    print("Action:", action)
