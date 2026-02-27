import pandas as pd

#Loading the raw data!! THERES SO MUCH EXTRA STUFF IN HERE WE DONT NEED IN HERE!! LETS CLEAN IT UP AND MAKE A BRAND NEW CSV FILE WITH JUST THE COLUMNS WE CARE ABOUT!!
df = pd.read_csv('pokemon.csv')

#We will only be needing these columns moving forward, so we will filter the DataFrame to keep only these columns and then save it as a new CSV file for all future analysis and plotting!
columns_to_keep = [
    'name', 
    'generation', 
    'is_legendary', 
    'base_total', 
    'hp', 
    'attack', 
    'defense', 
    'sp_attack', 
    'sp_defense', 
    'speed',
    'type1', 
    'type2'
]

#Filter the DataFrame to keep ONLY those columns
cleaned_df = df[columns_to_keep]

#Save it as a brand new, lightweight CSV file
cleaned_df.to_csv('pokemon.csv', index=False)

#Print a quick summary to show it worked!
print("Data successfully cleaned!")
print(f"Original number of columns: {len(df.columns)}")
print(f"Cleaned number of columns: {len(cleaned_df.columns)}")
print("Your new file 'pokemon.csv' is ready to go!")