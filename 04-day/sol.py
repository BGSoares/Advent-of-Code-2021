"""



"""
import numpy as np

class Board():
    def __init__(self, matrix):
        self.matrix = matrix
        self.bingo = False
    
    def mark_number(self, draw:int):
        row, col = np.where(self.matrix==draw)
        if len(row):
            self.matrix[row[0], col[0]]=-1
            if sum(self.matrix[row[0],:])==-5:
                self.bingo = True
            elif sum(self.matrix[:,col[0]])==-5:
                self.bingo = True

    def score(self):
        return sum(np.where(self.matrix==-1, 0, self.matrix))

# -----------

class Game():
    def __init__(self, file): # functions here are only called once on instanciation
        self.file = file
        self.winner = None
        self.score = None
        self.draw = None
        self.boards = self.create_boards()

    @property
    def data(self):
        with open(self.file) as f:
            return f.read().split("\n\n")

    @property
    def draws(self) -> list:
        return list(map(int, self.data[0].split(",")))
    
    def create_boards(self) -> np.array:
        boards = []
        for b in self.data[1:]:
            board = []
            for l in b.splitlines():
                board.append(list(map(int, l.split())))
            boards.append(Board(np.array(board)))
        return boards

    def play(self):
        for draw in self.draws:
            print(draw)
            for board in self.boards: # every time I call boards I calculate it again
                board.mark_number(draw)
                print(board.matrix)
                if board.bingo:
                    self.winner = board
                    self.score = 
                    self.draw = draw

                    return board.matrix, board.score()
                print(board.matrix)

    @property
    def score(self):
        return sum(np.where(self.matrix==-1, 0, self.matrix))

game = Game("input.txt")
game_test = Game("input_test.txt")