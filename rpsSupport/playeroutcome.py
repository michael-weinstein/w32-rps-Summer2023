import typing


def playeroutcome(gamedict: typing.Dict[str, typing.List[str]], playerthrow: str, computerthrow: str) -> str:
    if playerthrow == computerthrow:
        return "tie"
    if computerthrow in gamedict[playerthrow]:
        return "win"
    else:
        return "lose"
    