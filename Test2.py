Figuren = {
    "Black_King": '\u2654',
    "Black_Queen": '\u2655',
    "Black_Rook": '\u2656',
    "Black_Bishop": '\u2657',
    "Black_Knight": '\u2658',
    "Black_Pawn": '\u2659',
    "White_King": '\u265A',
    "White_Queen": '\u265B',
    "White_Rook": '\u265C',
    "White_Bishop": '\u265D',
    "White_Knight": '\u265E',
    "WhitePawn": '\u265F'
}

GRID_SIZE = 8
matrix = []
chessMate = False


# Machen des Boards
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
            #                row[x][y] = "\u2656"
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
                row[x].append('\u265C')

            else:
                row[x].append('\u2003')
    return row


# Zeichnen des Boards
def Board(row):
    print(" 1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ")

    for x in range(GRID_SIZE):
        print("{} ".format(x + 1), end="")
        for y in range(GRID_SIZE):
            print("{}".format(row[x][y]), end="")
            if y < GRID_SIZE:
                print("|", end="")

        if x < GRID_SIZE:
            print()


# Spielregeln der Figuren
def Rook():
    if chessMate:
        return True
    else:
        return False


def Knight(opy, opx, npy, npx):
    if opy - 2 or opy + 2 and opx - 1 or opx + 1 == npy and npx:
        return True
    elif opx - 2 or opx + 2 and opy - 1 or opy + 1 == npy and npx:
        return True
    else:
        return False


def Bishop(opy, opx, npy, npx):
    numberToCalculate = opy - npy
    if numberToCalculate < 0:
        numberToCalculate *= -1

    if opy and opx != npy and npx:
        while 0 != numberToCalculate:
            numberToCalculate -= 1
            opx + 1 and opy + 1

        while 0 != numberToCalculate:
            numberToCalculate -= 1
            opx - 1 and opy + 1

        while 0 != numberToCalculate:
            numberToCalculate -= 1
            opx - 1 and opy - 1

        while 0 != numberToCalculate:
            numberToCalculate -= 1
            opx - 1 and opy - 1

        return True
    else:
        return False


# Updaten des Boards
def moveFigure(matrix):
    row = []
    figurart = input("Figur: ")
    opx = int(input("x Achse von der Figur eingeben: "))
    opy = int(input("y Achse von der Figur eingeben: "))
    npx = int(input("x Achse der neuen Position: "))
    npy = int(input("y Achse der neuen Positon: "))
    npx -= 1
    npy -= 1

    allowed = False

    if figurart == "Rook":
        allowed = Knight(opy, opx, npy, npx)

    elif figurart =="Pawn":
        allowed
    if not allowed:
        print("Your move is not valid!")
    else:
        targetFieldFigure = matrix[npx][npy]
        originFieldFigure = matrix[opx][opy]
        matrix[npx][npy] = originFieldFigure
        matrix[opx][opy] = "\u2003"
        if targetFieldFigure != " ":
            print(targetFieldFigure)
    return matrix


matrix = createBoard()
Board(matrix)

while not chessMate:
    matrix = moveFigure(matrix)
    Board(matrix)

# Board(updateBoard())
