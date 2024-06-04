from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = "FireMage Maze Solver"
        self.canvas = Canvas(width=width, height=height).pack()
