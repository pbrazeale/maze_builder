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

    def draw_walls(self, x1, x2, y1, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            p1 = 
            p2 = 
            left_wall = Line(Point(x1, y2), Point(x1, y1))
            self._win.draw_line(left_wall)
        if self.has_top_wall:
            p1 = Point(x1, y1)
            p2 = Point(x2, y1)
            top_wall = Line(p1, p2)
            self._win.draw_line(top_wall)
        if self.has_right_wall:
            p1 = Point(x2, y1)
            p2 = Point(x2, y2)
            right_wall = Line(p1, p2)
            self._win.draw_line(right_wall)
        if self.has_bottom_wall:
            p1 = Point(x2, y2)
            p2 = Point(x1, y2)
            bottom_wall = Line(p1, p2)
            self._win.draw_line(bottom_wall)
