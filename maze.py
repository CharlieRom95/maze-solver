from cell import Cell
from window import Window
import time
import random

class Maze():
    def __init__( self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self._cells = []
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):

        if self.win is None:
            canvas = None
        else:
            canvas = self.win.canvas
    
        for i in range(self.num_cols):
            column = []
            self._cells.append(column)
            for j in range(self.num_rows):
            # Calculate cell coordinates
                x1 = self.x1 + (i * self.cell_size_x)
                y1 = self.y1 + (j * self.cell_size_y)
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
            
            # Create cell with calculated coordinates
                cell = Cell(canvas, x1, y1, x2, y2)
                column.append(cell)
                self._draw_cell(i, j)
            
        
    def _draw_cell(self, i, j):
        if self.win is not None:
            self._cells[i][j].draw("black")
            self._animate()

    def _animate(self):
        if self.win is None:
            return 
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        ult_col = self.num_cols - 1
        ult_row = self.num_rows - 1
        self._cells[ult_col][ult_row].has_bottom_wall = False
        self._draw_cell(ult_col, ult_row)

    def _break_walls_r(self, i, j):
         
         self._cells[i][j].visited = True
    
         while True:
            # Build list of unvisited neighbors
            new_lt = []
            # Check all four directions
            directions = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for ni, nj in directions:
            # Make sure the neighbor is valid and not visited
                if 0 <= ni < len(self._cells) and 0 <= nj < len(self._cells[0]):
                    if not self._cells[ni][nj].visited:
                        new_lt.append((ni, nj))
        
        # If no unvisited neighbors, break out of the loop
            if len(new_lt) == 0:
                self._cells[i][j].draw("black")
                return
        
        # Choose a random direction and break walls
            rnd = random.randrange(len(new_lt))
            ni, nj = new_lt[rnd]
        
        # Knock down walls between cells
            if nj > j:  # East
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False
            elif nj < j:  # Moving west
                self._cells[i][j].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False
            elif ni > i:  # Moving south
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False
            elif ni < i:  # Moving north
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False
            self._break_walls_r(ni, nj)

    def _reset_cells_visited(self):
        for i in self._cells:
            for j in i:
                j.visited = False




    
