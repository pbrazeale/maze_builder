from graphics import Line, Point

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw_walls(self, x1, y1, x2, y2):
        if self._win == None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        left_wall = Line(Point(x1, y2), Point(x1, y1))
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        bottom_wall = Line(Point(x2, y2), Point(x1, y2))

        if self.has_left_wall:
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall, "white")

        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall, "white")
                            
        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall, "white")

        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall)
        else:
            self._win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        if self._win == None:
            return
        fill_color = "red"
        if undo:
            fill_color = "gray"

        start_x = int((self._x1 + self._x2) / 2)
        start_y = int((self._y1 + self._y2) / 2)

        end_x = int((to_cell._x1 + to_cell._x2) / 2)
        end_y = int((to_cell._y1 + to_cell._y2) / 2)

        connect = Line(Point(start_x, start_y), Point(end_x, end_y))
        self._win.draw_line(connect, fill_color)


