from graphics import Line, Point

class Cell():
    def __init__(self, win):
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
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            left_wall = Line(Point(x1, y2), Point(x1, y1))
            self._win.draw_line(left_wall)
        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall)
        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(x2, y2), Point(x1, y2))
            self._win.draw_line(bottom_wall)

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"

        start_x = int((self._x1 + self._x2) / 2)
        start_y = int((self._y1 + self._y2) / 2)

        end_x = int((to_cell._x1 + to_cell._x2) / 2)
        end_y = int((to_cell._y1 + to_cell._y2) / 2)

        connect = Line(Point(start_x, start_y), Point(end_x, end_y))
        self._win.draw_line(connect, fill_color)


