from graphics import Window
from cell import Cell
from maze import Maze
import random

def main ():
    num_rows = random.randint(12,25)
    num_cols = random.randint(12,25)
    margin = 50
    screen_x = 1000
    screen_y = 800
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
