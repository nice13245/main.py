import discord
import random
from discord.ext import commands
from discord.ext.commands import command
import secrets
import os
import requests
prefix = "$"
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix= prefix, intents=intents )


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def repeat(ctx, times: int, content='Богдан гей ебанный'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        
from discord.ext.commands import CommandNotFound
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

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

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def random_photo(ctx):
    folder_path = (r"C:\Users\kirll\OneDrive\Рабочий стол\proj\images")
    files = os.listdir(folder_path)
    random_file = random.choice(files)

    # Отправка файла пользователю
    await ctx.send(file=discord.File(os.path.join(folder_path, random_file)))
    
@bot.command()
async def animal(ctx):
    folder_path = r"C:\Users\kirll\OneDrive\Рабочий стол\proj\animals"
    files = ['animals_meme1.jpg', 'animals_meme2.jpg', 'cats_meme1.jpg', 'dogs_meme1.jpg']
    random_files = []
    for file in files:
        random_files.append(file)
    random_file = random.choice(random_files)
    await ctx.send(file=discord.File(os.path.join(folder_path, random_file)))
bot.run("token")
