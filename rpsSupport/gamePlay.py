import typing
from . import rules
from . import getPlayerThrows
from . import getComputerThrow
from . import playeroutcome


def playGame(gameDict: typing.Dict[str, typing.List[str]]) -> typing.Tuple[str, str]:
    playerThrow = getPlayerThrows.getUserInput(gameDict)
    computerThrow = getComputerThrow.computerthrow(gameDict)
    return playeroutcome.playeroutcome(gameDict, playerThrow, computerThrow), computerThrow


def getGameChoice() -> typing.Dict[str, typing.List[str]]:
    choices = {
        1: "Rock paper scissors",
        2: "Rock paper scissors lizard spock"
    }
    gameTable = {
        1: rules.rps,
        2: rules.rpsls
    }
    print("Game options:")
    for number, game in choices.items():
        print("%s: %s" %(number, game))
    userInput = False
    while not userInput:
        userInput = input("Game choice:")
        try:
            userInput = int(userInput)
        except ValueError:
            print("Invalid Selection!")
        if userInput not in choices:
            print("Invalid Selection!")
            userInput = False
    return gameTable[userInput]