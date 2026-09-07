# Experiment 24
# REINFORCE Trading Simulation

import random

prices = [
    100, 102, 105, 103, 108,
    110, 107, 112, 115, 118
]

actions = [
    "BUY",
    "SELL",
    "HOLD"
]

# Policy
policy = {}

for i in range(len(prices)):
    policy[i] = {
        action: 1 / 3
        for action in actions
    }


def choose_action(state):

    return random.choices(
        actions,
        weights=list(policy[state].values())
    )[0]


balance = 1000
shares = 0

print("Automated Trading")
print("-----------------")

for i in range(len(prices)):

    price = prices[i]

    action = choose_action(i)

    if action == "BUY":

        if balance >= price:
            shares += 1
            balance -= price

    elif action == "SELL":

        if shares > 0:
            shares -= 1
            balance += price

    print(
        "Price:",
        price,
        "Action:",
        action,
        "Balance:",
        round(balance, 2)
    )


# Final portfolio value
final_value = balance + shares * prices[-1]

print("\nFinal Balance:",
      round(balance, 2))

print("Shares:",
      shares)

print("Final Portfolio Value:",
      round(final_value, 2))
