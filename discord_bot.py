import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='<')

# let us know the bot is online
@bot.event
async def on_ready():
    print(">> Bot is online <<")

# notify when member join    
@bot.event
async def on_member_join(member):
    print(f'{member} join!') 
    
# notify when member left
@bot.event
async def on_member_remove(member):
    print(f'{member} leave...')

bot.run('OTQyOTQxNDA0MDEzOTM2NjUw.Ygr0nQ.mbNFGurUR9mOPcQBRm8W3b4ANDM')

