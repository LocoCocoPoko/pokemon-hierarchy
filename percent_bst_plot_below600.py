import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('pokemon.csv')

# 2. Calculate the specific counts and percentages
total_legends = len(df[df['is_legendary'] == 1])
total_regulars = len(df[df['is_legendary'] == 0])

legends_below_600 = len(df[(df['is_legendary'] == 1) & (df['base_total'] < 600)])
regulars_below_600 = len(df[(df['is_legendary'] == 0) & (df['base_total'] < 600)])

pct_legends_below = (legends_below_600 / total_legends) * 100 if total_legends > 0 else 0
pct_regulars_below = (regulars_below_600 / total_regulars) * 100 if total_regulars > 0 else 0

# 3. Create the Bar Chart
plt.figure(figsize=(10, 8))
ax = plt.gca()

# Data for plotting
categories = ['Legendary', 'Non-Legendary']
percentages = [pct_legends_below, pct_regulars_below]
colors = ['#e74c3c', '#3498db'] # Red for Legendary, Blue for Non-Legendary

bars = plt.bar(categories, percentages, color=colors, edgecolor='black', linewidth=2, width=0.5)

# --- Add Value Labels on top of bars ---
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2, 
        height + 1.5, 
        f'{height:.1f}%', 
        ha='center', 
        va='bottom', 
        fontweight='bold', 
        fontsize=16,
        color='black'
    )

# 4. Styling and Formatting
plt.title("Legendary and Regular Pokémon Below 600 BST", fontsize=18, fontweight='bold', pad=20)
plt.ylabel("Percentage of Pokémon Below 600 BST", fontsize=14, labelpad=15)

plt.ylim(0, max(percentages) + 15)

plt.xticks(fontsize=14, fontweight='bold')
plt.yticks(fontsize=12)

for spine in ax.spines.values():
    spine.set_linewidth(2.5)

ax.set_axisbelow(True)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Save and Show
plt.tight_layout()
plt.savefig('pct_below_600_bst.png', dpi=300)
plt.show()