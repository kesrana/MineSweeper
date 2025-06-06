from tkinter import *
import settings
import utils
from cell import Cell

root = Tk() #using root as a variable is standard practice when using tkinter
#Overriding the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Mine Sweeper')
root.resizable(False, False) #makes this window not resizable

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)

top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)

left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(
    x=utils.width_prct(25), y=utils.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_obj(center_frame)
        c.cell_btn_obj.grid(
            column =x, row=y
        )

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_obj.place(x=0, y=0)

Cell.randomize_mines()
#run the window
root.mainloop() #this is needed to keep the window running


