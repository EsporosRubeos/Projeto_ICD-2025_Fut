import pandas as pd
import os

# Create the data directory for storing the datasets
os.makedirs('data', exist_ok=True)

# scrape the pages for the years 2024 to 2014 
for page in range(11):
    
    url = f"https://fbref.com/en/comps/24/{2024 - page}/{2024 - page}-Serie-A-Stats"
    tables = pd.read_html(url)
    
    # Convert each table to a DataFrame
    dfs = {f"df_{2024 - page}_{i+1}": table for i, table in enumerate(tables)}

    # Convert each table into a .csv file
    for name, df in dfs.items():
        df.to_csv(f"data/{name}.csv", index=False)