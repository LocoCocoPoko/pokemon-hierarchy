import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('pokemon.csv')

# 2. Filter for "Frauds" (Gen 7 only, Legendary, BST < 600)
frauds = df[(df['is_legendary'] == 1) & (df['generation'] == 7) & (df['base_total'] < 600)].copy()
frauds = frauds.sort_values('base_total')

# 3. Create the Bar Chart
plt.figure(figsize=(12, 14))
ax = plt.gca()

colors = []
for name in frauds['name']:
    if name == 'Cosmog': colors.append('#5D5D81')      # Purple
    elif name == 'Cosmoem': colors.append('#FFD700')    # Gold
    elif name == 'Poipole': colors.append('#9B59B6')    # Purple
    elif name == 'Type: Null': colors.append('#9E9E9E') # Gray
    elif name == 'Silvally': colors.append('#C0C0C0')   # Silver
    elif name == 'Tapu Koko': colors.append('#F1C40F')  # Yellow
    elif name == 'Tapu Lele': colors.append('#E91E63')  # Pink
    elif name == 'Tapu Bulu': colors.append('#E67E22')  # Orange/Red
    elif name == 'Tapu Fini': colors.append('#3498DB')  # Blue
    elif name == 'Nihilego': colors.append('#ECF0F1')   # White/Glass
    elif name == 'Buzzwole': colors.append('#C0392B')   # Muscle Red
    elif name == 'Pheromosa': colors.append('#F5EEF8')  # Cream White
    elif name == 'Xurkitree': colors.append('#2C3E50')  # Wire Black
    elif name == 'Celesteela': colors.append('#A2D9CE') # Bamboo Green
    elif name == 'Kartana': colors.append('#F39C12')    # Paper Orange/White
    elif name == 'Guzzlord': colors.append('#212F3C')   # Void Blue/Black
    elif name == 'Stakataka': colors.append('#566573')  # Stone Gray
    elif name == 'Blacephalon': colors.append('#D7BDE2') # Fireworks Pink/Blue
    elif name == 'Naganadel': colors.append('#6C3483')   # Stinger Purple
    else: colors.append('gray')

bars = plt.barh(frauds['name'], frauds['base_total'], color=colors, edgecolor='black', linewidth=1.5)

# --- Add Text on Bars ---
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 3,       
        bar.get_y() + bar.get_height()/2, 
        f'{int(width)}', 
        va='center',     
        fontweight='bold',
        color='black'    
    )

# --- God Line ---
plt.axvline(600, color='black', linestyle='--', linewidth=3)
plt.text(610, len(frauds) - 7, 'God Threshold (600)', fontsize=10, fontweight='bold', color='black')

# 5. Styling
plt.title("The Hall of Frauds: Gen 7", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Base Stat Total (BST)", fontsize=12)
plt.ylabel("Pokémon Name", fontsize=12)

# Set X-axis from 0 to fit Cosmog
plt.xlim(0, 750) 
plt.ylim(-1, len(frauds))

# Thicker outline box
for spine in ax.spines.values():
    spine.set_linewidth(3.0)

plt.grid(axis='x', linestyle='--', alpha=0.3)
plt.tight_layout()

# 6. Save
plt.savefig('gen7_frauds.png', dpi=300)
plt.show()