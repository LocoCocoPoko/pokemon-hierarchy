import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('pokemon.csv')

# 2. Filter for "Frauds" (Gen 2 only)
frauds = df[(df['is_legendary'] == 1) & (df['generation'] == 2) & (df['base_total'] < 600)]
frauds = frauds.sort_values('base_total')

# 3. Create the Bar Chart
plt.figure(figsize=(10, 6))


colors = []
for name in frauds['name']:
    if name == 'Suicune':
        colors.append('#3498db') # bright blue
    elif name == 'Entei':
        colors.append('#e74c3c') # bright red
    elif name == 'Raikou':
        colors.append('yellow') # bright yellow
    else:
        colors.append('gray')

bars = plt.barh(frauds['name'], frauds['base_total'], color=colors,edgecolor='black',linewidth=1.5)

for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 1,       
        bar.get_y() + bar.get_height()/2,
        f'{int(width)}', 
        va='center',     
        fontweight='bold',
        color='black'   
    )

plt.axvline(600, color='black', linestyle='--', linewidth=3)

text_y_pos = len(frauds) - 2.0
plt.text(602, text_y_pos, 'God Threshold (600)', fontsize=10, fontweight='bold', color='black')

# 5. Styling
plt.title("The Hall of Frauds: Gen 2", fontsize=16, fontweight='bold')
plt.xlabel("Base Stat Total (BST)", fontsize=12)
plt.ylabel("Pokémon Name", fontsize=12)

plt.xlim(400, 650) 

plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()

# 6. Save
plt.savefig('gen2_frauds.png', dpi=300)
plt.show()