import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('pokemon.csv')

# 2. Filter for "Underdogs" (Gen 4 only, Non-Legendary, BST >= 600)
underdogs = df[(df['is_legendary'] == 0) & (df['generation'] == 4) & (df['base_total'] >= 600)].copy()
underdogs = underdogs.sort_values('base_total')

# 3. Create the Bar Chart
plt.figure(figsize=(14, 8))
ax = plt.gca()

colors = []
for name in underdogs['name']:
    if name == 'Lucario':
        colors.append('#2D4F94')  # Mega Lucario Deep Blue
    elif name == 'Gallade':
        colors.append('#6BB577')  # Mega Gallade Cape Green
    elif name == 'Garchomp':
        colors.append('#A52A2A')  # Mega Garchomp Deep Red/Crimson
    else:
        colors.append('gray')

# Plot bars
bars = plt.barh(underdogs['name'], underdogs['base_total'], color=colors, edgecolor='black', linewidth=1.5)

# --- Add Text on Bars ---
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 5, 
        bar.get_y() + bar.get_height()/2,
        f'{int(width)}',
        va='center',
        fontweight='bold',
        color='black'
    )

# --- God Line ---
plt.axvline(600, color='black', linestyle='--', linewidth=3)
text_y_pos = len(underdogs) - 0.2
plt.text(605, text_y_pos, 'God Threshold (600)', fontsize=12, fontweight='bold', color='black')

# 5. Styling
plt.title("The Underdogs: Gen 4", fontsize=20, fontweight='bold', pad=20)
plt.xlabel("Base Stat Total (BST)", fontsize=14, labelpad=15)
plt.ylabel("Pokémon Name", fontsize=14, labelpad=15)

# --- PADDING & SPACING ---
plt.xlim(350, 750) 
plt.ylim(-1, len(underdogs) + 0.2)

# Thick Outline
for spine in ax.spines.values():
    spine.set_linewidth(3.0) 

# Outer Margins
plt.subplots_adjust(left=0.15, right=0.9, top=0.75, bottom=0.15)

plt.grid(axis='x', linestyle='--', alpha=0.5)

# 6. Save
plt.savefig('gen4_underdogs.png', dpi=300)
plt.show()