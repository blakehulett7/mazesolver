from graphics import Window
from logic import Maze


def main():
    win = Window(800, 600)

    goated_maze = Maze(50, 50, 10, 14, 50, win)
    goated_maze.animate("black")
    goated_maze.break_entrance_and_exit()
    goated_maze.break_interior_walls(goated_maze.entrance)
    goated_maze.reset_visited()
    goated_maze.solver(goated_maze.entrance)

    win.wait_for_close()


main()
