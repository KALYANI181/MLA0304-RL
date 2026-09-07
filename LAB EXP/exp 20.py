# Experiment 20
# POMDP for Search and Rescue Robot

import random

locations = [
    "Room A",
    "Room B",
    "Room C",
    "Room D"
]

actions = [
    "SEARCH",
    "MOVE"
]

# Hidden actual location of victim
victim_location = random.choice(locations)

# Robot starts at Room A
robot_location = "Room A"

print("Search and Rescue Robot")
print("-----------------------")

print("Robot Starting Location:",
      robot_location)

for step in range(10):

    # Sensor gives partial information
    observation = random.choice([
        "Victim Detected",
        "No Victim Detected"
    ])

    print("\nStep:", step + 1)
    print("Robot Location:", robot_location)
    print("Sensor Observation:", observation)

    if (
        observation == "Victim Detected"
        and robot_location == victim_location
    ):

        print("Victim Found!")
        break

    # Choose action
    if observation == "Victim Detected":

        action = "SEARCH"

    else:

        action = "MOVE"

    print("Selected Action:", action)

    # Move to another location
    if action == "MOVE":

        robot_location = random.choice(
            locations
        )

else:

    print("\nSearch completed.")

print("\nActual Victim Location:",
      victim_location)
