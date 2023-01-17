# Product management assigment
import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='rps@123', host='localhost', database='kpmg')
cursor = cnx.cursor()

# Create a new product
def create_product(name, price):
    query = "INSERT INTO products (name, price) VALUES (%s, %s)"
    values = (name, price)
    cursor.execute(query, values)
    cnx.commit()
    print("Product created successfully.")

# Read all products
def read_products():
    query = "SELECT * FROM products"
    cursor.execute(query)
    products = cursor.fetchall()
    for product in products:
        print(product)

# Update a product
def update_product(id, name, price):
    query = "UPDATE products SET name = %s, price = %s WHERE id = %s"
    values = (name, price, id)
    cursor.execute(query, values)
    cnx.commit()
    print("Product updated successfully.")

# Delete a product
def delete_product(id):
    query = "DELETE FROM products WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)
    cnx.commit()
    print("Product deleted successfully.")

# Close the database connection
def close_connection():
    cursor.close()
    cnx.close()
    print("Connection closed.")
