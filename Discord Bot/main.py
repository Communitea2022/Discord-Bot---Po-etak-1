import discord
from discord.ext import commands

#prefix za bota
client = commands.Bot(command_prefix=">")

#Pokretanje Bota
@client.event
async def on_ready():
    print("[+] Bot je pokrenut.")

#Komanda za Bota
@client.command()
async def hello(ctx):
    await ctx.send("Zdravo")

client.run("VAS DISCORD TOKEN")
