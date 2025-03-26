from window import Window
from point import Point
from line import Line 
from cell import Cell
from maze import Maze

def main():

    win = Window(800, 600)

    a = Point(0, 300)
    b = Point(400, 300)
    l = Line(a, b)
    color = "black"
    maze = Maze(0, 0, 12, 16, 50, 50, win)
    maze._break_walls_r(0,0)
    
    
    

    win.wait_for_close()



main()
