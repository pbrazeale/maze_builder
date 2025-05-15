from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Builder")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        