-- Analyze the price points of Nike and Puma products

-- Calculate the average price for Nike products
USE product_database;

SELECT 'Nike' AS brand, 
    ROUND(AVG(CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL)), 2) AS avg_price,
    MIN(CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL)) AS min_price,
    MAX(CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL)) AS max_price
FROM nike_products;

-- Calculate the average price for Puma products
SELECT 'Puma' AS brand, 
    ROUND(AVG(CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL)), 2) AS avg_price,
    MIN(CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL)) AS min_price,
    MAX(CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL)) AS max_price
FROM puma_products;

-- Calculate the price distribution for Nike products
SELECT 'Nike' AS brand,
       CASE
           WHEN CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL) < 50 THEN 'Under $50'
           WHEN CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL) BETWEEN 50 AND 100 THEN '$50 - $100'
           WHEN CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL) BETWEEN 100 AND 150 THEN '$100 - $150'
           WHEN CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL) > 150 THEN 'Over $150'
       END AS price_range,
       COUNT(*) AS product_count
FROM nike_products
GROUP BY price_range;

-- Calculate the price distribution for Puma products
SELECT 'Puma' AS brand,
       CASE
           WHEN CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL) < 50 THEN 'Under $50'
           WHEN CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL) BETWEEN 50 AND 100 THEN '$50 - $100'
           WHEN CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL) BETWEEN 100 AND 150 THEN '$100 - $150'
           WHEN CAST(SUBSTRING_INDEX(Price, '$', -1) AS DECIMAL) > 150 THEN 'Over $150'
       END AS price_range,
       COUNT(*) AS product_count
FROM puma_products
GROUP BY price_range;