from discord_api import Client
from json import dump

client = Client(log = False)
with open("config.json") as f:
    config = dump(f)

@client.event
async def on_ready():
    print("ready!")
    
client.run(config["token"])
