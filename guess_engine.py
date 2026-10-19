

def guess_engine(level):
    import random

    if level == "easy":
        the_number = random.randint(1,50)
    elif level == "medium":
        the_number = random.randint(1,100)
    else:
        the_number = random.randint(1,500)


    user_guess = 0
    attempt = 0
    print("~~~~~~~~~~~~ Computer have selected a number ~~~~~~~~~~")
    print("+++++++++++++Guess the Number+++++++++++++\n")
    while True:
        user_guess = (input())
        if isinstance(int(user_guess),int):
            n=int(user_guess)
            if n<100 or n>0:
                if n == the_number:
                    attempt += 1
                    return attempt
                elif n>the_number:
                    attempt += 1
                    print("Your Guess is Higher, Try a Smaller Number than this")
                elif n<the_number:
                    attempt += 1
                    print("Your Guess is Lower, Try a Higher Number than this")
            else:
                print("Guess is Beyond Your Level")
        elif user_guess == "stop":
            return user_guess.lower().strip()
        else:
            print("Invalid Input: IT IS NOT AN INTEGER")
            print("Try Again...")


            
            









    