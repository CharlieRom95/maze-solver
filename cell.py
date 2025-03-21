from line import Line
from point import Point
from tkinter import Tk, BOTH, Canvas

class Cell():
    def __init__(self, x1, y1, x2, y2, canvas):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self._win = canvas

    def draw(self, color):
        if self.has_left_wall:
            self._win.create_line(self.x1, self.y1, self.x1, self.y2, fill=color, width=2)

        if self.has_right_wall:
            self._win.create_line(self.x2, self.y1, self.x2, self.y2, fill=color, width=2)

        if self.has_top_wall:
            self._win.create_line(self.x1, self.y1, self.x2, self.y1, fill=color, width=2)

        if self.has_bottom_wall:
            self._win.create_line(self.x1, self.y2, self.x2, self.y2, fill=color, width=2)

    def draw_move(self, to_cell, undo=False):
        center_x_1 = (self.x2-self.x1)/2 + self.x1
        center_y_1 = (self.y1+self.y2)/2 
        center_x_2 = (to_cell.x2-to_cell.x1)/2 + to_cell.x1
        center_y_2 = (to_cell.y1+to_cell.y2)/2 

        if undo:
            self._win.create_line(center_x_1, center_y_1, center_x_2, center_y_2, fill="gray", width=2)

        else:
            self._win.create_line(center_x_1, center_y_1, center_x_2, center_y_2, fill="red", width=2)
