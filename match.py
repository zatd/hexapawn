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

import tkinter
import sys
    
def changeplayer():
    global player
    
    if player == 1: player = 2
    else: player = 1
    
def printgameboard():
    global pieces, slots
    
    for i in range(0,7,3):
        print (pieces[i:i+3], slots[i:i+3])

def checkvalidity(move):
    global pieces, slots, player
    
    validity = True
    try:
        if len(move) != 2: validity = False
        #move within range
        if move[0] and move[1] not in slots: validity = False
        #can only move 'x' or 'o'
        if pieces[int(move[0])-1] is 'x':
            #move own piece only
            if player != 1: validity = False
            #walk into teammate invalid
            if pieces[int(move[1])-1] is 'x': validity = False
            #take opponent
            if pieces[int(move[1])-1] is 'o':
                #using modulo operation to validate diagonal direction
                if int(move[0])%3 == 0:
                    if int(move[0])+2 != int(move[1]): validity = False
                if int(move[0])%3 == 1:
                    if int(move[0])+4 != int(move[1]): validity = False
                if int(move[0])%3 == 2:
                    if int(move[0])+2 != int(move[1]) and int(move[0])+4 != int(move[1]): validity = False
            #walk onto empty slot
            if pieces[int(move[1])-1] is ' ':
                if int(move[0])+3 != int(move[1]): validity = False
            
        elif pieces[int(move[0])-1] is 'o':
            #move own piece only
            if player != 2: validity = False
            #walk into teammate invalid
            if pieces[int(move[1])-1] is 'o': validity = False
            #take opponent
            if pieces[int(move[1])-1] is 'x':
                if int(move[0])%3 == 0:
                    if int(move[0])-4 != int(move[1]): validity = False
                if int(move[0])%3 == 1:
                    if int(move[0])-2 != int(move[1]): validity = False
                if int(move[0])%3 == 2:
                    if int(move[0])-4 != int(move[1]) and int(move[0])-2 != int(move[1]): validity = False
            #walk onto empty slot
            if pieces[int(move[1])-1] is ' ':
                if int(move[0])-3 != int(move[1]): validity = False
       
        elif pieces[int(move[0])-1] is ' ': validity = False
        
        return validity
    
    except:
        print ("Error has occured!")
        
def movepiece(move):
    global pieces, player
    
    move = int(move) - 11
    #destination piece replaced by origin piece
    pieces[move%10] = pieces[move // 10**1 % 10]
    #origin piece replaced by blank
    pieces[move // 10**1 % 10] = ' '
    
    printgameboard()
    
def checkpossiblemoves():
    global pieces, player
    
    if player != 1: 
        for poscheck in [i+1 for i, x in enumerate(pieces) if x == "x"]:
            if pieces[poscheck+3-1] is " ": return True
            if poscheck%3 == 0 and pieces[poscheck+2-1] == "o": return True
            if poscheck%3 == 1 and pieces[poscheck+2-1] == "o" and pieces[poscheck+4-1] == "o": return True
            if poscheck%3 == 2 and pieces[poscheck+4-1] == "o": return True
    if player != 2: 
        for poscheck in [i+1 for i, x in enumerate(pieces) if x == "o"]:
            if pieces[poscheck-3-1] is " ": return True
            if poscheck%3 == 0 and pieces[poscheck-4-1] == "x": return True
            if poscheck%3 == 1 and (pieces[poscheck-4-1] == "x" or pieces[poscheck-2-1] == "x"): return True
            if poscheck%3 == 2 and pieces[poscheck-2-1] == "x": return True
    return False

def checkwin():
    global pieces, player, winner
    
    winner = player
    #check if opponent is trapped
    if checkpossiblemoves() == False: return True
    
    #check if player reached the end
    if player == 1:    
        for poscheck in [i+1 for i, x in enumerate(pieces) if x == "x"]:
            if poscheck in [7,8,9]: return True
    if player == 2:
        for poscheck in [i+1 for i, x in enumerate(pieces) if x == "o"]:
            if poscheck in [1,2,3]: return True
    
    winner = 0
    
def main():
    global pieces, slots, player, winner, expression
    pieces = ['x','x','x',' ',' ',' ','o','o','o']
    slots = ['1','2','3','4','5','6','7','8','9']
    player = 1
    winner = 0
    expression = ""
    printgameboard()
    
    while True:
        move = input("Player "+ str(player) + "! Your move: ")
        #quit game with 'q'
        if move is 'q': 
            print ("Quit game!")
            break
        #game continues
        if checkvalidity(move) == True: 
            movepiece(move)
            if checkwin() == True: break
            changeplayer()
        else: print ("Invalid move!")
    
    print ("Player", winner, "wins")
    
if __name__ == '__main__':
    main()
