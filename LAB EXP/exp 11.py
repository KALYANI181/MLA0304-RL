# Experiment 11
# Comparison of DQN, DDQN, Dueling DQN and PER

import numpy as np

# Simulated traffic waiting times
np.random.seed(10)

dqn_wait = np.random.randint(20, 50, 10)
ddqn_wait = np.random.randint(15, 40, 10)
dueling_wait = np.random.randint(10, 35, 10)
per_wait = np.random.randint(8, 30, 10)

print("Traffic Signal Control")
print("----------------------")

print("DQN Waiting Times:")
print(dqn_wait)

print("\nDDQN Waiting Times:")
print(ddqn_wait)

print("\nDueling DQN Waiting Times:")
print(dueling_wait)

print("\nPER Waiting Times:")
print(per_wait)

print("\nAverage Waiting Time")

print("DQN:",
      round(np.mean(dqn_wait), 2))

print("DDQN:",
      round(np.mean(ddqn_wait), 2))

print("Dueling DQN:",
      round(np.mean(dueling_wait), 2))

print("PER:",
      round(np.mean(per_wait), 2))

# Find best algorithm
averages = {
    "DQN": np.mean(dqn_wait),
    "DDQN": np.mean(ddqn_wait),
    "Dueling DQN": np.mean(dueling_wait),
    "PER": np.mean(per_wait)
}

best = min(averages, key=averages.get)

print("\nBest Algorithm:", best)
