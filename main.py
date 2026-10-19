import lvl_selector as Lselect
import guess_engine as Gengine

print("==============Welcome to the Game=============\n|||||||||||||||Guess The Number|||||||||||||||| \n\n")
print("************* TO START THE GAME, TYPE 'START' *************")
print("************* TO EXIT THE GAME, TYPE 'STOP' *************")

level=""
while True:
    execute=input()
    if execute.lower().strip() == "start" :
        level = Lselect.lvl_selector() #Fetching level.
        if level == "stop":
            print("Game Ended")
            break
        else:
            guess = Gengine.guess_engine(level) #Returned the Number of attempts to guess.
            if guess == "stop":
                print("Game Ended")
                break
            else:
                print(f"You did it in {guess} attempt")
                print("Enter 'START' to play again")
                print("Enter 'STOP' to exit")
    
    elif execute.lower().strip() == "stop" :
        print("Game Ended")
        break
    else:
        print("Error: Invalid_Input")