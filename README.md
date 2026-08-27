# sqlite-product-management-python
A simple Python project that manages products using SQLite, including inserting, deleting, updating, and searching data.

Features:
Create a SQLite database
Create a products table
Insert multiple products
Delete products
Update product information
Search for products
Store product name, price, and stock

Technologies Used:
Python
SQLite
sqlite3 module

Database Structure:
The project creates a products table with the following columns:
Column    	Type  	    Description
id	      INTEGER    	Product ID
name 	     TEXT	      Product name
price 	  INTEGER	    Product price
stock     INTEGER	    Available stock

How It Works:
The program connects to a SQLite database named data.db.
If the products table does not exist, the program creates it.
The program then adds a list of products to the database.
It also demonstrates several SQL operations:

INSERT — Add products
DELETE — Delete products
UPDATE — Update product information
SELECT — Search for products
Finally, the program searches for the product named Watermelon and displays the result.

How to Run:
Run the following command in the terminal:
python p7.py
The data.db database file will be created automatically when the program runs.

SQL Operations Demonstrated:
CREATE TABLE
INSERT
DELETE
UPDATE
SELECT

Files:
p7.py — Main Python program
data.db — SQLite database created automatically by the program
