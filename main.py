from window import Window
from point import Point
from line import Line 
from cell import Cell

def main():

    win = Window(800, 600)

    a = Point(0, 300)
    b = Point(400, 300)
    l = Line(a, b)
    color = "black"
    square = Cell(350, 350, 450, 250, win.canvas)
    square2 = Cell(550, 350, 650, 250, win.canvas)
    square.draw(color)
    square2.draw(color)
    square.draw_move(square2)

    win.wait_for_close()



main()
