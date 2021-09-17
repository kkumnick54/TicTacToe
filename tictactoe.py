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

def main():
    
    game()

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

def robotMind(values):
    # s7 (3) | s8 (2) | s9 (3)
    #-------------------------
    # s4 (2) | s5 (4) | s6 (2)
    #-------------------------
    # s1 (3) | s2 (2) | s3 (3)

    #Spot values
    s2 = 0
    s4 = 0
    s6 = 0
    s8 = 0
    s1 = 0
    s3 = 0
    s7 = 0
    s9 = 0
    s5 = 0    
    bestMove = 0
    highValue = 0

    if values.tL == " ":
        if values.tC == " " and values.tR == " ":
            s1 += 8
        if values.cC == " " and values.bR == " ":
            s1 += 10
        if values.cL == " " and values.bL == " ":
            s1 += 8
        if s1 > highValue :
            highValue = s7
            bestMove = 7
        print("space 7 evaluated")
    if values.tC == " ":
        if values.tL == " " and values.tR == " ":
            s2 += 8
        if values.cC == " " and values.bC == " ":
            s2 += 8
        if s2 > highValue :
            highValue = s8
            bestMove = 8
        print("space 8 evaluated")
    if values.tR == " ":
        if values.tC == " " and values.tL == " ":
            s3 += 8
        if values.cC == " " and values.bL == " ":
            s3 += 10
        if values.cR == " " and values.bR == " ":
            s3 += 8
        if s3 > highValue :
            highValue = s9
            bestMove = 9
        print("space 9 evaluated")

    if values.cL == " ":
        if values.cC == " " and values.cR == " ":
            s4 += 8
        if values.cC == " " and values.bR == " ":
            s4 += 8
        if s4 > highValue :
            highValue = s4
            bestMove = 4
        print("space 4 evaluated")
    if values.cC == " ":
        if values.tL == " " and values.bR == " ":
            s5 += 10
        if values.tC == " " and values.bC == " ":
            s5 += 8
        if values.bL == " " and values.tR == " ":
            s5 += 10
        if values.cL == " " and values.cR == " ":
            s5 += 8
        if s5 > highValue :
            highValue = s5
            bestMove = 5
        print("space 5 evaluated")
    if values.cR == " ":
        if values.tR == " " and values.bR == " ":
            s6 += 8
        if values.cC == " " and values.cL == " ":
            s6 += 8
        if s6 > highValue :
            highValue = s6
            bestMove = 6
        print("space 6 evaluated")

    if values.bL == " ":
        if values.tL == " " and values.cL == " ":
            s7 += 8
        if values.cC == " " and values.tR == " ":
            s7 += 10
        if values.bC == " " and values.bL == " ":
            s7 += 8
        if s7 > highValue :
            highValue = s1
            bestMove = 1
        print("space 1 evaluated")
    if values.bC == " ":
        if values.bL == " " and values.bR == " ":
            s8 += 8
        if values.cC == " " and values.tC == " ":
            s8 += 8
        if s8 > highValue :
            highValue = s2
            bestMove = 2
        print("space 2 evaluated")
    if values.bR == " ":
        if values.bL == " " and values.bC == " ":
            s9 += 8
        if values.cC == " " and values.tL == " ":
            s9 += 10
        if values.cR == " " and values.tR == " ":
            s9 += 8
        if s9 > highValue :
            highValue = s3
            bestMove = 3
        print("space 3 evaluated")

    print("the chosen spot is %i" %bestMove)
    return bestMove

def game():
    mode = 0    
    while(mode != 1 and mode != 2):
        print("Press 1 for single player or 2 for two player game")
        mode = int(input())
        if (mode != 1 and mode != 2):
            print("That was an invalid choice. Please enter a 1 or 2")
            mode = int(input())
    
    print("Press enter to start")
    random =  input()
    win = False
    tie = False
    spots = []
    entries = values()
    counter = 0
    printGrid(entries)

    if (mode == 1):
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
                choice = robotMind(entries)
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
            print("Computer has won the game")

    if (mode == 2):
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
       
if __name__ == "__main__":
    main() 