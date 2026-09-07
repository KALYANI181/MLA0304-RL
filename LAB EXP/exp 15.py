# Experiment 15
# PPO and TRPO for Humanoid Robot Balance

import random

# Robot balance state
balance = 0

# Target balance
target = 0

# PPO learning rate
ppo_lr = 0.1

# TRPO learning rate
trpo_lr = 0.05


def calculate_reward(balance):
    return -abs(balance - target)


# PPO simulation
print("PPO Training")
print("------------")

balance = 5

for episode in range(20):

    # PPO adjusts balance toward zero
    if balance > 0:
        balance -= ppo_lr

    elif balance < 0:
        balance += ppo_lr

    reward = calculate_reward(balance)

    print(
        "Episode:",
        episode + 1,
        "Balance:",
        round(balance, 2),
        "Reward:",
        round(reward, 2)
    )


# TRPO simulation
print("\nTRPO Training")
print("-------------")

balance = 5

for episode in range(20):

    if balance > 0:
        balance -= trpo_lr

    elif balance < 0:
        balance += trpo_lr

    reward = calculate_reward(balance)

    print(
        "Episode:",
        episode + 1,
        "Balance:",
        round(balance, 2),
        "Reward:",
        round(reward, 2)
    )


print("\nHumanoid balance optimization completed.")
