# TD(0)

import random

states = ["A", "B", "C", "D"]

V = {s: 0 for s in states}

V["D"] = 10

alpha = 0.1
gamma = 0.9

for episode in range(100):

    state = random.choice(["A", "B", "C"])

    if state == "A":
        next_state = "B"
    elif state == "B":
        next_state = "C"
    else:
        next_state = "D"

    reward = 10 if next_state == "D" else -1

    # TD(0) update
    V[state] += alpha * (
        reward + gamma * V[next_state] - V[state]
    )


print("TD(0) Values:")
print(V)
