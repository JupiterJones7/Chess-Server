#BlackKing = '\u2654'
#BlackQueen = '\u2655'
#BlackRook = '\u2656'
#BlackBishop = '\u2657'
#BlackKnight = '\u2658'
#BlackPawn = '\u2659'
#WhiteKing = '\u265A'
#WhiteQueen = '\u265B'
#WhiteRook = '\u265C'
#WhiteBishop = '\u265D'
#WhiteKnight = '\u265E'
#WhitePawn = '\u265F'

GRID_SIZE = 8
def createBoard():
    row = []
    for x in range(GRID_SIZE):
        row.append([])
        for y in range(GRID_SIZE):
            if x == 1:
                row[x].append("\u2659")
            elif x == 6:
                row[x].append("\u265F")
            elif x == 0 and y == 0:
                row[x].append("\u2656")
            elif x == 0 and y == 1:
                row[x].append("\u2658")
            elif x == 0 and y == 2:
                row[x].append("\u2657")
            elif x == 0 and y == 3:
                row[x].append("\u2655")
            elif x == 0 and y == 4:
                row[x].append("\u2654")
            elif x == 0 and y == 5:
                row[x].append("\u2657")
            elif x == 0 and y == 6:
                row[x].append("\u2658")
            elif x == 0 and y == 7:
                row[x].append("\u2656")
            elif x == 7 and y == 0:
                row[x].append("\u265C")
            elif x == 7 and y == 1:
                row[x].append("\u265E")
            elif x == 7 and y == 2:
                row[x].append("\u265D")
            elif x == 7 and y == 3:
                row[x].append("\u265B")
            elif x == 7 and y == 4:
                row[x].append("\u265A")
            elif x == 7 and y == 5:
                row[x].append("\u265D")
            elif x == 7 and y == 6:
                row[x].append("\u265E")
            elif x == 7 and y == 7:
                row[x].append("\u265C")

            else:
                row[x].append("\u2658")
    return row


def Board(row):

    print("  A", " B", " C", " D", " E", " F", " G", " H")

    for x in range(GRID_SIZE):
        print("{} ".format(x + 1), end="")
        for y in range(GRID_SIZE):
            print("{}".format(row[x][y]), end="")
            if y < GRID_SIZE:
                print("|", end="")

        if x < GRID_SIZE:
            print()


Board(createBoard())
