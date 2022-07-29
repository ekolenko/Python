import sqlite3
import os
from app.model import tel


conn = None
db_file_name = './data/data.db'

def get_data(str_pattern):
    res = conn.execute(tel.select_tel_query(str_pattern))
    return res.fetchall()

def push_data(lst_in):
    conn.executemany(tel.get_add_tel_query(),lst_in)
    conn.commit()

def create_table():
    conn.execute(tel.get_create_table_query())
    conn.commit()


def remove_data(data):
    conn.execute(tel.get_remove_query(data))
    conn.commit()

def init():
    global conn
    if os.path.isfile(db_file_name):
        try:
            conn = sqlite3.connect(db_file_name)
        except:
            print('Error connecting to SQLite database')
    else:
        conn = sqlite3.connect(db_file_name)
    
    create_table()