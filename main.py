from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responces import get_response
from typing import Union
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True #NUH UH
client: Client = Client(intents=intents)

# MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:

    if not user_message:
        print('Message was empty or unable to be read. Intents were likely not enabled properly')
        return

    try:
        response: str = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

# STARTUP
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# HANDLING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()