from get_info import get_info
import logger


def write_file_string():
    info = get_info()
    with open('Phonebook_string.csv', 'a', encoding='utf-8', newline='') as file:
        file.write(f'{info[0]},{info[1]},{info[2]},{info[3]}\n')
    logger.info_logger(f'Новая запись в тел.книгу 1: {info}')


def read_file_string():
    with open ('Phonebook_string.csv', 'r', encoding='utf-8', newline='') as file:
        list = file.read()
        some_list = list.replace(','," ")
        return(some_list)
        