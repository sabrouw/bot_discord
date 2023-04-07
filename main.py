from json import load
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")
# définition de discord avec les droits qu'on a cocher sur discord dev
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


#définir client  à déclarer au début!
bot = commands.Bot(command_prefix="!", intents=intents)

# creer une fonction avec event de discord et son décorateur client.event
@bot.event
async def on_ready():
    print("je suis pret noob!")



# fonction qui envoie un message en recuperant le serveur qui envoie et répondant
@bot.event
async def on_message(message):
    # condition de réponse 
    if message.content == "ping":
       await message.channel.send("pong")

    
# fonction pour envoyer un message au membre qui joigne le server
@bot.event
async def on_membre_join(member):
    # text channel pour specifier le menu deroulant des methode disponible
    # récuperer le salon general avec son identifiant en mode dev + clique droit sur discord
    # dans general_channel
    general_channel : discord.TextChannel = bot.get_channel(526468501360214018)
    # on send un message de bienvenue avec le nom du membre placé en paramètre de la fonction
    await general_channel.send(content=f"Bienvenue noob {member.display.name}")

@bot.command(name="clear")
async def on_message_delete(ctx, number: int):
    CHANNEL_ID = 526468501360214018
    if ctx.channel.id == CHANNEL_ID:
        messages = await ctx.channel.hystory(limit=number + 1).flatten()
    

        for each_message in messages:
            await each_message.delete()
       
# run le token de notre bot connexion du bot au server sur discord
bot.run(os.getenv("TOKEN"))
