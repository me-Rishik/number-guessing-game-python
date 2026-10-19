def lvl_selector():
    print("Select the Level you want to play:")
    print("*Note: these level will only decide the Range of the number to play on. \n\n")
    print("Select a level and type it :- \n\n Easy (1-50) \n Medium (1-100) \n Hard (1-500) \n")


    while True:
        lvl=input()
        lvl=lvl.lower().strip()
        if lvl=="easy" or lvl=="medium" or lvl=="hard" :
            return lvl
        else:
            print("Invalid Level Input:")
            if lvl=="stop":
                return "stop"
            
    
        

            
        
#game mode (Arcade and compititive)
#history of the guessed value (attempts of Arcade mode.).
#
#






