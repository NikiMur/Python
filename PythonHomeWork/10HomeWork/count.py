from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

def count(update, context):
    count_bot = 0
    count_user = 0

    if WINNER ==1:
        count_user += 1

    elif WINNER == -1:
        count_bot += 1

    else:
        context.bot.send_message(update.effective_chat.id, 'Ничья')

    context.bot.send_message(update.effective_chat.id, f'Общий счет игры: Bot {count_bot} очков;' 
                                                        '{update.effective_user.first_name}: {count_user} очков')

    if count_bot > count_user:
        context.bot.send_message(update.effective_chat.id, f'Игру ведет Bot с общим счетом {count_bot} : {count_user}')
    elif count_bot < count_user:
        context.bot.send_message(update.effective_chat.id, f'Игру ведет {update.effective_user.first_name} с общим счетом {count_user} : {count_bot}')
    else:
        context.bot.send_message(update.effective_chat.id, f'Ничья {count_user} : {count_bot}')