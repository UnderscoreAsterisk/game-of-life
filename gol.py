import scipy.signal as signal
import numpy as np

kernel = np.ones((3,3), dtype=np.uint8)
init_board = np.array([[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0]], dtype=np.uint8)

def update(board):
    old_board = board
    new_board = signal.convolve2d(old_board, kernel, mode="same")

    (m, n) = old_board.shape
    for i in range(m):
        for j in range(n):
            if new_board[i,j] == 3:
                new_board[i, j] = 1
            elif new_board[i, j] == 4:
                new_board[i, j] = old_board[i, j]
            else:
                new_board[i, j] = 0

    print(new_board)
    return new_board

print(init_board)
new_board = update(init_board)
new_board = update(new_board)