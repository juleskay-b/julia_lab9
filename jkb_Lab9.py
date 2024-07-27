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

def decode(encoded_password): # function to decode password - Sofia
    original = ""
    for i in encoded_password:
        if i == "0":
            original += "7"
        elif i == "1":
            original += "8"
        elif i == "2":
            original += "9"
        else:
            original += str(int(i) - 3)
    return original

