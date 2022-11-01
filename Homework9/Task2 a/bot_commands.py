from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from main import *

app = ApplicationBuilder().token('Token').build()

app.add_handler(CommandHandler('hi', hi_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('sum', sum_command))
app.add_handler(CommandHandler('sub', sub_command))
app.add_handler(CommandHandler('mult', mult_command))
app.add_handler(CommandHandler('div', div_command))



print('server start')
app.run_polling()
