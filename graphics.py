from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__window_on = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__window_on = True
        while self.__window_on:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self.__window_on = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point_a.x, 
            self.point_a.y, 
            self.point_b.x, 
            self.point_b.y, 
            fill=fill_color, 
            width=2
        )


class Cell():
    def __init__(self, window, x_top, y_top, x_bottom, y_bottom):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x_top
        self._y1 = y_top
        self._x2 = x_bottom
        self._y2 = y_bottom
        self._win = window
        self.draw_walls(self._x1, self._x2, self._y1, self._y2)

    def draw_walls(self, _x1, _x2, _y1, _y2):
        if self.has_left_wall:
            p1 = Point(_x1, _y2)
            p2 = Point(_x1, _y1)
            left_wall = Line(p1, p2)
            left_wall.draw(self._win)
        if self.has_top_wall:
            p1 = Point(_x1, _y1)
            p2 = Point(_x2, _y1)
            left_wall = Line(p1, p2)
            left_wall.draw(self._win)
        if self.has_right_wall:
            p1 = Point(_x2, _y1)
            p2 = Point(_x2, _y2)
            left_wall = Line(p1, p2)
            left_wall.draw(self._win)
        if self.has_bottom_wall:
            p1 = Point(_x2, _y2)
            p2 = Point(_x1, _y2)
            left_wall = Line(p1, p2)
            left_wall.draw(self._win)

