import random
import math

prices = [50, 75, 100, 125, 150]

# Probability of customer buying at each price
buy_probability = [0.90, 0.75, 0.60, 0.40, 0.25]

rounds = 1000


# ---------------- EPSILON GREEDY ----------------
def epsilon_greedy():
    counts = [0] * len(prices)
    revenue = [0] * len(prices)
    total_revenue = 0

    for _ in range(rounds):
        epsilon = 0.1

        if random.random() < epsilon:
            arm = random.randrange(len(prices))
        else:
            averages = [
                revenue[i] / counts[i] if counts[i] > 0 else 0
                for i in range(len(prices))
            ]
            arm = averages.index(max(averages))

        sale = random.random() < buy_probability[arm]

        counts[arm] += 1

        if sale:
            revenue[arm] += prices[arm]
            total_revenue += prices[arm]

    return total_revenue


# ---------------- UCB ----------------
def ucb():
    counts = [0] * len(prices)
    revenue = [0] * len(prices)
    total_revenue = 0

    for i in range(len(prices)):
        sale = random.random() < buy_probability[i]
        counts[i] += 1

        if sale:
            revenue[i] += prices[i]
            total_revenue += prices[i]

    for t in range(len(prices), rounds):
        scores = []

        for i in range(len(prices)):
            average = revenue[i] / counts[i]

            confidence = math.sqrt(
                2 * math.log(t + 1) / counts[i]
            )

            scores.append(average + confidence)

        arm = scores.index(max(scores))

        sale = random.random() < buy_probability[arm]

        counts[arm] += 1

        if sale:
            revenue[arm] += prices[arm]
            total_revenue += prices[arm]

    return total_revenue


# ---------------- THOMPSON SAMPLING ----------------
def thompson_sampling():
    success = [1] * len(prices)
    failure = [1] * len(prices)

    total_revenue = 0

    for _ in range(rounds):

        samples = [
            random.betavariate(success[i], failure[i])
            for i in range(len(prices))
        ]

        arm = samples.index(max(samples))

        sale = random.random() < buy_probability[arm]

        if sale:
            success[arm] += 1
            total_revenue += prices[arm]
        else:
            failure[arm] += 1

    return total_revenue


print("Dynamic Pricing - Revenue Comparison")
print("--------------------------------------")

eg = epsilon_greedy()
ucb_revenue = ucb()
ts = thompson_sampling()

print("Epsilon-Greedy Revenue :", eg)
print("UCB Revenue            :", ucb_revenue)
print("Thompson Sampling      :", ts)
