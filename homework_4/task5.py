#!/usr/bin/python3

# Даны два файла, в каждом из которых находится 
# запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.

import re
import my_func

def read_from_file(f_name: str) -> str:
    with open(f_name,'r') as f:
        return f.readline()


def get_pow_from_chlen(str_chlen: str) -> int:
    pow_symbol = str_chlen.find('^')
    if pow_symbol > -1:
        return int(str_chlen[pow_symbol + 1:])
    else:
        return pow_from_unicode(str_chlen)


def pow_from_unicode(str_chlen: str) -> int:
    x_symbol = str_chlen.find('x')
    return my_func.pow_to_int(str_chlen[x_symbol + 1:])


def get_dict_chlen(list_chlen: list) -> dict:
    dict_chlen = {}
    for chlen in list_chlen:    
        n = chlen.find('x')
        if n == -1: 
            dict_chlen[0] = float(chlen)
        elif n == len(chlen) - 1:
            dict_chlen[1] = float(chlen[:n])
        else:
            dict_chlen[get_pow_from_chlen(chlen)] = float(chlen[:n])
    return dict_chlen


def get_list_chlen(str_mchlen: str) -> list:
    
    str_mchlen = str_mchlen.replace(' ','')
    str_mchlen = str_mchlen[:-2]
    str_mchlen = '+' + str_mchlen

    n = len(str_mchlen)
    list_chlen = []

    while True:    
        reg_exp = re.search(r'[+-][0-9,.,x,^,\u2070-\u2079,\u00B9,\u00B2-\u00B3]+$', str_mchlen[:n])
        if reg_exp != None:
            list_chlen.append(str_mchlen[reg_exp.start():reg_exp.end()])
            n = reg_exp.start()       
        else:
            break
    return list_chlen


def gen_str_mchlen(dict_in: dict) -> str:
    str_mchlen = '= 0'
    str_x = ''
    str_pow = ''

    for sorted_key in sorted(dict_in.keys()):
        match sorted_key:
            case 0:
                str_x = ''
                str_pow = ''
            case 1:
                str_x = 'x'
                str_pow = ''
            case __:
                str_x = 'x'
                str_pow = my_func.int_to_pow(sorted_key)
        
        if dict_in[sorted_key] > 0:
            str_mchlen = '+ {0:g}'.format(dict_in[sorted_key]) + str_x + str_pow + ' ' + str_mchlen
        else:
            str_mchlen = '- ' + '{0:g}'.format(dict_in[sorted_key])[1:] + str_x + str_pow + ' ' + str_mchlen
    
    if str_mchlen[0] == '-':
        return '-' + str_mchlen[2:]
    else:
        return str_mchlen[2:]


def write_to_file(file_name: str, str_in: str):
    with open(file_name,'w') as f:
        f.write(str_in)


def get_sum_mchlen_dict(dict_1: dict, dict_2: dict) -> dict:
    dict_res = dict_1.copy()
    for key in dict_2:
        if key in dict_res:
            dict_res[key] += dict_2[key]
        else:
            dict_res[key] = dict_2[key]
    return dict_res


def get_sum_mchlen_str_from_files(fname_1: str, fname_2: str) -> str:
    str_m_1 = read_from_file(fname_1)
    str_m_2 = read_from_file(fname_2)

    list_chlen_1 = get_list_chlen(str_m_1)
    list_chlen_2 = get_list_chlen(str_m_2)

    dict_chlen_1 = get_dict_chlen(list_chlen_1)
    dict_chlen_2 = get_dict_chlen(list_chlen_2)

    dict_res = get_sum_mchlen_dict(dict_chlen_1, dict_chlen_2)

    return gen_str_mchlen(dict_res)


file_name_1 = 'task5_1.txt'
file_name_2 = 'task5_2.txt'
file_name_3 = 'task5_3.txt'

try:
    write_to_file(file_name_3, get_sum_mchlen_str_from_files(file_name_1, file_name_2))
except:
    print('something wrong. check files')