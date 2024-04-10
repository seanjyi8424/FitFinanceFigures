-- Create the products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    brand VARCHAR(50),
    product_name VARCHAR(100),
    category VARCHAR(50)
);

-- Create the prices table
CREATE TABLE prices (
    price_id INT PRIMARY KEY,
    product_id INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);