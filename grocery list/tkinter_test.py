import tkinter as tk

root = tk.Tk()
root.title("Grocery Store Management")
root.geometry("400x300")  # Set window size

label = tk.Label(root, text="Welcome to Grocery Store", font=("Arial", 14))
label.pack(pady=20)  # Add space around the label

btn = tk.Button(root, text="Click Me")


import tkinter as tk
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this
    password="chaitra0611",  # Change this
    database="grocery_store"
)
cursor = db.cursor()

def add_product():
    name = name_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()

    if name and price and quantity:
        cursor.execute("INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)", (name, price, quantity))
        db.commit()
        messagebox.showinfo("Success", "Product added successfully!")
        name_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

root = tk.Tk()
root.title("Grocery Store Management")
root.geometry("400x400")

tk.Label(root, text="Product Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Price:").pack()
price_entry = tk.Entry(root)
price_entry.pack()

tk.Label(root, text="Quantity:").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

add_button = tk.Button(root, text="Add Product", command=add_product)
add_button.pack(pady=10)

root.mainloop()
from tkinter import ttk

def view_products():
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    for row in tree.get_children():
        tree.delete(row)

    for row in rows:
        tree.insert("", "end", values=row)

view_button = tk.Button(root, text="View Products", command=view_products)
view_button.pack(pady=10)

tree = ttk.Treeview(root, columns=("ID", "Name", "Price", "Quantity"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Price", text="Price")
tree.heading("Quantity", text="Quantity")
tree.pack()

root.mainloop()
