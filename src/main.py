from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    point_1 = Point(400, 150)
    point_2 = Point(400, 450)
    point_3 = Point(350, 225)
    point_4 = Point(450, 225)
    line_1 = Line(point_1, point_2)
    line_2 = Line(point_3, point_4)
    win.draw_line(line_1, "black")
    win.draw_line(line_2, "black")
    win.wait_for_close()


main()
