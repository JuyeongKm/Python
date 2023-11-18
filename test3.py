from tkinter import *
from tkinter.simpledialog import *

window = Tk()
window.geometry('400x100')

label1 = Label(window, text='입력된 값')
label1.pack()

value = askinteger('배수 입력', '주사위 숫자(1~6) 입력', minvalue = 1, maxvalue = 6)
label1.configure(text= str(value))
window.mainloop()
