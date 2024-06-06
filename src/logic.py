from graphics import Line, Point
import random
import time


class Cell:
    def __init__(self,
                 top_left_x, top_left_y,
                 bottom_right_x, bottom_right_y,
                 window):
        self.__x1 = top_left_x
        self.__y1 = top_left_y
        self.__x2 = bottom_right_x
        self.__y2 = bottom_right_y
        self.__win = window
        self.center_x = (bottom_right_x + top_left_x) / 2
        self.center_y = (bottom_right_y + top_left_y) / 2
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def __repr__(self):
        return f"Cell with center at ({self.center_x}, {self.center_y})!"

    def draw(self, fill_color):
        if self.has_left_wall:
            Line(Point(self.__x1, self.__y1,),
                 Point(self.__x1, self.__y2),
                 self.__win).draw(fill_color)
        else:
            Line(Point(self.__x1, self.__y1,),
                 Point(self.__x1, self.__y2),
                 self.__win).draw("white")
        if self.has_top_wall:
            Line(Point(self.__x1, self.__y1),
                 Point(self.__x2, self.__y1),
                 self.__win).draw(fill_color)
        else:
            Line(Point(self.__x1, self.__y1),
                 Point(self.__x2, self.__y1),
                 self.__win).draw("white")
        if self.has_right_wall:
            Line(Point(self.__x2, self.__y1),
                 Point(self.__x2, self.__y2),
                 self.__win).draw(fill_color)
        else:
            Line(Point(self.__x2, self.__y1),
                 Point(self.__x2, self.__y2),
                 self.__win).draw("white")
        if self.has_bottom_wall:
            Line(Point(self.__x1, self.__y2),
                 Point(self.__x2, self.__y2),
                 self.__win).draw(fill_color)
        else:
            Line(Point(self.__x1, self.__y2),
                 Point(self.__x2, self.__y2),
                 self.__win).draw("white")

    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        line = Line(Point(self.center_x, self.center_y),
                    Point(to_cell.center_x, to_cell.center_y),
                    self.__win)
        line.draw(fill_color)


class Maze:
    def __init__(self, x1, y1, rows, columns, cell_size, window, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__win = window
        self.__rows = rows
        self.__columns = columns
        self.__cell_size = cell_size
        self.create_cells()
        random.seed(seed)

    def create_cells(self):
        self.cells = []
        for j in range(self.__rows):
            row_list = []
            for i in range(self.__columns):
                row_list.append(Cell(self.__x1 + i * self.__cell_size,
                                     self.__y1 + j * self.__cell_size,
                                     self.__x1 + (i + 1) * self.__cell_size,
                                     self.__y1 + (j + 1) * self.__cell_size,
                                     self.__win))
            self.cells.append(row_list)
        self.entrance = self.cells[0][0]
        self.exit = self.cells[-1][-1]

    def draw(self, fill_color):
        for row in self.cells:
            for cell in row:
                cell.draw(fill_color)

    def animate(self, fill_color):
        for row in self.cells:
            for cell in row:
                cell.draw(fill_color)
                self.__win.redraw()
                time.sleep(.05)

    def break_entrance_and_exit(self):
        self.entrance.has_top_wall = False
        self.entrance.draw("black")
        time.sleep(.05)
        self.exit.has_bottom_wall = False
        self.exit.draw("black")

    def break_interior_walls(self, cell):
        y_index = 0
        for row in self.cells:
            if cell in row:
                break
            y_index += 1
        x_index = self.cells[y_index].index(cell)
        cell.visited = True

        while True:

            possible_visits = []

            left_cell = None
            top_cell = None
            right_cell = None
            bottom_cell = None

            if x_index != 0:
                left_cell = self.cells[y_index][x_index - 1]
            if y_index != 0:
                top_cell = self.cells[y_index - 1][x_index]
            if x_index != self.__columns - 1:
                right_cell = self.cells[y_index][x_index + 1]
            if y_index != self.__rows - 1:
                bottom_cell = self.cells[y_index + 1][x_index]

            if left_cell and not left_cell.visited:
                possible_visits.append(left_cell)
            if top_cell and not top_cell.visited:
                possible_visits.append(top_cell)
            if right_cell and not right_cell.visited:
                possible_visits.append(right_cell)
            if bottom_cell and not bottom_cell.visited:
                possible_visits.append(bottom_cell)

            if possible_visits == []:
                cell.draw("black")
                return

            chosen_cell = possible_visits[random.randrange(
                len(possible_visits))]

            if chosen_cell == left_cell:
                cell.has_left_wall = False
                chosen_cell.has_right_wall = False
            if chosen_cell == top_cell:
                cell.has_top_wall = False
                chosen_cell.has_bottom_wall = False
            if chosen_cell == right_cell:
                cell.has_right_wall = False
                chosen_cell.has_left_wall = False
            if chosen_cell == bottom_cell:
                cell.has_bottom_wall = False
                chosen_cell.has_top_wall = False

            self.break_interior_walls(chosen_cell)
