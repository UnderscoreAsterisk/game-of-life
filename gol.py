import scipy.signal as signal
import numpy as np
import json

CONFIG_PATH = "config.json"

class GameOfLife:
    def __init__(self):
        with open(CONFIG_PATH) as f:
            json_str = f.read()
        
        self.config = json.loads(json_str)
        
        self.cur_board = None
        
        #Initialise Stats
        self.num_iters = 0
        self.num_alive = 0
        self.pattern_name = None

    def get_options(self):
        return self.config

    def select(self, pattern_name):
        if pattern_name.lower() not in self.config:
            return False #err: invalid selection
        else:
            self.pattern_name = pattern_name
            self.cur_board = np.array(self.config[pattern_name.lower()], dtype=np.uint8)
            self.num_alive = 0
            self.num_iters = 0
            return True

    def update(self):
        kernel = np.ones((3,3), dtype=np.uint8)
        if self.cur_board is None:
            return False #err: No board chosen

        new_board = signal.convolve2d(self.cur_board, kernel, mode="same")

        (m, n) = self.cur_board.shape
        for i in range(m):
            for j in range(n):
                if new_board[i,j] == 3:
                    new_board[i, j] = 1
                elif new_board[i, j] == 4:
                    new_board[i, j] = self.cur_board[i, j]
                else:
                    new_board[i, j] = 0

        self.cur_board = new_board
        self.num_iters += 1
        self.num_alive = sum(sum(self.cur_board))
        return True

    def get_board(self):
        return self.cur_board

    def get_stats(self):
        d = {
            "pattern": self.pattern_name,
            "alive": self.num_alive,
            "iters": self.num_iters
        }
        return d