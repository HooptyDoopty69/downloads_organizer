from tkinter import filedialog
from tkinter import *
import ttkbootstrap as ttk
import functools as fun

#############
# CONSTANTS #
#############


WIDTH = 800
HEIGHT = 950
NAME = "Downloads Organizer"
FONT = "Calibri"
H1 = "24"
H2 = "20"
H3 = "26"
B = "bold"


########
# MAIN #
########

def ask_directory(val):
    folder = filedialog.askdirectory()
    val.set(folder)


def main():
    app = ttk.Window(themename='simplex')
    app.title(NAME)
    app.geometry(f"{WIDTH}x{HEIGHT}")
    app.minsize(width=WIDTH, height=HEIGHT)

    # TITLE #

    title_frame = Frame(master=app)
    title_label = Label(
        master=title_frame,
        text=f"{NAME}",
        font=f"{FONT} {H1} {B}"
    )

    # SELECT DIRECTORY TO ORAGANIZE #

    folder = StringVar()

    sdo_frame = Frame(master=app)
    sdo_button = Button(
        master=sdo_frame,
        text="Select Directory",
        command=fun.partial(ask_directory, folder),
        font=f"{FONT} {H3}"
    )
    sdo_label = Label(
        master=sdo_frame,
        textvariable=folder,
        font=f"{FONT} {H3}"
    )

    # PACKING #

    title_frame.pack(fill='x', pady=25)
    title_label.pack()

    sdo_frame.pack(fill='x')
    sdo_button.pack()
    sdo_label.pack(pady=20)

    app.mainloop()


if __name__ == "__main__":
    main()
