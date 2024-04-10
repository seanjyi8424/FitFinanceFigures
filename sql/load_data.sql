-- Load data into the products table
INSERT INTO products (product_id, brand, product_name, category)
VALUES
    (1, 'Nike', 'Nike Air Max 270', 'Footwear'),
    (2, 'Adidas', 'Adidas Ultraboost', 'Footwear'),
    (3, 'Nike', 'Nike Dri-FIT T-Shirt', 'Clothing'),
    (4, 'Adidas', 'Adidas Lifestyle Shorts', 'Clothing');

-- Load data into the prices table
INSERT INTO prices (price_id, product_id, price)
VALUES
    (1, 1, 129.99),
    (2, 2, 179.99),
    (3, 3, 29.99),
    (4, 4, 39.99);