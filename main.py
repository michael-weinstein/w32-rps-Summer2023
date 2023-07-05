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
    print("TIE")
elif(outcome == "win"):
    print("WIN")
else:
    print("LOSE")