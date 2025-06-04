import pandas as pd
import sqlite3
import os

# File paths
csv_file = 'stock_data/AAPL_stock_data.csv'
db_file = 'stock_data/stock_data.db'

# Load CSV into DataFrame
df = pd.read_csv(csv_file)

# Ensure correct data types
numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Convert Date to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Connect to SQLite and write to table
conn = sqlite3.connect(db_file)
df.to_sql('stock_prices', conn, if_exists='replace', index=False)

conn.close()

print(f"✅ Data loaded into database at {db_file}")
print(df.head())