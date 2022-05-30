Figures = {
    "Black_King" : '\u2654',
    "Black_Queen" : '\u2655',
    "Black_Rook" : '\u2656',
    "Black_Bishop" : '\u2657',
    "Black_Knight" : '\u2658',
    "Black_Pawn" : '\u2659',
    "White_King" : '\u265A',
    "White_Queen" : '\u265B',
    "White_Rook" : '\u265C',
    "White_Bishop" : '\u265D',
    "White_Knight" : '\u265E',
    "WhitePawn" : '\u265F'
}


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
    print(" 1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ")

    for x in range(GRID_SIZE):
        print("{} ".format(x + 1), end="")
        for y in range(GRID_SIZE):
            print("{}".format(row[x][y]), end="")
            if y < GRID_SIZE:
                print("|", end="")

        if x < GRID_SIZE:
            print()


#Board(createBoard())


def updateBoard():

    row = []
    input1 = int(input("x Achse: "))
    input2 = int(input("y Achse: "))
    input3 = input("Figur: ")
    for x in range(GRID_SIZE):
        row.append([])
        for y in range(GRID_SIZE):
            if x == input1 and y == input2:
                row[x].append(str(Figures[input3]))

            else:
                row[x].append("\u2658")

    return row




Board(updateBoard())