import utils as u
from utils import Render  # print statement for the game board
import time
from random import randint
import AiLogic as Ai
from AiLogic import logic


def Player(player1, player2):
    board = u.New_Board()  # making a new board
    turn = randint(0, 1)
    winner = None

    Render(board)

    while winner is None:

        if turn == 0:
            print(f"it is {player1}'s turn")
        else:
            print(f"it is {player2}'s turn")

        move = u.Get_move()

        while True:
            if u.Is_Move_Valid(board, move):
                break
            else:
                move = u.Get_move()

        XorO = "X" if turn == 0 else "O"
        board = u.Make_Move(board, move, XorO)
        Render(board)

        winner = u.Check_Winner(board)

        if turn == 0:
            turn = 1
        else:
            turn = 0

    if winner == "DRAW":
        print("It was a Draw...")
    elif winner == "X":
        print(f"The winner is {player1}")
    else:
        print(f"The winner is {player2}")


def Computer(player):
    board = u.New_Board()
    turn = randint(0, 1)

    if turn == 0:
        who = "X"
    else:
        who = "O"

    winner = None

    Render(board)

    while winner is None:

        if turn == 0:
            print(f"it is the computers turn")

            place = logic(board, who)

            counter = 0
            if place[0] == "move":
                for i in range(len(board)):
                    for j in range(len(board[i])):
                        move = (i, j)

                        if Ai.Is_Move_Valid(board, move):
                            if counter == place[1]:
                                u.Make_Move(board, move, "X")
                                free = True
                                break
                            else:
                                counter += 1
                                free = False

                    if free is True:
                        break
            elif place[0] == "Block":
                u.Make_Move(board, place[1], "X")
            Render(board)

        else:
            print(f"it is {player}'s turn")

            move = u.Get_move()

            while True:
                if u.Is_Move_Valid(board, move):
                    break
                else:
                    move = u.Get_move()

            board = u.Make_Move(board, move, "O")
            Render(board)

        winner = u.Check_Winner(board)

        if turn == 0:
            turn = 1
        else:
            turn = 0

    if winner == "DRAW":
        print("It was a Draw...")
    elif winner == "X":
        print(f"The winner is the Computer")
    else:
        print(f"The winner is {player}")


def main():

    choice = 0
    while True:

        while choice != 3:
            choice = u.Menu()
            if choice == 1:
                player1 = u.Get_Name(1)  # getting the players name
                player2 = u.Get_Name(2)  # gatting the players name
                Player(player1, player2)
                break

            elif choice == 2:
                Computer(u.Get_Name())
                break

            elif choice == 3:
                pass
            else:
                print("Invalid choice, try again")
                time.sleep(0.8)
        if choice == 3:
            break

        elif input("Start again? y/n ") == "n":
            break
    u.Quit()


if __name__ == "__main__":
    main()
