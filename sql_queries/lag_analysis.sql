SELECT 
    Date,
    Close,
    LAG(Close, 1) OVER (ORDER BY Date) AS Lag_Close,
    LEAD(Close, 1) OVER (ORDER BY Date) AS Lead_Close
FROM stock_prices
ORDER BY Date;
