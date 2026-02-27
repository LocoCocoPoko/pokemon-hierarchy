import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv('pokemon.csv')
legends = df[(df['is_legendary'] == 1) & (df['generation'] <= 7)]

# 2. Count Frauds vs True Gods
frauds_count = len(legends[legends['base_total'] < 600])
gods_count = len(legends[legends['base_total'] >= 600])

# 3. Create the Donut Chart
plt.figure(figsize=(8, 8))
labels = [f'Frauds (<600 BST)\n({frauds_count})', f'True Gods (≥600 BST)\n({gods_count})']
sizes = [frauds_count, gods_count]
colors = ['#ff4d4d', '#2ecc71'] # Red for frauds, Green for gods

# Plot
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', 
        startangle=90, pctdistance=0.85, textprops={'fontsize': 12, 'weight': 'bold'})

# Draw a circle in the middle to make it a donut
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Add center text
plt.text(0, 0, f"Legendary\nIntegrity", ha='center', va='center', fontsize=16, fontweight='bold')

plt.title("The Legendary Scandal: Data Breakdown", fontsize=18, fontweight='bold')
plt.tight_layout()
plt.savefig('legendary_donut_chart.png', dpi=300)
plt.show()