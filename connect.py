import discord
import random
from flipcoindef import flip_coin
from genpass import gen_pass
from passlengthdef import passask
from randomemoji import gen_emodji

with open("token.txt", "r" ) as f:
    token = f.read()


# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/halo'):
        await message.channel.send("Hi! :smile: :wave:")
    elif message.content.startswith('/bye'):
        await message.channel.send(":wave: :pensive: ")
    elif message.content.startswith('/help'):
        await message.channel.send("Please Write /cmdlist ")
    elif message.content.startswith('/cmdlist'):
        await message.channel.send("Command List: /halo, /bye, /cmdlist, /help, /flipcoin, /passgenerator, /randomemoji")
    elif message.content.startswith('/flipcoin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('/randomemoji'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('/passgenerator'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send(message.content)

client.run(token)