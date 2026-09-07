# Experiment 4: Bellman Equation
# Autonomous Delivery Robot

states = ["A", "B", "C", "D"]

# Travel costs
costs = {
    "A": {"B": 2, "C": 5},
    "B": {"C": 1, "D": 6},
    "C": {"D": 2}
}

# Initialize values
V = {
    "A": float("inf"),
    "B": float("inf"),
    "C": float("inf"),
    "D": 0
}

# Bellman update
for iteration in range(10):

    old_V = V.copy()

    for state in ["C", "B", "A"]:

        values = []

        for next_state, cost in costs[state].items():

            value = cost + old_V[next_state]
            values.append(value)

        V[state] = min(values)


print("Optimal State Values")
print("--------------------")

for state in states:
    print(state, "=", V[state])

print("\nMinimum cost from A to D:", V["A"])
