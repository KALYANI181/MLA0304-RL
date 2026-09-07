import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Actor Network
actor = Sequential([
    Dense(32, activation="relu", input_shape=(2,)),
    Dense(32, activation="relu"),
    Dense(1, activation="sigmoid")
])

# Critic Network
critic = Sequential([
    Dense(32, activation="relu", input_shape=(3,)),
    Dense(32, activation="relu"),
    Dense(1)
])

actor.compile(
    optimizer="adam",
    loss="mse"
)

critic.compile(
    optimizer="adam",
    loss="mse"
)


# Training data
# State = [resources, enemy_strength]

states = np.array([
    [10, 2],
    [20, 3],
    [30, 5],
    [40, 7],
    [50, 9]
], dtype=float)

# Desired gathering action
target_actions = np.array([
    [0.2],
    [0.3],
    [0.5],
    [0.7],
    [0.9]
])

print("Training Actor...")

actor.fit(
    states,
    target_actions,
    epochs=100,
    verbose=0
)

print("Actor training completed.")


# Test state
test_state = np.array([[35, 4]])

action = actor.predict(
    test_state,
    verbose=0
)

print("\nCurrent resources:", test_state[0][0])
print("Enemy strength:", test_state[0][1])

print("Recommended gathering action:",
      round(float(action[0][0]), 2))
