import rpsSupport
from rpsSupport import playeroutcome
from rpsSupport import rules
from rpsSupport import getPlayerThrows #placeholder
from rpsSupport import getComputerThrows #placeholder

outcome = playeroutcome.playeroutcome(
    rules.GameDict,
    getPlayerThrows.getThrow(rules.GameDict),
    getComputerThrows.getThrow(rules.GameDict)
)

if(outcome == "tie"):
    print("The game is a tie. -_-")
elif(outcome == "win"):
    print("The player wins!!! :)")
else:
    print("The player losses :(")