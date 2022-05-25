import numpy as np
import matplotlib.pyplot as plt


dx, dy = 0.015, 0.05
x = np.arange(-4.0, 4.0, dx)
y = np.arange(-4.0, 4.0, dy)
X, Y = np.meshgrid(x,y)
min_max = np.min(x), np.max(x), np.min(y), np.max(y)
res = np.add.outer(range(8), range(8))%2
plt.imshow(res, cmap="binary_r")
plt.xlabel('\u2654')
plt.ylabel('\u2655')
plt.xticks([])
plt.yticks([])
plt.show()
print('\u2654')
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
