# MAXQ Hierarchical Reinforcement Learning
# Simple demonstration

def go_to_item():
    print("Subtask 1: Moving to item...")
    return 2


def pick_item():
    print("Subtask 2: Picking item...")
    return 5


def go_to_customer():
    print("Subtask 3: Moving to customer...")
    return 3


def drop_item():
    print("Subtask 4: Dropping item...")
    return 10


def delivery_task():
    print("Starting main delivery task...\n")

    reward = 0

    reward += go_to_item()
    reward += pick_item()
    reward += go_to_customer()
    reward += drop_item()

    return reward


total_reward = delivery_task()

print("\nDelivery completed!")
print("Total Reward:", total_reward)
