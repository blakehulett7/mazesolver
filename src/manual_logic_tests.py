from logic import Maze

test_maze = Maze(50, 50, 10, 14, 50, False)
print(test_maze.break_interior_walls(test_maze.entrance))
print(test_maze.break_interior_walls(test_maze.cells[1][0]))
print(test_maze.break_interior_walls(test_maze.cells[2][1]))
print(test_maze.break_interior_walls(test_maze.cells[3][2]))
print(test_maze.break_interior_walls(test_maze.cells[4][3]))
print(test_maze.break_interior_walls(test_maze.cells[5][4]))
