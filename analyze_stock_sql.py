import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('stock_data/stock_data.db')

# Correct SQL query using Date
query = """
SELECT 
    Date,
    Open,
    High,
    Low,
    Close,
    Volume,

    -- 5-day Moving Average
    AVG(Close) OVER (ORDER BY Date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS MA_5,

    -- 1-day Lag
    LAG(Close, 1) OVER (ORDER BY Date) AS Lag_Close,

    -- 1-day Lead
    LEAD(Close, 1) OVER (ORDER BY Date) AS Lead_Close

FROM stock_prices
ORDER BY Date;
"""

# Read SQL result into DataFrame
df = pd.read_sql_query(query, conn)

# Convert full timestamp to short date
df['Date'] = pd.to_datetime(df['Date']).dt.date

# Compute rolling volatility in pandas
df['Volatility_5'] = df['Close'].rolling(window=5).std()

# Close DB connection
conn.close()

# Export to CSV
df.to_csv('stock_data/analysis_results.csv', index=False)

print("✅ Analysis complete. Cleaned data saved to: stock_data/analysis_results.csv")
