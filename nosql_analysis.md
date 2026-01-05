### Section A – Limitations of RDBMS

* Products with different attributes:

RDBMS uses fixed columns in tables.

Example: Laptop table has RAM, Processor, Storage. Shoe table has Size, Color.

Hard to fit all types in one table without leaving many empty columns.

* Frequent schema changes:

Adding a new product type requires altering tables.

This is time-consuming and can break existing queries.

* Nested data (e.g., customer reviews):

Each review has rating, comment, date.

RDBMS stores this in a separate table → complex joins to fetch reviews with products.



### Section B – NoSQL Benefits

* Flexible schema:

MongoDB uses documents (JSON-like objects).

Each product can have its own set of attributes without changing the database structure.

Example: Laptop document → {"RAM": "16GB", "Processor": "i7"}, Shoe document → {"Size": 9, "Color": "Red"}

* Embedded documents for nested data:

Customer reviews can be stored inside the product document.

Example:

{

&nbsp; "product\_name": "Laptop",

&nbsp; "reviews": \[

&nbsp;   {"user": "Rahul", "rating": 5, "comment": "Excellent"},

&nbsp;   {"user": "Priya", "rating": 4, "comment": "Good"}

&nbsp; ]

}

* Horizontal scalability:

MongoDB can handle huge amounts of data by distributing across multiple servers (sharding).

Useful for FlexiMart as catalog and users grow.



### Section C – Trade-offs

* Lack of complex transactions:

MongoDB is eventually consistent by default; complex multi-document transactions are harder.

* Joins are limited:

SQL databases are better for complex queries across multiple tables.



