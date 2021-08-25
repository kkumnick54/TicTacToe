class values:
    tL = " "
    tC = " "
    tR = " "
    cL = " "
    cC = " "
    cR = " "
    bL = " "
    bC = " "
    bR = " "

def printGrid(values):
    print(" %s | %s | %s " % (values.tL, values.tC, values.tR))
    print("-----------")
    print(" %s | %s | %s " % (values.cL, values.cC, values.cR))
    print("-----------")
    print(" %s | %s | %s " % (values.bL, values.bC, values.bR))

def turnCollection(turn,usedSpots):
    if turn:
        print("Player 1, choose a # from 1-9 to place your mark")
        temp = int(input())
        while temp > 9 or temp < 0:
            print("Invalid entry. Please choose a number between 1 -9")
            temp = int(input())
        while temp in usedSpots:
            print("That space is already taken, please input a valid entry")
            temp = int(input())
        return temp
    else:
        print("Player 2, choose a # from 1-9 to place your mark")
        temp = int(input())
        while temp > 9 or temp < 0:
            print("Invalid entry. Please choose a number between 1 -9")
            temp = int(input())
        while temp in usedSpots:
            print("That space is already taken, please input a valid entry")
            temp = int(input())
        return temp
        
def winP1(values):
    if ( values.tL == "X" and values.tC == "X" and values.tR == "X"):
        return 1
    if ( values.cL == "X" and values.cC == "X" and values.cR == "X"):
        return 1
    if ( values.bL == "X" and values.bC == "X" and values.bR == "X"):
        return 1
    if ( values.tL == "X" and values.cL == "X" and values.bL == "X"):
        return 1
    if ( values.tC == "X" and values.cC == "X" and values.bC == "X"):
        return 1
    if ( values.tR == "X" and values.cR == "X" and values.bR == "X"):
        return 1
    if ( values.tL == "X" and values.cC == "X" and values.bR == "X"):
        return 1
    if ( values.bL == "X" and values.cC == "X" and values.tR == "X"):
        return 1
    return 0

def winP2(values):
    if ( values.tL == "O" and values.tC == "O" and values.tR == "O"):
        return 1
    if ( values.cL == "O" and values.cC == "O" and values.cR == "O"):
        return 1
    if ( values.bL == "O" and values.bC == "O" and values.bR == "O"):
        return 1
    if ( values.tL == "O" and values.cL == "O" and values.bL == "O"):
        return 1
    if ( values.tC == "O" and values.cC == "O" and values.bC == "O"):
        return 1
    if ( values.tR == "O" and values.cR == "O" and values.bR == "O"):
        return 1
    if ( values.tL == "O" and values.cC == "O" and values.bR == "O"):
        return 1
    if ( values.bL == "O" and values.cC == "O" and values.tR == "O"):
        return 1
    return 0

def entryInput(choice,player,values):
    temp = values

    if (choice == 1):
        if(player == 1):
            temp.bL = "X"
        else:
            temp.bL = "O"
        return temp
    if (choice == 2):
        if(player == 1):
            temp.bC = "X"
        else:
            temp.bC = "O"
        return temp
    if (choice == 3):
        if(player == 1):
            temp.bR = "X"
        else:
            temp.bR = "O"
        return temp
    if (choice == 4):
        if(player == 1):
            temp.cL = "X"
        else:
            temp.cL = "O"
        return temp
    if (choice == 5):
        if(player == 1):
            temp.cC = "X"
        else:
            temp.cC = "O"
        return temp
    if (choice == 6):
        if(player == 1):
            temp.cR = "X"
        else:
            temp.cR = "O"
        return temp
    if (choice == 7):
        if(player == 1):
            temp.tL = "X"
        else:
            temp.tL = "O"
        return temp
    if (choice == 8):
        if(player == 1):
            temp.tC = "X"
        else:
            temp.tC = "O"
        return temp
    if (choice == 9):
        if(player == 1):
            temp.tR = "X"
        else:
            temp.tR = "O"
        return temp

def game():
    print("Press enter to play")
    random =  input()
    win = False
    tie = False
    spots = []
    entries = values()
    counter = 0
    printGrid(entries)

    while (win != True and tie != True) :
        player = 1
        choice = turnCollection(player, spots)
        spots.append(choice)
        entries = entryInput(choice, player, entries)
        printGrid(entries)
        win = winP1(entries)
        counter += 1

        if (counter == 9):
            tie = True
        if (win != True and tie != True):
            player = 2
            choice = turnCollection(player, spots)
            spots.append(choice)
            entries = entryInput(choice, player, entries)
            printGrid(entries)
            win = winP2(entries)
            counter += 1
    
    if (tie == True):
        print("The game has ended in a tie")
    
    if(counter < 9 and (counter % 2) == 1):
        print("Player 1 won the game")
    
    if(counter < 9 and (counter % 2) == 0):
        print("Player 2 won the game")


game()