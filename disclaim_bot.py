import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Set up environment variables and get the Bots oauth2 token
project_folder = os.path.expanduser('~/disclaimer_bot')
load_dotenv(os.path.join(project_folder, '.env'))
TOKEN = os.getenv("TOKEN")

# Create an instance of the bot
bot = commands.Bot(command_prefix='!',case_insensitive=True, description='A simple bot to let you know who\'s not liable')

# Set an on ready event
@bot.event
async def on_ready():
    print('Bot is ready')

# Set commands for bot

# The disclaimer command using an embed
@bot.command(description='Legal message')
async def disclaimer(ctx, mention, *, alliance):
    embed = discord.Embed(title='Disclaimer',
                        description='The opinions expressed by {0} are not necessarily the views of the {1} alliance and {0} speaks soley as the individual they are. With this in mind please do not complain to {1} leadership as you may be unceremoniously told where you can shove it. You have been warned.'.format(mention, alliance),
                        color=0xff0000)
    embed.add_field(name="Signed", value='{}'.format(alliance), inline=False)
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

# Command to allow administrator to logout the bot
@bot.command(description='Stop bot completely - Only Greedo can restart')
@commands.has_permissions(administrator=True)
async def stop(ctx):
    await bot.logout()

def is_it_greedo(ctx):
    return ctx.author.id == 267051171955343361

@bot.command(description='Show guilds bot is using')
@commands.check(is_it_greedo)
async def list_guilds(ctx):
    print(bot.guilds)

bot.run(TOKEN)