import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Lambda
from tensorflow.keras.models import Model

state_size = 4
action_size = 4


# ---------------- STANDARD DQN ----------------

inputs = Input(shape=(state_size,))

x = Dense(32, activation="relu")(inputs)
x = Dense(32, activation="relu")(x)

outputs = Dense(action_size)(x)

dqn = Model(inputs, outputs)

dqn.compile(
    optimizer="adam",
    loss="mse"
)


# ---------------- DUELING DQN ----------------

inputs2 = Input(shape=(state_size,))

x = Dense(32, activation="relu")(inputs2)
x = Dense(32, activation="relu")(x)

value = Dense(1)(x)
advantage = Dense(action_size)(x)

q_values = Lambda(
    lambda x: x[0] + x[1] - tf.reduce_mean(
        x[1], axis=1, keepdims=True
    )
)([value, advantage])

dueling_dqn = Model(inputs2, q_values)

dueling_dqn.compile(
    optimizer="adam",
    loss="mse"
)


# Sample GridWorld states
X = np.array([
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 0]
], dtype=float)

Y = np.array([
    [1, 2, 3, 1],
    [2, 3, 1, 0],
    [3, 2, 1, 2],
    [4, 2, 1, 0],
    [2, 3, 4, 1]
], dtype=float)


# Train standard DQN
dqn.fit(X, Y, epochs=50, verbose=0)

# Train Dueling DQN
dueling_dqn.fit(X, Y, epochs=50, verbose=0)


print("Standard DQN and Dueling DQN training completed.")

sample_state = np.array([[1, 0, 0, 1]])

dqn_q = dqn.predict(sample_state, verbose=0)
dueling_q = dueling_dqn.predict(sample_state, verbose=0)

print("\nStandard DQN Q-values:")
print(np.round(dqn_q[0], 2))

print("\nDueling DQN Q-values:")
print(np.round(dueling_q[0], 2))

print("\nComparison completed.")
