
import random

while True:
    randomizer_choice = str(input("Choose a randomizer:\n   Six-Sided Die (D6)\n   Ten-Sided Die (D10)\n   Twenty-Sided Die (D20)\n   8 Ball"))
    
    if randomizer_choice == "Quit" or randomizer_choice == "quit":
        print("Aborting Randomizer Tools
        break

    elif randomizer_choice == "D6" or randomizer_choice == "d6":
        roll = input("Press Enter to Roll.\nType in Anything to Quit")
        if roll == "":
            result = random.randint(1, 6)
            print(f"You rolled a {result}.")
        else:
            break


    elif randomizer_choice == "D10" or randomizer_choice == "d10":
        roll = input("Press Enter to Roll.\nType in Anything to Quit")
        if roll == "":
            result = random.randint(1, 10)
            print(f"You rolled a {result}.")
        else:
            break

    elif randomizer_choice == "D20" or randomizer_choice == "d20":
        roll = input("Press Enter to Roll.\nType in Anything to Quit")
        if roll == "":
            result = random.randint(1, 20)
            print(f"You rolled a {result}.")
        else:
            break

    elif randomizer_choice == "8 Ball" or randomizer_choice == "8 ball" or randomizer_choice == "8ball":                                           # Checks if user input is 8 Ball
        while True:
           query=input("Enter Your Query: ")                        # User enters query input
           answer=random.randint(1,20)                              # Sets randomized answer values

            if query == "stop" or query == "quit" or query == "exit":  # Option to exit game
                print("Exiting Game.")
                break
            if answer == 1:                                          # Assigns answers to values
                print("It is certain.\n")
            elif answer == 2:
                print("It is decidedly so.\n")
            elif answer == 3:
                print("Without a doubt.\n")
            elif answer == 4:
                print("Yes definitely.\n")
            elif answer == 5:
                print("You may rely on it.\n")
            elif answer == 6:
                print("As I see it, yes.\n")
            elif answer == 7:
                print("Most likely.\n")
            elif answer == 8:
                print("Outlook good.\n")
            elif answer == 9:
                print("Yes.\n")
            elif answer == 10:
                print("Signs point to yes.\n")
            elif answer == 11:
                print("Reply hazy, try again.\n")
            elif answer == 12:
                print("Ask again later.\n")
            elif answer == 13:
                print("Better not tell you now.\n")
            elif answer == 14:
                print("Cannot predict now.\n")
            elif answer == 15:
                print("Concentrate and ask again.\n")
            elif answer == 16:
                print("Don't count on it.\n")
            elif answer == 17:
                print("My reply is no.\n")
            elif answer == 18:
                print("My sources say no.\n")
            elif answer == 19:
                print("Outlook not so good.\n")
            elif answer == 20:
                print("Very doubtful.\n")
    else:
        print ("Invalid Input.\n")