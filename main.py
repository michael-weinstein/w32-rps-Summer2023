import rpsSupport


def playGame():
    gameDict = rpsSupport.rules.rps
    playerThrow = rpsSupport.getPlayerThrows.getUserInput(gameDict)
    computerThrow = rpsSupport.getComputerThrow.computerthrow(gameDict)
    outcome = rpsSupport.playeroutcome.playeroutcome(gameDict, playerThrow, computerThrow)
    print("Computer chose %s" %computerThrow)
    if(outcome == "tie"):
        print("The game is a tie. -_-")
    elif(outcome == "win"):
        print("The player wins!!! :)")
    else:
        print("The player losses :(")


if __name__ == "__main__":
    playGame()