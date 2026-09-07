# Experiment 10: Simple DQN for Drone Delivery

import numpy as np
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


# State:
# [position, battery]

state_size = 2
action_size = 3

# Actions
# 0 = Stay
# 1 = Move Forward
# 2 = Move Backward

model = Sequential([
    Dense(24, input_dim=state_size, activation="relu"),
    Dense(24, activation="relu"),
    Dense(action_size, activation="linear")
])

model.compile(
    loss="mse",
    optimizer=Adam(learning_rate=0.001)
)


# Environment
def step(state, action):

    position, battery = state

    if action == 1:
        position += 1
        battery -= 1

    elif action == 2:
        position -= 1
        battery -= 1

    # Keep position inside road
    position = max(0, min(10, position))

    # Reward
    if position == 10:
        reward = 100
        done = True

    elif battery <= 0:
        reward = -100
        done = True

    else:
        reward = -1
        done = False

    return [position, battery], reward, done


# Training
gamma = 0.95
epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995

for episode in range(200):

    state = [0, 15]

    for step_count in range(30):

        # Exploration / exploitation
        if random.random() < epsilon:
            action = random.randint(0, action_size - 1)
        else:
            q_values = model.predict(
                np.array([state]),
                verbose=0
            )

            action = np.argmax(q_values[0])

        next_state, reward, done = step(
            state, action
        )

        # Current Q values
        target = model.predict(
            np.array([state]),
            verbose=0
        )

        # Next Q values
        next_q = model.predict(
            np.array([next_state]),
            verbose=0
        )

        if done:
            target[0][action] = reward
        else:
            target[0][action] = (
                reward + gamma * np.max(next_q[0])
            )

        # Train neural network
        model.fit(
            np.array([state]),
            target,
            epochs=1,
            verbose=0
        )

        state = next_state

        if done:
            break

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay


# Testing
state = [0, 15]

print("Drone Delivery Simulation")
print("-------------------------")

for step_count in range(30):

    q_values = model.predict(
        np.array([state]),
        verbose=0
    )

    action = np.argmax(q_values[0])

    next_state, reward, done = step(
        state, action
    )

    print(
        "Step:", step_count + 1,
        "State:", next_state,
        "Action:", action,
        "Reward:", reward
    )

    state = next_state

    if done:
        break


if state[0] == 10:
    print("\nDelivery Successful!")
else:
    print("\nDelivery Failed!")
