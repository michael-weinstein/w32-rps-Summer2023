def playeroutcome(gamedict: dict, playerthrow: str, computerthrow: str) -> str:
    if playerthrow == computerthrow:
        return "tie"
    if computerthrow in gamedict[playerthrow]:
        return "win"
    else:
        return "lose"
    