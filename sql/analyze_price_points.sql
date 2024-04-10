-- Analyze the price points of Nike and Adidas products

-- Calculate the average price for Nike products
SELECT 
    'Nike' AS brand,
    ROUND(AVG(price), 2) AS avg_price
FROM 
    products p
    JOIN prices pr ON p.product_id = pr.product_id
WHERE 
    p.brand = 'Nike';

-- Calculate the average price for Adidas products
SELECT 
    'Adidas' AS brand,
    ROUND(AVG(price), 2) AS avg_price
FROM 
    products p
    JOIN prices pr ON p.product_id = pr.product_id
WHERE 
    p.brand = 'Adidas';

-- Calculate the minimum and maximum prices for Nike products
SELECT 
    'Nike' AS brand,
    MIN(price) AS min_price,
    MAX(price) AS max_price
FROM 
    products p
    JOIN prices pr ON p.product_id = pr.product_id
WHERE 
    p.brand = 'Nike';

-- Calculate the minimum and maximum prices for Adidas products
SELECT 
    'Adidas' AS brand,
    MIN(price) AS min_price,
    MAX(price) AS max_price
FROM 
    products p
    JOIN prices pr ON p.product_id = pr.product_id
WHERE 
    p.brand = 'Adidas';

-- Calculate the price distribution for Nike products
SELECT 
    'Nike' AS brand,
    CASE
        WHEN price < 50 THEN 'Under $50'
        WHEN price BETWEEN 50 AND 100 THEN '$50 - $100'
        WHEN price BETWEEN 100 AND 150 THEN '$100 - $150'
        WHEN price > 150 THEN 'Over $150'
    END AS price_range,
    COUNT(*) AS product_count
FROM 
    products p
    JOIN prices pr ON p.product_id = pr.product_id
WHERE 
    p.brand = 'Nike'
GROUP BY 
    price_range;

-- Calculate the price distribution for Adidas products
SELECT 
    'Adidas' AS brand,
    CASE
        WHEN price < 50 THEN 'Under $50'
        WHEN price BETWEEN 50 AND 100 THEN '$50 - $100'
        WHEN price BETWEEN 100 AND 150 THEN '$100 - $150'
        WHEN price > 150 THEN 'Over $150'
    END AS price_range,
    COUNT(*) AS product_count
FROM 
    products p
    JOIN prices pr ON p.product_id = pr.product_id
WHERE 
    p.brand = 'Adidas'
GROUP BY 
    price_range;