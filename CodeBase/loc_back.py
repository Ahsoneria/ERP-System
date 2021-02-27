import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

        
        self.cur.execute("CREATE TABLE IF NOT EXISTS `location` ( `id` INTEGER, `name` TEXT, `category_id` INTEGER )")
        self.conn.commit()

    def insert(self,id, name, cat):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute("INSERT INTO `location` VALUES(?,?,?)", (id,name,cat))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM `location`")
        rows = self.cur.fetchall()
        return rows

    def search(self, id="", name="", cat=""):
        self.cur.execute("SELECT * FROM `location` WHERE id = ? OR name = ? OR category_id = ? ", (id ,name,cat))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id,cat):
        self.cur.execute("DELETE FROM `location` WHERE id = ? AND category_id = ? ", (id,cat))
        self.conn.commit()
        #conn.close()

    def update(self,id,name,cat,oricat):
        self.cur.execute("UPDATE `location` SET name = ?, category_id = ? WHERE id = ? AND category_id = ? ", (name, cat,id,oricat))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()