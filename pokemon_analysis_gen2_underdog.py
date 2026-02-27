import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('pokemon.csv')

# 2. Filter for "Underdogs" (Gen 2 only, Non-Legendary, BST >= 600)
underdogs = df[(df['is_legendary'] == 0) & (df['generation'] == 2) & (df['base_total'] >= 600)].copy()
underdogs = underdogs.sort_values('base_total')

# 3. Create the Bar Chart
fig, ax = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor('white')

colors = []
for name in underdogs['name']:
    if name == 'Tyranitar':
        colors.append('#5D9035')  # Mega Green
    elif name == 'Ampharos':
        colors.append('#FBEE81')  # Mega Yellow
    elif name == 'Steelix':
        colors.append('#8DB3C4')  # Mega Steelix Silver/Blue
    elif name == 'Houndoom':
        colors.append('#3E3E3E')  # Mega Dark Gray
    elif name == 'Scizor':
        colors.append('#D8334A')  # Mega Crimson Red
    elif name == 'Heracross':
        colors.append('#3B5998')  # Mega Beetle Blue
    else:
        colors.append('gray')

# Plot bars
bars = ax.barh(underdogs['name'], underdogs['base_total'], color=colors, edgecolor='black', linewidth=2)

# --- Add Text on Bars ---
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 5, 
        bar.get_y() + bar.get_height()/2,
        f'{int(width)}',
        va='center',
        fontweight='bold',
        color='black',
        fontsize=12
    )

# --- God Line ---
ax.axvline(600, color='black', linestyle='--', linewidth=3)
text_y_pos = len(underdogs) - 0.5
ax.text(605, text_y_pos, 'God Threshold (600)', fontsize=12, fontweight='bold', color='black')

# 4. Styling
ax.set_title("The Underdogs: Gen 2", fontsize=22, fontweight='bold', pad=25)
ax.set_xlabel("Base Stat Total (BST)", fontsize=14, labelpad=15)
ax.set_ylabel("Pokémon Name", fontsize=14, labelpad=15)

ax.set_xlim(350, 750) 
ax.set_ylim(-1, len(underdogs))

# Thick Outline
for spine in ax.spines.values():
    spine.set_linewidth(3.5) 

# Outer Margins
plt.subplots_adjust(left=0.2, right=0.8, top=0.85, bottom=0.15)

ax.grid(axis='x', linestyle='--', alpha=0.5)

# 5. Save
plt.savefig('gen2_underdogs.png', dpi=300)
plt.show()