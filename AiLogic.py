import utils as u
import boards as b

SCORE = []


def Is_Move_Valid(board, position):
    if board[position[0]][position[1]] is None:
        return True
    else:
        return False


def counting(board, whofirst):
    x_count = 0
    o_count = 0
    if whofirst == "X":
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == "X":
                    x_count += 1
                elif board[i][j] == "O":
                    o_count += 1

        if x_count == o_count:
            return "X"
        else:
            return "O"
    else:
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == "X":
                    x_count += 1
                elif board[i][j] == "O":
                    o_count += 1

        if x_count == o_count:
            return "O"
        else:
            return "X"


def Scoring(board, whofirst):
    global SCORE
    winner = u.Check_Winner(board)
    if winner is None:
        for i in range(0, 3):
            for j in range(0, 3):
                move = (i, j)
                if Is_Move_Valid(board, move):
                    board[i][j] = counting(board, whofirst)
                    SCORE.append(Scoring(board, whofirst))
                    board[i][j] = None

    if winner == "X":
        val = 1
        SCORE.append(val)

    elif winner == "O":
        val = -1
        SCORE.append(val)

    elif winner == "DRAW":
        val = 0
        SCORE.append(val)


def run1(board, whofirst):
    global SCORE
    result = []
    score = []
    win = 0
    draw = 0
    lose = 0
    total = 0
    for i in range(0, 3):
        for j in range(0, 3):
            move = (i, j)
            if Is_Move_Valid(board, move):
                SCORE = []
                board[i][j] = counting(board, whofirst)
                Scoring(board, whofirst)
                win = SCORE.count(1)
                draw = SCORE.count(0)
                lose = SCORE.count(-1)
                score.append(SCORE)
                board[i][j] = None

                total = win + draw + lose
                win = win/total*100
                draw = draw/total*100
                lose = lose/total*100

                result.append([win, draw, lose])
    return result


def check_lose(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            move = (i, j)
            if Is_Move_Valid(board, move):
                board[i][j] = "O"
                lose = u.Check_Winner(board)
                board[i][j] = None
                if lose == "O":
                    return True, move
    return False


def logic(board, whofirst):
    stats = run1(board, whofirst)
    move = 0
    if check_lose(board):
        return "Block", check_lose(board)[1]

    for i in range(len(stats)):
        if stats[i][0] >= stats[i][1] and stats[i][0] >= stats[i][2]:
            if stats[i][0] >= stats[move][0]:
                move = i
        elif stats[i][1] >= stats[i][2]:
            if stats[i][1] >= stats[move][1]:
                move = i
        elif stats[i][2] >= stats[i][1] and stats[i][2] >= stats[i][1]:
            if stats[i][2] <= stats[move][2]:
                move = i

    return "move", move
