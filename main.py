from tkinter import *

root = Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="white")

board = [["","",""],["","",""],["","",""]]
count = 0

# Disable Buttons
def disable():
    b1["state"] = "disabled"
    b2["state"] = "disabled"
    b3["state"] = "disabled"
    b4["state"] = "disabled"
    b5["state"] = "disabled"
    b6["state"] = "disabled"
    b7["state"] = "disabled"
    b8["state"] = "disabled"
    b9["state"] = "disabled"

def board_value(x,y,z):
    global board
    global count
    count += 1

    # Decide whether is it X or O turn
    if (count % 2) != 0:
        x["text"] = "X"
        board[y][z] = "X"
        player["text"] = "Player: 2 (O)"
    else:
        x["text"] = "O"
        board[y][z] = "O"
        player["text"] = "Player: 1 (X)"
    print(board)
    # Identify Winner or Tie
    if count>=9:
        winner["text"] = "No Winner! It is a TIE"
        winner["fg"] = "red"
        disable()
    elif (board[0][0]==board[0][1]==board[0][2]=="X" or board[1][0]==board[1][1]==board[1][2]=="X" or board[2][0]==board[2][1]==board[2][2]=="X" or
        board[0][0]==board[1][0]==board[2][0]=="X" or board[0][1]==board[1][1]==board[2][1]=="X" or board[0][2]==board[1][2]==board[2][2]=="X" or
        board[0][0]==board[1][1]==board[2][2]=="X" or board[0][2]==board[1][1]==board[2][0]=="X"):
        # Declare Winner in red text
        winner["text"] = "Winner: X"
        winner["fg"] = "red"
        # Change winning Tiles to purple
        if (board[0][0]==board[0][1]==board[0][2]=="X"):
            b1["bg"] = "Purple"
            b2["bg"] = "Purple"
            b3["bg"] = "Purple"
        elif (board[1][0]==board[1][1]==board[1][2]=="X"):
            b4["bg"] = "Purple"
            b5["bg"] = "Purple"
            b6["bg"] = "Purple"
        elif (board[2][0]==board[2][1]==board[2][2]=="X"):
            b7["bg"] = "Purple"
            b8["bg"] = "Purple"
            b9["bg"] = "Purple"
        elif (board[0][0]==board[1][0]==board[2][0]=="X"):
            b1["bg"] = "Purple"
            b4["bg"] = "Purple"
            b7["bg"] = "Purple"
        elif (board[0][1]==board[1][1]==board[2][1]=="X"):
            b2["bg"] = "Purple"
            b5["bg"] = "Purple"
            b8["bg"] = "Purple"
        elif (board[0][2]==board[1][2]==board[2][2]=="X"):
            b3["bg"] = "Purple"
            b6["bg"] = "Purple"
            b9["bg"] = "Purple"
        elif (board[0][0]==board[1][1]==board[2][2]=="X"):
            b1["bg"] = "Purple"
            b5["bg"] = "Purple"
            b9["bg"] = "Purple"
        elif (board[0][2]==board[1][1]==board[2][0]=="X"):
            b3["bg"] = "Purple"
            b5["bg"] = "Purple"
            b7["bg"] = "Purple"
        disable()
    elif (board[0][0]==board[0][1]==board[0][2]=="O" or board[1][0]==board[1][1]==board[1][2]=="O" or board[2][0]==board[2][1]==board[2][2]=="O" or
        board[0][0]==board[1][0]==board[2][0]=="O" or board[0][1]==board[1][1]==board[2][1]=="O" or board[0][2]==board[1][2]==board[2][2]=="O" or
        board[0][0]==board[1][1]==board[2][2]=="O" or board[0][2]==board[1][1]==board[2][0]=="O"):
        # Declare Winner in red text
        winner["text"] = "Winner: O"
        winner["fg"] = "red"
        # Change winning Tiles to purple
        if (board[0][0]==board[0][1]==board[0][2]=="O"):
            b1["bg"] = "Purple"
            b2["bg"] = "Purple"
            b3["bg"] = "Purple"
        elif (board[1][0]==board[1][1]==board[1][2]=="O"):
            b4["bg"] = "Purple"
            b5["bg"] = "Purple"
            b6["bg"] = "Purple"
        elif (board[2][0]==board[2][1]==board[2][2]=="O"):
            b7["bg"] = "Purple"
            b8["bg"] = "Purple"
            b9["bg"] = "Purple"
        elif (board[0][0]==board[1][0]==board[2][0]=="O"):
            b1["bg"] = "Purple"
            b4["bg"] = "Purple"
            b7["bg"] = "Purple"
        elif (board[0][1]==board[1][1]==board[2][1]=="O"):
            b2["bg"] = "Purple"
            b5["bg"] = "Purple"
            b8["bg"] = "Purple"
        elif (board[0][2]==board[1][2]==board[2][2]=="O"):
            b3["bg"] = "Purple"
            b6["bg"] = "Purple"
            b9["bg"] = "Purple"
        elif (board[0][0]==board[1][1]==board[2][2]=="O"):
            b1["bg"] = "Purple"
            b5["bg"] = "Purple"
            b9["bg"] = "Purple"
        elif (board[0][2]==board[1][1]==board[2][0]=="O"):
            b3["bg"] = "Purple"
            b5["bg"] = "Purple"
            b7["bg"] = "Purple"
        disable()


# Current Playing Player Display
player = Label(root, text="Player: 1 (X)", height=3, font=("COMIC SANS MS", 10, "bold"), bg="white")
player.grid(row=0, column=0)

# Exit Button
exitButton = Button(root, text="Quit", command=quit, font=("COMIC SANS MS", 10, "bold"))
exitButton.grid(row=0, column=2)

# Buttons/Grid
b1=Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold", command=lambda: board_value(b1,0,0))
b2=Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold", command=lambda: board_value(b2,0,1))
b3=Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold", command=lambda: board_value(b3,0,2))

b4=Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold", command=lambda: board_value(b4,1,0))
b5=Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold", command=lambda: board_value(b5,1,1))
b6=Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold", command=lambda: board_value(b6,1,2))

b7=Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold", command=lambda: board_value(b7,2,0))
b8=Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold", command=lambda: board_value(b8,2,1))
b9=Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold", command=lambda: board_value(b9,2,2))

# Put Button on Screen
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)

# Winner Display
winner = Label(root, text="Winner: ", height=3, font=("COMIC SANS MS", 10, "bold"), bg="white")
winner.grid(row=4, column=1)


root.mainloop()