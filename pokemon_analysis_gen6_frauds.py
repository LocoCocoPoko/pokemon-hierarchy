import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('pokemon.csv')

frauds = df[(df['is_legendary'] == 1) & (df['generation'] == 6) & (df['base_total'] < 600)].copy()
frauds = frauds.sort_values('base_total')

# 3. Create the Bar Chart
plt.figure(figsize=(12, 8))
ax = plt.gca()

colors = []
for name in frauds['name']:
    if name == 'Cobalion':
        colors.append('#7196B0') # Steel Blue
    elif name == 'Terrakion':
        colors.append('#A59782') # Rock Brown
    elif name == 'Virizion':
        colors.append('#78A560') # Grass Green
    elif name == 'Keldeo':
        colors.append('#48A8A8') # Water Teal
    elif name == 'Tornadus':
        colors.append('#70C888') # Sky Green
    elif name == 'Thundurus':
        colors.append('#70B8F0') # Electric Blue
    elif name == 'Landorus':
        colors.append('#F08030') # Earth Orange
    else:
        colors.append('gray')

bars = plt.barh(frauds['name'], frauds['base_total'], color=colors, edgecolor='black', linewidth=1.5)

for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 2,       
        bar.get_y() + bar.get_height()/2, 
        f'{int(width)}', 
        va='center',     
        fontweight='bold',
        color='black'    
    )

plt.axvline(600, color='black', linestyle='--', linewidth=3)

# Positioning the text near the top
text_y_pos = len(frauds) - 3.5
plt.text(602, text_y_pos, 'God Threshold (600)', fontsize=10, fontweight='bold', color='black')

# 5. Styling
plt.title("The Hall of Frauds: Gen 6", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Base Stat Total (BST)", fontsize=12)
plt.ylabel("Pokémon Name", fontsize=12)

plt.xlim(400, 700) 
plt.ylim(-1, len(frauds))

# Thicker outline box
for spine in ax.spines.values():
    spine.set_linewidth(3.0)

plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()

# 6. Save
plt.savefig('gen6_frauds.png', dpi=300)
plt.show()