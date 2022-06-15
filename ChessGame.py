
GRID_SIZE = 8

chessMate = False

#Verwertet die Arrays diese Funciton als row bekommt, und gibt diese im Terminal aus
def Board(row):
    print("  A", " B", " C", " D", " E", " F", " G", " H")

    #Wiederholt diese for Schleife, bis x so gross wie GRID_SIZE ist
    for x in range(GRID_SIZE):
        #Hier werden die Zahlen an den Ränden ausgegeben
        print("{} ".format(x + 1), end="")
        #Printet eine ganze Reihe aus
        #durch die Variabel row, wird der gewollte Wert immer eingefügt
        for y in range(GRID_SIZE):
            print("{}".format(row[x][y]), end="")
            if y < GRID_SIZE:
                print("|", end="")

        if x < GRID_SIZE:
            print()

#Legt die Startposition aller Figuren fest
#Übergibt der Board Funktion row als Array gefüllt mit den Werten
def createBoard():
    row = []
    #Falls x kleiner ist als GRID_SIZE, fügt es eine neue Zeile hinzu
    for x in range(GRID_SIZE):
        row.append([])
        #Füllt die Arrayfelder mit bestimmten Koordinaten mit Unicodes
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
                row[x].append("\u2003")
    return row

#Gibt True zurück
#Für Test Zwecke
def RookTest(opy, opx, npy, npx):
    return True

#Checkt, ob Zug mit Rook Valid ist
def Rook(opy, opx, npy, npx):
    if opy == npy or opx == npx:
        return True
    else:
        return False
#Checkt, ob Zug mit Knight Valid ist
def Knight(opy, opx, npy, npx):
    if opy - 2 or opy + 2 and opx - 1 or opx + 1 == npy and npx:
        return True
    elif opx - 2 or opx + 2 and opy - 1 or opy + 1 == npy and npx:
        return True
    else:
        return False

#Checkt, ob Zug mit Bishop Valid ist
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

#Checkt, ob Zug mit Pawn Valid ist
def Pawn(opy, opx, npy, npx):
    if opy == npy + 1 or opy == npy - 1:
        return True
    else:
        return False

#Checkt, ob Zug mit Queen Valid ist
def Queen(opy, opx, npy, npx):
    if Bishop(opy, opx, npy, npx) or Rook(opy, opx, npy, npx) == True:
        return True
    else:
        return False

#Checkt, ob Zug mit King Valid ist
def King(opy, opx, npy, npx):
    if opy == npy - 1 or opy == npy + 1 or opx == npx - 1 or opx == npx + 1:
        return True
    else:
        return False




#Verarbeitet Inputs vom User, Validiert Züge, Gibt Wert von Zielfeld aus
def moveFigure(matrix):
    row = []
    #Legt inputs fest
    figurart = input("Figur: ")
    opx = int(input("x Achse von der Figur eingeben: "))
    opy = int(input("y Achse von der Figur eingeben: "))
    npx = int(input("x Achse der neuen Position: "))
    npy = int(input("y Achse der neuen Positon: "))
    npx -= 1
    npy -= 1

    #allowed auf False gesetzt, sodass man Returnwerte von Funktions nach True und False überprüfen kann
    allowed = False

    #Überprüft, welche Funktion ,je nach eingabe anders, augerufen werden muss
    if figurart == "Rook":
        allowed = Knight(opy, opx, npy, npx)

    elif figurart == "RookTest":
        allowed = RookTest(opy, opx, npy, npx)

    elif figurart == "Pawn":
        allowed = Pawn(opy, opx, npy, npx)

    elif figurart == "Bishop":
        allowed = Bishop(opy, opx, npy, npx)

    elif figurart == "Queen":
        allowed = Queen(opy, opx, npy, npx)

    elif figurart == "Knight":
        allowed = Knight(opy, opx, npy, npx)

    elif figurart == "King":
        allowed = King(opy, opx, npy, npx)

    #Falls nichts davon zutrifft, gibt es eine Fehlermeldug zurück
    if not allowed:
        print("Your move is not valid!")


    #Ausgeben des Zielfeldes
    #Ausgeben aller leeren Felder
    else:
        #Neuen Variabel Wert von Inputs geben
        targetFieldFigure = matrix[npx][npy]
        originFieldFigure = matrix[opx][opy]
        matrix[npx][npy] = originFieldFigure
        matrix[opx][opy] = "\u2003"
        #printet die Spielfigur auf den Zeilfeld aus
        if targetFieldFigure != " ":
            print(targetFieldFigure)
    return matrix


matrix = createBoard()

#aufrufen der Funktionen
while not chessMate:
    matrix = moveFigure(matrix)
    Board(matrix)
