import discord, os, alive, asyncio, datetime, pytz
from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='!',
  self_bot=True
)

@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = "Tuỳ chỉnh", url = "https://www.twitch.tv/đặt_theo_link_của_bạn"))
  #Ví dụ: await client.change_presence(activity = discord.Streaming(name = "AFK | 24/7", url = "https://www.twitch.tv/nnittsuu_"))

alive.alive()
client.run(os.getenv("TOKEN"), bot=False)
