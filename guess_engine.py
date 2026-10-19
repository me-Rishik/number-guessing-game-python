

def guess_engine(level):
    import random

    print("~~~~~~~~~~~~ Computer have selected a number ~~~~~~~~~~")
    print("+++++++++++++Guess the Number+++++++++++++\n")
    while True:
        user_guess = 0
        attempt = 0
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
            the_number = random.randint(1,50)
            if num > 0 or num < 50:
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
            the_number = random.randint(1,100)
            if num > 0 or num < 100:
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
            the_number = random.randint(1,500)
            if num > 0 or num < 500:
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
        

            
            









    