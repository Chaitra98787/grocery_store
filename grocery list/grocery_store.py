import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this
    password="chaitra0611",  # Change this
    database="grocery_store"
)
cursor = db.cursor()

print("Connected to MySQL successfully!")
def add_product(name, price, quantity):
    query = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
    values = (name, price, quantity)
    cursor.execute(query, values)
    db.commit()
    print("Product added successfully!")

add_product("Apples", 50.00, 100)
def view_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(product)

view_products()
def sell_product(product_id, quantity_sold):
    cursor.execute("SELECT price, quantity FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    
    if product and product[1] >= quantity_sold:
        total_price = product[0] * quantity_sold
        cursor.execute("INSERT INTO sales (product_id, quantity_sold, total_price) VALUES (%s, %s, %s)",
                       (product_id, quantity_sold, total_price))
        cursor.execute("UPDATE products SET quantity = quantity - %s WHERE id = %s", (quantity_sold, product_id))
        db.commit()
        print("Sale recorded successfully!")
    else:
        print("Not enough stock available!")

sell_product(1, 10)
