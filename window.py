from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Builder")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.window_on = False

        def redraw(self):
            self.__root.update_idletasks()
            self.__root.update()
        
        def wait_for_close(self):
            self.window_on = True
            while self.window_on:
                