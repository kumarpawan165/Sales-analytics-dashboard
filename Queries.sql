CREATE DATABASE sales_dashboard;

USE sales_dashboard;

CREATE TABLE sales (
      order_id INT,
      product_name VARCHAR(100),
      customer_name VARCHAR(100),
      region VARCHAR(50),
      sales_amount DECIMAL(10,2)
      profit DECIMAL(10,2)
      order_date DATE
);