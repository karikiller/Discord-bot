import discord
from discord import app_commands
from discord.ext import commands

TOKEN = 'Here is my token'
PREFIX = '/'
intents = discord.Intents().all()

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print("Бот готов работать!")
    try:
        synced = await bot.tree.sync()
        print(f"Синхронизированно {len(synced)} команд")
    except Exception as e:
        print(e)

@bot.tree.command(name="salam",description="Бот кидает вам плотный саламчик")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Саламалейкум братищке, жи есть?")

@bot.tree.command(name="song1", description="Пишет вам текст одной песни")
async def slash_command(interaction: discord.Interaction):
    await interaction.response.send_message("""За тебя калым отдам, душу дьяволу продам! 
И как будто бы с небес, всё к тебе толкает бес 
За тебя калым отдам, душу дьяволу продам! 
Пусть бушует в сердце кровь, мне нужна твоя любовь""")

@bot.tree.command(name="slash_testr")
async def slash_test(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.name}, это команды слэша", ephemeral=True)

@bot.tree.command(name="say1")
@app_commands.describe(thing_to_say = "What should i say?")
async def say1(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} сказал: `{thing_to_say}`")

@bot.command()
async def summa(ctx, num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        await ctx.send('Error')
        return
    result = num1 + num2
    await ctx.send(str(result))

bot.run(TOKEN)
