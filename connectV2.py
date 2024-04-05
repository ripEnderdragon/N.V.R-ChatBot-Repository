import discord
import random
import requests
import os
from discord.ext import commands
from genpass import gen_pass
from randomemoji import gen_emodji
from flipcoindef import flip_coin
from envitipsdef import print_tips
with open ("token.txt", "r") as f:
    token = f.read()

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def cmdlist(ctx):
    await ctx.send(f"Command List: $hello, $cmdlist, $flipcoin, $passwd, $randemo, $heh, $add")

@bot.command()
async def passwd(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def envitips(ctx):
    await ctx.send (print_tips())

@bot.command()
async def meme(ctx):
    randommeme = random.choice(os.listdir('pictures'))

    with open(f'pictures/{randommeme}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

def get_cat_image_url():    
    url = 'https://api.thecatapi.com/v1/images/search'
    res = requests.get(url)
    data = res.json()
    return data['id']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('fox')
async def fox(ctx, count):
    for i in range (count):
        image_url = get_fox_image_url()
        await ctx.send(image_url)

@bot.command('cat')
async def cat(ctx):
    image_url = get_cat_image_url()
    await ctx.send(image_url)

@bot.command()
async def flipcoin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def randemo(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def arrangenum(ctx, num1: int, num2: int):
    #  num3: int, num4: int, num5: int):
    result = ""
    if num1 < num2 and num3 and num4 and num5:
        result += num1
    elif num2 < num1 and num3 and num4 and num5:
        result += num2
    # elif num3 < num1 and num2 and num4 and num5:
    #     result += num3
    # elif num4 < num1 and num2 and num3 and num5:
    #     result += num3
    # elif num5 < num1 and num2 and num3 and num4:
    #     result += num5
    return result





@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


bot.run(token)