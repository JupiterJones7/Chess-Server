import chess
board = chess.Board()
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



#Updaten des Boars
def updateBoard():
    newBoard = str(board)
    newBoard = newBoard.replace("r", '\u2656' + " |")
    newBoard = newBoard.replace("n", '\u2658' + " |")
    newBoard = newBoard.replace("b", '\u2657' + " |")
    newBoard = newBoard.replace("q", '\u2655' + " |")
    newBoard = newBoard.replace("k", '\u2654' + " |")
    newBoard = newBoard.replace("p", '\u2659' + " |")
    newBoard = newBoard.replace("R", '\u265C' + " |")
    newBoard = newBoard.replace("N", '\u265E' + " |")
    newBoard = newBoard.replace("B", '\u265D' + " |")
    newBoard = newBoard.replace("Q", '\u265B' + " |")
    newBoard = newBoard.replace("K", '\u265A' + " |")
    newBoard = newBoard.replace("P", '\u2659' + " |")
    newBoard = newBoard.replace(".", '\u2003' + " |")
    print(newBoard)
    print(board.legal_moves)
    input1 = input("What move would you like to make: ")
    board.push_san(input1)



while board.is_checkmate() == False:
    updateBoard()
