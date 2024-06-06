import unittest
from logic import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )

    def test_maze_break_entrance_and_exit(self):
        m1 = Maze(50, 50, 12, 10, 10, None)
        m1.break_entrance_and_exit()
        m1_entrance = m1.cells[0][0]
        m1_exit = m1.cells[-1][-1]
        self.assertFalse(m1_entrance.has_top_wall, "entrance not created")
        self.assertFalse(m1_exit.has_bottom_wall, "exit not created")


if __name__ == "__main__":
    unittest.main()
