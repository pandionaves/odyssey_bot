from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
from typing import Union
import random

from fastapi import FastAPI

app = FastAPI()

verbalPrompt = 0


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
client: Client = Client(intents=intents)


# MESSAGE FUNCTIONALITY

def choose_verbal_prompts():
    if verbalPrompt == 1:
        return ('**A Colorful Problem:** Name a color and something that is that color. Example: Yellow - bananas are'
                ' yellow. Red - books are read. Fuchsia - Fuchsias are Fuchsia.')
    if verbalPrompt == 2:
        return '**Im Blue:** Name things that are blue.'
    if verbalPrompt == 3:
        return '**Sounds Like Spontaneous:** Name things that produce sound and what causes them to produce it.'
    if verbalPrompt == 4:
        return '**You Can Coat-tally Do This!:** List things that have a coat.'
    if verbalPrompt == 5:
        return '**Thats It:** Name all the different ways you can use the word "IT."'
    if verbalPrompt == 6:
        return ('**Alternate Tree-ality:** Weve all heard it said that money does not grow on trees, though most of us '
                'wish it did. If you could have any type of tree in your backyard what would it be and why?')
    if verbalPrompt == 7:
        return '**Atop Lady Liberty:** If you were stuck on top of the Statue Of Liberty how would you get down?'
    if verbalPrompt == 8:
        return '**A Wheel Problem:** What would you say if you were a wagon wheel on a wagon on the Oregon Trail?'
    if verbalPrompt == 9:
        return ('**A Royal Story:** Tell a story to a deck of cards. Example: The King of Hearts married the Queen of '
                'Clubs and had 9 children.')


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
