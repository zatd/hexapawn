# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:39:48 2019

@author: tp-AizatKA
"""

"""#hexapawn
rules: 
    1. pawns can only move forwards to an available slot
    2. can move diagonally to take an opponent
    
win condition:
    1. get a pawn to the end
    2. take all opponent pawns
    3. leave opponent without a possible move

"""

def printgameboard():
    global pieces, slots
    for i in range(0,7,3):
        print (pieces[i:i+3], slots[i:i+3])
    
def checkvalidity(move):
    global pieces,slots
    validity = True
    try:
        if len(move) != 2: validity = False
        #move within range
        if move[0] and move[1] not in slots: validity = False
        #can only move 'x' or 'o'
        if pieces[int(move[0])-1] is 'x':
            
            
        elif pieces[int(move[o])-1] is 'o':
            
        #walk on empty slot
        if pieces[int(move[1])-1] is ' ':
            #can only walk forwards
            if pieces[int(move[0])-1] is 'x':
                if int(move[0])+3 != int(move[1]): validity = False
            elif pieces[int(move[0])-1] is 'o':
                if int(move[0])-3 != int(move[1]): validity = False
        #take opponent
        elif pieces[int(move[0])-1] != pieces[int(move[1])-1]:
            #can only walk diagonals
            if pieces[int(move[0])-1] is 'x':
                if int(move[0]) < int(move[1]): validity = False
            elif pieces[int(move[0])-1] is 'o':
                if int(move[0]) > int(move[1]): validity = False
                    
        return validity
    except:
        print ("Error has occured!")
        
    
def movepiece(move):
    global pieces
    
    move = int(move) - 11
    pieces[move%10] = pieces[move // 10**1 % 10]
    pieces[move // 10**1 % 10] = ' '
    
    printgameboard()
    
def main():
    global pieces, slots
    pieces = ['x','x','x',' ',' ',' ','o','o','o']
    slots = ['1','2','3','4','5','6','7','8','9']
    printgameboard()
    
    while True:
        move = input("Your move: ")
        if checkvalidity(move) == True: movepiece(move)
        else: print ("Invalid move!")
        
        if move == 'q': break
    
if __name__ == '__main__':
    main()
