🛒 Store Management System
This is a basic Python-based Store Management System that uses SQLite to handle product data such as adding, updating, deleting, and displaying products. It also includes a foundation for sales tracking (although the sales functionality is not yet implemented).

📦 Features
Add a new product (name, price, quantity)

Delete an existing product by ID

Update product details (name, price, quantity)

View a list of all available products

SQLite database used for data persistence

🧱 Database Structure
Product Table
Stores product details:

prodID (Primary Key)

prodName (Text)

prodPrice (Float)

prodQuantity (Integer)

Sales Table
Placeholder table created for future use (currently unused):

saleID

saleDate

prodName

saleTotal

🛠 How It Works
The program uses sqlite3 to connect to store_database.db.

A manage_products class handles all operations on the product table.

A menu() function displays options for the user to choose from.

Based on the user's input, a corresponding method is called.

🚀 How to Run
Make sure you have Python 3 installed.

Save the script in a .py file (e.g., store_manager.py).

Run the script using:

bash
Copy
Edit
python store_manager.py
Choose options from the menu to manage your store's products.

✅ Example Menu
css
Copy
Edit
    1.  Add a product 
    2.  Remove a product 
    3.  Update a product 
    4.  Display all products 
    5.  Sell a product 
    6.  Exit
🔒 Notes
All inputs are taken via command line.

The sales feature (Sell a product) is shown in the menu but not implemented.

SQL commands use f-strings — for real-world applications, always use parameterized queries to prevent SQL injection.

📌 To Improve
Implement the sales functionality

Add data validation (e.g., preventing negative prices or quantities)

Refactor to use parameterized queries

Add exception handling for errors (like invalid input types or DB errors)
