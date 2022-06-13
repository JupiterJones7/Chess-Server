import chess
import chess.svg
import IPython
from IPython.core.display_functions import display

html_code = chess.svg.piece(chess.Piece.from_symbol("R"))
display(IPython.display.HTML(html_code))