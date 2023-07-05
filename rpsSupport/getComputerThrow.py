import random
import typing


def computerthrow(gamedict: typing.Dict[str, typing.List[str]]) -> str:
    choice_list = list(gamedict.keys())
    computer_choice = random.choice(choice_list)
    return computer_choice