import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('pokemon.csv')

# 2. Separate the Groups
regulars = df[df['is_legendary'] == 0]['base_total']
legends = df[df['is_legendary'] == 1]['base_total']

# 3. Build the Graph (Overlapping Histograms)
plt.figure(figsize=(12, 8))
ax = plt.gca()

# Plot histograms with transparency (alpha)
plt.hist(regulars, bins=30, color='#3498db', alpha=0.6, edgecolor='white', linewidth=1.5, label='Non-Legendary')
plt.hist(legends, bins=30, color='#e67e22', alpha=0.7, edgecolor='white', linewidth=1.5, label='Legendary')

# 4. Add the Competitive Threshold Line
plt.axvline(600, color='red', linestyle='--', linewidth=3, label='God Threshold (600)')

# Titles and Labels
plt.title("BST Distribution Overlap", fontsize=20, fontweight='bold', pad=20)
plt.xlabel("BST", fontsize=14, labelpad=15)
plt.ylabel("Frequency", fontsize=14, labelpad=15)

# Thick Outline for Presentation
for spine in ax.spines.values():
    spine.set_linewidth(2.5)

# Grid and Legend
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(loc='upper right', fontsize=12, framealpha=1, edgecolor='black')

# Outer Margins
plt.subplots_adjust(left=0.15, right=0.9, top=0.85, bottom=0.15)

# 5. Save and Show
plt.savefig('histogram_bst_overlap.png', dpi=300)
plt.show()