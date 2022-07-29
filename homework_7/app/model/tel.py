def get_create_table_query():
    res_query = 'CREATE TABLE IF NOT EXISTS telephones('+\
                'name TEXT, '+\
                'tel TEXT);'
    return res_query


def get_add_tel_query() -> str:
    res_query = 'INSERT INTO telephones '+\
                'VALUES(?, ?);'
    return res_query


def select_tel_query(str_pattern) -> str:

    res_query = 'SELECT name,tel,rowid FROM telephones'

    if str_pattern == '':
        return res_query + ';'
    else:
        return res_query + f' WHERE name LIKE \"%{str_pattern}%\" OR tel LIKE \"%{str_pattern}%\";'


def get_remove_query(data: tuple) -> str:
    res_query = f'DELETE FROM telephones WHERE rowid = {data[2]};'
    return res_query


