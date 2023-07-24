import psycopg2
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import *

# Connect to PostgreSQL database
db = psycopg2.connect(
    dbname="your database name",
    user="user name",
    password="your password",
    host="localhost",
    port="5432"
)

cursor = db.cursor()

# Rest of the code remains unchanged...
# (Please keep the rest of your code as it is)


# Main application window
window = Tk()
window.title("Cozy Cafe || Developed by Rakib Hasan")
window.geometry("800x800")

# Title label
title_label = Label(window, text="Cozy Cafe", font=("Arial", 28), fg="#1b1b1b")
title_label.pack(pady=20)


# Function to fetch and display employees from the database
def show_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    # Create a new window to display employees
    employees_window = Toplevel(window)
    employees_window.title("Employees")

    # Create a treeview to display employees' information
    tree = ttk.Treeview(employees_window)
    tree.pack()

    tree["columns"] = ("ID", "Name", "Position")
    tree.column("#0", width=0, stretch=NO)
    tree.column("ID", width=50, anchor=CENTER)
    tree.column("Name", width=200, anchor=W)
    tree.column("Position", width=200, anchor=W)

    tree.heading("#0", text="", anchor=W)
    tree.heading("ID", text="ID", anchor=CENTER)
    tree.heading("Name", text="Name", anchor=W)
    tree.heading("Position", text="Position", anchor=W)

    # Insert employees' information into the treeview
    for employee in employees:
        tree.insert("", END, values=employee)


# Function to fetch and display menu items from the database
def show_menu():
    cursor.execute("SELECT * FROM menu")
    menu_items = cursor.fetchall()

    # Create a new window to display menu items
    menu_window = Toplevel(window)
    menu_window.title("Menu")

    # Create a treeview to display menu items
    tree = ttk.Treeview(menu_window)
    tree.pack()

    tree["columns"] = ("ID", "Item", "Price")
    tree.column("#0", width=0, stretch=NO)
    tree.column("ID", width=50, anchor=CENTER)
    tree.column("Item", width=200, anchor=W)
    tree.column("Price", width=100, anchor=CENTER)

    tree.heading("#0", text="", anchor=W)
    tree.heading("ID", text="ID", anchor=CENTER)
    tree.heading("Item", text="Item", anchor=W)
    tree.heading("Price", text="Price", anchor=CENTER)

    # Insert menu items into the treeview
    for item in menu_items:
        tree.insert("", END, values=item)

# Button to show employees
show_employees_btn = Button(window, text="Show Employees", command=show_employees)
show_employees_btn.pack(pady=10)

# Button to show menu items
show_menu_btn = Button(window, text="Show Menu", command=show_menu)
show_menu_btn.pack(pady=10)

# Function to refresh the treeview
def refresh_tree(tree):
    tree.delete(*tree.get_children())

    # Fetch transactions from the database and insert them into the treeview
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    for transaction in transactions:
        tree.insert("", END, values=transaction)




# Function to add a new transaction to the database
def add_transaction():
    # Fetch employee ID, item ID, and quantity
    employee_id = employee_entry.get()
    item_id = item_entry.get()
    quantity = quantity_entry.get()

    if employee_id == "" or item_id == "" or quantity == "":
        messagebox.showwarning("Warning", "Please fill in all the fields.")
        return

    try:
        employee_id = int(employee_id)
        item_id = int(item_id)
        quantity = int(quantity)
    except ValueError:
        messagebox.showwarning("Warning", "Invalid input for Employee ID, Item ID, or Quantity.")
        return

    # Fetch employee name and item price
    cursor.execute("SELECT name FROM employees WHERE id = %s", (employee_id,))
    employee = cursor.fetchone()

    cursor.execute("SELECT item, price FROM menu WHERE id = %s", (item_id,))
    item = cursor.fetchone()

    if employee is None or item is None:
        messagebox.showwarning("Warning", "Employee ID or Item ID not found.")
        return

    employee_name = employee[0]
    item_name = item[0]
    item_price = item[1]

    # Calculate total price
    total_price = item_price * quantity

    # Insert transaction into the database
    cursor.execute("INSERT INTO transactions (emp_id, item_id, quantity, total_price) VALUES (%s, %s, %s, %s)",
                   (employee_id, item_id, quantity, total_price))
    db.commit()

    messagebox.showinfo("Success", f"Transaction added: Employee {employee_name} sold {quantity} {item_name}(s) for a total of ${total_price}")

    # Clear entry fields and refresh treeview
    employee_entry.delete(0, END)
    item_entry.delete(0, END)
    quantity_entry.delete(0, END)
    refresh_tree(transactions_tree)

# Button to refresh the transactions treeview
refresh_btn = Button(window, text="Refresh", command=lambda: refresh_tree(transactions_tree))
refresh_btn.pack(pady=10)

# Create a treeview to display transactions
transactions_tree = ttk.Treeview(window)
transactions_tree.pack()

transactions_tree["columns"] = ("ID", "Employee ID", "Item ID", "Quantity", "Total Price")
transactions_tree.column("#0", width=0, stretch=NO)
transactions_tree.column("ID", width=50, anchor=CENTER)
transactions_tree.column("Employee ID", width=100, anchor=CENTER)
transactions_tree.column("Item ID", width=100, anchor=CENTER)
transactions_tree.column("Quantity", width=100, anchor=CENTER)
transactions_tree.column("Total Price", width=100, anchor=CENTER)

transactions_tree.heading("#0", text="", anchor=W)
transactions_tree.heading("ID", text="ID", anchor=CENTER)
transactions_tree.heading("Employee ID", text="Employee ID", anchor=CENTER)
transactions_tree.heading("Item ID", text="Item ID", anchor=CENTER)
transactions_tree.heading("Quantity", text="Quantity", anchor=CENTER)
transactions_tree.heading("Total Price", text="Total Price", anchor=CENTER)

# Fetch transactions from the database and insert them into the treeview
cursor.execute("SELECT * FROM transactions")
transactions = cursor.fetchall()
for transaction in transactions:
    transactions_tree.insert("", END, values=transaction)

# Labels and entry fields for adding transactions
employee_label = Label(window, text="Employee ID:")
employee_label.pack()

employee_entry = Entry(window)
employee_entry.pack()

item_label = Label(window, text="Item ID:")
item_label.pack()

item_entry = Entry(window)
item_entry.pack()

quantity_label = Label(window, text="Quantity:")
quantity_label.pack()

quantity_entry = Entry(window)
quantity_entry.pack()

transaction_btn = Button(window, text="Add Transaction", command=add_transaction)
transaction_btn.pack(pady=10)

# Main event loop
window.mainloop()
