from loader import bot

import handlers, buttons


@bot.event
async def on_ready():
    print('Ready!')

bot.start()