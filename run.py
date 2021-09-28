import discord
import asyncio
from discord.ext import commands

# bot setting
token = 'ODkyMzY1NDcxNDY1MjI2MzAw.YVL2Gw.FCieK-E-o6iITuQoP8dbaiiK090'
game = discord.Game("!도움말")
bot = commands.Bot(command_prefix='!',
                   status=discord.Status.online, activity=game)


@bot.event
async def on_ready():
    print('Bot START')


@bot.command()
async def 도움말(ctx):
    await ctx.send("무엇을 도와드릴까요?")


bot.run(token)
