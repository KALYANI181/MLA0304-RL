import random

road = [
    "Start",
    "Intersection",
    "Road",
    "Destination"
]

actions = ["FORWARD", "LEFT", "RIGHT", "STOP"]

position = 0
total_reward = 0

print("Autonomous Car Navigation")
print("-------------------------")

for step in range(10):

    action = random.choice(actions)

    print("Position :", road[position])
    print("Action   :", action)

    if action == "FORWARD":

        if position < len(road) - 1:
            position += 1
            total_reward -= 1

        if position == len(road) - 1:
            total_reward += 10
            print("Destination reached!")
            break

    elif action == "STOP":
        total_reward -= 1

    else:
        total_reward -= 5
        print("Unsafe/incorrect action")

print("\nTotal Reward:", total_reward)
print("Final Position:", road[position])
