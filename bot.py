import discord
from discord.ext import commands

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
    
    async def setup_hook(self):
        await self.tree.sync()
    
    async def on_ready(self):
        print(f"Bot {self.user} is ready !")

bot = MyBot()

@bot.tree.command(name="hello", description="Bot respond \"Hello\"")
async def hello(interaction : discord.Interaction):
    await interaction.response.send_message("Hello")

bot.run("YOUR TOKEN")