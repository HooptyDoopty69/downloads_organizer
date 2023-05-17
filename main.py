from tkinter import filedialog
from tkinter import *
import ttkbootstrap as ttk
import functools as fun
import os

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


#############
# FUNCTIONS #
#############
labels = []


def print_contents(directory, parent, label_list):
    files = os.listdir(directory)

    for label in label_list:
        label.pack_forget()

    for file in files:
        lb = Label(
            master=parent,
            text=file,
            font=f"{FONT} 12"
        )
        lb.pack()
        label_list.append(lb)


def ask_directory(val, parent):
    folder = filedialog.askdirectory()
    val.set(folder)
    print_contents(folder, parent, labels)


########
# MAIN #
########


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
    files_frame = Frame(master=sdo_frame)
    sdo_button = Button(
        master=sdo_frame,
        text="Select Directory",
        command=fun.partial(ask_directory, folder, files_frame),
        font=f"{FONT} {H3}"
    )
    sdo_label = Label(
        master=sdo_frame,
        textvariable=folder,
        font=f"{FONT} 12 bold"
    )

    # PACKING #

    title_frame.pack(fill='x', pady=25)
    title_label.pack()

    sdo_frame.pack(fill='x')
    sdo_button.pack()
    sdo_label.pack(pady=20)
    files_frame.pack()

    app.mainloop()


if __name__ == "__main__":
    main()
