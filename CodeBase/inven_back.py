import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS `inventory` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `sku_id` INTEGER, `preadv_id` INTEGER, `margin` INTEGER, `qcheck` INTEGER, `rate` INTEGER, `qavail` INTEGER, `name` TEXT, `loc_id` INTEGER )")
        self.conn.commit()

    def insert(self,sku_id, preadv_id, margin, qcheck, rate, qavail):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute(" SELECT name FROM `product` WHERE sku_id = ? ",(sku_id,))
        name = (self.cur.fetchall())[0][0]
        # print(name,"name")
        self.cur.execute(" SELECT category_id FROM `product` WHERE sku_id = ? ",(sku_id,))
        cat_id = (self.cur.fetchall())[0][0]
        # print(cat_id,"cat")
        self.cur.execute(" SELECT id FROM `location` WHERE category_id = ? ",(cat_id,))
        loc_id = (self.cur.fetchall())[0][0]

        self.cur.execute("INSERT INTO `inventory` VALUES(NULL,?,?,?,?,?,?,?,?)", (sku_id, preadv_id, margin, qcheck, rate, qavail,name,loc_id))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM `inventory` ")
        rows = self.cur.fetchall()
        return rows

    def search(self, id="", sku_id="", preadv_id="", margin="", qcheck="", rate="", qavail="", name="", loc_id=""):
        self.cur.execute("SELECT * FROM `inventory` WHERE id = ? OR sku_id = ? OR preadv_id = ? OR margin = ? OR qcheck = ? OR rate = ? OR qavail = ? OR name= ? OR loc_id=?", (id ,sku_id, preadv_id, margin, qcheck, rate, qavail,name,loc_id))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM `inventory` WHERE id = ?", (id,))
        self.conn.commit()
        #conn.close()

    def update(self,id, preadv_id, margin, qcheck, rate, qavail):
        # print(id,name,type,phn1,phn2)
        self.cur.execute("UPDATE `inventory` SET preadv_id = ?, margin = ?, qcheck = ?, rate= ?, qavail =? WHERE id = ?", (preadv_id, margin, qcheck, rate, qavail, id))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()