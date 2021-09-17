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

    # 1 point value is added per O in the selection
    # 1 point value is subtracted per X in the selection
    # if two X's in a row, 5 points added for priority
    # if two O's in a row, 3 points added for priority

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
    
    # need to add logic for cases with choices in it. currently doesn't take into account choices other than the empty rows 

    if values.tL == " ":
        if values.tC == " " and values.tR == " ":
            s1 += 8
        if values.cC == " " and values.bR == " ":
            s1 += 10
        if values.cL == " " and values.bL == " ":
            s1 += 8
        
        if values.tC == "O" and values.tR == " ":
            s1 += 9
        if values.cC == "O" and values.bR == " ":
            s1 += 11
        if values.cL == "O" and values.bL == " ":
            s1 += 9
        
        if values.tC == " " and values.tR == "O":
            s1 += 9
        if values.cC == " " and values.bR == "O":
            s1 += 11
        if values.cL == " " and values.bL == "O":
            s1 += 9
        
        if values.tC == "O" and values.tR == "O":
            s1 += 11
        if values.cC == "O" and values.bR == "O":
            s1 += 13
        if values.cL == "O" and values.bL == "O":
            s1 += 11
        
        if values.tC == "X" and values.tR == " ":
            s1 += 7
        if values.cC == "X" and values.bR == " ":
            s1 += 9
        if values.cL == "X" and values.bL == " ":
            s1 += 7

        if values.tC == " " and values.tR == "X":
            s1 += 7
        if values.cC == " " and values.bR == "X":
            s1 += 9
        if values.cL == " " and values.bL == "X":
            s1 += 7

        if values.tC == "X" and values.tR == "X":
            s1 += 13
        if values.cC == "X" and values.bR == "X":
            s1 += 15
        if values.cL == "X" and values.bL == "X":
            s1 += 13

        if values.tC == "O" and values.tR == "X":
            s1 += 8
        if values.cC == "O" and values.bR == "X":
            s1 += 10
        if values.cL == "O" and values.bL == "X":
            s1 += 8

        if values.tC == "X" and values.tR == "O":
            s1 += 8
        if values.cC == "X" and values.bR == "O":
            s1 += 10
        if values.cL == "X" and values.bL == "O":
            s1 += 8

        if s1 > highValue :
            highValue = s7
            bestMove = 7
        print("space 7 evaluated")
        print(s7)
    if values.tC == " ":
        if values.tL == " " and values.tR == " ":
            s2 += 8
        if values.cC == " " and values.bC == " ":
            s2 += 8

        if values.tL == "O" and values.tR == " ":
            s2 += 9
        if values.cC == "O" and values.bC == " ":
            s2 += 9
        
        if values.tL == " " and values.tR == "O":
            s2 += 9
        if values.cC == " " and values.bC == "O":
            s2 += 9
        
        if values.tL == "O" and values.tR == "O":
            s2 += 11
        if values.cC == "O" and values.bC == "O":
            s2 += 11

        if values.tL == "X" and values.tR == " ":
            s2 += 7
        if values.cC == "X" and values.bC == " ":
            s2 += 7

        if values.tL == " " and values.tR == "X":
            s2 += 7
        if values.cC == " " and values.bC == "X":
            s2 += 7

        if values.tL == "X" and values.tR == "X":
            s2 += 13
        if values.cC == "X" and values.bC == "X":
            s2 += 13

        if values.tL == "X" and values.tR == "O":
            s2 += 8
        if values.cC == "X" and values.bC == "O":
            s2 += 8

        if values.tL == "O" and values.tR == "X":
            s2 += 8
        if values.cC == "O" and values.bC == "X":
            s2 += 8

        if s2 > highValue :
            highValue = s8
            bestMove = 8
        print("space 8 evaluated")
        print(s8)
    if values.tR == " ":
        if values.tC == " " and values.tL == " ":
            s3 += 8
        if values.cC == " " and values.bL == " ":
            s3 += 10
        if values.cR == " " and values.bR == " ":
            s3 += 8

        if values.tC == "O" and values.tL == " ":
            s3 += 9
        if values.cC == "O" and values.bL == " ":
            s3 += 11
        if values.cR == "O" and values.bR == " ":
            s3 += 9

        if values.tC == " " and values.tL == "O":
            s3 += 9
        if values.cC == " " and values.bL == "O":
            s3 += 11
        if values.cR == " " and values.bR == "O":
            s3 += 9

        if values.tC == "O" and values.tL == "O":
            s3 += 11
        if values.cC == "O" and values.bL == "O":
            s3 += 13
        if values.cR == "O" and values.bR == "O":
            s3 += 11

        if values.tC == "X" and values.tL == " ":
            s3 += 7
        if values.cC == "X" and values.bL == " ":
            s3 += 9
        if values.cR == "X" and values.bR == " ":
            s3 += 7

        if values.tC == " " and values.tL == "X":
            s3 += 7
        if values.cC == " " and values.bL == "X":
            s3 += 9
        if values.cR == " " and values.bR == "X":
            s3 += 7

        if values.tC == "X" and values.tL == "X":
            s3 += 13
        if values.cC == "X" and values.bL == "X":
            s3 += 15
        if values.cR == "X" and values.bR == "X":
            s3 += 13

        if values.tC == "X" and values.tL == "O":
            s3 += 8
        if values.cC == "X" and values.bL == "O":
            s3 += 10
        if values.cR == "X" and values.bR == "O":
            s3 += 8

        if values.tC == "O" and values.tL == "X":
            s3 += 8
        if values.cC == "O" and values.bL == "X":
            s3 += 10
        if values.cR == "O" and values.bR == "X":
            s3 += 8

        if s3 > highValue :
            highValue = s9
            bestMove = 9
        print("space 9 evaluated")
        print(s9)

    if values.cL == " ":
        if values.cC == " " and values.cR == " ":
            s4 += 8
        if values.cC == " " and values.bR == " ":
            s4 += 8

        if values.cC == "O" and values.cR == " ":
            s4 += 9
        if values.cC == "O" and values.bR == " ":
            s4 += 9

        if values.cC == " " and values.cR == "O":
            s4 += 9
        if values.cC == " " and values.bR == "O":
            s4 += 9

        if values.cC == "O" and values.cR == "O":
            s4 += 11
        if values.cC == "O" and values.bR == "O":
            s4 += 11

        if values.cC == "X" and values.cR == " ":
            s4 += 7
        if values.cC == "X" and values.bR == " ":
            s4 += 7

        if values.cC == " " and values.cR == "X":
            s4 += 7
        if values.cC == " " and values.bR == "X":
            s4 += 7

        if values.cC == "X" and values.cR == "X":
            s4 += 13
        if values.cC == "X" and values.bR == "X":
            s4 += 13

        if values.cC == "X" and values.cR == "O":
            s4 += 8
        if values.cC == "X" and values.bR == "O":
            s4 += 8

        if values.cC == "O" and values.cR == "X":
            s4 += 8
        if values.cC == "O" and values.bR == "X":
            s4 += 8

        if s4 > highValue :
            highValue = s4
            bestMove = 4
        print("space 4 evaluated")
        print(s4)
    if values.cC == " ":
        if values.tL == " " and values.bR == " ":
            s5 += 11
        if values.tC == " " and values.bC == " ":
            s5 += 8
        if values.bL == " " and values.tR == " ":
            s5 += 11
        if values.cL == " " and values.cR == " ":
            s5 += 8

        if values.tL == "O" and values.bR == " ":
            s5 += 12
        if values.tC == "O" and values.bC == " ":
            s5 += 9
        if values.bL == "O" and values.tR == " ":
            s5 += 12
        if values.cL == "O" and values.cR == " ":
            s5 += 9

        if values.tL == " " and values.bR == "O":
            s5 += 12
        if values.tC == " " and values.bC == "O":
            s5 += 9
        if values.bL == " " and values.tR == "O":
            s5 += 12
        if values.cL == " " and values.cR == "O":
            s5 += 9

        if values.tL == "O" and values.bR == "O":
            s5 += 14
        if values.tC == "O" and values.bC == "O":
            s5 += 11
        if values.bL == "O" and values.tR == "O":
            s5 += 14
        if values.cL == "O" and values.cR == "O":
            s5 += 11

        if values.tL == "X" and values.bR == " ":
            s5 += 10
        if values.tC == "X" and values.bC == " ":
            s5 += 7
        if values.bL == "X" and values.tR == " ":
            s5 += 10
        if values.cL == "X" and values.cR == " ":
            s5 += 7

        if values.tL == " " and values.bR == "X":
            s5 += 10
        if values.tC == " " and values.bC == "X":
            s5 += 7
        if values.bL == " " and values.tR == "X":
            s5 += 10
        if values.cL == " " and values.cR == "X":
            s5 += 7

        if values.tL == "X" and values.bR == "X":
            s5 += 16
        if values.tC == "X" and values.bC == "X":
            s5 += 13
        if values.bL == "X" and values.tR == "X":
            s5 += 16
        if values.cL == "X" and values.cR == "X":
            s5 += 13

        if values.tL == "X" and values.bR == "O":
            s5 += 11
        if values.tC == "X" and values.bC == "O":
            s5 += 8
        if values.bL == "X" and values.tR == "O":
            s5 += 11
        if values.cL == "X" and values.cR == "O":
            s5 += 8
        
        if values.tL == "O" and values.bR == "X":
            s5 += 11
        if values.tC == "O" and values.bC == "X":
            s5 += 8
        if values.bL == "O" and values.tR == "X":
            s5 += 11
        if values.cL == "O" and values.cR == "X":
            s5 += 8

        if s5 > highValue :
            highValue = s5
            bestMove = 5
        print("space 5 evaluated")
        print(s5)
    if values.cR == " ":
        if values.tR == " " and values.bR == " ":
            s6 += 8
        if values.cC == " " and values.cL == " ":
            s6 += 8

        if values.tR == "O" and values.bR == " ":
            s6 += 9
        if values.cC == "O" and values.cL == " ":
            s6 += 9

        if values.tR == " " and values.bR == "O":
            s6 += 9
        if values.cC == " " and values.cL == "O":
            s6 += 9

        if values.tR == "O" and values.bR == "O":
            s6 += 11
        if values.cC == "O" and values.cL == "O":
            s6 += 11

        if values.tR == "X" and values.bR == " ":
            s6 += 7
        if values.cC == "X" and values.cL == " ":
            s6 += 7

        if values.tR == " " and values.bR == "X":
            s6 += 7
        if values.cC == " " and values.cL == "X":
            s6 += 7

        if values.tR == "X" and values.bR == "X":
            s6 += 13
        if values.cC == "X" and values.cL == "X":
            s6 += 13

        if values.tR == "X" and values.bR == "O":
            s6 += 8
        if values.cC == "X" and values.cL == "O":
            s6 += 8

        if values.tR == "O" and values.bR == "X":
            s6 += 8
        if values.cC == "O" and values.cL == "X":
            s6 += 8

        if s6 > highValue :
            highValue = s6
            bestMove = 6
        print("space 6 evaluated")
        print(s6)

    if values.bL == " ":
        if values.tL == " " and values.cL == " ":
            s7 += 8
        if values.cC == " " and values.tR == " ":
            s7 += 10
        if values.bC == " " and values.bL == " ":
            s7 += 8

        if values.tL == "O" and values.cL == " ":
            s7 += 9
        if values.cC == "O" and values.tR == " ":
            s7 += 11
        if values.bC == "O" and values.bL == " ":
            s7 += 9

        if values.tL == " " and values.cL == "O":
            s7 += 9
        if values.cC == " " and values.tR == "O":
            s7 += 11
        if values.bC == " " and values.bL == "O":
            s7 += 9

        if values.tL == "O" and values.cL == "O":
            s7 += 11
        if values.cC == "O" and values.tR == "O":
            s7 += 13
        if values.bC == "O" and values.bL == "O":
            s7 += 11

        if values.tL == "X" and values.cL == " ":
            s7 += 7
        if values.cC == "X" and values.tR == " ":
            s7 += 9
        if values.bC == "X" and values.bL == " ":
            s7 += 7

        if values.tL == " " and values.cL == "X":
            s7 += 7
        if values.cC == " " and values.tR == "X":
            s7 += 9
        if values.bC == " " and values.bL == "X":
            s7 += 7

        if values.tL == "X" and values.cL == "X":
            s7 += 13
        if values.cC == "X" and values.tR == "X":
            s7 += 15
        if values.bC == "X" and values.bL == "X":
            s7 += 13

        if values.tL == "X" and values.cL == "O":
            s7 += 8
        if values.cC == "X" and values.tR == "O":
            s7 += 10
        if values.bC == "X" and values.bL == "O":
            s7 += 8

        if values.tL == "O" and values.cL == "X":
            s7 += 8
        if values.cC == "O" and values.tR == "X":
            s7 += 10
        if values.bC == "O" and values.bL == "X":
            s7 += 8

        if s7 > highValue :
            highValue = s1
            bestMove = 1
        print("space 1 evaluated")
        print(s1)
    if values.bC == " ":
        if values.bL == " " and values.bR == " ":
            s8 += 8
        if values.cC == " " and values.tC == " ":
            s8 += 8

        if values.bL == "O" and values.bR == " ":
            s8 += 8
        if values.cC == "O" and values.tC == " ":
            s8 += 8

        if values.bL == " " and values.bR == "O":
            s8 += 8
        if values.cC == " " and values.tC == "O":
            s8 += 8

        if values.bL == "O" and values.bR == "O":
            s8 += 8
        if values.cC == "O" and values.tC == "O":
            s8 += 8

        if values.bL == "X" and values.bR == " ":
            s8 += 8
        if values.cC == "X" and values.tC == " ":
            s8 += 8

        if values.bL == " " and values.bR == "X":
            s8 += 8
        if values.cC == " " and values.tC == "X":
            s8 += 8

        if values.bL == "X" and values.bR == "X":
            s8 += 8
        if values.cC == "X" and values.tC == "X":
            s8 += 8

        if values.bL == "X" and values.bR == "O":
            s8 += 8
        if values.cC == "X" and values.tC == "O":
            s8 += 8

        if values.bL == "O" and values.bR == "X":
            s8 += 8
        if values.cC == "O" and values.tC == "X":
            s8 += 8

        if s8 > highValue :
            highValue = s2
            bestMove = 2
        print("space 2 evaluated")
        print(s2)
    if values.bR == " ":
        if values.bL == " " and values.bC == " ":
            s9 += 8
        if values.cC == " " and values.tL == " ":
            s9 += 10
        if values.cR == " " and values.tR == " ":
            s9 += 8

        if values.bL == "O" and values.bC == " ":
            s9 += 8
        if values.cC == "O" and values.tL == " ":
            s9 += 10
        if values.cR == "O" and values.tR == " ":
            s9 += 8

        if values.bL == " " and values.bC == "O":
            s9 += 8
        if values.cC == " " and values.tL == "O":
            s9 += 10
        if values.cR == " " and values.tR == "O":
            s9 += 8

        if values.bL == "O" and values.bC == "O":
            s9 += 8
        if values.cC == "O" and values.tL == "O":
            s9 += 10
        if values.cR == "O" and values.tR == "O":
            s9 += 8

        if values.bL == "X" and values.bC == " ":
            s9 += 8
        if values.cC == "X" and values.tL == " ":
            s9 += 10
        if values.cR == "X" and values.tR == " ":
            s9 += 8

        if values.bL == " " and values.bC == "X":
            s9 += 8
        if values.cC == " " and values.tL == "X":
            s9 += 10
        if values.cR == " " and values.tR == "X":
            s9 += 8

        if values.bL == "X" and values.bC == "X":
            s9 += 8
        if values.cC == "X" and values.tL == "X":
            s9 += 10
        if values.cR == "X" and values.tR == "X":
            s9 += 8

        if values.bL == "X" and values.bC == "O":
            s9 += 8
        if values.cC == "X" and values.tL == "O":
            s9 += 10
        if values.cR == "X" and values.tR == "O":
            s9 += 8

        if values.bL == "O" and values.bC == "X":
            s9 += 8
        if values.cC == "O" and values.tL == "X":
            s9 += 10
        if values.cR == "O" and values.tR == "X":
            s9 += 8
        
        if s9 > highValue :
            highValue = s3
            bestMove = 3
        print("space 3 evaluated")
        print(s3)

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

            if (counter > 9):
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
        
        if(counter <= 9 and (counter % 2) == 1):
            print("Player 1 won the game")
        
        if(counter <= 9 and (counter % 2) == 0):
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