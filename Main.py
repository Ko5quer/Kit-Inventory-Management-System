import sqlite3


class ManageProducts:
    def __init__(self):
        self.con = sqlite3.connect("store_database.db")
        self.curs = self.con.cursor()

        self.curs.execute("""
        CREATE TABLE IF NOT EXISTS Product(
            prodID INTEGER PRIMARY KEY AUTOINCREMENT,
            prodName TEXT,
            prodPrice REAL,
            prodQuantity INTEGER
        )
        """)

        self.curs.execute("""
        CREATE TABLE IF NOT EXISTS Sales(
            saleID INTEGER PRIMARY KEY AUTOINCREMENT,
            saleDate TEXT,
            prodName TEXT,
            saleTotal REAL
        )
        """)

        self.con.commit()

    def addProduct(self):
        prodName = input("Enter product name: ")
        prodPrice = float(input("Enter product price: "))
        prodQuantity = int(input("Enter product quantity: "))

        self.curs.execute("""
            INSERT INTO Product(prodName, prodPrice, prodQuantity)
            VALUES (?, ?, ?)
        """, (prodName, prodPrice, prodQuantity))

        self.con.commit()
        print("Product added successfully")

    def deleteProduct(self):
        remove = int(input("Enter ID of product to remove: "))

        self.curs.execute("DELETE FROM Product WHERE prodID = ?", (remove,))
        self.con.commit()

        print("Product deleted successfully")

    def updateProduct(self):
        update = int(input("Enter ID of product to update: "))
        prodName = input("Enter new product name: ")
        prodPrice = float(input("Enter new product price: "))
        prodQuantity = int(input("Enter new product quantity: "))

        self.curs.execute("""
            UPDATE Product
            SET prodName = ?, prodPrice = ?, prodQuantity = ?
            WHERE prodID = ?
        """, (prodName, prodPrice, prodQuantity, update))

        self.con.commit()
        print("Product updated successfully")

    def displayProduct(self):
        self.curs.execute("SELECT * FROM Product")
        results = self.curs.fetchall()

        for row in results:
            print(row)

    def sellProduct(self):
        productID = int(input("Enter product ID: "))
        saleDate = input("Enter sale date: ")
        saleQuantity = int(input("Enter sale quantity: "))

        self.curs.execute("""
            SELECT prodQuantity, prodPrice, prodName
            FROM Product
            WHERE prodID = ?
        """, (productID,))

        result = self.curs.fetchone()

        if result is None:
            print("Product not found")
            return

        quantity, price, name = result

        if saleQuantity > quantity:
            print("Not enough stock!")
            return

        new_quantity = quantity - saleQuantity
        total_price = price * saleQuantity

        self.curs.execute("""
            INSERT INTO Sales(saleDate, prodName, saleTotal)
            VALUES (?, ?, ?)
        """, (saleDate, name, total_price))

        self.curs.execute("""
            UPDATE Product
            SET prodQuantity = ?
            WHERE prodID = ?
        """, (new_quantity, productID))

        self.con.commit()
        print("Sale recorded successfully")

    def close(self):
        self.con.close()


def menu():
    print("""
    1. Add a product
    2. Remove a product
    3. Update a product
    4. Display all products
    5. Sell a product
    6. Exit
    """)


def main():
    manage = ManageProducts()

    while True:
        print("\nWelcome to the Store Management System")
        menu()

        try:
            choice = int(input("Select a choice: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if choice == 1:
            manage.addProduct()
        elif choice == 2:
            manage.deleteProduct()
        elif choice == 3:
            manage.updateProduct()
        elif choice == 4:
            manage.displayProduct()
        elif choice == 5:
            manage.sellProduct()
        elif choice == 6:
            manage.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
