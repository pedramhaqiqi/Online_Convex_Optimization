import math
import matplotlib.pyplot as plt

x = 0
losses = [0]  # Store losses in a separate list
z = -0.5
T_values = list(range(2, 1000)) 
T_= 1000 # Create a list of T values from 2 to 256
best = [0]

for T in T_values:
    if T % 2 == 0:
        z = 1
    else:
        z = -1
    x = x - (2 / math.sqrt(T)) * z
    losses.append(x * z)

# Plot the losses with respect to T
plt.plot(T_values, losses[1:])  # Start from the second element to match the R code
plt.xlabel('T')
plt.ylabel('Loss')
plt.title('Losses vs. T')
plt.grid(True)
plt.show()
