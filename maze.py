from cell import Cell
import time
import random

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
        seed=None,
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
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
            
        if seed != None:
            self.__seed = random.seed(seed)


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

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        start_cell = self.__cells[i][j]
        start_cell.visited = True
        while True:
            to_visit = []
            # up
            if j >= 1 and self.__cells[i][j-1].visited == False:
                to_visit.append((i,j-1))
            # down
            if j < (self.__num_rows - 1) and self.__cells[i][j+1].visited == False:
                to_visit.append((i,j+1))
            # left
            if i >= 1 and self.__cells[i-1][j].visited == False:
                to_visit.append((i-1,j))
            # right
            if i < (self.__num_cols - 1) and self.__cells[i+1][j].visited == False:
                to_visit.append((i+1,j))
            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return
                        
            pair = random.choice(to_visit)
            
            if pair[1] == j:
                #left
                if pair[0] < i:
                    self.__cells[pair[0]][pair[1]].has_right_wall = False
                    self.__cells[i][j].has_left_wall = False
                #right
                if pair[0] > i:
                    self.__cells[pair[0]][pair[1]].has_left_wall = False
                    self.__cells[i][j].has_right_wall = False
            #down
            elif pair[1] > j:
                self.__cells[pair[0]][pair[1]].has_top_wall = False
                self.__cells[i][j].has_bottom_wall = False
            #up
            else:
                self.__cells[pair[0]][pair[1]].has_bottom_wall = False
                self.__cells[i][j].has_top_wall = False

            self.__draw_cell(pair[0], pair[1])
            self.__break_walls_r(pair[0], pair[1])
