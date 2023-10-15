import numpy as np
import matplotlib.pyplot as plt

#[0,1]
BEST_CHOICE = 0.5 
ITERATIONS = 2000

def calculate_regret(predicted, actual):
    """Calculate the regret for given choices."""
    regret_diff = np.square(predicted - actual)
    return regret_diff.sum() - np.square(BEST_CHOICE - actual).sum()

def total_loss(predicted, actual):
    """Calculate total loss."""
    return np.square(predicted - actual).sum()

user_decisions = np.array([])
enemy_decisions = np.array([])
stored_regret = np.array([])
ftl_loss_data = np.array([])
best_case_cum_loss = np.array([])

for step in range(ITERATIONS):
    user_value = enemy_decisions.mean()
    if not user_decisions.size:
        user_value = BEST_CHOICE   
    enemy_value = np.random.uniform()
    
    enemy_decisions = np.hstack([enemy_decisions, enemy_value])
    user_decisions = np.hstack([user_decisions, user_value])
    
    stored_regret = np.hstack([stored_regret, calculate_regret(user_decisions, enemy_decisions)])
    ftl_loss_data = np.hstack([ftl_loss_data, total_loss(user_decisions, enemy_decisions)])
    best_case_cum_loss = np.hstack([best_case_cum_loss, total_loss(np.full_like(enemy_decisions, BEST_CHOICE), enemy_decisions)])


# Plotting the stored regret over time
plt.figure(figsize=(10, 5))
plt.plot(stored_regret, label="Stored Regret")
plt.title("Regret over Time")
plt.xlabel("Time")
plt.ylabel("Regret")
plt.legend()
plt.grid(True)
plt.show()

# Plotting the follow-the-leader loss over time
plt.figure(figsize=(10, 5))
plt.plot(ftl_loss_data, label="FTL Loss")
plt.title("FTL Loss over Time")
plt.xlabel("Time")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()

# Plotting the average loss over time
plt.figure(figsize=(10, 5))
plt.plot(best_case_cum_loss, label="best single value loss")
plt.title("best single over Time")
plt.xlabel("Time")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()