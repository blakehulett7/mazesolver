from graphics import Window, Line, Point
from logic import Cell


def main():
    win = Window(800, 600)

    cell_1 = Cell(50, 50, 100, 100)
    cell_2 = Cell(150, 50, 200, 100)
    cell_3 = Cell(250, 50, 300, 100)
    cell_4 = Cell(350, 50, 400, 100)
    cell_5 = Cell(450, 50, 500, 100)
    cell_6 = Cell(550, 50, 600, 100)
    cell_7 = Cell(650, 50, 700, 100)
    cell_8 = Cell(750, 50, 800, 100)

    cell_2.has_left_wall = False
    cell_3.has_top_wall = False
    cell_4.has_right_wall = False
    cell_5.has_bottom_wall = False
    cell_6.has_top_wall = False
    cell_6.has_bottom_wall = False
    cell_7.has_left_wall = False
    cell_7.has_right_wall = False
    cell_8.has_left_wall = False
    cell_8.has_top_wall = False
    cell_8.has_right_wall = False
    cell_8.has_bottom_wall = False

    cell_list = [cell_1, cell_2, cell_3, cell_4,
                 cell_5, cell_6, cell_7, cell_8]

    for cell in cell_list:
        win.draw_cell(cell, "black")

    test_line = Line(Point(cell_1.center_x, cell_1.center_y),
                     Point(cell_2.center_x, cell_2.center_y))
    win.draw_line(test_line, "red")

    win.wait_for_close()


main()
