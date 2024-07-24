def encode(password): #function to encode password - Julia
    new = ""
    for i in password:
        if i == "7":
            new += "0"
        elif i == "8":
            new += "1"
        elif i == "9":
            new += "2"
        else:
            new += str(int(i) + 3)

    return new

