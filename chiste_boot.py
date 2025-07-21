import discord
from discord.ext import commands
import random

# Lista de chistes y URLs de imágenes
chistes = [
    {
        "texto": "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
        "imagen": "https://i.imgur.com/mHqrm2U.jpeg"
    },
    {
        "texto": "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "imagen": "https://i.imgur.com/Kpc5eA6.jpeg"
    },
    {
        "texto": "¿Cómo se despiden los químicos? Ácido un placer.",
        "imagen": "https://i.imgur.com/b4SlgWl.jpeg"
    }
]

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command(name='chiste')
async def enviar_chiste(ctx):
    chiste = random.choice(chistes)
    embed = discord.Embed(title="😂 ¡Chiste del día!", description=chiste["texto"], color=0xff6666)
    embed.set_image(url=chiste["imagen"])
    await ctx.send(embed=embed)

# Reemplaza este token con el tuyo
bot.run('MTM5NjU0NTczMTY2MTEzOTk3OQ.GuL3S3.R0s4XYaJvUECWKJzjowxzPBBbLeVupSFMeWtNo')
