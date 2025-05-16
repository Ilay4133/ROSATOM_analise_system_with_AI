import sqlite3

with sqlite3.connect('Rosatom.data') as db:
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Rosatom_users (
                    code TEXT PRIMARY KEY,
                    name TEXT,
                    sec_name TEXT,
                    mail TEXT,
                    tel TEXT)""")


while True:
    x = str(input())
    if x != "0":
        db = sqlite3.connect('Rosatom.data')
        cur = db.cursor()
        code = str(input())
        name = str(input())
        sec_name = str(input())
        mail = str(input())
        tel = str(input())
        values = [code,name,sec_name,mail,tel]
        print(values)
        cur.execute("INSERT INTO Rosatom_users (code,name,sec_name,mail,tel) VALUES (?,?,?,?,?)",
                    (code,name,sec_name,mail,tel))
        db.commit()
        db.close()
    else:
        break

db =  sqlite3.connect('Rosatom.data')
cur = db.cursor()
cur.execute("SELECT * FROM Rosatom_users")
u = cur.fetchall()
print(u)
db.commit()
db.close()

