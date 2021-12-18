from interactions.context import CommandContext
from loader import bot, scope


@bot.command(name='ping', description='ngbfds',  scope=scope)
async def ping(ctx: CommandContext):
    await ctx.send(f'Pong! ({bot.latency*1000}ms)')
