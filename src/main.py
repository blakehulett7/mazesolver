from graphics import Window, Line, Point
from logic import Cell, Maze


def main():
    win = Window(800, 600)

    test_maze = Maze(50, 50, 10, 14, 50, win, 7)
    test_maze.animate("black")
    test_maze.break_entrance_and_exit()
    test_maze.break_interior_walls(test_maze.entrance)
    test_maze.reset_visited()
    test_maze.solver(test_maze.entrance)

    win.wait_for_close()


main()
