import discord
from discord.ext import commands 
import matplotlib.pyplot as plt
import os
import numpy as np

os.environ['MPLCONFIGDIR'] = '/tmp'
intents = discord.Intents.default()
bot = commands.Bot(commands.when_mentioned_or("m!"),intents=intents,activity=discord.Activity(type=discord.ActivityType.listening,name="Created by 5232TheElder#1923 - Prefix: m!"), case_insensitive=True)

@bot.command()
async def piechart(ctx,*data):
  plt.pie(data)
  plt.savefig("output1.jpg")
  with open("output1.jpg", "rb") as fileBytes:
    f = discord.File(fileBytes, filename="output1.jpg")
  await ctx.send(file=f)
  with open("output1.jpg", "wb") as fileBytes:
    fileBytes.truncate(0)
@bot.command()
async def barchart(ctx,color="red",*x):
  plt.bar(np.arange(len(x)), x, color=color)
  plt.savefig("output.jpg")
  with open("output.jpg", "rb") as fileBytes1:
    f1 = discord.File(fileBytes1, filename="output.jpg")
  await ctx.send(file=f1)
  with open("output.jpg", "wb") as fileBytes:
    fileBytes.truncate(0)
@bot.event
async def on_ready():
  print("Connected")
bot.run(os.environ['token'])


