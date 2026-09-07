import random
def Game():
    Bot = random.randint(1,3)
    while True:
        player = input("""
        Enter:
        1 for Rock
        2 for Paper
        3 for Scissors
        """)
        if player in ["1", "2", "3"]:
            break
        else:
            print("Please,")#then gonna be Enter: ... so please, Enter
    if Bot == 1 and player == "2":
        return "w"
    elif Bot == 1 and  player == "3":
        return "l"
    elif Bot == 1 and player == "1":
        return "d"
    if Bot == 2 and player == "2":
        return "d"
    elif Bot == 2 and  player == "3":
        return "w"
    elif Bot == 2 and player == "1":
        return "l"
    elif Bot == 3 and player == "2":
        return "l"
    elif Bot == 3 and  player == "3":
        return "d"
    elif Bot == 3 and player == "1":
        return "w"  
    else:
        print("What the fuck???") 
def InitializationOfApp():
    print("Initialization...")
    print("Rock Paper Scissors")
    print("By N1tyTheDev")
    print("Version 1.0")
    print("Initialization Complete.")
def Exit():
    print("Bye!")
def Main():
    result = Game()
    if result == "w":
        print("You won!")
    elif result == "l":
        print("You lost!")
    elif result == "d":
        print("Draw!")
    choice = input("Wanna play again? (Y/N)")
    if choice == "Y":
        Main()
    else:
        Exit()
InitializationOfApp()
Main()