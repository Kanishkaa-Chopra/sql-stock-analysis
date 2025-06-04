WITH Moving_Avg AS (
    SELECT 
        Date,
        Close,
        AVG(Close) OVER (ORDER BY Date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS MA_5
    FROM stock_prices
)
SELECT 
    Date,
    Close,
    MA_5,
    SQRT(
        SUM((Close - MA_5) * (Close - MA_5)) OVER (ORDER BY Date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) / 5
    ) AS Volatility_5
FROM Moving_Avg
ORDER BY Date;
