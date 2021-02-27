import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

        
        self.cur.execute("CREATE TABLE IF NOT EXISTS `prodcat` ( `id` INTEGER NOT NULL, `desc` TEXT, PRIMARY KEY(`id`) )")
        self.conn.commit()

    def insert(self,id, desc):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute("INSERT INTO `prodcat` VALUES(NULL,?)", (desc,))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM `prodcat`")
        rows = self.cur.fetchall()
        return rows

    def search(self, id="", name=""):
        self.cur.execute("SELECT * FROM `prodcat` WHERE id = ? OR desc = ? ", (id ,name))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM `prodcat` WHERE id = ?", (id,))
        self.conn.commit()
        #conn.close()

    def update(self,id, name):
        # print(id,name,type,phn1,phn2)
        self.cur.execute("UPDATE `prodcat` SET desc = ? WHERE id = ?", (name, id))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()