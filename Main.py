import sqlite3
class manage_products:
    def __init__(self,choice):
        self.choice=choice
    
    def create_Db(self):
        table=sqlite3.connect("Management_System.db")
        cursor=table.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS product(
                prodID INTERGER PRIMARY KEY,
                prodName TEXT NOT NULL,
                prodPrice REAL NOT NULL,
                prodQuantity INTERGER
            )
            """
        )

