import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('pokemon.csv')

# 2. Compute average BST per Generation for Legendary and Non-Legendary
# Group by generation and is_legendary, then calculate the mean of base_total
avg_bst = df.groupby(['generation', 'is_legendary'])['base_total'].mean().unstack()

# 3. Create the Line Plot
plt.figure(figsize=(12, 8))
ax = plt.gca()

# Plot Non-Legendary (is_legendary = 0)
plt.plot(
    avg_bst.index, 
    avg_bst[0], 
    marker='o', 
    markersize=10, 
    linewidth=3, 
    color='#3498db', 
    label='Non-Legendary'
)

# Plot Legendary (is_legendary = 1)
plt.plot(
    avg_bst.index, 
    avg_bst[1], 
    marker='s', 
    markersize=10, 
    linewidth=3, 
    color='#e67e22', 
    label='Legendary'
)

# 4. Add the 600 Threshold Line
plt.axhline(600, color='red', linestyle='--', linewidth=3, label='God Threshold (600)')

# 5. Styling
plt.title("Average BST by Generation", fontsize=20, fontweight='bold', pad=20)
plt.xlabel("Generation", fontsize=14, labelpad=15)
plt.ylabel("Average Base Stat Total (BST)", fontsize=14, labelpad=15)

# Ensure X-axis shows whole numbers for generations
plt.xticks(avg_bst.index, fontsize=12, fontweight='bold')
plt.yticks(fontsize=12)

# Thick Outline for Presentation
for spine in ax.spines.values():
    spine.set_linewidth(2.5)

# Grid and Legend
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='best', fontsize=12, framealpha=1, edgecolor='black')

# Outer Margins
plt.subplots_adjust(left=0.15, right=0.9, top=0.85, bottom=0.15)

# 6. Save and Show
plt.savefig('avg_bst_by_generation.png', dpi=300)
plt.show()