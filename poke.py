import pandas as pd
import matplotlib.pyplot as plt

# 1. Load and filter for Gen 1-7
df = pd.read_csv('pokemon.csv')
gen7_df = df[df['generation'] <= 7]

# 2. Identify the "Frauds" (Legendary but BST < 600)
frauds = gen7_df[(gen7_df['is_legendary'] == 1) & (gen7_df['base_total'] < 600)]
frauds = frauds.sort_values('base_total', ascending=True)

# 3. Plotting
plt.figure(figsize=(10, 8))
colors = ['#ff4d4d' if x < 600 else '#4dff4d' for x in frauds['base_total']]

plt.barh(frauds['name'], frauds['base_total'], color='#ff4d4d')

# 4. Add the "God Threshold" line
plt.axvline(600, color='black', linestyle='--', linewidth=2)
plt.text(602, 1, 'God Threshold (600)', fontweight='bold', color='black')

# 5. Styling
plt.title("The Hall of Frauds: Legendaries Below 600 BST", fontsize=16)
plt.xlabel("Base Stat Total (BST)")
plt.xlim(550, 610) # Zoom in to show the gap clearly
plt.grid(axis='x', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('hall_of_frauds.png')
plt.show()