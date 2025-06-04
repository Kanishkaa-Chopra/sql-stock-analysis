WITH Moving_Avg AS (
    SELECT 
        Date,
        Open,
        High,
        Low,
        Close,
        Volume,
        AVG(Close) OVER (ORDER BY Date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS MA_5
    FROM stock_prices
)
SELECT 
    Date,
    Open,
    High,
    Low,
    Close,
    Volume,
    MA_5,
    LAG(Close, 1) OVER (ORDER BY Date) AS Lag_Close,
    LEAD(Close, 1) OVER (ORDER BY Date) AS Lead_Close,
    SQRT(
        SUM((Close - MA_5) * (Close - MA_5)) OVER (ORDER BY Date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) / 5
    ) AS Volatility_5
FROM Moving_Avg
ORDER BY Date;
