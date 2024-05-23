import random

import discord
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)
intents.message_content = True
intents.guilds = True
intents.members = True

welcome_message = "Bienvenue sur le serveur"


@bot.event
async def on_ready():
    print(f"{bot.user.name} s'est bien connecté !")


@bot.command()
async def ping(ctx):
    await ctx.send("pong :ping_pong:")


@bot.command()
async def touché(ctx):
    await ctx.send("coulé :sailboat:")


@bot.command()
async def members(ctx):
    message_content = f"**Membres du serveur ({len(ctx.guild.members)}) :**\n"

    for member in ctx.guild.members:
        roles = [role.name for role in member.roles]
        message_content += f"- {member.display_name} -> {roles}\n"

    await ctx.send(message_content)


@bot.command()
async def joke(ctx):
    jokes = [
        "Pourquoi les développeurs n'aiment-ils pas la nature ? Parce qu'il y a trop de bugs.",
        "Pourquoi les pirates informatiques aiment-ils les bateaux ? Parce qu'ils peuvent naviguer sur les nets.",
        "Combien de programmeurs faut-il pour changer une ampoule ? Aucun, c'est un problème matériel.",
        "Pourquoi les programmeurs préfèrent-ils le noir ? Parce que ça réduit les bugs.",
        "Pourquoi Java a-t-il du mal à faire des amis ? Parce qu'il est toujours en train de créer des classes.",
        "Quelle est la différence entre un pirate et un développeur ? Le pirate casse les codes, le développeur les écrit.",
        "Pourquoi les programmeurs détestent-ils les cercles ? Parce qu'ils ont trop de boucles infinies.",
        "Pourquoi les ordinateurs ne peuvent-ils pas se battre ? Parce qu'ils n'ont pas assez de RAM pour se souvenir de la colère.",
        "Pourquoi les programmeurs préfèrent-ils utiliser des espaces au lieu des tabulations ? Parce qu'ils ne veulent pas être dépendants.",
        "Pourquoi les programmeurs confondent-ils souvent Halloween et Noël ? Parce que OCT 31 == DEC 25."
    ]
    joke = random.choice(jokes)
    await ctx.send(joke)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "bonjour" in message.content.lower():
        await message.add_reaction("👋")
    elif "bonne nuit" in message.content.lower():
        await message.add_reaction("🌙")
    elif "félicitations" in message.content.lower():
        await message.add_reaction("🎉")
    elif "triste" in message.content.lower():
        await message.add_reaction("😢")

    await bot.process_commands(message)


@bot.event
async def on_member_join(member):
    await member.guild.system_channel.send(f"{member.mention}, {welcome_message}")


bot.run("MTI0MjgzNjk4NzQ0NzIxNDI1Mw.GcZt8V.0niIKAC39G9Zty2qAePWX0IpSKy-J3PLx8GnE8")
