
import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import ttk
from tkinter import *
import os
import pathlib

root = Tk()
root.title("Chalk n' Board")
root.geometry("1200x650+400+200")
root.configure(bg="#3A1F04")
root.resizable(False,False)

current_x = 0
current_y = 0
color = 'white'
width_of_line = 4

board_x = 1200 - 200
board_y = 650 - 70

def loc_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y

def draw_line(work):
    global current_x, current_y, width_of_line
    width_of_line = get_current_width()
    canvas.create_line((current_x, current_y,work.x,work.y), width=width_of_line, fill=color)
    current_x = work.x
    current_y = work.y

def show_color(new_color):
    global color, width_of_line
    color = new_color
    width_of_line = 2

def erase():
    global color, width_of_line
    color = "#1b663e"
    width_of_line = 50

def clear_board():
    canvas.delete('all')


icon = PhotoImage(file=os.fspath(pathlib.Path(__file__).parent / 'images' / 'LOGO.png'))
root.iconphoto(False,icon)

side_bar = PhotoImage(file=os.fspath(pathlib.Path(__file__).parent / 'images' / 'SideBar.png'))
Label(root, image=side_bar, bg="#3A1F04").place(x=10,y=20)

logo_image = PhotoImage(file=os.fspath(pathlib.Path(__file__).parent / 'images' / '_logo.png'))
Label(root, image=logo_image, bg="#3A1F04").place(x=25,y=530)

eraser = PhotoImage(file=os.fspath(pathlib.Path(__file__).parent / 'images' / 'Eraser.png'))
Button(root, image=eraser, bg="white", command=erase).place(x=40,y=420)

clear_all = PhotoImage(file=os.fspath(pathlib.Path(__file__).parent / 'images' / 'Clear ALL.png'))
Button(root, image=clear_all, bg="white", command=clear_board).place(x=40,y=350)

colors = Canvas(root, bg="#a9a9a9", width=37, height = 130, bd=0)
colors.place(x=43, y=60)

def display_colors():
    id = colors.create_rectangle((10, 10, 30, 30), fill = "white")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('white'))

    id = colors.create_rectangle((10, 40, 30, 60), fill = "orange")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((10, 70, 30, 90), fill = "red")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id = colors.create_rectangle((10, 100, 30, 120), fill = "yellow")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

display_colors()

# the board

canvas = Canvas(root, bg="#1b663e", width=board_x, height=board_y, cursor='hand2')
canvas.place(x=150, y=30)
canvas.bind('<Button-1>', loc_xy)
canvas.bind('<B1-Motion>', draw_line)

# Size Slider

current_width = tk.DoubleVar()

def get_current_width():
    return '{: .2f}'.format(current_width.get())

def slider_changed(event):
    value_label.configure(text=get_current_width())

slider = ttk.Scale(root, from_=2, to=20, orient='vertical',
                   command=slider_changed, variable=current_width)
slider.place(x=50, y=240)

value_label = ttk.Label(root, text=get_current_width())
value_label.place(x=45, y=210)


root.mainloop()
