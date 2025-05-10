import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.bans = True
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

@bot.command()
@commands.has_permissions(administrator=True)
async def unbanall(ctx):
    bans = [entry async for entry in ctx.guild.bans()]
    if not bans:
        await ctx.send("❌ Aucun utilisateur n'est actuellement banni.")
        return

    count = 0
    for ban_entry in bans:
        user = ban_entry.user
        try:
            await ctx.guild.unban(user)
            count += 1
        except Exception as e:
            await ctx.send(f"⚠️ Erreur pour {user}: {e}")

    await ctx.send(f"✅ {count} utilisateur(s) ont été débannis.")

bot.run("VOTRE_TOKEN_DISCORD")
