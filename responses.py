from random import choice, randint
from main import choose_verbal_prompts
import random


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if '!testcode' in lowered:
        return 'This message indicates the bot is running.'
    if '!spont' in lowered:
        verbalPrompt = random.randint(1, 9)
        choose_verbal_prompts()
