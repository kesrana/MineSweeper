from tkinter import Button

class Cell:
    #class constructor
    def __init__(self, x, y, is_mine: bool = False):
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.x = x
        self.y = y

    #makes the created class into a button given a location!
    def create_btn_obj(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x}, {self.y}"
        )
        #bind function makes our button actionable. <Button-1> makes the button left clickable)
        #<Button-3> makes the button right clickable
        btn.bind('<Button-1>', self.left_click_actions) #Left click
        btn.bind('<Button-2>', self.right_click_actions) #right click
        self.cell_btn_obj = btn

    def left_click_actions(self, event):
        print(event)
        print("I am left clicked!")

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")
