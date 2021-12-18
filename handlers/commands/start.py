from interactions.context import CommandContext

from loader import bot, scope
from buttons.action_rows.greetings import action_row


@bot.command(name="start", description='ghbjnmk', scope=scope)
async def start(ctx: CommandContext):
    await ctx.send(f"Привет, {ctx.author.nick}", components=action_row)

