def getUserInput(gamedict: dict) -> str:
    inputs= gamedict.keys()
    print("Throw options:")
    listofnumbers=range(1,len(inputs))
    for i in listofnumbers:
        print(f"{i}: {inputs[i-1]}")
    userInput=input("Choose your throw:")
    return inputs[userInput-1]