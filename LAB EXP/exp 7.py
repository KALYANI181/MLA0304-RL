# Experiment 7: Taxi Routing using Dynamic Programming

states = ["A", "B", "C", "D"]

actions = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["D"],
    "D": []
}

# Travel costs
cost = {
    ("A", "B"): 2,
    ("A", "C"): 5,
    ("B", "C"): 1,
    ("B", "D"): 6,
    ("C", "D"): 2
}

# Destination
destination = "D"

# Initialize values
V = {state: float("inf") for state in states}
V[destination] = 0

# Dynamic Programming
for iteration in range(10):

    old_V = V.copy()

    for state in states:

        if state == destination:
            continue

        values = []

        for next_state in actions[state]:

            values.append(
                cost[(state, next_state)] + old_V[next_state]
            )

        V[state] = min(values)


# Display values
print("Optimal State Values")
print("--------------------")

for state in states:
    print(state, ":", V[state])


# Generate policy
print("\nOptimal Taxi Route:")

state = "A"
route = [state]

while state != destination:

    next_state = min(
        actions[state],
        key=lambda x: cost[(state, x)] + V[x]
    )

    route.append(next_state)
    state = next_state

print(" -> ".join(route))
print("Minimum Cost:", V["A"])
