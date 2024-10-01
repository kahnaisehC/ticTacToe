# Requirements
# Some possible questions to ask:

# What are the rules of the game?
# What size is the grid?
# How many players are there? Player vs Computer? Player vs Player?
# Are we keeping track of the score?


# Basics
# The game will be played by only two players, player vs player
# The game board should be of variable dimensions
# The target is to connect N discs in a row (vertically, horizontally or diagonally)
# N is a variable (e.g. connect 4, 5, 6, etc)
# There should be a score tracking system
# After a player reaches the target score, they are the winner


# Design
# High-level
# We will need a Grid class to maintain the state of the 2-D board
# The board cell can be empty, yellow (occupied by Player 1) or red (occupied by Player 2)
# The grid will also be responsible for checking for a win condition
# We can have a Player class to represent the player's piece color
# This isn't super important, but encapsulating information is generally a good practice
# The Game class will be composed of the Grid and Players
# The Game class will be responsible for the game loop and keeping track of the score

# https://neetcode.io/courses/ood-interview/0

def create_grid(n):
    grid = []
    for i in range(0, n):
        col = []
        for j in range(0, n):
            col.append('_')
        grid.append(col)
    return grid

    


class Game:
    def __init__(self, size, lineSize):
        self._size = size 
        self._line_size = lineSize
        self._grid = create_grid(size)
        self._current_turn = 0

    def display_grid(self):
        n = len(self._grid)
        for i in range(0, n):
            for j in range(0, n):
                print(self._grid[i][j]+" ", end="")
            print()

    def declare_move(self, x:int, y:int):
        # if not valid
        # rerun the function
        if(x < 0 
           or x >= self._size
           or y < 0
           or y >= self._size
           or self._grid[x][y] != '_'
        ):
            print("invalid move!!")
            self.display_grid
            self.declare_move
            return

        # if valid
        character = 'O'
        if self._current_turn%2 == 0:
            character = 'X'
        self._grid[x][y] = character
        self._current_turn += 1

    def check(self):
        n = len(self._grid)
        # check horizontal
        for col in self._grid:
            count = 1
            for i in range(1, n):
                if col[i] == '_':
                    count = 1
                    continue
                if col[i] == col[i-1]:
                    count += 1
                else:
                    count = 1
                if count >= self._line_size:
                    return False
        
        # check vertical
        for y in range(0, n):
            count = 1
            for x in range(1, n):
                if self._grid[x][y] == '_':
                    count = 1
                    continue
                if self._grid[x][y] == self._grid[x-1][y]:
                    count += 1
                else:
                    count = 1
                if count >= self._line_size:
                    return False
        
        #check diagonal
        for x in range(0, n):
            count = 1
            for offset in range(1, n):
                if (x+offset >= n
                    or self._grid[x+offset][offset] == '_'
                    ):
                    count = 1
                    continue
                if self.grid[x+offset][offset] == self[x+offset-1][offset-1]:
                    count += 1
                else:
                    count = 1
                if count >= self._line_size:
                    return False
            
        for x in range(0, n):
            count = 1
            for offset in range(1, n):
                if (x-offset < 0
                    or self._grid[x-offset][offset] == '_'
                    ):
                    count = 1
                    continue
                if self.grid[x-offset][offset] == self[x-offset+1][offset-1]:
                    count += 1
                else:
                    count = 1
                if count >= self._line_size:
                    return False
            
        return True

    def play(self):
        winner = ""
        while(self.check()):
            self.display_grid()
            x = int(input("Input the x coordinate: "))
            y = int(input("Input the y coordinate: "))
            self.declare_move(int(x), int(y))
            winner = self._grid[x][y]
        self.display_grid()
        print("THE WINNER IS: " + winner + "!!!!!!")


        
        
g = Game(5, 4)

g.play()
