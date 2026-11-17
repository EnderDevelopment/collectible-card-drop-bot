import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='drop')
async def drop(ctx, user: discord.Member, card: str, group: str, era: str, rarity: int):
    rarity_emoji = {
        1: '<:emoji_1:>',
        2: '<:emoji_2:>',
        3: '<:emoji_3:>'
    }.get(rarity, '')
    await ctx.send(f'{user.mention}, you got {rarity_emoji} {card} from {group} era {era}')

bot.run(TOKEN)