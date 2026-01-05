##### \#Section 1-

##### 

##### \# Star Schema Overview – Fleximart



Fleximart uses a star schema to analyze sales data in a simple and efficient way.  

In this design, one main fact table is connected to multiple dimension tables that provide descriptive details.



##### \# Fact Table: fact\_sales



The fact\_sales table stores all sales transactions.  

Each record represents one product sold in one order.



It contains important numerical values such as:

\- Quantity sold

\- Unit price at the time of sale

\- Discount applied

\- Total amount after discount



This table is linked to dimension tables using foreign keys for date, product, and customer.



##### \# Dimension Tables



\- dim\_date: Stores date-related information like day, month, year, quarter, and weekend indicator. It is used for time-based sales analysis.

\- dim\_product: Contains product details such as product name, category, brand, and price. It helps analyze sales by product and category.

\- dim\_customer: Stores customer information like name, city, country, and registration date. It helps understand customer purchasing behavior.



\# Conclusion

This star schema design separates numerical sales data from descriptive information, making reporting and business analysis faster and easier.





### \#Section 2-

###### 

###### \#Design Decisions



The granularity of the fact table is chosen at the transaction line-item level, where each row represents one product sold in a single order. This level of detail is selected because it provides the most accurate and flexible data for analysis. It allows the business to track exact quantities, prices, discounts, and total amounts for each product sale, making detailed reporting and analysis possible.



Surrogate keys are used instead of natural keys to improve performance and consistency. Natural keys such as product IDs or customer IDs may change over time or differ across source systems. Surrogate keys are system-generated, stable, and smaller in size, which helps in faster joins and better handling of slowly changing dimensions.



This star schema design supports drill-down and roll-up operations efficiently. Users can drill down from yearly sales to monthly, daily, or product-level details, and roll up detailed data into summaries such as total sales by month, category, or customer group for better decision-making.





#### \# Section 3- 



##### Sample Data Flow



A sales transaction is first recorded in the source system and then transformed before being stored in the data warehouse.



\# Source Transaction



\- Order Number: 101  

\- Customer Name: John Doe  

\- Product Name: Laptop  

\- Quantity: 2  

\- Unit Price: 50,000  



\#Data Warehouse Representation

After ETL processing, the transaction is stored using surrogate keys in the star schema.



* fact\_sales

\- date\_key: 20240115  

\- product\_key: 5  

\- customer\_key: 12  

\- quantity\_sold: 2  

\- unit\_price: 50000  

\- total\_amount: 100000  



* dim\_date

\- date\_key: 20240115  

\- full\_date: 2024-01-15  

\- month: 1  

\- quarter: Q1  



* dim\_product

\- product\_key: 5  

\- product\_name: Laptop  

\- category: Electronics  



* dim\_customer

\- product\_key: 12  

\- customer\_name: John Doe  

\- city: Mumbai  



This process shows how detailed source data is converted into structured fact and dimension records for easy analysis.



