import matplotlib.pyplot as plt
import numpy as np

# Lamp lifetime data in hours
lifetimes = [
    919, 1196, 785, 1126, 936, 918, 1156, 920, 948, 1067, 1092, 1162,
    1170, 929, 950, 905, 972, 1035, 1045, 855, 1195, 1195, 1340, 1122,
    938, 970, 1237, 956, 1102, 1157, 978, 832, 1009, 1157, 1151, 1009,
    765, 958, 902, 1022, 1333, 811, 1217, 1085, 896, 958, 1311, 1037,
    702, 923
]

# Create the box plot
plt.figure(figsize=(10, 5))
plt.boxplot(lifetimes, vert=False, patch_artist=True, 
            boxprops=dict(facecolor='skyblue', color='navy'),
            medianprops=dict(color='red', linewidth=2))

plt.title('Box Plot of Lamp Lifetimes (Hours)')
plt.xlabel('Hours')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.show()

# Calculating IQR and potential outliers for verification
q1, q3 = np.percentile(lifetimes, [25, 75])
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = [x for x in lifetimes if x < lower_bound or x > upper_bound]

print(f"Q1 (25th percentile): {q1}")
print(f"Q3 (75th percentile): {q3}")
print(f"IQR: {iqr}")
print(f"Outliers detected: {outliers}")