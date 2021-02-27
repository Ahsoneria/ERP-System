import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS `product` ( `name` TEXT, `sku_id` INTEGER PRIMARY KEY AUTOINCREMENT, `category_id` INTEGER, `desc` TEXT, `reorder` INTEGER )")
        self.conn.commit()

    def insert(self,id, name, cat, desc, reorder):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute("INSERT INTO product VALUES(NULL,?,?,?,?)", (name,cat,desc,reorder))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM product")
        rows = self.cur.fetchall()
        return rows

    def search(self, id="", name="", cat="", desc="", reorder=""):
        self.cur.execute("SELECT * FROM product WHERE sku_id = ? OR name = ? OR category_id = ? OR desc = ? "
                    "OR reorder = ?", (id ,name, cat, desc, reorder))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM product WHERE sku_id = ?", (id,))
        self.conn.commit()
        #conn.close()

    def update(self,id, name, cat, desc, reorder):
        # print(id,name,type,phn1,phn2)
        self.cur.execute("UPDATE product SET name = ?, category_id = ?, desc = ?, reorder = ? WHERE sku_id = ?", (name, cat, desc, reorder, id))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()