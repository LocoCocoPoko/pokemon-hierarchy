import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('pokemon.csv')

# 2. Filter for "Frauds" (Gen 4 only: Uxie, Mesprit, Azelf)
frauds = df[(df['is_legendary'] == 1) & (df['generation'] == 5) & (df['base_total'] < 600)]
frauds = frauds.sort_values('base_total')

# 3. Create the Bar Chart
plt.figure(figsize=(10, 6))

# --- ONLY CHANGE: Define Custom Colors for the Lake Guardians ---
colors = []
for name in frauds['name']:
    if name == 'Uxie':
        colors.append('#F0D860') # Yellow (Knowledge)
    elif name == 'Mesprit':
        colors.append('#F080B0') # Pink (Emotion)
    elif name == 'Azelf':
        colors.append('#60A8D8') # Blue (Willpower)
    else:
        colors.append('gray')

bars = plt.barh(frauds['name'], frauds['base_total'], color=colors, edgecolor='black', linewidth=1.5)

# --- FIX 1: Add the "580" Text on the bars ---
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 1,       # X-position
        bar.get_y() + bar.get_height()/2, # Y-position
        f'{int(width)}', # The text
        va='center',     
        fontweight='bold',
        color='black'    
    )

# --- FIX 2: Add the "God Line" and fix text position ---
plt.axvline(600, color='black', linestyle='--', linewidth=3)

# Positioning the text relative to the number of bars
text_y_pos = len(frauds) - 3.5
plt.text(602, text_y_pos, 'God Threshold (600)', fontsize=10, fontweight='bold', color='black')

# 5. Styling
plt.title("The Hall of Frauds: Gen 5", fontsize=16, fontweight='bold')
plt.xlabel("Base Stat Total (BST)", fontsize=12)
plt.ylabel("Pokémon Name", fontsize=12)

# --- FIX 3: Zoom so we see the gap between 580 and 600 ---
plt.xlim(400, 650) 

plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()

# 6. Save
plt.savefig('gen5_frauds.png', dpi=300)
plt.show()