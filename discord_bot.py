import discord
import requests
import ast
import random

URL = "https://covidapi.info/api/v1/country/JPN/latest"
TOKEN = "your bot's TOKEN"
client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/hello':
        await message.channel.send('hello')
    if message.content == '/covid JPN':
        res = requests.get(URL).text
        dic = ast.literal_eval(res)
        date = list(dic['result'].keys())[0]
        data = dic['result'][date]
        covid_info = '[' + date + ']'
        covid_info += ' confirmed: ' + str(data['confirmed'])
        covid_info += ' | deaths: ' + str(data['deaths'])
        covid_info += ' | recovered: ' + str(data['recovered'])
        await message.channel.send(covid_info)
    if message.content == '/hungry':
        words = ["Dig in! ", "Enjoy your meal♪", "Bon appetit."]
        foods = []
        for i in range(7):
            foods.append(discord.File(f"food{i}.jpg"))
        await message.channel.send(file=random.choice(foods))
        await message.channel.send(random.choice(words))

client.run(TOKEN)