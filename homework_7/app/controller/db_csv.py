# тут будет модуль работы с CSV

def get_data_from_file(file_name=None):

    if file_name == None:
        return []
    try:
        with open(file_name,'r') as f:
            lst_str = f.read().splitlines()

        return [tuple(elem_str.split(',')) for elem_str in lst_str]
    except:
        return []

def get_data(str_pattern):
    print('CSV mode not supported yet')
    return []
