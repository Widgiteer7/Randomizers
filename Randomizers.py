
import random

def d_roll(sides):
        return random.randint(1, sides)




while True:
    randomizer_choice = str(input("Choose a randomizer:\n   Coinflip\n   Dice Roll\n   8 Ball\n\n"))
    

        # Quit Option
    if randomizer_choice == "quit" or randomizer_choice == "Quit":
        print("Aborting Randomizer Tools")
        break


        # Coinflip
    elif randomizer_choice == "coinflip" or randomizer_choice == "Coin flip" or randomizer_choice == "Coin Flip" or randomizer_choice == "coin" or randomizer_choice == "Coin":
        print("Press Enter to Flip Coin.\nType in Anything to Quit")
        while True:
            coin_flip = str(input())

            if coin_flip == "":
                coin_result = random.randint(1, 2)
                if coin_result == 1:
                    print("Heads")
                elif coin_result == 2:
                    print("Tails")
            else:
                break


        # Dice Roll
    elif randomizer_choice == "die" or randomizer_choice == "Die" or randomizer_choice == "dice" or randomizer_choice == "Dice":
        while True:
            num_dice = int(input("Enter how many dice you wish to roll.\nEnter 0 to quit.\n"))
            if num_dice == 0:
                break

            dice_to_roll = []
            for i in range(1, num_dice + 1):
                num_sides = str(input(f"\nHow Many Sides Does Die {i} have?\n"))
                dice_to_roll.append(d_roll(int(num_sides)))
            print()
            for i in range(1, num_dice + 1):
                print(f"Die {i} (D{num_sides}) rolled a {dice_to_roll[i - 1]}")
            print(f"Dice Result Total is {sum(dice_to_roll)}\n")
        

        # 8 Ball
    elif randomizer_choice == "8 Ball" or randomizer_choice == "8 ball" or randomizer_choice == "8ball":
        print("Enter Your Query to recieve an answer.\n Enter ""quit"" or ""stop"" to exit 8 Ball.\n\n")
        while True:
            eb_query = str(input())
            eb_answer = random.randint(1,20)

            if eb_query == "stop" or eb_query == "Stop" or eb_query == "quit" or eb_query == "Quit" or eb_query == "exit" or eb_query == "Exit":
                print("Exiting 8 Ball.")
                break
            
            else:
                if eb_answer == 1:
                    print("It is certain.\n")
                elif eb_answer == 2:
                    print("It is decidedly so.\n")
                elif eb_answer == 3:
                    print("Without a doubt.\n")
                elif eb_answer == 4:
                    print("Yes definitely.\n")
                elif eb_answer == 5:
                    print("You may rely on it.\n")
                elif eb_answer == 6:
                    print("As I see it, yes.\n")
                elif eb_answer == 7:
                    print("Most likely.\n")
                elif eb_answer == 8:
                    print("Outlook good.\n")
                elif eb_answer == 9:
                    print("Yes.\n")
                elif eb_answer == 10:
                    print("Signs point to yes.\n")
                elif eb_answer == 11:
                    print("Reply hazy, try again.\n")
                elif eb_answer == 12:
                    print("Ask again later.\n")
                elif eb_answer == 13:
                    print("Better not tell you now.\n")
                elif eb_answer == 14:
                    print("Cannot predict now.\n")
                elif eb_answer == 15:
                    print("Concentrate and ask again.\n")
                elif eb_answer == 16:
                    print("Don't count on it.\n")
                elif eb_answer == 17:
                    print("My reply is no.\n")
                elif eb_answer == 18:
                    print("My sources say no.\n")
                elif eb_answer == 19:
                    print("Outlook not so good.\n")
                elif eb_answer == 20:
                    print("Very doubtful.\n")


    else:
        print ("Invalid Input.\n")


       # side_values = {
       #                 "D3": 3, "d3": 3,
       #                 "D4": 4, "d4": 4,
       #                 "D5": 5, "d5": 5,
       #                 "D6": 6, "d6": 6,
       #                 "D7": 7, "d7": 7,
       #                 "D8": 8, "d8": 8,
       #                 "D9": 9, "d9": 9,
       #                 "D10": 10, "d10": 10,
       #                 "D11": 11, "d11": 11,
       #                 "D12": 12, "d12": 12,
       #                 "D13": 13, "d13": 13,
       #                 "D14": 14, "d14": 14,
       #                 "D15": 15, "d15": 15,
       #                 "D16": 16, "d16": 16,
       #                 "D17": 17, "d17": 17,
       #                 "D18": 18, "d18": 18,
       #                 "D19": 19, "d19": 19,
       #                 "D20": 20, "d20": 20
       #              }