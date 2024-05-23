import discord
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)
intents.message_content = True
intents.guilds = True
intents.members = True


@bot.event
async def on_ready():
    print (f"{bot.user.name} s'est bien connecté !")

@bot.command
async def ping(ctx):
    await ctx.send("pong")


bot.run("MTI0MjgzNjk4NzQ0NzIxNDI1Mw.GcZt8V.0niIKAC39G9Zty2qAePWX0IpSKy-J3PLx8GnE8")