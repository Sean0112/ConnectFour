from tkinter import *
import sys, os

board =     [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
counter = 0
color1 = "SlateBlue1"
color2 = "DodgerBlue2"
gameover = False


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def winner1():
    result = False
    # horizontal
    for i in range(6):
        for j in range(4):
            if board[i][j] == 1 and board[i][j + 1] == 1 and board[i][j + 2] == 1 and board[i][j + 3] == 1:
                result = True
    # vertical
    for i in range(3):
        for j in range(7):
            if board[i][j] == 1 and board[i + 1][j] == 1 and board[i + 2][j] == 1 and board[i + 3][j] == 1:
                result = True

    # diagonal
    for i in range(3):
        for j in range(4):
            if board[i][j] == 1 and board[i + 1][j + 1] == 1 and board[i + 2][j + 2] == 1 and board[i + 3][j + 3] == 1 :
                result = True

    # diagonal
    for i in range(2, -1, -1):
        for j in range(6, 2, -1):
            if board[i][j] == 1 and board[i + 1][j - 1] == 1 and board[i + 2][j - 2] == 1 and board[i + 3][j - 3] == 1 :
                result = True
    return result

def winner2():
    result = False
    # horizontal
    for i in range(6):
        for j in range(4):
            if board[i][j] == 2 and board[i][j + 1] == 2 and board[i][j + 2] == 2 and board[i][j + 3] == 2:
                result = True
    # vertical
    for i in range(3):
        for j in range(7):
            if board[i][j] == 2 and board[i + 1][j] == 2 and board[i + 2][j] == 2 and board[i + 3][j] == 2:
                result = True
    # diagonal
    for i in range(3):
        for j in range(4):
            if board[i][j] == 2 and board[i + 1][j + 1] == 2 and board[i + 2][j + 2] == 2 and board[i + 3][j + 3] == 2:
                result = True
    # diagonal
    for i in range(2, -1, -1):
        for j in range(6, 2, -1):
            if board[i][j] == 2 and board[i + 1][j - 1] == 2 and board[i + 2][j - 2] == 2 and board[i + 3][j - 3] == 2:
                result = True
    return result

def click(event):
    global counter
    global gameover
    #first player selects a column by double clicking
    if counter % 2 == 0:
        row = 5
        x = event.x # int(x/100) indicates the column
        x -= 50 # compensate for shift of UI
        if x > 0 and x < 700 and not gameover: # ensure a valid input from user and that the game is not over
            for i in range(6):
                if board[row][int(x/100)] != 0 :
                    row -= 1 # decrement the row value if space is occupied
            if row >= 0:
                board[row][int(x/100)] = 1
                for x in range(7):
                    for y in range(6):
                        if board[y][x] == 1:
                            canvas.create_oval(x * 100 + 60, y * 100 + 60, x * 100 + 140, y * 100 + 140, outline="black",
                                        fill=color1, width=2)
            counter += 1
        if winner1(): # game is over; two options: quit or replay
            Button(root, text="Click here to exit.", command=quit).pack()
            Button(root, text="Click here to play again.", command=restart_program).pack()
            gameover = True

    #second player
    else :
        row = 5
        x = event.x
        x -= 50  # compensate for shift of UI
        if x > 0 and x < 700 and not gameover: # ensure a valid input from user and that the game is not over
            for i in range (6) :
                if board[row][int(x/100)] != 0 :
                    row -= 1 # decrement the row value if space is occupied
            if row >= 0:
                board[row][int(x/100)] = 2
                for x in range(7):
                    for y in range(6):
                        if board[y][x] == 2:
                            canvas.create_oval(x * 100 + 60, y * 100 + 60, x * 100 + 140, y * 100 + 140, outline="black",
                                      fill=color2, width=2)
            counter += 1
        if winner2(): # game is over; two options: quit or replay
            Button(root, text="Click here to exit.", command=quit).pack()
            Button(root, text="Click here to play again.", command=restart_program).pack()
            gameover = True

root = Tk()
root.bind('<Double-Button-1>', click)
root.geometry("800x740")
root.title("Connect Four")
w = Message(root, text="Double click to select column", width = 200)
w.pack()
canvas = Canvas()
#draw the board
for x in range(8) :
    canvas.create_line(x*100+50,50,x*100+50,650) #vertical lines
for y in range(7) :
    canvas.create_line(50,y*100+50,750,y*100+50) #horizontal lines
canvas.pack(fill=BOTH, expand=1)
root.mainloop()

