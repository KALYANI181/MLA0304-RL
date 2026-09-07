import numpy as np

temperature = 25

actions = [
    "Decrease",
    "Maintain",
    "Increase"
]

# Policy probabilities
policy = np.array([0.3, 0.4, 0.3])

learning_rate = 0.1

print("REINFORCE Smart Home Temperature Control")
print("----------------------------------------")

for episode in range(10):

    # Select action according to policy
    action = np.random.choice(
        len(actions),
        p=policy
    )

    print("\nEpisode:", episode + 1)
    print("Temperature:", temperature)
    print("Action:", actions[action])

    # Reward
    if temperature == 24:
        reward = 10

    elif temperature < 20 or temperature > 30:
        reward = -5

    else:
        reward = 5

    # Update temperature
    if action == 0:
        temperature -= 1

    elif action == 2:
        temperature += 1

    # Simple policy-gradient update
    if reward > 0:
        policy[action] += learning_rate

    else:
        policy[action] -= learning_rate

    # Keep probabilities valid
    policy = np.maximum(policy, 0.01)
    policy = policy / np.sum(policy)

print("\nFinal Policy:")
print("Decrease :", round(policy[0], 2))
print("Maintain :", round(policy[1], 2))
print("Increase :", round(policy[2], 2))
