from graphics import Window, Line, Point
from logic import Cell, Maze


def main():
    win = Window(800, 600)

    test_maze = Maze(50, 50, 10, 14, 50)
    win.draw_maze(test_maze, "black")

    win.wait_for_close()


main()
