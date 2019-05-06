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

from tkinter import Tk, Label, Button, IntVar, W, E

class GameBoardGUI:

    def __init__(self, master):
        self.master = master
        master.title("Hexapawn")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set((self.total)/10)
        self.total_label1 = Label(master, textvariable=self.total_label_text)
        self.total_label_text.set(self.total%10)
        self.total_label2 = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Move:")

        self.button0 = Button(master, text=pieces[0], command=lambda: self.update(0))
        self.button1 = Button(master, text=pieces[1], command=lambda: self.update(1))
        self.button2 = Button(master, text=pieces[2], command=lambda: self.update(2))
        self.button3 = Button(master, text=pieces[3], command=lambda: self.update(3))
        self.button4 = Button(master, text=pieces[4], command=lambda: self.update(4))
        self.button5 = Button(master, text=pieces[5], command=lambda: self.update(5))
        self.button6 = Button(master, text=pieces[6], command=lambda: self.update(6))
        self.button7 = Button(master, text=pieces[7], command=lambda: self.update(7))
        self.button8 = Button(master, text=pieces[8], command=lambda: self.update(8))
        
        self.submit_button = Button(master, text="Submit", command=lambda: self.update("submit"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        self.quit_button = Button(master, text="Quit", command=lambda: self.update("quit"))

        # LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label1.grid(row=0, column=1, columnspan=1, sticky=W+E)
        self.total_label2.grid(row=0, column=2, columnspan=1, sticky=W+E)

        self.button0.grid(row=1, column=0, sticky=W+E, columnspan=1, rowspan=1, padx=5, pady=5, ipadx=15, ipady=10)
        self.button1.grid(row=1, column=1, sticky=W+E, columnspan=1, rowspan=1, padx=5, pady=5, ipadx=15, ipady=10)
        self.button2.grid(row=1, column=2, sticky=W+E, columnspan=1, rowspan=1, padx=5, pady=5, ipadx=15, ipady=10)
        self.button3.grid(row=2, column=0, sticky=W+E, columnspan=1, rowspan=1, padx=5, pady=5, ipadx=15, ipady=10)
        self.button4.grid(row=2, column=1, sticky=W+E, columnspan=1, rowspan=1, padx=5, pady=5, ipadx=15, ipady=10)
        self.button5.grid(row=2, column=2, sticky=W+E, columnspan=1, rowspan=1, padx=5, pady=5, ipadx=15, ipady=10)
        self.button6.grid(row=3, column=0, sticky=W+E, columnspan=1, rowspan=1, padx=5, pady=5, ipadx=15, ipady=10)
        self.button7.grid(row=3, column=1, sticky=W+E, columnspan=1, rowspan=1, padx=5, pady=5, ipadx=15, ipady=10)
        self.button8.grid(row=3, column=2, sticky=W+E, columnspan=1, rowspan=1, padx=5, pady=5, ipadx=15, ipady=10)
        
        self.submit_button.grid(row=4, column=0, sticky=W+E, columnspan=3, rowspan=1, padx=15, pady=5)
        self.reset_button.grid(row=5, column=0, sticky=W+E, columnspan=3, rowspan=1, padx=15, pady=5)
        self.quit_button.grid(row=6, column=0, sticky=W+E, columnspan=3, rowspan=1, padx=15, pady=5)
        
    def update(self, method):
        global move
        if method in [0,1,2,3,4,5,6,7,8]:
            self.total *= 10
            self.total += (method+1)
            if self.total >= 100: self.total %= 100
        elif method == "submit":
            move = self.total
        elif method == "reset":
            self.total = 0    
        else: # quit
            move = 'q'
        self.total_label_text.set(self.total)

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
        move = str(move)
        if len(move) != 2: 
            print ("Error! Only choose two numbers!")
            validity = False
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
    global pieces, slots, player, winner, expression, move
    pieces = ['x','x','x',' ',' ',' ','o','o','o']
    slots = ['1','2','3','4','5','6','7','8','9']
    player = 1
    winner = 0
    expression = ""
    printgameboard()
    
    while True:
        root = Tk()
        move = GameBoardGUI(root)
        root.mainloop()
#        move = input("Player "+ str(player) + "! Your move: ")
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
