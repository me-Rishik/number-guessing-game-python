

def guess_engine(level):
    import random

    if level == "easy":
        the_number = random.randint(1,50)
    elif level == "medium":
        the_number = random.randint(1,100)
    else:
        the_number = random.randint(1,500)

    print("~~~~~~~~~~~~ Computer have selected a number ~~~~~~~~~~")
    print("+++++++++++++Guess the Number+++++++++++++\n")

    user_guess = 0
    attempt = 0
    
    while True:
        user_guess = (input())
        try:
            num = int(user_guess)
        except ValueError:
            if user_guess == "stop":
                return user_guess.lower().strip()
            else:
                print("Error: Invalid_Input")
                continue

        if level == "easy":
            if num > 0 and num < 50:
                if num == the_number:
                    attempt += 1
                    return attempt
                elif num > the_number:
                    attempt += 1
                    print("Your Guess is Higher, Try a Smaller Number than this")
                elif num < the_number:
                    attempt += 1
                    print("Your Guess is Lower, Try a Higher Number than this")
            else:
                print("Error :GuessIsBeyondYourLevel")
            
        elif level == "medium":
            if num > 0 and num < 100:
                if num == the_number:
                    attempt += 1
                    return attempt
                elif num > the_number:
                    attempt += 1
                    print("Your Guess is Higher, Try a Smaller Number than this")
                elif num < the_number:
                    attempt += 1
                    print("Your Guess is Lower, Try a Higher Number than this")
            else:
                print("Error :GuessIsBeyondYourLevel")
        else:
            if num > 0 and num < 500:
                if num == the_number:
                    attempt += 1
                    return attempt
                elif num > the_number:
                    attempt += 1
                    print("Your Guess is Higher, Try a Smaller Number than this")
                elif num < the_number:
                    attempt += 1
                    print("Your Guess is Lower, Try a Higher Number than this")
            else:
                print("Error :GuessIsBeyondYourLevel")
        

            
            









    