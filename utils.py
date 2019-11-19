import os
import time


def Menu():
    os.system("cls")
    print("Menu:\n(1)\tPlayer vs Player\n(2)\tPlayer vs computer\n(3)\tQuit")
    try:
        choice = int(input("-->"))
    except ValueError:
        choice = 0
    return choice


def Quit():
    print("GoodBye!!")
    time.sleep(1.5)
    os.system("cls")


def New_Board():
    return [[None, None, None], [None, None, None], [None, None, None]]


def Render(board):
    """A Fancy Print for the board"""
    print("   0 1 2")
    for i in range(0, 3):
        spot1 = " " if board[i][0] is None else str(board[i][0])
        spot2 = " " if board[i][1] is None else str(board[i][1])
        spot3 = " " if board[i][2] is None else str(board[i][2])
        print(f"{i} |{spot1} {spot2} {spot3}|")


def Get_Name(playerNumber=0):
    if playerNumber == 1:
        name = input("What is player 1's name? ")
    elif playerNumber == 2:
        name = input("What is player 2's name? ")
    elif playerNumber == 0:
        name = input("What is your name? ")

    return name


def Get_move():
    x_pos = -1
    y_pos = -1

    while x_pos < 0 or x_pos > 2:
        try:
            x_pos = int(input("What is the x pos of your move? "))
        except ValueError:
            x_pos = -1

    while y_pos < 0 or y_pos > 2:
        try:
            y_pos = int(input("What is the y pos of your move? "))
        except ValueError:
            y_pos = -1

    return y_pos, x_pos


def Is_Move_Valid(board, position):
    if board[position[0]][position[1]] is None:
        return True
    else:
        print("Spot already taken, Try again!")
        return False


def Make_Move(board, position, XorO):
    board[position[0]][position[1]] = XorO

    return board


def Check_Winner(board):

    for i in range(0, 3):
        if set(board[i]) == set("X"):
            return "X"

    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] == "X":
            return "X"

    if board[0][2] == board[1][1] == board[2][0] == "X":
        return "X"
    elif board[0][0] == board[1][1] == board[2][2] == "X":
        return "X"

    for i in range(0, 3):
        if set(board[i]) == set("O"):
            return "O"

    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] == "O":
            return "O"

    if board[0][2] == board[1][1] == board[2][0] == "O":
        return "O"
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        return "O"

    if Is_Full(board) is True:
        return "DRAW"

    return None


def Is_Full(board):
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] is None:
                return False

    return True
