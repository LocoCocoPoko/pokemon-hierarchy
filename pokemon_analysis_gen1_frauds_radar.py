import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# 1. Load data
df = pd.read_csv('pokemon.csv')

# 2. Filter for the birds
birds_names = ['Articuno', 'Zapdos', 'Moltres']
birds_data = df[df['name'].isin(birds_names)].set_index('name')
birds_data = birds_data.reindex(birds_names)

# 3. Define stats
categories = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']
labels = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
N = len(categories)

# 4. Calculate angles
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

colors = {'Articuno': '#00BFFF', 'Zapdos': '#FFD700', 'Moltres': '#FF4500'}

# 5. Create Plot
fig, axes = plt.subplots(1, 3, figsize=(24, 10), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('white')

plt.subplots_adjust(wspace=0.8, top=0.85, bottom=0.05)

for ax, name in zip(axes.flatten(), birds_names):
    values = birds_data.loc[name, categories].tolist()
    values_loop = values + values[:1]
    
    color = colors[name]
    
    # Plot line
    ax.plot(angles, values_loop, linewidth=2, linestyle='solid', color=color)
    ax.fill(angles, values_loop, color=color, alpha=0.4)
    
    # Setup Axis
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    
    # Draw axis labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, size=12, weight='bold')
    ax.tick_params(axis='x', pad=40) # Push labels OUT
    
    # Remove y-axis labels
    ax.set_yticklabels([])
    ax.set_yticks([50, 100, 150]) 
    ax.set_ylim(0, 210) 
    
    # Add values
    for angle, value in zip(angles[:-1], values):
        deg = np.degrees(angle)
        
        ha = 'center' 
        va = 'center'
        
        if np.isclose(deg, 0):             # Top (HP)
            va = 'bottom'
        elif 0 < deg < 180:                # Right Side
            ha = 'left'
        elif np.isclose(deg, 180):         # Bottom (Sp Atk)
            va = 'top'
        elif 180 < deg < 360:              # Left Side
            ha = 'right'
            
        ax.text(angle, value + 30, str(value), 
                size=12, color='black', weight='bold',
                ha=ha, va=va)

    # Title moved up
    ax.set_title(name, size=24, color=color, weight='bold', y=1.3)
    ax.grid(color='#AAAAAA', alpha=0.3)

plt.savefig('legendary_birds_radar_spaced_out.png', bbox_inches='tight')
plt.show()