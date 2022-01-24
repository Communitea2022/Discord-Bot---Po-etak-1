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

client.run("OTM1MjM2MDkyMjU5NjE0Nzgw.Ye7sfA.I9CRtEpTmN8g8Yq3JLurFmRfuH0")