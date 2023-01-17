# Product management assigment
import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='rps@123', host='localhost', database='kpmg')
cursor = cnx.cursor()

# Create a new product
def create_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
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
def update_product():
    id = int(input("Enter product ID: "))
    name = input("Enter new product name: ")
    price = float(input("Enter new product price: "))
    query = "UPDATE products SET name = %s, price = %s WHERE id = %s"
    values = (name, price, id)
    cursor.execute(query, values)
    cnx.commit()
    print("Product updated successfully.")

# Delete a product
def delete_product():
    id = int(input("Enter product ID: "))
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

# Main Menu
while True:
    print("1. Create Product")
    print("2. Read Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_product()
    elif choice == 2:
        read_products()
    elif choice == 3:
        update_product()
    elif choice == 4:
        delete_product()
    elif choice == 5:
        close_connection()
        break
    else:
        print("Invalid choice. Please try again.")

