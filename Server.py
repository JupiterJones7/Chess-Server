import sys
from xmlrpc.server import SimpleXMLRPCServer

# Informationen
argumentList = sys.argv
hostAddress = '0.0.0.0'
port = '12345'
server = SimpleXMLRPCServer((hostAddress, int(port)))

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




def updateBoard(input1):
    print(board.legal_moves)


    board.push_san(input1)
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
server.register_function(updateBoard)
server.serve_forever()
