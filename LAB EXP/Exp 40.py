import random

states = [
    "Low Score",
    "Medium Score",
    "High Score"
]

actions = [
    "Easy Lesson",
    "Practice",
    "Advanced Lesson"
]

Q = {}

alpha = 0.1
epsilon = 0.2


def choose_action(state):

    if random.random() < epsilon:
        return random.choice(actions)

    values = [
        Q.get((state, action), 0)
        for action in actions
    ]

    max_value = max(values)

    best_actions = [
        action
        for action, value in zip(actions, values)
        if value == max_value
    ]

    return random.choice(best_actions)


# Training
for episode in range(1000):

    score_state = random.choice(states)

    action = choose_action(score_state)

    # Reward
    if score_state == "Low Score" and action == "Easy Lesson":
        reward = 10

    elif score_state == "Medium Score" and action == "Practice":
        reward = 10

    elif score_state == "High Score" and action == "Advanced Lesson":
        reward = 10

    else:
        reward = -5

    old_value = Q.get(
        (score_state, action),
        0
    )

    Q[(score_state, action)] = (
        old_value +
        alpha * (reward - old_value)
    )


print("Personalized Education RL Training Completed\n")

for state in states:

    values = [
        Q.get((state, action), 0)
        for action in actions
    ]

    best_action = actions[
        values.index(max(values))
    ]

    print("Student State:", state)
    print("Recommended Content:", best_action)
    print()
