import sqlite3
class manage_products:
    def __init__(self):
        self.con=sqlite3.connect("store_database.db")
        self.curs=self.con.cursor()
        self.curs.execute("""
        CREATE TABLE IF NOT EXISTS Product(
                          prodID INTEGER PRIMARY KEY AUTOINCREMENT,
                          prodName,
                          prodPrice,
                          prodQuantity
                          )

        """)
        self.curs.execute("CREATE TABLE IF NOT EXISTS Sales(saleID,saleDate,prodName,saleTotal)" )
        self.con.commit()

    def addProduct(self):
        prodName=str(input("Enter product name: "))
        prodPrice=float(input("Enter product price: "))
        prodQuantity=int(input("Enter product quantity: "))
        self.curs.execute(f"""
                          INSERT INTO Product(prodName,prodPrice,prodQuantity) 
                          VALUES('{prodName}', {prodPrice}, {prodQuantity})
        """)
        self.con.commit()
    
    def deleteProduct(self):
        remove=int(input("Enter ID of product to remove: "))
        self.curs.execute(f"DELETE FROM Product WHERE prodID={remove}")
        print("Data deleted succesfully")
        self.con.commit()

    def UpdateProduct(self):
        update=int(input("Enter ID of product to update: "))
        prodName=input("Enter new product name: ")
        prodPrice=input("Enter new product price: ")
        prodQuantity=input("Enter new product quantity: ")
        self.curs.execute(f"UPDATE Product SET prodName='{prodName}', prodPrice={prodPrice},prodQuantity={prodQuantity} WHERE prodID={update}")
        self.con.commit()

def menu():
    print("\t1.\t Add a product \n\t2.\t Remove a product \n\t3.\t Update a product \n\t4.\t Display all products \n\t5.\t Sell a product \n\t6.\t Exit\n")
while True:
    print("\tWelcome to the store Management System")
    menu()
    choice=int(input("Select a choice: "))
    manage=manage_products()
    if(choice==1):
        manage.addProduct()
    elif(choice==2):
        manage.deleteProduct()
    elif(choice==3):
        manage.UpdateProduct()


