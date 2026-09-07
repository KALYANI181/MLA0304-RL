import random

Q = {}

alpha = 0.1
gamma = 0.9
epsilon = 0.2


def get_state(board):
    return tuple(board)


def get_actions(board):
    return [i for i in range(9) if board[i] == " "]


def choose_action(state, actions):
    if random.random() < epsilon:
        return random.choice(actions)

    values = [Q.get((state, a), 0) for a in actions]
    max_value = max(values)

    best_actions = [
        a for a, v in zip(actions, values)
        if v == max_value
    ]

    return random.choice(best_actions)


def winner(board):
    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    if " " not in board:
        return "Draw"

    return None


# Training
for episode in range(5000):

    board = [" "] * 9

    while True:

        state = get_state(board)
        actions = get_actions(board)

        if not actions:
            break

        action = choose_action(state, actions)

        board[action] = "X"

        result = winner(board)

        if result == "X":
            reward = 1

            key = (state, action)

            Q[key] = Q.get(key, 0) + alpha * (
                reward - Q.get(key, 0)
            )

            break

        if result == "Draw":
            reward = 0
            break

        # Opponent plays randomly
        opponent_action = random.choice(get_actions(board))
        board[opponent_action] = "O"

        result = winner(board)

        if result == "O":
            reward = -1
            next_state = get_state(board)

            key = (state, action)

            Q[key] = Q.get(key, 0) + alpha * (
                reward - Q.get(key, 0)
            )

            break

        next_state = get_state(board)
        next_actions = get_actions(board)

        if not next_actions:
            break

        next_action = choose_action(next_state, next_actions)

        reward = 0

        old_value = Q.get((state, action), 0)
        next_value = Q.get((next_state, next_action), 0)

        Q[(state, action)] = old_value + alpha * (
            reward + gamma * next_value - old_value
        )

        # SARSA continues with next action


print("SARSA Tic-Tac-Toe training completed.")
print("Number of learned state-action pairs:", len(Q))
