from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from spy import *

async def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')
async def help_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'/hi\n/sum\n/sub\n/mult\n/div\n/help')
async def sub_command(update: Update, context: CallbackContext):
    log(update, context)
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} - {y} = {x-y}')
    
async def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')
async def mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x*y}')    
async def div_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} / {y} = {x/y}')   

