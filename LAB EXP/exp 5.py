# Experiment 5: Epsilon-Greedy Multi-Armed Bandit

import random

# True click probabilities of advertisements
true_probabilities = [0.2, 0.5, 0.8]

# Number of advertisements
n_ads = len(true_probabilities)

# Estimated rewards
Q = [0] * n_ads

# Number of times each ad is selected
N = [0] * n_ads

epsilon = 0.1

total_reward = 0

# Run 1000 rounds
for i in range(1000):

    # Exploration or exploitation
    if random.random() < epsilon:

        # Exploration
        ad = random.randint(0, n_ads - 1)

    else:

        # Exploitation
        ad = Q.index(max(Q))

    # Simulate user click
    if random.random() < true_probabilities[ad]:
        reward = 1
    else:
        reward = 0

    # Update count
    N[ad] += 1

    # Update estimated reward
    Q[ad] = Q[ad] + (reward - Q[ad]) / N[ad]

    total_reward += reward


print("Advertisement Results")
print("---------------------")

for i in range(n_ads):
    print("Ad", i + 1)
    print("Times Selected:", N[i])
    print("Estimated Click Rate:", round(Q[i], 3))
    print()

print("Total Clicks:", total_reward)
print("Best Advertisement:", Q.index(max(Q)) + 1)
