from tkinter import Tk, BOTH, Canvas
from point import Point

class Line():
    def __init__(self, a, b):

        if not isinstance(a, Point) or not isinstance(b, Point):
            raise TypeError("Both a and b must be instances of the Point class")

        self.point1 = a
        self.point2 = b

    def draw(self, canvas, color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=color, width=2)
