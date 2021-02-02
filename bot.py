import os
import discord
import asyncio
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='!')

slurdict = [ "nigger", "tranny", "fag", "faggot", "spic", "coon", "kike", "lesbo", "chink", "dyke", "paki"] #pls do not kill me that's the slur dictionary i'm using

@bot.event
async def on_message(message):
    #uncomment the four lines below if you want to add a channel that bypasses the slur restrictions
    # if message.channel.id == insert id:
    #    return
    # else:
        msg = message.content.lower()
        for i in slurdict:
            if i in msg:
                await message.delete()
                await message.channel.send("Please do not use slurs, they're not appreciated!")

    #Ignore messages sent by the bot
    if message.author == bot.user:
        return
    await bot.process_commands(message)
    
bot.run(TOKEN)

