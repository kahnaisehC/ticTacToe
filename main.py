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

def normal(self, x, y, grid):
        # if not valid
        # rerun the function
        x = int(input("Input the x coordinate: ")) # funny example of a function not telling that it can crash
        y = int(input("Input the y coordinate: ")) # TODO: handle exception
        if(x < 0 
           or x >= len(grid[0])
           or y < 0
           or y >= len(grid) 
           or grid[y][x] != '_'
        ):
            print("invalid move!!")
            return

        # if valid
        # make the move
        grid[y][x] = self.character
        return grid

PLAYING_ALGORITHMS = {
    "default": normal
}

def create_grid(n):
    grid = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            row.append('_')
        grid.append(row)
    return grid

class Player:
    def __init__(self, name, desc="Lorem ipsum", character="X", type="default"):
        self.name = name
        self.desc = desc    
        self.character = character
        # sets the "move" method to the value mapped in the PLAYING_ALGORITHMS
        # map with the key whose value is type
        setattr(self, "move", PLAYING_ALGORITHMS[type].__get__(self, self.__class__))
class Game:
    def __init__(self, size, linesize):
        self._size = size 
        self._line_size = linesize
        self._grid = create_grid(size)
        self._current_turn = 0
        self._winner = '_'
        

    def get_grid(self):
        return self._grid
    
    def get_winner(self):
        return self._winner
        

    def display_grid(self):
        n = len(self._grid)
        print("c ", end="")
        for i in range(0, n):
            print(i, end=" ")
        print()
        for i in range(0, n):
            print(i, end=" ")
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
           or self._grid[y][x] != '_'
        ):
            print("invalid move!!")
            self.display_grid
            self.declare_move
            return

        # if valid
        # make the move
        character = 'O'
        if self._current_turn%2 == 0:
            character = 'X'             # TODO: refactor to be able to select different characters
        self._grid[y][x] = character
        self._current_turn += 1

    def check(self):
        n = len(self._grid)
        # check horizontal
        for row in self._grid:
            count = 1
            for i in range(1, n):
                if row[i] == '_':
                    count = 1
                    continue
                if row[i] == row[i-1]:
                    count += 1
                else:
                    count = 1
                if count >= self._line_size:
                    self._winner = "X" 
                    if self._current_turn%2 == 0: self._winner = "O" # TODO: refactor + characters
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
                    self._winner = "X"                              # TODO: refactor + characters
                    if self._current_turn%2 == 0: self._winner = "O"
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
                if self._grid[x+offset][offset] == self._grid[x+offset-1][offset-1]:
                    count += 1
                else:
                    count = 1
                if count >= self._line_size:
                    self._winner = "X"                          # TODO: refactor + characters
                    if self._current_turn%2 == 0: self._winner = "O"
                    return False
            
        for x in range(0, n):
            count = 1
            for offset in range(1, n):
                if (x-offset < 0
                    or self._grid[x-offset][offset] == '_'
                    ):
                    count = 1
                    continue
                if self._grid[x-offset][offset] == self._grid[x-offset+1][offset-1]:
                    count += 1
                else:
                    count = 1
                if count >= self._line_size:
                    self._winner = "X"                          # TODO: refactor + characters
                    if self._current_turn%2 == 0: self._winner = "O"
                    return False
        # Check draw
        if self._current_turn == self._size**2:
            return False
        
        return True
