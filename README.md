# SQL Stock Analysis (AAFL)

This repository contains a complete pipeline for fetching, loading, and analyzing historical stock data using **Python**, **SQLite**, and **SQL**. The example stock chosen here is **AAFL**, but you can easily swap in any other ticker. By the end of this project, you will have:

1. A local **CSV** of daily OHLCV data.
2. A **SQLite** database (`.db`) containing the same data in a `stock_prices` table.
3. A set of standalone **SQL scripts** (in `sql_queries/`) that compute:
   - 5-day moving average
   - 1-day lag & lead
   - (Volatility is computed in Python)
   - A combined “full analysis” query
4. A **Python analysis** that reads from SQLite, computes rolling volatility, and exports a final `analysis_results.csv`.
5. Instructions for opening and exploring the DB in **DB Browser for SQLite** (or VS Code’s SQLite extension).
6. A suggested folder structure you can push directly to GitHub.

---

- **`fetch_stock_data.py`**  
  Downloads historical OHLCV for AAFL (or any specified ticker), flattens columns, and writes a CSV to `stock_data/`.

- **`load_to_sql.py`**  
  Reads the CSV from `stock_data/`, converts types, and writes to a SQLite database (`stock_data/stock_data.db`) in a table named `stock_prices`.

- **`analyze_stock.py`**  
  Connects to the SQLite DB, runs a SQL query (for MA, lag, lead), then uses pandas to compute a 5-day rolling volatility. The final result is exported to `stock_data/analysis_results.csv`.

- **`stock_data/`**  
  - `AAFL_stock_data.csv` – The raw CSV of Date / Open / High / Low / Close / Volume.  
  - `stock_data.db` – The generated SQLite file containing a table `stock_prices`.

- **`sql_queries/`**  
  Standalone SQL scripts you can run inside any SQLite client. 

- **`screenshots/`**  

---

## 📦 Dependencies

1. **Python 3.8+**  
2. **pip** (for installing Python packages)  
3. **yfinance**  
4. **pandas**  
5. **sqlite3** (standard library)  
6. **DB Browser for SQLite** (or any SQLite client/VS Code SQLite extension)
