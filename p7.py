import sqlite3

#Connecting to the database
db = sqlite3.connect("data.db")
cur = db.cursor()


#Creating a table
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS products (
        id  INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        stock INTEGER
    )
    """
    
) 


# List of new products to add to the database
new_products = [
    ("Watermelon", 80000, 5),
    ("Lemon", 20000, 100),
    ("orange", 55000, 25),
    ("Peach", 60000, 12),
    ("apple", 30000, 10)
]

# Delete all products
cur.execute("DELETE FROM products")

#insert query
cur.executemany("""INSERT INTO products(name, price, stock) VALUES(?,?,?)""" , new_products)
db.commit()


#delet qurery
cur.execute("""DELETE FROM products WHERE id=?""" ,(3,))
db.commit()

#update qurery
cur.execute("""UPDATE products SET name = 'cucumber' WHERE name = 'apple' """)
db.commit()

#search qurery
cur.execute("SELECT * FROM products WHERE name = ?", ('Watermelon',) )
result = cur.fetchall()
print(result)

db.close()
