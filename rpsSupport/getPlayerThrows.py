import typing


def getUserInput(gamedict: typing.Dict[str, typing.List[str]]) -> str:
    inputs = list(gamedict.keys())
    print("Throw options:")
    listofnumbers = range(1, len(inputs) + 1)
    for i in listofnumbers:
        print(f"{i}: {inputs[i-1]}")
    userInput = False
    while not userInput:
        userInput = input("Choose your throw:")
        try:
            userInput = int(userInput)
        except ValueError:
            print("Invalid Selection!")
        if not 0 < userInput <= len(inputs):
            print("Invalid Selection!")
            userInput = False
    return inputs[userInput-1]
