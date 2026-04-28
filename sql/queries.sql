-- 1. Total Revenue
SELECT SUM(total_price) AS total_revenue FROM orders;

-- 2. Top Selling Products
SELECT product, SUM(quantity) AS total_sold
FROM orders
GROUP BY product
ORDER BY total_sold DESC;

-- 3. Monthly Revenue
SELECT strftime('%Y-%m', order_date) AS month,
       SUM(total_price) AS revenue
FROM orders
GROUP BY month;

-- 4. Top Customers
SELECT customer_id, SUM(total_price) AS total_spent
FROM orders
GROUP BY customer_id
ORDER BY total_spent DESC;

-- 5. Average Order Value
SELECT AVG(total_price) FROM orders;