import telebot

from random import randint

bot = telebot.TeleBot(token, parse_mode = None)

game_move = False
candies = 2021

def comp(message):
    global candies, game_move
    n = randint(1, 28)
    if n < candies:
        candies -= n
        bot.send_message(message.chat.id, f'Компьютер забрал {n} конфет. Осталось {candies} конфет.')
    else:
        game_move = False
        bot.send_message(message.chat.id, 'Игра окончена. Компьютер выиграл!')

@bot.message_handler(commands = ['start'])
def start_game(message):
    player = message.from_user.first_name 
    global game_move
    if not game_move:
        global candies
        game_move = True
        players_turn = bool(randint(0, 1))
        bot.send_message(message.chat.id, f'Сначало было {candies} конфет. {"Игрок" if players_turn else "Бот"} делает первый ход')
        bot.send_message(message.chat.id,  f'{player}, введите число, не большее 28.') if players_turn else comp(message)
        if game_move: players_turn = not players_turn

@bot.message_handler(func = lambda _: game_move)
def players(message):
    player = message.from_user.first_name
    global candies, game_move
    try:
        n = int(message.text)
        if n > 28:
            bot.send_message(message.chat.id, f'{player}, число должно быть не больше 28. Попытайтесь ещё раз.')
        else:
            if n < candies:
                candies -= n
                bot.send_message(message.chat.id, f'Осталось {candies} конфет.')
                comp(message)
                if game_move: bot.send_message(message.chat.id,  f'{player}, введите число, не большее 28.')
            else:
                candies = 0
                game_move = False
                bot.send_message(message.chat.id, f'Игра окончена. {player}, Вы выйграли!')
    except:
        bot.send_message(message.chat.id, 'Неверные данные. Попробуйте еще раз.')

bot.infinity_polling()