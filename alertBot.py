import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Bot is created by https://cracked.io/Tana')

@client.command()
async def alert(ctx, user: discord.Member):
    if ctx.message.guild.owner == ctx.message.author:
        embed = discord.Embed(title="Alert Set", description=f"Alert set for {user.mention}. Please respond within 12 hours.", color=discord.Color.green())
        await ctx.send(f'{user.mention}')
        await ctx.send(embed=embed)
        await asyncio.sleep(43200) # change to 43200 for 12 hours
        channel = ctx.message.channel
        role = ctx.guild.default_role
        await channel.set_permissions(role, read_messages=False)
        await user.send('Ticket closed due to no response within 12 hours.')
    else:
        await ctx.send('Only server owner can set alerts.')

client.run('BOT_TOKEN')
