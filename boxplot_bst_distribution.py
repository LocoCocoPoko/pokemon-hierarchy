import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('pokemon.csv')

# 2. Separate the Groups
regulars = df[df['is_legendary'] == 0]['base_total']
legends = df[df['is_legendary'] == 1]['base_total']

# 3. Calculate and Print Statistics
print("--- Non-Legendary Pokémon ---")
print(f"Mean BST:   {regulars.mean():.2f}")
print(f"Median BST: {regulars.median():.2f}")
print(f"Std Dev:    {regulars.std():.2f}\n")

print("--- Legendary Pokémon ---")
print(f"Mean BST:   {legends.mean():.2f}")
print(f"Median BST: {legends.median():.2f}")
print(f"Std Dev:    {legends.std():.2f}\n")

# 4. Build the Graph (Boxplot)
plt.figure(figsize=(10, 8))
ax = plt.gca()

# Customize boxplot aesthetics
box_colors = ['#3498db', '#e67e22'] # Blue for Regulars, Orange for Legends
box_data = [regulars, legends]

bp = ax.boxplot(
    box_data, 
    patch_artist=True, 
    widths=0.5,
    boxprops=dict(facecolor='white', color='black', linewidth=2),
    capprops=dict(color='black', linewidth=2),
    whiskerprops=dict(color='black', linewidth=2),
    flierprops=dict(marker='o', color='black', alpha=0.5),
    medianprops=dict(color='black', linewidth=3) 
)

# Apply colors to the boxes
for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# 5. Add the Competitive Threshold Line
plt.axhline(600, color='red', linestyle='--', linewidth=3, label='Competitive Threshold (600)')

# Titles and Labels
plt.title("BST Distribution: Legendary vs Non-Legendary", fontsize=18, fontweight='bold', pad=20)
plt.ylabel("Base Stat Total (BST)", fontsize=14, labelpad=15)
plt.xticks([1, 2], ['Non-Legendary', 'Legendary'], fontsize=14, fontweight='bold')

# Thick Outline for Presentation
for spine in ax.spines.values():
    spine.set_linewidth(2.5)

# Grid and Legend
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(loc='lower right', fontsize=12, framealpha=1, edgecolor='black')

# Outer Margins
plt.subplots_adjust(left=0.15, right=0.9, top=0.85, bottom=0.15)

# 6. Save and Show
plt.savefig('boxplot_bst_distribution.png', dpi=300)
plt.show()