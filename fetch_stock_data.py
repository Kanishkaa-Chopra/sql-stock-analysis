import yfinance as yf
import pandas as pd
import os

# Create the folder if it doesn't exist
os.makedirs('stock_data', exist_ok=True)

# Define the ticker and date range
ticker = 'AFFLE.NS'
start_date = '2019-01-01'
end_date = '2024-12-31'

# Download data with yfinance
data = yf.download(ticker, start=start_date, end=end_date, group_by='ticker')

# If data has multi-level columns, flatten it
if isinstance(data.columns, pd.MultiIndex):
    # Rename columns: ('AAPL', 'Close') → 'Close'
    data.columns = [col[1] for col in data.columns]

# Reset the index to move Date from index to column
data.reset_index(inplace=True)

# Keep only the desired columns in a standard order
#columns_to_keep = ['Date', 'Open', 'High', 'Low', 'Close',  'Volume']
#data = data[columns_to_keep]
print(data.head())
# Save to CSV
csv_path = f'stock_data/{ticker}_stock_data.csv'
data.to_csv(csv_path, index=False)

print(f"{ticker} stock data saved to {csv_path}")
