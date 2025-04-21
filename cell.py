from tkinter import Button, Label, messagebox
import random
import settings
import ctypes


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_obj = None
    #class constructor
    def __init__(self, x, y, is_mine: bool = False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
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
        )
        #bind function makes our button actionable. <Button-1> makes the button left clickable)
        #<Button-3> makes the button right clickable
        btn.bind('<Button-1>', self.left_click_actions) #Left click
        btn.bind('<Button-2>', self.right_click_actions) #right click
        self.cell_btn_obj = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left:{Cell.cell_count}",
            width=12,
            height=4,
            font=("", 30)
        )
        Cell.cell_count_label_obj = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mine_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cell_count == settings.MINES_COUNT:
                messagebox.showinfo('Congrats u won the game SHEEESH')
        self.cell_btn_obj.unbind('<Button-1>')
        self.cell_btn_obj.unbind('<Button-2>')





    #return cell object given x and y coordinates
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mine_length(self):
        count = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                count += 1

        return count

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_obj.configure(text=self.surrounded_cells_mine_length)
            self.cell_count_label_obj.configure(
                text=f"Cells left:{Cell.cell_count}"
            )
        self.is_opened = True

    #interrupt the game and display a message that the player lost.
    def show_mine(self):
        self.cell_btn_obj.configure(text='💣')
        messagebox.showinfo('You clicked on a mine!', 'Game Over',)

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_obj.configure(
                text='🚩'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_obj.configure(
                text=""
            )
            self.is_mine_candidate = False

    #created static functions to randomize mines from the all list created in the constructor.
    #Created a repr function to print the cells cleanly.
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

