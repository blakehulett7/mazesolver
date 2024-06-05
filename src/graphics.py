from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "FireMage Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, bg="white",
                             width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running is True:
            self.redraw()
        print("Window Closed")

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2, window):
        self.__point_1 = point_1
        self.__point_2 = point_2
        self.__win = window

    def draw(self, fill_color):
        window = self.__win
        window.canvas.create_line(self.__point_1.x, self.__point_1.y,
                                  self.__point_2.x, self.__point_2.y,
                                  fill=fill_color, width=2)
