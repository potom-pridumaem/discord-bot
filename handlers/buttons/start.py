from interactions.context import ComponentContext
from loader import bot
from buttons.buttons.greetings import fuck_off, hello

@bot.component(fuck_off)
async def butt(ctx: ComponentContext):
    await ctx.send(content="Сам отстань")

@bot.component(hello)
async def butt2(ctx: ComponentContext):
    await ctx.edit(content="🎨")