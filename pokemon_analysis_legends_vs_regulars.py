import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('pokemon.csv')

# Keep only Gen 1 through Gen 7
df = df[df['generation'] <= 7]

# Separate the Groups
regulars = df[df['is_legendary'] == 0]['base_total']
legends = df[df['is_legendary'] == 1]['base_total']

plt.figure(figsize=(12, 8))
ax = plt.gca()

# Set up jitter to prevent dot overlap
np.random.seed(42)
jitter_strength = 0.08

# Generate X-coordinates (1 for Regulars, 2 for Legendaries) + jitter
x_regs = np.random.normal(1, jitter_strength, size=len(regulars))
x_legs = np.random.normal(2, jitter_strength, size=len(legends))

# Plot the scatter points
plt.scatter(x_regs, regulars, color='#3498db', alpha=0.6, edgecolors='white', linewidth=1, s=70, label='Non-Legendary')
plt.scatter(x_legs, legends, color='#e67e22', alpha=0.8, edgecolors='white', linewidth=1, s=70, label='Legendary')


# The Red Line at 600 BST (The "God Tier" threshold)
plt.axhline(600, color='red', linestyle='--', linewidth=3, label='God Threshold (600)')

plt.title("The Power Overlap: Legendaries vs. Regulars", fontsize=20, fontweight='bold', pad=20)
plt.ylabel("Base Stat Total (BST)", fontsize=14, labelpad=15)

plt.xticks([1, 2], ['Non-Legendary', 'Legendary'], fontsize=14, fontweight='bold')
plt.xlim(0.5, 2.5)

# Thick Outline for that clean, competition-ready look
for spine in ax.spines.values():
    spine.set_linewidth(2.5)

plt.legend(loc='lower right', fontsize=12, framealpha=1, edgecolor='black')

# Grid
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Outer Margins
plt.subplots_adjust(left=0.15, right=0.9, top=0.85, bottom=0.15)

# 6. Save and Show
plt.savefig('scatter_legends_vs_regulars.png', dpi=300) 
plt.show()