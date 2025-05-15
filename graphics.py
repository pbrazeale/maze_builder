from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__window_on = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

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

class Point():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

class Line():
    

