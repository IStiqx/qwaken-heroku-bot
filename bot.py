import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os



bot = commands.Bot(command_prefix="a.")



@bot.event
async def on_ready():
  print(bot.user.name)

  
  
@bot.command(pass_context=True)
async def hi(ctx):
  await bot.say("Hello there"+" "+ctx.message.author.name)
  
  
  
  
bot.run(os.environ['NDU1NDA5ODUyNzg5ODE3Mzk1.Df_KMQ.L2B4jTgX87INQ8ivPIej4ixCumk'])
