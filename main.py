import discord
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
TOKEN = os.getenv("TOKEN")

USER_ID_1 = os.getenv("USER_ID_1") #lou
USER_ID_2 = os.getenv("USER_ID_2") #igod
USER_ID_3 = os.getenv("USER_ID_3") #dirion
USER_ID_4 = os.getenv("USER_ID_4") #sebi
GIF_URL_1 = "https://c.tenor.com/yupsD6HaSMMAAAAd/tenor.gif"
GIF_URL_2 = "https://c.tenor.com/hBFJV2kNYBQAAAAd/tenor.gif"
GIF_URL_3 = ""
GIF_URL_4 = "https://c.tenor.com/cgWc0q0vIU0AAAAd/tenor.gif"

# Discord Intents konfigurieren
""" The line intents = discord.Intents.default() creates 
an instance of the Intents class from the discord library, using
 its default() factory method. In the context of Discord bots, 
"intents" are a way to specify which types of events your bot wants to receive from 
Discord's API.  """

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
KEYWORDS = ["Asiate", "DCs", "Roster", "heul"]

# Dictionary für Zeit-Tracking pro User
last_sent = {}

@client.event
async def on_message(message):
    now = datetime.now()
    # User 1 lou
    if message.author.id == USER_ID_1:
        content = message.content.lower()
        if any(word in content for word in KEYWORDS):
            last_time = last_sent.get(USER_ID_1)
            if not last_time or now - last_time > timedelta(hours=1):
                embed = discord.Embed(title="Cry Me A GAC-River")
                embed.set_image(url=GIF_URL_1)
                await message.channel.send(embed=embed)
                last_sent[USER_ID_1] = now
    # User 2 (beachte: .id , nicht == Objekt) igod
    elif message.author.id == USER_ID_2:
        last_time = last_sent.get(USER_ID_2)
        if not last_time or now - last_time > timedelta(hours=1):
            embed = discord.Embed(title="ichse liebse diesese spielse!")
            embed.set_image(url=GIF_URL_2)
            await message.channel.send(embed=embed)
            last_sent[USER_ID_2] = now
    # User 4 sebi
    elif message.author.id == USER_ID_4:
        last_time = last_sent.get(USER_ID_4)
        if not last_time or now - last_time > timedelta(hours=1):
            embed = discord.Embed(title="Less cryin, more tryin!")
            embed.set_image(url=GIF_URL_4)
            await message.channel.send(embed=embed)
            last_sent[USER_ID_4] = now

if __name__ == "__main__":
    client.run(TOKEN)