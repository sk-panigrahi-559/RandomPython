import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.geometry('296x240')
window.title('my_calculator')  # window designed

exp = ''
input_text = tkinter.StringVar()


def clicked_num(num):  # function for number and operators
    global exp
    exp += str(num)
    input_text.set(exp)


def clicked_clear():  # clear karma pai
    global exp
    exp = ''
    input_text.set(exp)


def clicked_eq():  # equal chipile
    global exp
    try:
        input_text.set(str(eval(exp)))
        exp = ''
    except:
        messagebox.showinfo('ERROR', '''CHECK AGAIN
                                        YOU HAVE
                                        PROBABLY ENTERED
                                        INVALID EXPRESSION''')


# creating input frame and input field

input_frame = tkinter.Frame(window, width=87, height=60, highlightbackground='green', highlightcolor='black', bd=0)
input_frame.pack(side='top')

field = tkinter.Entry(input_frame, textvariable=input_text, font=('arial', 20, 'bold'), bg='black', fg='green')
field.grid(row=0, column=0)
field.pack(ipady=20)

# creating button frame

button_frame = tkinter.Frame(window, width=300, height=100, bd=0)
button_frame.pack(side='left')

# now the buttons
#   prathama row
one = tkinter.Button(button_frame,
                     width=5,
                     height=2,
                     bg='black', fg='white',
                     text="1",
                     command=lambda: clicked_num(1)).grid(row=0, column=0)
two = tkinter.Button(button_frame,
                     width=5,
                     height=2,
                     bg='black', fg='white',
                     text="2",
                     command=lambda: clicked_num(2)).grid(row=0, column=1)
three = tkinter.Button(button_frame,
                       width=5,
                       height=2,
                       bg='black', fg='white',
                       text="3",
                       command=lambda: clicked_num(3)).grid(row=0, column=2)

#   dvitiya row
four = tkinter.Button(button_frame,
                      width=5,
                      height=2,
                      bg='black', fg='white',
                      text="4",
                      command=lambda: clicked_num(4)).grid(row=1, column=0)
five = tkinter.Button(button_frame,
                      width=5,
                      height=2,
                      bg='black', fg='white',
                      text="5",
                      command=lambda: clicked_num(5)).grid(row=1, column=1)
six = tkinter.Button(button_frame,
                     width=5,
                     height=2,
                     bg='black', fg='white',
                     text="6",
                     command=lambda: clicked_num(6)).grid(row=1, column=2)

#   trutiya row
seven = tkinter.Button(button_frame,
                       width=5,
                       height=2, bg='black', fg='white',
                       text="7",
                       command=lambda: clicked_num(7)).grid(row=2, column=0)
eight = tkinter.Button(button_frame,
                       width=5,
                       height=2,
                       bg='black', fg='white',
                       text="8",
                       command=lambda: clicked_num(8)).grid(row=2, column=1)
nine = tkinter.Button(button_frame,
                      width=5,
                      height=2,
                      bg='black',
                      fg='white', text="9",
                      command=lambda: clicked_num(9)).grid(row=2, column=2)
#   chaturtha row
zero = tkinter.Button(button_frame,
                      width=5,
                      height=2,
                      bg='black', fg='white',
                      text="0",
                      command=lambda: clicked_num(0)).grid(row=3, column=0)
point_deci = tkinter.Button(button_frame,
                            width=5,
                            height=2,
                            bg='black', fg='white',
                            text=".",
                            command=lambda: clicked_num(".")).grid(row=3, column=1)
equal_to = tkinter.Button(button_frame,
                          width=5,
                          height=2,
                          bg='yellow', fg='black',
                          text="=",
                          command=lambda: clicked_eq()).grid(row=3, column=2)

# operator buttons
add = tkinter.Button(button_frame,
                     width=10,
                     height=2,
                     bg='cyan', fg='black',
                     text="+", font=('arial', 9, 'bold'),
                     command=lambda: clicked_num('+')).grid(row=0, column=3)
subt = tkinter.Button(button_frame,
                      width=10,
                      height=2,
                      bg='cyan', fg='black',
                      text="--", font=('arial', 9, 'bold'),
                      command=lambda: clicked_num('-')).grid(row=1, column=3)
multi = tkinter.Button(button_frame,
                       width=10,
                       height=2,
                       bg='cyan', fg='black',
                       text="X", font=('arial', 9, 'bold'),
                       command=lambda: clicked_num('*')).grid(row=2, column=3)
div = tkinter.Button(button_frame,
                     width=10,
                     height=2,
                     bg='cyan', fg='black',
                     text="/", font=('arial', 9, 'bold'),
                     command=lambda: clicked_num('/')).grid(row=3, column=3)
clear = tkinter.Button(button_frame,
                       width=10,
                       height=2,
                       bg='red', fg='black',
                       text="C", font=('arial', 9, 'bold'),
                       command=lambda: clicked_clear()).grid(row=0, column=4)


window.mainloop()
