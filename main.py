from graphics import Window, Point, Line

def main ():
    win = Window(800, 600)

    start_point = Point(10, 10)
    end_point = Point(20, 50)
    first_line = Line(start_point, end_point)
    win.draw_line(first_line, "red")



    win.wait_for_close()


if __name__ == "__main__":
    main()
