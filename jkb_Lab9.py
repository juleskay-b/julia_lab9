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

def main(): #Main function - Julia
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        selection = input("Please enter an option: ")
        if selection == "1":
            password = input("Please enter the password to encode: ")
            print("Your password has been encoded and stored!")
            print("")

        elif selection == "2":
            e_password = encode(password)
            d_password = decode(e_password)
            print(f"The encoded password is {e_password}, and the original password is {d_password}.")
            print("")
        elif selection == "3":
            break
        else:
            print("Error. Invalid option.")
            print("")

    return

if __name__ == "__main__":
    main()