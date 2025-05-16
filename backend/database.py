import sqlite3
from datetime import datetime
import pytz
from rosatom_project.backend.ai_model import model_start1



def create_db_table1(db_path='C:/Users/User/PycharmProjects/pythonProject5/rosatom_project/backend/filters1.db'):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS filter_data
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  filter_number INTEGER,
                  status_int INTEGER,
                  status_text TEXT,
                  flow REAL,
                  delta_pressure REAL,
                  timestamp DATETIME)''')
    conn.commit()
    conn.close()


def save_to_db1(data, db_path='C:/Users/User/PycharmProjects/pythonProject5/rosatom_project/backend/filters1.db') -> list:
    filter_status: str =""
    timestamp = datetime.now(pytz.timezone('Europe/Kaliningrad')).strftime('%Y-%m-%d %H:%M:%S')
    if data[1]==0:
        filter_status="100%"
        int_filter_status: int = 100
    elif data[1]==1:
        con = (1 - (data[3]-5000)/5000) * 100
        filter_status=str(con)+"%"
        int_filter_status: int = int(con)
    elif data[1]==2:
        filter_status="0%"
        int_filter_status: int = 0
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''INSERT INTO filter_data
                 (filter_number, status_int, status_text, flow, delta_pressure, timestamp)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (data[0],data[1],filter_status, data[2],data[3], timestamp))
    conn.commit()
    conn.close()
    print("Данные успешно сохранены в базу данных")
    return [data[1],int_filter_status, data[2],data[3], timestamp]

def save_to_database1() -> list:
    create_db_table1()
    data_list_db=model_start1()
    data = [
        1739127850170,
        data_list_db[0],
        data_list_db[1],
        data_list_db[2]
    ]
    filter_values=save_to_db1(data)

    conn = sqlite3.connect('C:/Users/User/PycharmProjects/pythonProject5/rosatom_project/backend/filters1.db')
    c = conn.cursor()
    c.execute("SELECT * FROM filter_data")
    print("\nСодержимое базы данных:")
    for row in c.fetchall():
        print(row)
    conn.close()
    return filter_values

#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________


