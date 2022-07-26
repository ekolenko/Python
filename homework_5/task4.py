#!/usr/bin/python3

import os


def input_command():
    print('Выберите действие:\n  1 - сжать данные из файла\n  2 - извлечь данные из файла')
    while True:
        str_in = input().replace(' ','') 
        if str_in == '1':
            return 1
        elif str_in == '2':
            return 2
        else:
            print('Ошибка ввода')

def imput_file_name():
    while True:
        file_name = input("Введите имя файла: ")
        if os.path.isfile(file_name):
            return file_name
        else:
            print("Файл не найден")

def open_file(file_name: str):
    with open(file_name, 'r') as data:
        string_data = data.readline()
    return string_data


def zip_file(string_data: str):
    counter = 0
    new_string = ''
    prev_char = string_data[0]
    for index in range(len(string_data)):
        if string_data[index] != prev_char:
            if counter == 1:
                new_string += prev_char
            else:
                new_string += prev_char + str(counter)
                counter = 1
        else:
            counter += 1
        prev_char = string_data[index]
        if index == len(string_data) - 1:
            new_string += prev_char + str(counter)
    return new_string


def unzip_file(string_data: str):
    new_string = ''
    string_data += "+"
    index = 0
    while index < len(string_data)-1:
        char_data = ""
        num_data = ""
        if not string_data[index].isdigit() and not string_data[index+1].isdigit():
            new_string += string_data[index]
            index += 1
        if not string_data[index].isdigit() and string_data[index + 1].isdigit():
            char_data += string_data[index]
            index += 1
            while string_data[index].isdigit():
                    num_data += string_data[index]
                    index += 1
            new_string += char_data * int(num_data)

    return new_string

file_name = imput_file_name()

match input_command():
    case 1:
        print(f"Сжатые данные: {zip_file(open_file(file_name))}")
    case 2:
        print(f"Извлеченные данные: {unzip_file(open_file(file_name))}")


