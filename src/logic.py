from graphics import Line, Point
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

    def __repr__(self):
        return f"Cell with center at ({self.center_x}, {self.center_y})!"

    def draw(self, fill_color):
        if self.has_left_wall:
            Line(Point(self.__x1, self.__y1,),
                 Point(self.__x1, self.__y2),
                 self.__win).draw(fill_color)
        if self.has_top_wall:
            Line(Point(self.__x1, self.__y1),
                 Point(self.__x2, self.__y1),
                 self.__win).draw(fill_color)
        if self.has_right_wall:
            Line(Point(self.__x2, self.__y1),
                 Point(self.__x2, self.__y2),
                 self.__win).draw(fill_color)
        if self.has_bottom_wall:
            Line(Point(self.__x1, self.__y2),
                 Point(self.__x2, self.__y2),
                 self.__win).draw(fill_color)

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
    def __init__(self, x1, y1, rows, columns, cell_size, window):
        self.__x1 = x1
        self.__y1 = y1
        self.__win = window
        self.__rows = rows
        self.__columns = columns
        self.__cell_size = cell_size
        self.create_cells()

    def create_cells(self):
        self.__cells = []
        for j in range(self.__rows):
            row_list = []
            for i in range(self.__columns):
                row_list.append(Cell(self.__x1 + i * self.__cell_size,
                                     self.__y1 + j * self.__cell_size,
                                     self.__x1 + (i + 1) * self.__cell_size,
                                     self.__y1 + (j + 1) * self.__cell_size,
                                     self.__win))
            self.__cells.append(row_list)

    def draw(self, fill_color):
        for row in self.__cells:
            for cell in row:
                cell.draw(fill_color)

    def animate(self, fill_color):
        for row in self.__cells:
            for cell in row:
                cell.draw(fill_color)
                self.__win.redraw()
                time.sleep(.05)
