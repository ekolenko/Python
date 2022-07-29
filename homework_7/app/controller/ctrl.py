from app.view import tk_view
from app.view import c_view
from . import db_sqlite3
from . import db_csv
from . import db_mysql

g_mod = None
d_mod = None


def init_view():
    global g_mod
    match g_mod:
        case 1: c_view.init()
        case 2: tk_view.init()


def init_db():
    global d_mod
    match d_mod:
        case 1:
            db_sqlite3.init()
        case 2:
            pass
        case 3:
            pass


def get_data_from_database(str_pattern) -> list:
    global d_mod
    match d_mod:
        case 1:
            return db_sqlite3.get_data(str_pattern)
        case 2:
            return []
        case 3:
            return []

def load_from_csv(file_name):
    
    global d_mod
    
    lst_data = db_csv.get_data_from_file(file_name)
    match d_mod:
        case 1:
            db_sqlite3.push_data(lst_data)
        case 2:
            pass
        case 3:
            pass

def remove_data_from_database(data):
    global d_mod
    match d_mod:
        case 1:
            return db_sqlite3.remove_data(data)
        case 2:
            pass
        case 3:
            pass


def init(g_in,d_in):
    global g_mod
    global d_mod
    g_mod = g_in
    d_mod = d_in
    init_db()
    init_view()
    
