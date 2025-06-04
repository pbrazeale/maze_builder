from cell import Cell
import time

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
        


    def __create_cells(self):
        for i in range(0, self.__num_cols):
            self.__cells.append([])
            for j in range(0, self.__num_rows):
                self.__cells[i].append(Cell(self.__win)) 
                self.__draw_cell(i, j)
    
    def __draw_cell(self, i, j):
        if self.__win == None:
            return
        x1 = self.__x1 + (self.__cell_size_x * i)
        x2 = x1 + self.__cell_size_x
        y1 = self.__y1 + (self.__cell_size_y * j)
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw_walls(x1, y1, x2, y2)
        self.__animate()
    
    def __animate(self):
        if self.__win == None:
            return
        self.__win.redraw()
        time.sleep(0.05)
