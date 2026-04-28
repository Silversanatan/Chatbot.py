from scipy.stats import norm

# (a) Area to the right of z is 0.3622
# This means P(Z > z) = 0.3622, so P(Z <= z) = 1 - 0.3622
z_a = norm.ppf(1 - 0.3622)

# (b) Area to the left of z is 0.1131
# This means P(Z <= z) = 0.1131
z_b = norm.ppf(0.1131)

# (c) Area between 0 and z, with z > 0, is 0.4838
# Since P(Z <= 0) = 0.5, then P(Z <= z) = 0.5 + 0.4838
z_c = norm.ppf(0.5 + 0.4838)

# (d) Area between -z and z, with z > 0, is 0.9500
# The remaining area is 1 - 0.95 = 0.05. 
# Due to symmetry, each tail has 0.025. So P(Z <= z) = 1 - 0.025 = 0.975
z_d = norm.ppf((1 + 0.9500) / 2)

print(f"(a) z = {z_a:.4f}")
print(f"(b) z = {z_b:.4f}")
print(f"(c) z = {z_c:.4f}")
print(f"(d) z = {z_d:.4f}")



from scipy.stats import norm

# Parameters: Mean (mu) and Standard Deviation (sigma)
mu = 30
sigma = 2

# (a) What percentage of the loaves are longer than 31.7 cm?
# We want P(X > 31.7). This is 1 - P(X <= 31.7).
prob_a = 1 - norm.cdf(31.7, loc=mu, scale=sigma)
percent_a = prob_a * 100

# (b) What percentage are between 29.3 and 33.5 cm?
# We want P(29.3 < X < 33.5). This is P(X <= 33.5) - P(X <= 29.3).
prob_b = norm.cdf(33.5, loc=mu, scale=sigma) - norm.cdf(29.3, loc=mu, scale=sigma)
percent_b = prob_b * 100

# (c) What percentage are shorter than 25.5 cm?
# We want P(X < 25.5). This is simply P(X <= 25.5).
prob_c = norm.cdf(25.5, loc=mu, scale=sigma)
percent_c = prob_c * 100

# Display results
print(f"(a) Longer than 31.7 cm: {percent_a:.2f}%")
print(f"(b) Between 29.3 and 33.5 cm: {percent_b:.2f}%")
print(f"(c) Shorter than 25.5 cm: {percent_c:.2f}%")


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters for b(x; 15, 0.4)
n, p = 15, 0.4
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

# 1. Define the range of x values (0 to 15)
x_discrete = np.arange(0, n + 1)
x_continuous = np.linspace(0, n, 100)

# 2. Calculate probabilities
# PMF for the Binomial bars
binomial_pmf = binom.pmf(x_discrete, n, p)
# PDF for the Normal curve
normal_pdf = norm.pdf(x_continuous, mu, sigma)

# 3. Create the plot
plt.figure(figsize=(8, 5))

# Plot the Binomial Distribution as bars
# width=1.0 makes the bars touch like a histogram
plt.bar(x_discrete, binomial_pmf, width=1.0, color='white', edgecolor='black', label='Binomial PMF')

# Plot the Normal Approximation as a blue line
plt.plot(x_continuous, normal_pdf, color='#00aaff', linewidth=2.5, label='Normal Approximation')

# Formatting to match the figure style
plt.title(f"Normal approximation of b(x; {n}, {p})")
plt.xlabel("x")
plt.xticks(x_discrete) # Show all integer labels on x-axis
plt.ylim(0, max(binomial_pmf) + 0.05)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.show()