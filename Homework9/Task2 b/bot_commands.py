import re
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from get_info import get_info
import logger
from write_read import read_file_string

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/help\n/search\n/write\n/delete\n')

async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    surname = update.message.text
    surname = surname.split()
    file = read_file_string.write_read()
    new_file = file.split()
    if surname in new_file:
        for i in range(len(new_file)):
            if surname == new_file[i]:
                print(new_file [i], new_file[i+1], new_file[i+2], new_file[i+3])
    
    await update.message.reply_text(f'Найден контакт: {new_file [i], new_file[i+1], new_file[i+2], new_file[i+3]}')

async def write_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info = get_info()
    with open('Phonebook_string.csv', 'a', encoding='utf-8', newline='') as file:
        file.write(f'{info[0]},{info[1]},{info[2]},{info[3]}\n')
    logger.info_logger(f'Новая запись в тел.книгу 1: {info}')
    await update.message.reply_text(f'Запись: {info[0]},{info[1]},{info[2]},{info[3]}')

async def delete_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open ('Phonebook_string.csv', 'r', encoding='utf-8', newline='') as file:
        lst = file.readlines()
        surname = update.message.text
        pattern = re.compile(re.escape(surname))
        with open('Phonebook_string.csv', 'w', encoding='utf-8', newline='') as f:
            for i in lst:
                result = pattern.search(i)
                if result is None:
                    f.write(i)
    logger.info_logger(f'Удаление записи: {pattern}')
    await update.message.reply_text(f'Запись удалена')