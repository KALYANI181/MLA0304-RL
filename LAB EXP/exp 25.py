# Experiment 25
# Bandit Algorithms for Online Advertisement

import random
import math

# True click probabilities
probabilities = [0.2, 0.5, 0.8]

n_ads = 3
rounds = 1000


# ------------------------------------------------
# 1. Epsilon-Greedy
# ------------------------------------------------

def epsilon_greedy():

    counts = [0] * n_ads
    rewards = [0] * n_ads

    epsilon = 0.1

    for t in range(rounds):

        if random.random() < epsilon:

            ad = random.randint(
                0,
                n_ads - 1
            )

        else:

            averages = []

            for i in range(n_ads):

                if counts[i] == 0:
                    averages.append(0)

                else:
                    averages.append(
                        rewards[i] / counts[i]
                    )

            ad = averages.index(
                max(averages)
            )

        reward = (
            1
            if random.random()
            < probabilities[ad]
            else 0
        )

        counts[ad] += 1
        rewards[ad] += reward

    return sum(rewards)


# ------------------------------------------------
# 2. UCB
# ------------------------------------------------

def ucb():

    counts = [0] * n_ads
    rewards = [0] * n_ads

    total_reward = 0

    for t in range(rounds):

        # Select each ad once
        if t < n_ads:

            ad = t

        else:

            ucb_values = []

            for i in range(n_ads):

                average = (
                    rewards[i] /
                    counts[i]
                )

                confidence = math.sqrt(
                    2 * math.log(t + 1)
                    / counts[i]
                )

                ucb_values.append(
                    average + confidence
                )

            ad = ucb_values.index(
                max(ucb_values)
            )

        reward = (
            1
            if random.random()
            < probabilities[ad]
            else 0
        )

        counts[ad] += 1
        rewards[ad] += reward
        total_reward += reward

    return total_reward


# ------------------------------------------------
# 3. Thompson Sampling
# ------------------------------------------------

def thompson_sampling():

    successes = [1] * n_ads
    failures = [1] * n_ads

    total_reward = 0

    for t in range(rounds):

        samples = []

        for i in range(n_ads):

            sample = random.betavariate(
                successes[i],
                failures[i]
            )

            samples.append(sample)

        ad = samples.index(
            max(samples)
        )

        reward = (
            1
            if random.random()
            < probabilities[ad]
            else 0
        )

        if reward == 1:
            successes[ad] += 1
        else:
            failures[ad] += 1

        total_reward += reward

    return total_reward


# Run algorithms

eg_reward = epsilon_greedy()
ucb_reward = ucb()
ts_reward = thompson_sampling()


print("Advertisement Recommendation")
print("----------------------------")

print(
    "Epsilon-Greedy Clicks:",
    eg_reward
)

print(
    "UCB Clicks:",
    ucb_reward
)

print(
    "Thompson Sampling Clicks:",
    ts_reward
)


results = {
    "Epsilon-Greedy": eg_reward,
    "UCB": ucb_reward,
    "Thompson Sampling": ts_reward
}

best = max(
    results,
    key=results.get
)

print("\nBest Algorithm:",
      best)
