import random

states = ["LOW", "MEDIUM", "HIGH"]

actions = ["SHORT", "LONG"]

# Initial policy
policy = {
    "LOW": "SHORT",
    "MEDIUM": "LONG",
    "HIGH": "LONG"
}

# Waiting cost for each state-action pair
cost = {
    ("LOW", "SHORT"): 1,
    ("LOW", "LONG"): 2,

    ("MEDIUM", "SHORT"): 5,
    ("MEDIUM", "LONG"): 2,

    ("HIGH", "SHORT"): 8,
    ("HIGH", "LONG"): 3
}

print("Traffic Light Policy Iteration")
print("------------------------------")

for iteration in range(5):

    print("\nIteration", iteration + 1)

    # Policy evaluation
    value = {}

    for state in states:
        value[state] = cost[(state, policy[state])]

    # Policy improvement
    stable = True

    for state in states:

        best_action = min(
            actions,
            key=lambda a: cost[(state, a)]
        )

        if best_action != policy[state]:
            policy[state] = best_action
            stable = False

    print("Policy:", policy)
    print("Value :", value)

    if stable:
        print("\nPolicy converged.")
        break

print("\nFinal Traffic Signal Policy:")

for state in states:
    print(state, "->", policy[state])
