from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot_commands import hi_command
from bot_commands import search_command
from bot_commands import help_command
from bot_commands import write_command
from bot_commands import delete_command

app = ApplicationBuilder().token('Token').build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("search", search_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("write", write_command))
app.add_handler(CommandHandler("delete", delete_command))

print('server start')
app.run_polling()
