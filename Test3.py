def Rook(opy, opx, npy, npx):
    if opy == npy or opx == npx:
        return True
    else:
        return False




if Rook(opy, opx, npy, npx):
    return figurenPlatzieren(row, npy, npx, figurart)
else:
    return "Dieser Zug ist nicht Valid"

def figurenPlatzieren(row, npy, npx, figurart):
    for x in range(GRID_SIZE):
        row.append([])
        for y in range(GRID_SIZE):
            if x == npy and y == npx:
                row[x].append(str(Figures[figurart]))

            else:
                row[x].append("\u2658")

    return row

    for x in range(GRID_SIZE):
        row.append([])
        for y in range(GRID_SIZE):
            if x == npy and y == npx:
                row[x].append(str(Figures[figurart]))

            else:
                row[x].append("\u2658")

    return row