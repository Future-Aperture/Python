def two_fer(name = "you"):
    if name.isnumeric():
        raise Exception("You can't use numbers as a name.")
    
    return f"One for {name}, one for me."