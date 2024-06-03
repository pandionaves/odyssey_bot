from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if '!testcode' in lowered:
        return 'This message indicates the bot is running.'

    