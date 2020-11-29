import os
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')


bot = TelegramClient('bots', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a message when the command /start is issued."""
    await event.respond('''Moin! Я смотрю, решил подняться. Ну чтож, давай проверим, насколько успешная у тебя стратегия.
Чтобы составить прогноз, введи команду /newcheck. И да, валюта не имеет значения, так что вводи просто числа.''')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/newcheck'))
async def invest(event):
    await event.respond("Для начала введи сумму, с которой хочешь начать инвестировать")
    with event.conversation(chat) as conv:
        conv.send_message('Для начала введи сумму, с которой хочешь начать инвестировать')
        first_deposit = conv.get_response()

        conv.send_message("Сколько ты готов вкладывать ежемесячно?")
        deposit = conv.get_response()

        conv.send_message(f"Ваш стартовый - {first_deposit}, и не стратовый - {deposit}")


"""
async def first_deposit(event):
    await event.respond("Для начала введи сумму, с которой хочешь начать инвестировать")
    first_deposit = event.raw_text
    raise events.StopPropagation

@bot.on(events.NewMessage)
async def deposit(event):
    await event.respond("Сколько ты готов вкладывать ежемесячно?")
    deposit = event.raw_text
    return deposit

@bot.on(events.NewMessage)
async def growth(event):  
    deposit = event.raw_text
    await event.respond("Какой ежемесячный рост вы ожидаете?")
    await event.respond(f"Ваш стартовый - {first_deposit}, и не стратовый - {deposit}")
    raise events.StopPropagation

@bot.on(events.NewMessage)
async def year(event):
    growth = event.raw_text
    await event.respond("Введите количество месяцев, которое вы хотите инвестировать:")
    raise events.StopPropagation"""



def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()