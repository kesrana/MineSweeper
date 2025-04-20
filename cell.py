from tkinter import Button
import random
import settings


class Cell:
    all = []
    #class constructor
    def __init__(self, x, y, is_mine: bool = False):
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.x = x
        self.y = y

        Cell.all.append(self)
    #makes the created class into a button given a location!
    def create_btn_obj(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text = f"{self.x}, {self.y}"
        )
        #bind function makes our button actionable. <Button-1> makes the button left clickable)
        #<Button-3> makes the button right clickable
        btn.bind('<Button-1>', self.left_click_actions) #Left click
        btn.bind('<Button-2>', self.right_click_actions) #right click
        self.cell_btn_obj = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    #return cell object given x and y coordinates
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_cell(self):
        surrounded_cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        print(surrounded_cells)
    #interrupt the game and display a message that the player lost.
    def show_mine(self):
        self.cell_btn_obj.configure(text='💣')

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")

    #created static functions to randomize mines from the all list created in the constructor.
    #Created a repr function to print the cells cleanly.
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

