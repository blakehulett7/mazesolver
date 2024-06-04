from graphics import Line, Point


class Cell:
    def __init__(self,
                 top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        self.__x1 = top_left_x
        self.__y1 = top_left_y
        self.__x2 = bottom_right_x
        self.__y2 = bottom_right_y
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True

    def draw(self, canvas, fill_color):
        if self.has_left_wall:
            Line(Point(self.__x1, self.__y1), Point(
                self.__x1, self.__y2)).draw(canvas, fill_color)
        if self.has_top_wall:
            Line(Point(self.__x1, self.__y1), Point(
                self.__x2, self.__y1)).draw(canvas, fill_color)
        if self.has_right_wall:
            Line(Point(self.__x2, self.__y1), Point(
                self.__x2, self.__y2)).draw(canvas, fill_color)
        if self.has_bottom_wall:
            Line(Point(self.__x1, self.__y2), Point(
                self.__x2, self.__y2)).draw(canvas, fill_color)
