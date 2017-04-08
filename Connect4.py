from tkinter import Tk, Canvas, Frame, BOTH

board =     [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
counter = 0

def winner1():
    result = False
    # horizontal
    for i in range(6):
        for j in range(4):
            if board[i][j] == 1 and board[i][j + 1] == 1 and board[i][j + 2] == 1 and board[i][j + 3] == 1:
                result = True
    # vertical
    for i in range(3):
        for j in range(5):
            if board[i][j] == 1 and board[i + 1][j] == 1 and board[i + 2][j] == 1 and board[i + 3][j] == 1:
                result = True

    for i in range(3):
        for j in range(4):
            if board[i][j] == 1 and board[i + 1][j + 1] == 1 and board[i + 2][j + 2] == 1 and board[i + 3][j + 3] == 1 :
                result = True

    for i in range(2, 0, -1):
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
        for j in range(5):
            if board[i][j] == 2 and board[i + 1][j] == 2 and board[i + 2][j] == 2 and board[i + 3][j] == 2:
                result = True

    for i in range(3):
        for j in range(4):
            if board[i][j] == 2 and board[i + 1][j + 1] == 2 and board[i + 2][j + 2] == 2 and board[i + 3][j + 3] == 2:
                result = True

    for i in range(2, 0, -1):
        for j in range(6, 2, -1):
            if board[i][j] == 2 and board[i + 1][j - 1] == 2 and board[i + 2][j - 2] == 2 and board[i + 3][j - 3] == 2:
                result = True
    return result

def click1(event):
    global counter
    #first player selects a good column
    if counter % 2 == 1:
        row = 5
        x = event.x
        for i in range (6) :
            if board[row][int(x/100)] != 0 :
                row = row-1
        if row >= 0 :
            board[row][int(x / 100)] = 1
            for x in range(7):
                for y in range(6):
                    if board[y][x] == 1:
                        canvas.create_oval(x * 100 + 10, y * 100 + 10, x * 100 + 90, y * 100 + 90, outline="black",
                                        fill="blue", width=2)
        if winner1():
            print("GAME OVER BLUE (PLAYER1) WINS")
    #second player
    else :
        row = 5
        x = event.x
        for i in range (6) :
            if board[row][int(x/100)] != 0 :
                row = row-1
        if row >= 0:
            board[row][int(x / 100)] = 2
            for x in range(7):
                for y in range(6):
                    if board[y][x] == 2:
                        canvas.create_oval(x * 100 + 10, y * 100 + 10, x * 100 + 90, y * 100 + 90, outline="black",
                                      fill="red", width=2)
        if winner2():
            print("GAME OVER RED (PLAYER2) WINS")
    counter += 1



c = 0
root = Tk()
root.bind('<Double-Button-1>', click1)
root.geometry("700x600")
root.title("Connect Four")
canvas = Canvas()
#draw the board
for x in range(7) :
    canvas.create_line((x+1)*100,0,(x+1)*100,600)
for y in range(6) :
    canvas.create_line(0,(y+1)*100,700,(y+1)*100)
canvas.pack(fill=BOTH, expand=1)
root.mainloop()

