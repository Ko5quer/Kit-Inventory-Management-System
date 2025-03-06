import sqlite3
class manage_products:
    def __init__(self,choice):
        self.choice=choice
        self.con=sqlite3.connect("store_database.db")
        self.curs=self.con.cursor()
        self.curs.execute("CREATE TABLE IF NOT EXISTS Product(prodID,prodName,prodPrice,prodQuantity)")
        self.curs.execute("CREATE TABLE IF NOT EXISTS Sales(saleID,saleDate,prodName,saleTotal)" )
        self.con.commit()

