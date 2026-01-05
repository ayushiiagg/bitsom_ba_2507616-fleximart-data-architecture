#### 1.Entity-Relationship Description (Text Format)



ENTITY: customers

Purpose:

Stores customer demographic and contact information for FlexiMart users



Attributes:

customer\_id (INT, PK): Unique surrogate identifier for each customer

first\_name (VARCHAR): Customer’s first name

last\_name (VARCHAR): Customer’s last name

email (VARCHAR, UNIQUE): Customer’s email address used for communication and identification

phone (VARCHAR): Customer’s contact number

city (VARCHAR): City of residence

registration\_date (DATE): Date when the customer registered

Relationships:

One customer can place many orders

Relationship type: 1 : M with orders



ENTITY: products

Purpose:

Stores product catalog information available for sale.



Attributes:

product\_id (INT, PK): Unique surrogate identifier for each product

product\_name (VARCHAR): Name of the product

category (VARCHAR): Product category (Electronics, Fashion, Groceries)

price (DECIMAL): Selling price per unit

stock\_quantity (INT): Available inventory count

Relationships:

One product can appear in many order items

Relationship type: 1 : M with order\_items



ENTITY: orders

Purpose:

Stores high-level order transaction details.



Attributes:

order\_id (INT, PK): Unique identifier for each order

customer\_id (INT, FK): References customers.customer\_id

order\_date (DATE): Date of order placement

total\_amount (DECIMAL): Total monetary value of the order

status (VARCHAR): Order status (Completed, Pending, Cancelled)

Relationships:

Each order belongs to one customer

Each order can have many order items



ENTITY: order\_items

Purpose:

Stores line-item level details for each order.



Attributes:

order\_item\_id (INT, PK): Unique identifier for each order item

order\_id (INT, FK): References orders.order\_id

product\_id (INT, FK): References products.product\_id

quantity (INT): Number of units ordered

unit\_price (DECIMAL): Price per unit at order time

subtotal (DECIMAL): quantity × unit\_price

Relationships:

Many order items belong to one order

Many order items reference one product

#### 

#### 2\. Normalization Explanation (Third Normal Form – 3NF)

The FlexiMart database is designed using Third Normal Form (3NF) to keep data clean, accurate, and free from repetition.



First, each table stores only one type of information. Customer details are stored only in the customers table, product details only in the products table, order details in orders, and item-level details in order\_items. This avoids mixing unrelated data.



Second, every table has a primary key, and all other attributes in that table depend only on that key. For example, a customer’s name, email, and phone depend only on customer\_id, and product price and category depend only on product\_id.



Third, there are no transitive dependencies. Customer or product information is not repeated in the orders or order\_items tables. Instead, foreign keys are used to create relationships.



Because of this design:

Update anomalies are avoided (updating customer data in one place)

Insert anomalies are avoided (products or customers can exist without orders)

Delete anomalies are avoided (deleting an order does not delete customer data)



#### 3\. Sample Data Representation:



##### customers

| customer\_id | first\_name | last\_name | email                                                   | phone          | city      | registration\_date |

| ----------- | ---------- | --------- | ------------------------------------------------------- | -------------- | --------- | ----------------- |

| 1           | Rahul      | Sharma    | \[rahul.sharma@gmail.com](mailto:rahul.sharma@gmail.com) | +91-9876543210 | Bangalore | 2023-01-15        |

| 2           | Priya      | Patel     | \[priya.patel@yahoo.com](mailto:priya.patel@yahoo.com)   | +91-9988776655 | Mumbai    | 2023-02-20        |

##### 

##### products



| product\_id | product\_name       | category    | price | stock\_quantity |

| ---------- | ------------------ | ----------- | ----- | -------------- |

| 1          | Samsung Galaxy S21 | Electronics | 45999 | 150            |

| 2          | Nike Running Shoes | Fashion     | 3499  | 80             |



##### orders



| order\_id | customer\_id | order\_date | total\_amount | status    |

| -------- | ----------- | ---------- | ------------ | --------- |

| 1        | 1           | 2024-01-15 | 45999        | Completed |

| 2        | 2           | 2024-01-16 | 5998         | Completed |



##### order\_items



| order\_item\_id | order\_id | product\_id | quantity | unit\_price | subtotal |

| ------------- | -------- | ---------- | -------- | ---------- | -------- |

| 1             | 1        | 1          | 1        | 45999      | 45999    |

| 2             | 2        | 2          | 2        | 2999       | 5998     |

















