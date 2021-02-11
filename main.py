"""---Calculator using Tkinter---
--------------------------------
"""

from tkinter import*

expression = ""


def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)


def equalpress():

    try:
        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""

    except:
        equation.set(" error ")
        expression = ""


# Function to clear
def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    # create GUI window
    gui = Tk()

    # set background colour of GUI window
    gui.configure(background="light blue")

    # set title of GUi window
    gui.title("Calculator Jesel")

    # set configuration of GUI window
    gui.geometry("240x220")
    # variable class
    equation = StringVar()

    # create text entry box(showing expression)
    expression_field = Entry(gui, textvariable=equation)

    # grid method for placing
    expression_field.grid(columnspan=90, ipadx=60)

    equation.set('Enter your expression: ')

    # create Buttons
    button1 = Button(gui, text=' 1 ', fg='black', bg='pink', command=lambda: press(1), height=2, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='pink', command=lambda: press(2), height=2, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='pink', command=lambda: press(3), height=2, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='pink', command=lambda: press(4), height=2, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='pink', command=lambda: press(5), height=2, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='pink', command=lambda: press(6), height=2, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='pink', command=lambda: press(7), height=2, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='pink', command=lambda: press(8), height=2, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='pink', command=lambda: press(9), height=2, width=7)
    button9.grid(row=4, column=2)

    divide = Button(gui, text=' / ', fg='black', bg='pink', command=lambda: press("/"), height=2, width=7)
    divide.grid(row=2, column=4)

    multiply = Button(gui, text=' * ', fg='black', bg='pink', command=lambda: press("*"), height=2, width=7)
    multiply.grid(row=3, column=4)

    subtract = Button(gui, text=' - ', fg='black', bg='pink', command=lambda: press("-"), height=2, width=7)
    subtract.grid(row=4, column=4)

    add = Button(gui, text=' + ', fg='black', bg='pink', command=lambda: press("+"), height=2, width=7)
    add.grid(row=5, column=4)

    button0 = Button(gui, text=' 0 ', fg='black', bg='pink', command=lambda: press(0), height=2, width=7)
    button0.grid(row=5, column=0)

    clear = Button(gui, text=' CLR ', fg='black', bg='pink', command=clear, height=2, width=7)
    clear.grid(row=5, column=1)

    equal = Button(gui, text=' = ', fg='black', bg='pink', command=equalpress, height=2, width=7)
    equal.grid(row=5, column=2)

    decimal = Button(gui, text=' . ', fg='black', bg='pink', command=lambda: press("."), height=2, width=7)
    decimal.grid(row=6, column=0)


gui.mainloop()




