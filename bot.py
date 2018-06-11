import discord

from discord.ext import commands

from discord.ext.commands import Bot

import random

import asyncio

import os



Client = discord.Client()

bot = commands.Bot(command_prefix="!")

lines = open(r'accounts.txt').read().splitlines()

bot_room = "455412662172647434"



@bot.event

async def on_ready():

    print("The bot is online!")



@bot.command(pass_context=True)

async def gen(ctx):

    userName = ctx.message.author.name

    userID = ctx.message.author.id



    if ctx.message.server:

        await bot.delete_message(ctx.message)



        if ctx.message.channel.id == bot_room: 

            myline = random.choice(lines)

            split = myline.partition(":")

            

            embed=discord.Embed(title="Minecraft Account", color=0x09ff05)

            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/454933279573803008/454980780045631488/how-to-draw-a-minecraft-creeper-16.png")

            embed.add_field(name="Email:", value=split[0], inline=False)

            embed.add_field(name="Password:", value=split[2], inline=False)

            await bot.send_message(ctx.message.author, embed=embed)



            print("{} Typed !gen".format(userName))

        else:

            bot_message = await bot.say("<@{}> please use the !gen command in <#{}>".format(userID, bot_room))

            await asyncio.sleep(5)

            await bot.delete_message(bot_message)

    else:

        myline = random.choice(lines)

        split = myline.partition(":")

        

        embed=discord.Embed(title="Minecraft Account", color=0xf45eff)

        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/454933279573803008/454980780045631488/how-to-draw-a-minecraft-creeper-16.png")

        embed.add_field(name="Email:", value=split[0], inline=False)

        embed.add_field(name="Password:", value=split[2], inline=False)

        await bot.send_message(ctx.message.author, embed=embed)



        print("{} Typed !gen".format(userName))



bot.run("NDU1NDA5ODUyNzg5ODE3Mzk1.Df_KMQ.L2B4jTgX87INQ8ivPIej4ixCumk")
