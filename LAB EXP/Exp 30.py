import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# State:
# [speed, distance_from_vehicle, lane_position]

model = Sequential([
    Dense(32, activation="relu", input_shape=(3,)),
    Dense(32, activation="relu"),
    Dense(3, activation="linear")
])

model.compile(
    optimizer="adam",
    loss="mse"
)

# Training data
X = np.array([
    [20, 80, 0],
    [40, 60, 0],
    [60, 30, 0],
    [80, 10, 0],
    [40, 100, 1],
    [60, 70, 1],
    [80, 40, 1]
], dtype=float)

# Target Q-values
# [Slow, Maintain, Speed]
Y = np.array([
    [1, 2, 3],
    [1, 3, 2],
    [4, 3, 1],
    [8, 2, 0],
    [1, 4, 2],
    [1, 4, 2],
    [5, 3, 1]
], dtype=float)

print("Training DQN...")

model.fit(
    X,
    Y,
    epochs=100,
    verbose=0
)

print("Training completed.")


# Test state
state = np.array([[60, 25, 0]])

q_values = model.predict(state, verbose=0)

action = np.argmax(q_values[0])

actions = [
    "Slow Down",
    "Maintain Speed",
    "Speed Up"
]

print("\nCurrent State:")
print("Speed = 60 km/h")
print("Distance = 25 m")
print("Lane = 0")

print("\nQ-values:", q_values[0])

print("Recommended Action:", actions[action])
