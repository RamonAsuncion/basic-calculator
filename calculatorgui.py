# Tinkering with tkinter


from tkinter import *


def press(num):
    global operator
    operator = operator + str(num)
    value.set(operator)


def clearButton():
    global operator
    operator = ''
    value.set('')


def calculate():
    return


# global screen
screen = Tk()
screen.title('3:00 am Calculator')
screen.configure(bg='#4b86d9')

value = StringVar()
operator = ""

mainEntryField = Entry(screen, textvariable=value, borderwidth=50, insertwidth=4,
                       justify='right', font={'lato', 25, 'bold'}).grid(columnspan=5)

buttonOne = Button(screen, font={'lato', 14}, width=4, height=4,
                   background='white', relief='raised', bd=7, text='1', command=lambda: press(1), padx=15, pady=15).grid(column=0, row=3)

buttonTwo = Button(screen, font={'lato', 14}, width=4, height=4,
                   background='white', relief='raised', bd=7, text='2', command=lambda: press(2), padx=15, pady=15).grid(column=1, row=3)

buttonThree = Button(screen, font={
    'lato', 14}, width=4, height=4, background='white', relief='raised', bd=7, text='3', command=lambda: press(3), padx=15, pady=15).grid(column=2, row=3)

buttonFour = Button(screen, font={'lato', 14}, width=4, height=4,
                    background='white', relief='raised', bd=7, text='4', command=lambda: press(4), padx=15, pady=15).grid(column=0, row=2)

buttonFive = Button(screen, font={'lato', 14}, width=4, height=4,
                    background='white', relief='raised', bd=7, text='5', command=lambda: press(5), padx=15, pady=15).grid(column=1, row=2)

buttonSix = Button(screen, font={'lato', 14}, width=4, height=4,
                   background='white', relief='raised', bd=7, text='6', command=lambda: press(6), padx=15, pady=15).grid(column=2, row=2)

buttonSeven = Button(screen, font={
    'lato', 14}, width=4, height=4, background='white', relief='raised', bd=7, text='7', command=lambda: press(7), padx=15, pady=15).grid(column=0, row=1)

buttonEight = Button(screen, font={
    'lato', 14}, width=4, height=4, background='white', relief='raised', bd=7, text='8', command=lambda: press(8), padx=15, pady=15).grid(column=1, row=1)

buttonNine = Button(screen, font={'lato', 14}, width=4, height=4,
                    background='white', relief='raised', bd=7, text='9', command=lambda: press(9), padx=15, pady=15).grid(column=2, row=1)

buttonZero = Button(screen, font={'lato', 14}, width=4, height=4,
                    background='white', relief='raised', bd=7, text='0', command=lambda: press(0), padx=15, pady=15).grid(column=0, row=4)

buttonClear = Button(screen, font={'lato', 14}, width=4, height=4,
                     background='white', relief='raised', bd=7, text='AC', command=clearButton, padx=15, pady=15).grid(column=5, row=1)

buttonMultiply = Button(screen, font={'lato', 14}, width=4, height=4,
                        background='white', relief='raised', bd=7, text='X', command=lambda: press('X'), padx=15, pady=15).grid(column=4, row=2)

buttonDivide = Button(screen, font={'lato', 14}, width=4, height=4,
                      background='white', relief='raised', bd=7, text='/', command=lambda: press('/'), padx=15, pady=15).grid(column=5, row=2)

buttonSubtract = Button(screen, font={'lato', 14}, width=4, height=4,
                        background='white', relief='raised', bd=7, text='-', command=lambda: press('-'), padx=15, pady=15).grid(column=5, row=3)

buttonAddition = Button(screen, font={'lato', 14}, width=4, height=4,
                        background='white', relief='raised', bd=7, text='+', command=lambda: press('+'), padx=15, pady=15).grid(column=4, row=3)

buttonDecimal = Button(screen, font={'lato', 18}, width=4, height=4,
                       background='white', relief='raised', bd=7, text='.', command=lambda: press('.'), padx=15, pady=15).grid(column=1, row=4)

buttonEquals = Button(screen, font={'lato', 14}, width=4, height=4,
                      background='white', relief='raised', bd=7, text='=', command=calculate, padx=15, pady=15).grid(column=2, row=4)
screen.mainloop()


# if __name__ == "__main__":
#     main()
