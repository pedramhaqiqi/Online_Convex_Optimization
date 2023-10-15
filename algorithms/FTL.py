import numpy as np
import matplotlib.pyplot as plt

#[0,1]
BEST_CHOICE = 0.5
ITERATIONS = 1000

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
our_cum_loss = np.array([])
best_case_cum_loss = np.array([])

for step in range(ITERATIONS):
    user_value = enemy_decisions.mean()
    if not user_decisions.size:
        user_value = BEST_CHOICE   
    # Maximize FTL over [0,1], try with uniform and see that the regret is less. 
    # This is showing that we can have a tigher lower bound on the regret.  sigma^2 Ω (log T) < Regret < O(logT)
    # So as yourself, what distribution on [0,1] at each sample, will have biggest variance with mean 1/2? Bernouli(1/2)
    enemy_value = np.random.binomial(1, 1/2) 
    
    enemy_decisions = np.hstack([enemy_decisions, enemy_value])
    user_decisions = np.hstack([user_decisions, user_value])
    
    stored_regret = np.hstack([stored_regret, calculate_regret(user_decisions, enemy_decisions)])
    our_cum_loss = np.hstack([our_cum_loss, total_loss(user_decisions, enemy_decisions)])
    best_case_cum_loss = np.hstack([best_case_cum_loss, total_loss(np.full_like(enemy_decisions, BEST_CHOICE), enemy_decisions)])

# Create a figure with three vertically stacked subplots
plt.figure(figsize=(10, 15))

# First subplot: Stored Regret
plt.subplot(3, 1, 1)  # 3 rows, 1 column, first subplot
plt.plot(stored_regret, label="Stored Regret")
plt.title("Regret over Time")
plt.xlabel("Time")
plt.ylabel("Regret")
plt.legend()
plt.grid(True)

# Add a log function on top of the Regret plot
x = np.linspace(1, len(stored_regret), len(stored_regret))
log_curve = 1/10 * np.log(x)
plt.plot(x, log_curve, label="log(x)", linestyle="--", color="red")
plt.legend()


# Second subplot: Our cum Loss
plt.subplot(3, 1, 2)  # 3 rows, 1 column, second subplot
plt.plot(our_cum_loss, label="Our cum Loss")
plt.title("Our cum loss over Time")
plt.xlabel("Time")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

# Third subplot: best single value loss
plt.subplot(3, 1, 3)  # 3 rows, 1 column, third subplot
plt.plot(best_case_cum_loss, label="Best single value loss")
plt.title("Best Single Value Loss over Time")
plt.xlabel("Time")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

# Adjust the layout
plt.tight_layout()

# Show the plots
plt.show()
