import rpsSupport
import typing

if __name__ == "__main__":
    ruleset = rpsSupport.gamePlay.getGameChoice()
    outcome, computerThrow = rpsSupport.gamePlay.playGame(ruleset)
    print("Computer chose %s" %computerThrow)
    if(outcome == "tie"):
        print("The game is a tie. -_-")
    elif(outcome == "win"):
        print("The player wins!!! :)")
    else:
        print("The player losses :(")