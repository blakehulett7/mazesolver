from logic import Maze

test_maze = Maze(50, 50, 10, 14, 50, False, 7)
test_maze.break_entrance_and_exit()
test_maze.break_interior_walls(test_maze.entrance)
test_maze.reset_visited()
print(test_maze.solver(test_maze.entrance))
print(test_maze.solver(test_maze.cells[0][13]))
print(test_maze.solver(test_maze.cells[4][7]))
print(test_maze.solver(test_maze.cells[9][0]))
print(test_maze.solver(test_maze.exit))
